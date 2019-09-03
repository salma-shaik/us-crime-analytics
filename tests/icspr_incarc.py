import pandas as pd

incarc_df = pd.read_csv('C:/Users/sshaik2/Downloads/ICPSR_37021-V1/ICPSR_37021/DS0001/37021-0001-Data.tsv', sep='\t')

print(set(incarc_df['STATE']).__len__())