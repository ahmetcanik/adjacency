import argparse
import itertools

import pandas as pd


def main():
    parser = argparse.ArgumentParser(
        description='Generates adjacency matrix from given excel file')

    parser.add_argument('--i', type=str, required=True,
                        help='Input excel file')

    parser.add_argument('--o', type=str, required=True,
                        help='Output excel file')
    args = parser.parse_args()
    generate_adjacency_matrix(args.i, args.o)


def generate_adjacency_matrix(input_file, output_file):
    df = pd.read_excel(input_file)
    df = df.fillna('')
    adj_dict = {}
    for index, row in df.iterrows():
        nodes = [item for item in row.array[1:] if item]
        for v1, v2 in itertools.combinations(nodes, 2):
            if v1 not in adj_dict:
                adj_dict[v1] = {}
            if v2 not in adj_dict:
                adj_dict[v2] = {}
            if v2 not in adj_dict[v1]:
                adj_dict[v1][v2] = 0
            if v1 not in adj_dict[v2]:
                adj_dict[v2][v1] = 0
            adj_dict[v1][v2] += 1
            adj_dict[v2][v1] += 1
    adj_df = pd.DataFrame(adj_dict)
    adj_df = adj_df.fillna(0)
    adj_df.to_excel(output_file)


if __name__ == '__main__':
    main()
