import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from transform import map_weather_code, generate_statistics
 

def test_map_weather_code_known():
    assert map_weather_code(0) == "Clear sky"


def test_map_weather_code_unknown():
    assert map_weather_code(999) == "Unknown"


def test_generate_statistics():
    df = pd.DataFrame({
        "temperature": [10, 20, 30]
    })

    stats = generate_statistics(df)

    assert stats.loc[0, "value_min_temp"] == 10
    assert stats.loc[0, "value_max_temp"] == 30
    assert stats.loc[0, "value_avg_temp"] == 20