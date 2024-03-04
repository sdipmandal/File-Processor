import os
import csv
import pandas as pd

def read_files(folder):
    """
    The function `read_files` reads all `.dat` files in a specified folder and returns their contents as
    a list of lines for each file.
    
    :param folder: The `folder` parameter in the `read_files` function is the directory path where the
    function will look for files with a `.dat` extension to read
    :return: The function `read_files` returns a list of lists, where each inner list contains the lines
    of text data from a file with a ".dat" extension in the specified folder.
    """
    files_data = []
    for file in os.listdir(folder):
        if file.endswith(".dat"):
            file_path = os.path.join(folder, file)
            with open(file_path, "r") as fread:
                data = fread.readlines()
                files_data.append(data)
    
    return files_data

def process_data(files_data):
    """
    The function `process_data` takes a list of files data, extracts unique lines from each file, and
    returns a set of processed data and a list of unique headers.
    
    :param files_data: The `files_data` parameter is expected to be a list of lists where each inner
    list represents data from a file. The first element of each inner list is considered as the header,
    and the subsequent elements are the lines of data in that file
    :return: The function `process_data` returns a tuple containing two elements:
    1. `processed_data`: a set of processed data lines with leading and trailing whitespaces removed.
    2. `headers`: a list of unique headers extracted from the first element of each data entry in
    `files_data`.
    """
    processed_data = set()
    headers = set()
    for data in files_data:
        headers.add(data[0])
        for line in data[1:]:
            processed_data.add(line.strip())

    return processed_data, list(headers)

def write_to_csv(processed_data, output_folder, headers):
    """
    The function writes processed data to a CSV file, calculates the second highest salary, average
    salary, and appends these values to the CSV file.
    
    :param processed_data: Processed data is the data that has been cleaned, transformed, or manipulated
    in some way to prepare it for analysis or presentation. It could be a list of strings where each
    string represents a row of data with values separated by tabs
    :param output_folder: The `output_folder` parameter is the directory path where the output CSV file
    will be saved. If the directory does not exist, the code will create it before writing the CSV file
    :param headers: The `headers` parameter in the `write_to_csv` function is a list containing the
    column headers for the CSV file. Each header is separated by a tab character ('\t')
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_file = os.path.join(output_folder, 'output.csv')
    header = headers[0].split('\t')
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for line in processed_data:
            writer.writerow(line.split('\t'))
        
        df = pd.DataFrame([x.split('\t') for x in processed_data], columns=header)
        
        second_highest_salary = df['basic_salary'].astype(int).unique()[1]
        average_salary = df['basic_salary'].astype(int).mean()

        writer.writerow(['Second Highest Salary:', second_highest_salary])
        writer.writerow(['Average Salary:', average_salary])


def main(input_folder, output_folder):
    """
    The main function reads files from an input folder, processes the data, and writes the processed
    data to a CSV file in an output folder.
    
    :param input_folder: The `input_folder` parameter in the `main` function is the directory path where
    the input files are located. This is where the function `read_files` will read the data from
    :param output_folder: The `output_folder` parameter in the `main` function is the directory path
    where the processed data will be saved as a CSV file. This is where the `write_to_csv` function will
    write the processed data along with the headers
    """
    files_data = read_files(input_folder)
    processed_data, headers = process_data(files_data)
    write_to_csv(processed_data, output_folder, headers)

if __name__ == "__main__":
    input_folder = "input_data"
    output_folder = "output_data"
    main(input_folder, output_folder)
