import pathlib

import pandas as pd
import tqdm


data = []
for fn in tqdm.tqdm(pathlib.Path("flats_data_ce").glob("*")):
    df = pd.read_excel(fn)
    data.append(df[["КН", "Площадь"]].dropna())

pd.concat(data).to_csv("flats_area.csv")
