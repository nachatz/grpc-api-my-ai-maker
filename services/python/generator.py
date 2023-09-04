from logger import Logger
from typing import Tuple, Type


class GeneratorService:
    def __init__(self):
        Logger.initialize("logger")

    def generate_python_code(self, features: list[str], types: list[str]) -> str:
        """
        Generate Python code based on features and types.

        Args:
            features (list[str]): List of feature names.
            types (list[str]): List of feature types.

        Returns:
            str: Generated Python code as a string.
        """
        Logger.info(f"Generating python3 code for: \n {features}")

        typed_features = zip(features, types)
        code = self.__init_code()
        code += self.__encode_features(typed_features)

        return code

    def __init_code(self) -> str:
        """
        Generate initialization code for the Python script.

        Returns:
            str: Initialization code as a string.
        """
        code = self.__append_snippet("\nimport pandas as pd", indentation=0, depth=2)
        code += self.__append_snippet("def main():", indentation=0, depth=1)
        code += self.__append_snippet(
            "df = pd.read_csv('file.[xlsx, csv]')", indentation=1, depth=1
        )
        return code

    def __encode_features(self, typed_features: Tuple[str, Type]) -> str:
        """
        Generate code to one-hot encode string features.

        Args:
            typed_features (Tuple[str, Type]): Tuple of feature names and types.

        Returns:
            str: Encoding code as a string.
        """
        encodings = ""

        for feature in typed_features:
            feat, type_ = feature

            if type_ == "string":
                encodings += self.__append_snippet(
                    f"df = pd.get_dummies(df, columns=['{feat}'])",
                    indentation=1,
                    depth=1,
                )
        return encodings

    def __append_snippet(self, snippet: str, indentation: int, depth: int) -> str:
        """
        Append an indented code snippet with optional new lines.

        Args:
            snippet (str): The code snippet to append.
            indentation (int): Number of indentation levels.
            depth (int): Number of new lines to append after the snippet.

        Returns:
            str: The indented code snippet as a string.
        """
        indented_snippet = " " * (4 * indentation) + snippet + "\n" * depth
        return indented_snippet
