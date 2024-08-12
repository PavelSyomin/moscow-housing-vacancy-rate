import pathlib

import pandas as pd
import tqdm

cols = ["Глобальный уникальный идентификатор дома по ФИАС", "Кадастровый номер"]
data = []
for fn in tqdm.tqdm(pathlib.Path(".").glob("Сведения по ОЖФ*")):
    df = pd.read_csv(fn, sep="|", dtype=str, na_values=["нет"])
    data.append(df[cols].dropna(subset="Кадастровый номер"))

pd.concat(data).to_csv("flats.csv", index=False)

