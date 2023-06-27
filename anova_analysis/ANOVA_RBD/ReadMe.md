# RBD Analysis

This is a part of `anova-analysis`.

This performs RBD (Randomized Block Design). It calculates various statistical measures and generates an ANOVA (Analysis of Variance) table along with additional results.

## Installation

install the package using pip:

```python
pip install anova_analysis
```

## Usage

1. When you have only one character to analyse:

      ```python          
        from anova_analysis import ANOVA_RBD

        #Set the replication, treatment, input file path
        replication = 4
        treatment = 23
        input_file_path = "data/MODEL_DATA.xlsx"

        #Perform ANOVA analysis
        ANOVA_RBD.RBD(replication, treatment, input_file_path)

2. When you have a folder with individual characters in separate excel files:

     ```python
        from anova_analysis import ANOVA_RBD
        import os

        folder_path = r'C:/Users/PlantReading/data/'

        # listing files in the folder_path 
        for file in os.listdir(folder_path):
                if file.endswith('.xlsx') or file.endswith('.xls'):
                        file_path = os.path.join(folder_path, file)
                        print(f"processing file: {file}")
                        ANOVA_RBD.RBD(rep,treat,file_path)

3. The `RBD()` function accepts an optional parameter called `save_file`, which determines whether the result file need to be saved or not. By default, the parameter is set to `True`, enabling the default operation.

4. To use the function, follow these steps:
    
     ```python  
        # default, will save the result
        ANOVA_RBD.RBD(replication, treatment, input_file_path) 

        # Will not save the result
        ANOVA_RBD.RBD(replication, treatment, input_file_path, False) 
- If you want the output to be used in for further analysis, 
you can then access the calculated values from the ``result`` dictionary:
     
     ```python
    result = ANOVA_RBD.RBD(replication, treatment, input_file_path)
    ```
- To access the ``result`` use the following in other code or for further analysis
     
     ```python
        CF = result["correction_factor"]
        TSS = result["total_sum_of_square"]
        RSS = result["replication_sum_of_square"]
        TSS = result["treatment_sum_of_square"]
        ESS = result["error_sum_of_square"]
        Rdf = result["replication_df"]
        Tdf = result["treatment_df"],
        Edf = result["errors_df"],
        RMSS = result["rep_mean_ss"],
        TMSS = result["tre_mean_ss"],
        EMSS = result["error_mean_ss"],
        TDF = result["total_df"],
        ToSS = result["total_ss"],
        tableDF = result["global_dataframe"]
    ```         
        # Where CF, TSS,.. are variables 
-  You can easily access them in your other Python file and use them as needed. Modify the returned data structure to suit your preferences and the specific values you want to access.

## Features

- Calculates the `correction factor, total sum of squares, replication sum of squares, treatment sum of squares, and error sum of squares`.
- Generates an ANOVA table with the `source, degrees of freedom, sum of squares, mean square, F-values, and p-values at the 5% and 1% significance levels`.
- Performs significance testing at the 5% and 1% levels to determine the statistical significance of the factors.
- Saves the ANOVA results in a text file for further analysis or reporting purposes.

## Example Dataset

- The package requires an Excel file containing the experimental data. The data should be arranged in a Randomized Block Design (RBD) format, with treatments (genotypes) in columns and replications in rows. 
- Please ensure that the excel file is in same format as it is given in this [repo](data/MODEL_DATA.xlsx) or below in separate excel file using the code from [here](https://github.com/Insight-deviler/Folder-based-Character-Column-Transformation)
        
        1. Days to Maturity.xlsx:

                | GENOTYPE  | R1    | R2     | R3     | 
                |-----------|-------|--------|--------|
                | G1        | 74.4  | 70.86  | 60.94  |
                | G2        | 91.82 | 99.18  | 118.88 |
                | G3        | 48.08 | 62.1   | 58.54  |
                | G4        | 59.06 | 65.62  | 81.62  |
                | G5        | 84.16 | 109.74 | 102.14 |

        2. PLANT HEIGHT (cm).xlsx:

                | GENOTYPE  | R1    | R2     | R3     | 
                |-----------|-------|--------|--------|
                | G1        | 74.4  | 70.86  | 60.94  |
                | G2        | 91.82 | 99.18  | 118.88 |
                | G3        | 48.08 | 62.1   | 58.54  |
                | G4        | 59.06 | 65.62  | 81.62  |
                | G5        | 84.16 | 109.74 | 102.14 |

- If you have data in the below format, transform it to above said model (individual character) by using this [code](https://github.com/Insight-deviler/Folder-based-Character-Column-Transformation)

        | GENOTYPE | REPLICATION | Days to Maturity | PLANT HEIGHT (cm) |
        |----------|-------------|------------------|-------------------|
        | G1       | R1          | 4                | 5                 |
        | G1       | R2          | 5                | 6                 |
        | G1       | R3          | 4                | 9.3               |
        | G2       | R1          | 3                | 9.9               |
        | G2       | R2          | 6                | 7.5               |
