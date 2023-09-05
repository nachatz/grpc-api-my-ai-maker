
import pandas as pd

def normalize(df, column_names, threshold=0.75)
for column_name in column_names:
        col = df[column_name]
        col_range = col.max() - col.min()

        if column_range > threshold:
            normalized_column = (col - col.min()) / col_range
            df[column_name] = normalized_column
        return df

def main():
    df = pd.read_csv('file.[xlsx, csv]')
if __name__ == '__main__':
    main()
