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

        code += self.__append_snippet("if __name__ == '__main__':", indentation=0)
        code += self.__append_snippet("main()")
        code = self.__normalize_applicability(code, typed_features)
        return code

    def __init_code(self) -> str:
        """
        Generate initialization code for the Python script.

        Returns:
            str: Initialization code as a string.
        """
        code = self.__append_snippet("\nimport pandas as pd", indentation=0, depth=2)
        code += self.__generate_functions()
        code += self.__append_snippet("def main():", indentation=0)
        code += self.__append_snippet("df = pd.read_csv('file.[xlsx, csv]')")
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
            feat, _type = feature

            if type == "string":
                encodings += self.__append_snippet(
                    f"df = pd.get_dummies(df, columns=['{feat}'])"
                )
        return encodings

    def __append_snippet(
        self, snippet: str, indentation: int = 1, depth: int = 1
    ) -> str:
        """
        Append an indented code snippet with optional new lines.

        Args:
            snippet (str): The code snippet to append.
            indentation (int): Number of indentation levels.
            depth (int): Number of new lines to append after the snippet.

        Returns:
            str: The indented code snippet as a string.
        """
        return " " * (4 * indentation) + snippet + "\n" * depth

    def __generate_functions(self):
        """
        Generate utilized functions
        Returns:
            Functions being used
        """

        funcs = """def normalize(df, column_names, threshold=0.75)
for column_name in column_names:
        col = df[column_name]
        col_range = col.max() - col.min()

        if column_range > threshold:
            normalized_column = (col - col.min()) / col_range
            df[column_name] = normalized_column
        return df\n\n"""
        return funcs

    def __normalize_applicability(self, code: str, typed_features: Tuple[str, Type]):
        """
        Determine if a column in a DataFrame should be normalized and normalize it if needed.

        Args:
            code (str): Current generated code
            typed_features (Tuple[str, Type]): Typed features

        Returns:
            normalized code generation
        """
        cols_to_normalize = [tupl[0] for tupl in typed_features if tupl[1] != "string"]
        code = self.__append_snippet(f"df = normalize(df, {cols_to_normalize})")

        return code
