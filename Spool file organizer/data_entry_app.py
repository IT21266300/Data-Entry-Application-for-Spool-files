import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from tkinter import filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to add data to the list
def add_data():
    branch_name = entry_branch_name.get()
    branch_code = entry_branch_code.get()
    user_data = entry_user_data.get().upper()  # Convert to uppercase
    report_name = entry_report_name.get().upper()  # Convert to uppercase
    required_date = entry_required_date.get()
    # remarks = entry_remarks.get()

    # Validate date format
    try:
        required_date_obj = datetime.strptime(required_date, '%d/%m/%Y')
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter a valid date in DD/MM/YYYY format")
        return

    # Add data to the list
    data.append({
        "Branch Name": branch_name,
        "Branch Code": branch_code,
        "User Data": user_data,
        "Report Name": report_name,
        "Required Date": required_date_obj,
        # "Remarks": remarks
    })

    # Clear entry fields
    entry_branch_name.delete(0, tk.END)
    entry_branch_code.delete(0, tk.END)
    entry_user_data.delete(0, tk.END)
    entry_report_name.delete(0, tk.END)
    entry_required_date.delete(0, tk.END)
    # entry_remarks.delete(0, tk.END)

    messagebox.showinfo("Success", "Data added successfully")

    # Enable the buttons after adding data
    button_sort_and_display.config(state=tk.NORMAL)
    button_print_table.config(state=tk.NORMAL)

    # Update table
    update_table()

# Function to sort and display data
def update_table():
    # Clear the table
    for row in table.get_children():
        table.delete(row)
    
    # Sort data by date in descending order
    sorted_data = sorted(data, key=lambda x: x['Required Date'], reverse=True)
    
    # Add sorted data to the table
    for item in sorted_data:
        table.insert('', 'end', values=(
            item['Branch Name'], 
            item['Branch Code'], 
            item['User Data'], 
            item['Report Name'], 
            item['Required Date'].strftime('%d/%m/%Y'), 
            # item['Remarks']
        ))

# Function to print the table to PDF
def print_table():
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", 
                                             filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")])
    if file_path:
        c = canvas.Canvas(file_path, pagesize=letter)
        width, height = letter
        y = height - 40

        # Title
        c.setFont("Helvetica-Bold", 12)
        c.drawString(30, y, "Restoration Report")
        y -= 20

        # Table header
        c.setFont("Helvetica-Bold", 10)
        headers = ["Branch Name", "Branch Code", "User Data", "Report Name", "Required Date"]
        # headers = ["Branch Name", "Branch Code", "User Data", "Report Name", "Required Date", "Remarks"]
        x = 30
        for header in headers:
            c.drawString(x, y, header)
            x += 100

        y -= 20

        # Table content
        c.setFont("Helvetica", 10)
        sorted_data = sorted(data, key=lambda x: x['Required Date'], reverse=True)
        for item in sorted_data:
            x = 30
            row = [
                item['Branch Name'], 
                item['Branch Code'], 
                item['User Data'], 
                item['Report Name'], 
                item['Required Date'].strftime('%d/%m/%Y'), 
                # item['Remarks']
            ]
            for value in row:
                c.drawString(x, y, value)
                x += 100
            y -= 20

            # Create new page if the content exceeds one page
            if y < 40:
                c.showPage()
                y = height - 40

        c.save()
        messagebox.showinfo("Success", f"Data saved to {file_path}")

# Initialize the data list
data = []

# Create the main window
root = tk.Tk()
root.title("Data Entry Application")

# Frame for data entry fields
frame_entry = tk.Frame(root)
frame_entry.pack(padx=10, pady=10, fill=tk.X)

# Create and place the input fields and labels
tk.Label(frame_entry, text="Branch Name").grid(row=0, column=0)
entry_branch_name = tk.Entry(frame_entry)
entry_branch_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_entry, text="Branch Code").grid(row=1, column=0)
entry_branch_code = tk.Entry(frame_entry)
entry_branch_code.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_entry, text="User Data").grid(row=2, column=0)
entry_user_data = tk.Entry(frame_entry)
entry_user_data.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_entry, text="Report Name").grid(row=3, column=0)
entry_report_name = tk.Entry(frame_entry)
entry_report_name.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame_entry, text="Required Date (DD/MM/YYYY)").grid(row=4, column=0)
entry_required_date = tk.Entry(frame_entry)
entry_required_date.grid(row=4, column=1, padx=5, pady=5)

# tk.Label(frame_entry, text="Remarks").grid(row=5, column=0)
# entry_remarks = tk.Entry(frame_entry)
# entry_remarks.grid(row=5, column=1, padx=5, pady=5)

# Frame for buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack(padx=10, pady=10, fill=tk.X)

# Create and place the buttons
tk.Button(frame_buttons, text="Add Data", command=add_data).grid(row=0, column=0, padx=5, pady=5)
button_sort_and_display = tk.Button(frame_buttons, text="Sort and Display Data", command=update_table, state=tk.DISABLED)
# button_sort_and_display.grid(row=0, column=1, padx=5, pady=5)
button_print_table = tk.Button(frame_buttons, text="Print Table", command=print_table, state=tk.DISABLED)
button_print_table.grid(row=0, column=2, padx=5, pady=5)

# Create the table view
columns = ("Branch Name", "Branch Code", "User Data", "Report Name", "Required Date")
# columns = ("Branch Name", "Branch Code", "User Data", "Report Name", "Required Date", "Remarks")
table = ttk.Treeview(root, columns=columns, show='headings')

for col in columns:
    table.heading(col, text=col)
    table.column(col, minwidth=0, width=120)

table.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Set the initial focus to the first input field
entry_branch_name.focus_set()

# Start the main event loop
root.mainloop()
