import pandas as pd

drug_df = pd.read_csv("ata/drug200.csv")
drug_df = drug_df.sample(frac=1)
drug_df.head(3)
# this file
# New feature add by Saqib Ameer