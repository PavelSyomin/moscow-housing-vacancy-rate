import pathlib

import numpy as np
import pandas as pd
import tqdm


def parse_floor(val: str | float) -> float:
    val = str(val).lower().replace("(этаж)", "").strip()
    try:
        return float(val)
    except:
        return np.nan


data = []
for fn in tqdm.tqdm(pathlib.Path("../intercarto-intergis/data/ce").glob("*.bz2")):
    df = pd.read_csv(fn, dtype=str)
    selected = df[["КН", "Площадь", "Этаж (для помещения)"]].copy()
    del df
    selected.columns = ["flat_cad_number", "flat_area", "flat_floor"]
    selected["flat_area"] = selected["flat_area"].apply(lambda x: round(float(x.replace(",", "."))))
    selected["flat_floor"] = selected["flat_floor"].apply(parse_floor)

    nrow_before = len(selected)
    selected.dropna(inplace=True)
    print(f"Dropped {(nrow_before - len(selected)) / nrow_before:.2f} of rows with missing values")

    data.append(selected)

pd.concat(data).to_parquet("flats_area.parquet")
