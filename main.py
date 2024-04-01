from textractor import Textractor
import os
import pandas as pd
from PIL import Image
from textractor.visualizers.entitylist import EntityList
from textractor.data.constants import TextractFeatures, Direction, DirectionalFinderType

extractor = Textractor(region_name="us-east-1")
file_source= "s3://ccs-bucket-332009426877-us-east-1/ccs.pdf"

queries = [
    "What is the Total Payment Due",
    "What is the Payment Due date",
    "What is the Credit Limit",
    "Whats is the Available credit limit",
    "What is the Minimum Payment due"
]


document = extractor.start_document_analysis(file_source,features=[TextractFeatures.TABLES, TextractFeatures.QUERIES], queries=queries, save_image=True)
tableList = EntityList(document.tables)

print(document.queries)

merged = [];
for table in tableList:
    df = table.to_pandas()
    if(df.iloc[0, 0].strip() == "DATE" or df.iloc[1, 0].strip() == "DATE"):
        merged.append(df.iloc[1:])
mergedDf = pd.concat(merged)
Crs = mergedDf[mergedDf.iloc[:, 3].str.contains('Cr')]
print(Crs)

Drs = mergedDf[mergedDf.iloc[:, 3].str.contains('Dr')]
print(Drs)