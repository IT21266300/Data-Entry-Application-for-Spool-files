## Data Entry Application

### Overview

This Data Entry Application is a simple, user-friendly tool designed for managing and organizing data entries. The application allows users to input and sort data including branch name and code, user data, report name, required date, and remarks. The data is displayed in a tabular format and can be sorted by the required date in descending order. Additionally, the application provides the functionality to print the data table to a PDF file.

### Features

- **Data Entry**: Input fields for branch name, branch code, user data, report name, required date (in DD/MM/YYYY format), and remarks.
- **Automatic Uppercase Conversion**: Automatically converts user data and report name to uppercase for consistency.
- **Data Sorting**: Sorts data entries by the required date in descending order.
- **PDF Export**: Exports the data table to a PDF file, ready for printing.
- **Keyboard Navigation**: Facilitates easy navigation through the input fields using the `Tab` key, while skipping non-essential fields like remarks and action buttons.
- **Toggle Print Button**: The "Print Table" button is initially hidden and can be toggled using the `Ctrl+P` keyboard shortcut.

### How to Use

1. **Data Entry**: Fill in the required fields and click the "Add Data" button.
2. **Sort and Display**: After adding data, click the "Sort and Display Data" button to view the sorted table.
3. **Print Table**: Use the `Ctrl+P` shortcut to reveal the "Print Table" button, and then click it to save the table as a PDF file.

### Installation

1. Ensure you have Python 3.x installed on your machine.
2. Install the required libraries using:
   ```sh
   pip install tkinter reportlab
   ```
3. Run the application:
   ```sh
   python data_entry_app.py
   ```

### Requirements

- Python 3.x
- `tkinter` for GUI
- `reportlab` for PDF generation

### Screenshots

(Add screenshots here to showcase the application interface and features)

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

### Contribution

Feel free to contribute to this project by submitting issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

### Author

This application was developed K.M.V. Thejan Bandara.

