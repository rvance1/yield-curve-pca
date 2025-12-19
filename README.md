# Yield Curve PCA

This project models U.S. Treasury yield curve dynamics using PCA to extract
level, slope, and curvature factors and tests simple mean-reversion trading signals.

## Data
- WRDS Treasury Yield Curve
- Daily maturities: 3M–30Y
- 2000–present

## Methodology
- Yield changes (Δy)
- Standardization
- PCA on covariance matrix
- Factor interpretation
- Signal backtesting

## Results
- PC1: Level (~75%)
- PC2: Slope (~15%)
- PC3: Curvature (~5%)

## Structure
