import csv
import pandas as pd

#File paths
search_path = 'quarantine.csv'
sort_path_all = 'all_filtered_quarantine.csv'

#User filter method inputs
def ask_input():
    """
    Ask for user how to sort the Quartine file
    """
    ask_for_filer = str(input('Wanna filter all data or specifical one(Yes/No): ')).lower()
    if ask_for_filer == 'yes':
        sort_data_all(search_path, sort_path_all)
    else:
        ask_how_to = str(input('Sort by option one: Type or option two: Type, "SenderAddress(One/Two): ')).lower()
        if ask_how_to == 'two':
            sort_data_ty_send(search_path, sort_path_all)
        else:
            sort_by_type = str(input('Eneter sorting types(spam, malware, high confidence phish, bulk, phish): ')).title()
            sort_data_type(search_path, sort_path_all, sort_by_type)
 
        
#Read the file and write it to correct format
def remove_quotes(path):
    """Read the file, and remove all quotes. Make csv file readeble to dataframe

    Args:
        path (string): Give a file path or use a path variable
    """

    with open(path, 'r', encoding='utf-8') as sp:
        text_input = sp.read()
        converted_text = text_input.replace('"', '')
        print(converted_text)
        with open(path, 'w', encoding='utf-8') as fp:
            fp.write(converted_text)
    ask_input()      

#Read the file and find, does quotes exists
def get_quotes(path):
    """Read file does it have quetes, 
    if it does exetues function to remove quotes else strat sorting

    Args:
        path (string): Give file name or file path
    """
    with open(path, 'r', encoding='utf-8') as sp:
        text_input = sp.read()
        if '"' in text_input:
            remove_quotes(search_path)
            
        else:
            print('File does not have')
            ask_input()
        
#Filter functions
def sort_data_all(path, sorted_out):
    """Sort by given csv file data and group by 'Type', 'SenderAddress', 'Subject'

    Args:
        path (string): Give a file name with variable where to read csv file
        sorted_out (string): Give a file name variable where to write sorted data
    """
    df = pd.read_csv(path, sep=';', usecols=range(4))
    df = df.groupby(['Type', 'SenderAddress', 'Subject']).size().reset_index(name='TimesSent')
    df.to_csv(sorted_out, sep=';', encoding='utf-8')
    print(df)

def sort_data_ty_send(path, sorted_out):
    """Sort by given csv file data and group by 'Type', 'SenderAddress'

    Args:
        path (string): Give a file name with variable where to read csv file
        sorted_out (string): Give a file name variable where to write sorted data
    """
    df = pd.read_csv(path, sep=';', usecols=range(4))
    df = df.groupby(['Type', 'SenderAddress']).size().reset_index(name='TimesSent')
    df.to_csv(sorted_out, sep=';', encoding='utf-8')

def sort_data_type(path, sorted_out, sort_by):
    """Sort by given type(spam, malware, high confidence phish, bulk, phish) fiven csv file data and group by 'Type', 'Sender'

    Args:
        path (string): Give a file name with variable where to read csv file
        sorted_out (string): Give a file name variable where to write sorted data
        sort_by (string): Give a string value to search from column
    """
    df = pd.read_csv(path, sep=';', usecols=range(4))
    df = df[df['Type'].str.startswith(sort_by)].groupby(['Type','SenderAddress']).size().reset_index(name='TimesSent')
    df.to_csv(sorted_out, sep=';', encoding='utf-8')

#Exetues function called get_quetes()
if __name__ == '__main__':
    quarantine_filter = get_quotes(search_path)