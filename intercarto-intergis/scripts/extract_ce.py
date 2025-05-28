import pathlib

import pandas as pd
import tqdm


data = []
for fn in tqdm.tqdm(pathlib.Path("../data/ce").glob("*.bz2")):
    df = pd.read_csv(fn)
    data.append(df[["КН", "Площадь"]].dropna())

pd.concat(data).to_parquet("../data/flats_area.parquet")
