import numpy as np

income_percentiles =    np.array(
    [
    (10, 14629),
    (20, 25600),
    (30, 37002),
    (40, 50000),
    (50, 63179),
    (60, 79542),
    (70, 100162),
    (80, 130000),
    (90, 184292)
]
)

print(f'Dimensions:{income_percentiles.shape}')
print(f'Size:{income_percentiles.size}')