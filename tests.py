import pandas as pd
from transform import map_weather_code, generate_statistics

# Test map_weather_code()
assert map_weather_code(0) == "Clear sky"
assert map_weather_code(95) == "Thunderstorm"
assert map_weather_code(999) == "Unknown"
print("map_weather_code tests passed")

# Test generate_statistics()
df_test = pd.DataFrame({'temperature':[10,20,30]})
stats = generate_statistics(df_test)
assert stats['value_min_temp'][0] == 10
assert stats['value_max_temp'][0] == 30
assert stats['value_avg_temp'][0] == 20
print("generate_statistics tests passed")