import pandas as pd 
import  scipy.stats as stats
import os
from tabulate import tabulate
import math
import warnings

# Suppress all future warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


def formatter (vals):
    return "{:.3f}".format(vals)

def CRD(Inputfile,Treatment,input_level,savefile=None):

    """
        Inputfile: Excel or CSV file(s)
        Treatment: Number of treament in analysis
        input_level: The significane or alpha level
        savefile: If you want to save the result(default: True)
    """

    # Validating alpha level
    al = [0.25, 0.1, 0.05, 0.025, 0.01]
    int_al = [5, 1, 25, 2.5, 10]
    alpha_level = ""

    if input_level in al:
        # Perform operations for 'al' listint
        alpha_level = float(input_level)

    elif input_level in int_al:
        # Perform operations for 'int_al' list
        alpha_level = float(input_level)/100

    else:
        # Invalid input, print accepted list of alpha levels
        raise ValueError("Invalid alpha level. Accepted values: " + str(al + int_al))

    # Get the extension of the file name
    getExtension = os.path.splitext(os.path.basename(Inputfile))[1]
        
    if getExtension == ".xlsx":
        df = pd.read_excel(Inputfile)
    elif getExtension == ".csv" :
        df = pd.read_csv(Inputfile)
    else:
        raise ValueError("Invalid input data. Must be Excel, or CSV file.")
    
    #Finding number of varieties
    varieties = len(df.iloc[:, 0])
    
    #Fill the empty cells with zero
    df.fillna(0, inplace=True)

    #Correction Factor
    data_subset = df.iloc[:, 1:]
    total_sum = data_subset.values.sum()
    correctionFactor = (total_sum ** 2) / (varieties * Treatment)
    
    #Total Sum of Square
    total_sum_squared = (data_subset ** 2).values.sum()
    totalsum = total_sum_squared - correctionFactor
    
    #Row Sum of Square
    row_sums = df.sum(axis=1)
    rowSum = ( 1 / varieties)*((row_sums ** 2).sum()) - correctionFactor
    
    #Error Sum of Square
    ErrorSum = float(formatter(totalsum)) - float(formatter(rowSum))
    
    #Degree of freedom
    rdf = Treatment - 1
    edf = (varieties*Treatment) - Treatment
    tdf = rdf + edf 

    #Mean Sum of Square
    rmss = rowSum/rdf 
    emss = ErrorSum/edf

    #F-ration Calculation
    rfr = rmss/emss

    # F-test and Significance Level
    p_value_row_5 = stats.f.ppf(1- float(alpha_level), rdf, edf)
    
    # Determine Significance
    row_significance = " *" if p_value_row_5 < rfr else " ns"
    
    #Creating the ANOVA table
    anova = {
        "Source" : ["Row", "Error","Total"],
        "df" : [rdf, edf, tdf],
        "SS" : [formatter(rowSum),ErrorSum, formatter(totalsum)],
        "MSS" : [formatter(rmss) + row_significance, formatter(emss),""],
        "F-ratio" : [formatter(rfr), "", ""],
        "p-value ({})".format(alpha_level) : [formatter(p_value_row_5),"",""]
        }

    if row_significance == " *":
        res = f"On comparing the F-ratio at {alpha_level} level with p-value, null hypothesis is rejected, that indicates there is significant differences between the Rows"
    elif row_significance == " ns":
        res = f"On comparing the F-ratio at {alpha_level} level with p-value, null hypothesis is accepted, that indicates there is no significant differences between the Rows"
    
    if row_significance == " *":  
        #Calculating Critical difference
        cd_1 = (2 * emss)/varieties
        cd_2 = math.sqrt(cd_1)
        error_F_value = stats.t.ppf(1-float(alpha_level)/2,edf)
        cd = cd_2 * error_F_value

        #Calculating the mean
        first_col = df.iloc[:,0]
        means = df.mean(axis=1)

        linked = {
            df.columns[0] : first_col,
            "Mean" : means
        }
        
        combinations = []
        combination_names = []

        for i in range(len(first_col)):
            for j in range(i+1, len(first_col)):
                combination = means[i] - means[j]
                combinations.append(combination)
                combination_name = first_col[i] + first_col[j]
                combination_names.append(combination_name)

        # Combine combination_names and combinations into a dictionary
        combined_data = dict(zip(combination_names, combinations))
        
        table = []
        for key, value in combined_data.items():
            significance = "*" if value > float(formatter(cd)) else "ns"
            table.append([key,value, significance])
            heads = ["Combinations", "Value", "Significance"]
            
        tanle = tabulate(table, headers=heads, tablefmt='grid')
        dat = pd.DataFrame(table)
        
        selected_combinations = dat.loc[dat[2] == '*', 0].tolist()

        greater_values = []
        for key, value in combined_data.items():
            comparison = "*" if value > 1 else "ns"
            if comparison == "*":
                greater_values.append(key)
        
    if savefile is None or savefile: 
        # Save the results in a text file
            directory_path = os.path.dirname(Inputfile)
            output_file_name = os.path.splitext(os.path.basename(Inputfile))[0]
            output_file_path = os.path.join(directory_path, f"{output_file_name}_result.txt")
        
            # Save the results in a text file
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(f"{output_file_name}: ")
                file.write("\n\n")
                file.write(f"Correction Factor: {formatter(correctionFactor)}\n")
                file.write(f"Total Sum of Square: {formatter(totalsum)}\n")
                file.write(f"Row Sum of Square: {formatter(rowSum)}\n")
                file.write(f"Error Sum of Square: {ErrorSum}\n")
                file.write(f"Row Mean Sum of Square: {formatter(rmss)}\n")
                file.write(f"Error Mean Sum of Square: {formatter(emss)}\n\n")
                file.write(tabulate(anova, headers='keys', tablefmt='grid'))
                file.write("\n\n")
                file.write(res)
                file.write("\n\n")
                if row_significance == " *":
                    file.write(f"Critical Difference: {formatter(cd)}\n\n")
                    file.write(tabulate(linked, headers= 'keys', tablefmt='grid'))
                    file.write("\n\n")
                    file.write("Comparing pairwise difference with Critical Difference:\n")
                    file.write(tanle)
                    file.write("\n\n")
                    file.write(f"Significant Combinations are: {str(selected_combinations)}")
                    
            print(f"Result saved in {output_file_path}")

    #Use of this in further use
    result = {
        "Title" : output_file_name,
        "global_dataframe" : anova,
        "cf": formatter(correctionFactor),
        "total_ss": formatter(totalsum),
        "row_ss": formatter(rowSum),
        "error_ss": formatter(ErrorSum),
        "row_df": rdf,
        "error_df": edf,
        "row_mss":formatter(rmss),
        "error_mss":formatter(emss),
        "total_df": tdf,
        "total_ss": formatter(totalsum),
        "CD" : cd if row_significance == " *" else "Nil",
        "sign_between" : selected_combinations if row_significance == " *" else "Nil"
    }

    return result