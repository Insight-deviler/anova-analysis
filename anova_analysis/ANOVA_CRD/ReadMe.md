# CRD Analysis

This is a part of `anova-analysis`.

This performs CRD (Completely Randomized Design). It calculates various statistical measures and generates an ANOVA (Analysis of Variance) table along with additional results.


## Prerequisites

Install this using pip:

```python
pip install anova-analysis
```

## Usage

```python

Inputfile = "Data.xlsx"
Treatment = 4
input_level = 5
savefile = False

CRD(Inputfile, Treatment, input_level, savefile)
```

## Parameters

- `Inputfile`: The input data file in Excel or CSV format.
- `Treatment`: Number of treatments in the analysis.
- `input_level`: The significance or alpha level (accepted values: 0.25, 0.1, 0.05, 0.025, 0.01, or their corresponding percentages).
- `savefile`: Optional. If you don't want to save the result, provide `False`. By default, the result is saved.

## Output

The package generates the following outputs:

- ANOVA table: Contains as degrees of freedom (df), sum of squares (SS), mean sum of squares (MSS), F-ratio, and p-value.
- Result statement: Indicates whether the null hypothesis is rejected or accepted.
- Critical difference (CD): If the null hypothesis is rejected, the critical difference is calculated.
- Mean table: Shows the mean values of rows.
- Pairwise comparison: Compares pairwise differences between row means and the critical difference.
- Significant combinations: Lists the combinations that are significant.

The results are also saved in a text file named `Inputfile_result.txt` in the same directory as the input file.

## Further Analysis

- If you want the output to be used in further analysis you can access the values from the dictionary :

```python
result = CRD(Inputfile, Treatment, input_level, savefile)
```

- In subsequent lines, you can access the result using the following 

```python
        title = result["Title"]
        CF = result["cf"]
        TSS = result["total_ss"]
        RSS = result["row_ss"]
        ESS = result["error_ss"]
        Rdf = result["row_df"]
        Edf = result["error_df"]
        RMSS = result["row_mss"]
        EMSS = result["error_mss"],
        TDF = result["total_df"],
        ToSS = result["total_ss"],
        cd = result["cd"]
        combination = result["sign_between"]
        table = result["global_dataframe"]
```