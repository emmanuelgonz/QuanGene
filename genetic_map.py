#!/usr/bin/env python3
"""
Author : eg
Date   : 2022-01-25
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import pandas as pd
import numpy as np 
import warnings
import itertools
warnings.filterwarnings("ignore")


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('csv',
                        metavar='str',
                        help='CSV containing SNP data')

    parser.add_argument('-of',
                        '--output_filename',
                        help='Output filename for recombination frequency CSV file.',
                        type=str,
                        default='recombination_frequency.csv')

    return parser.parse_args()


# --------------------------------------------------
def get_single_recombination_frequency(df, snp_1, snp_2):
    sample_df = df[[snp_1, snp_2]]
    sample_df['pa_recombination'] = sample_df.apply(lambda row: 1 if row[snp_1] != row[snp_2] else 0, axis=1)
    recombination_frequency = len(sample_df[sample_df['pa_recombination']==1])/len(sample_df)
    return recombination_frequency


# --------------------------------------------------
def get_pair_order_list(available_snps):
    pair_order_list = itertools.permutations(list(enumerate(available_snps)), 2)
    return pair_order_list


# --------------------------------------------------
def get_recombination_frequency_df(df, pair_order_list):
    result_df = pd.DataFrame()
    result_df['query_snp_1'] = result_df['query_snp_2'] = result_df['recombination_frequency'] = None
    cnt = 0

    for item in list(pair_order_list):
        cnt+= 1
        first_snp = item[0][1]
        second_snp = item[1][1]
        recombination_frequency = get_single_recombination_frequency(df, str(first_snp), str(second_snp))
        result_df.at[cnt, 'recombination_frequency'] = recombination_frequency
        result_df.at[cnt, 'query_snp_1'] = first_snp
        result_df.at[cnt, 'query_snp_2'] = second_snp
        
    recombination_frequency_df = result_df.drop_duplicates(subset=['recombination_frequency'])

    return recombination_frequency_df.sort_values(by='recombination_frequency', ascending=False)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    df = pd.read_excel(args.csv).drop('Unnamed: 0', axis=1)
    available_snps = [item for item in df.columns.to_list() if 'SNP' in item]
    pair_order_list = get_pair_order_list(available_snps)
    recombination_frequency_df = get_recombination_frequency_df(df, pair_order_list)
    recombination_frequency_df.to_csv(args.output_filename, index=False)


# --------------------------------------------------
if __name__ == '__main__':
    main()
