#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: <Keeman>
#Group Name: <...>
#Class: <PN2004Y>
#Date: <16/7/2021>
#Version: <...>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
#import matplotlib and numpy for data visualization
import matplotlib.pyplot as plt
import numpy as np

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################


#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
    def __init__(self):

        #load excel data (CSV format) to dataframe - 'df'
        dataframe = pd.read_csv('MonthyVisitors.csv')
        #show specific country dataframe
        sortCountry(dataframe)


#########################################################################
#CLASS Branch: End of Code
#########################################################################


#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):
    #Completely make a new dataframe for Part 2
    df_all = df.copy(deep=True)

    #print number of rows in dataframe
    print("There are " + str(len(df)) + " data rows read. \n")

    #display dataframe (rows and columns)
    SEAcountries = df.iloc[348:, 0:9]
    print(
        "The following dataframe for SEA from 2007 to 2017 are read as follows: \n"
    )
    print(SEAcountries)

    # removing the year and month
    Remove = SEAcountries.drop(columns=['Year', 'Month'])

    # convert from object to integer for calculation
    Remove[Remove.columns] = Remove[Remove.columns].astype(int)

    # use sum to add the number of visitors for each country
    TotalCountry = Remove.sum()

    #sort in descending order
    SortedCountries = TotalCountry.sort_values(ascending=False)

    # resetting the index back to default which also sets back the dtype to object
    SortedCountries = SortedCountries.reset_index()

    # since dtype is object, columns are addable
    SortedCountries.columns = ['Countries', 'Visitors']

    print(SortedCountries.head(3))

    #############################################################################

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:


    Top3 = SortedCountries.head(3)
    Countries = Top3['Countries']
    Visitors = Top3['Visitors']

    fig1, ax1 = plt.subplots()
    ax1.pie(Visitors,
            labels=Countries,
            autopct='%1.1f%%',
            shadow=False,
            startangle=90)
    ax1.axis(
        'equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
    ####################################################################################

    # Bar Graph
    #plt.rcdefaults()
    #fig, ax = plt.subplots()

    #countries = SortedCountries['Countries']
    #y_pos = np.arange(len(countries))
    #performance = SortedCountries['Visitors']

    #ax.barh(y_pos, performance,align='center')
    #ax.set_yticks(y_pos)
    # ax.set_yticklabels(countries)
    # ax.invert_yaxis()  # labels read top-to-bottom
    # ax.set_xlabel('Visitors')
    # ax.set_title('S.E.A Countries from 2007 to 2017')

    # plt.show()

    #########################################################################################
    # Part 2 extra
    #use a loop to execute until the user wants to exit
    while True:
        #extracting columns into different region
        year = df_all.iloc[:, 0]
        SEA2countries = df_all.iloc[:, 2:9]
        APRcountries = df_all.iloc[:, 9:14]
        SAPRcountries = df_all.iloc[:, 14:17]
        MERcountries = df_all.iloc[:, 17:20]
        EUcountries = df_all.iloc[:, 20:31]
        NAcountries = df_all.iloc[:, 31:33]
        AUScountries = df_all.iloc[:, 33:35]
        AFRcountries = df_all.iloc[:, 35:]

        #Testing to make sure columns are correct
        #print(SEA2countries.columns)
        #print(APRcountries.columns)
        #print(SAPRcountries.columns)
        #print(MERcountries.columns)
        #print(EUcountries.columns)
        #print(NAcountries.columns)
        #print(AUScountries.columns)
        #print(AFRcountries.columns)

        # a list containing all the different region dataframes
        DFs = [
            SEA2countries, APRcountries, SAPRcountries, MERcountries,
            EUcountries, NAcountries, AUScountries, AFRcountries
        ]
        # a list containing the different regions
        Regions = ['SEA', 'APR', 'SAPR', 'MER', 'EU', 'NA', 'AUS', 'AFR']
        # ask the user to input the region
        # use .join to add comma to each region
        temp = ','.join(Regions)
        #use .format to put Regions variable in the placeholder
        SelectedRegion = input(
            '\nThe available regions are {} \n Type exit to leave.\nPlease enter a region to continue: '
            .format(temp))

        # if user inputs exit, break the while loop
        if SelectedRegion == 'exit':
            break
        # if user enters a valid region, the region must be in the 'Regions' list
        elif SelectedRegion in Regions:

            # ask for the starting and ending year
            StartYear = int(input("Please enter start year: "))
            EndYear = int(input('Please enter end year: '))

            # Check if user enters a valid range for the years. e.g. starting year cannot be bigger or equal to ending year
            if EndYear > StartYear:
                # search for the index of the region from 'Regions'
                indexOfDf = Regions.index(SelectedRegion)
                # match the region index to the region dataframe index
                SelectedDf = DFs[indexOfDf]

                # add the 'Year' column to the selected dataframe, allow dataframe slicing at line 177 to 178
                SelectedDf['Year'] = year

                # filter the dataframe by the user's given year
                print(SelectedDf[(SelectedDf['Year'] >= StartYear)
                                 & (SelectedDf['Year'] <= EndYear)])
        # if user does not enter a valid range, e.g. year is bigger or equal to ending year, hint the user
            else:
                print('You did not enter a valid range')

        else:
            print('Region is not valid.')

    #display a specific country (Australia) in column #33
    # country_label = df.columns[33]
# print("\n\n" + country_label + "was selected.")

#display a sorted dataframe based on selected country
#print(" The" + country_label + "was sorted in ascending order. \n")
#sorted_df =df.sort_values(country_label,ascending=[0])
#print(sorted_df)

    return


#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':

    #Project Title
    print('######################################')
    print('# Data Analysis App - PYTHON Project #')
    print('######################################')

    #perform data analysis on specific excel (CSV) file
    DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################
