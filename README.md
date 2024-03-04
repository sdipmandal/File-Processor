# File-Processor
Objective:

The File Processor system is designed to efficiently read data from multiple files in a specified folder, process the data, and generate a CSV file with specific requirements. The system aims to handle large volumes of data while ensuring accuracy, reliability, and maintainability.

Functional Requirements:

Input Handling: The system should traverse the designated folder and identity files for processing. It should support file formats like .dat.
Data Parsing: The system should parse each file and extract relevant data. It should handle different data structures and formats within files.
Data Processing: Process the extracted data to remove duplicates, perform any necessary transformations and calculate required statistics such as the second-highest salary and average salary.
CSV Generation: Generate a CSV file with processed data, ensuring proper formatting, including headers and footers with statistical information.

Overall Architecture:
Input Module: Responsible for scanning the input folder, identifying files and initiating the processing pipeline.
Processing Module: Handles data parsing, processing and generation of the output CSV file. Utilizes appropriate data structures and algorithms for efficient processing.
Output Module: Manages the generation and writing of the output CSV file to the designated folder. Ensures proper formatting and includes necessary headers and footers.

Conclusion:
The File Processor system is a component for batch processing tasks. By adhering to the outlined design specifications and requirements, the system will efficiently handle file processing tasks while ensuring accuracy, reliability and scalability. It provides a solid foundation for future enhancements and maintenance, contributing to overall system effectiveness and performance. 
