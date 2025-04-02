import ujson as json
import pandas as pd

source=input("provide full path of source ndjson file")

file=source

records = map(json.loads, open(file, encoding="utf8"))
df=pd.DataFrame.from_records(records)
print("print first 5 rows")
df.head(5)