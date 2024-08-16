import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from tkinter import filedialog
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

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
        # Create a PDF document
        pdf = SimpleDocTemplate(file_path, pagesize=letter, leftMargin=100, rightMargin=100, topMargin=20, bottomMargin=20 )
        # Create a PDF document with margins (left, right, top, bottom)


        
        elements = []

        # Title
        styles = getSampleStyleSheet()
        title_style = styles['Heading1']
        title_style.alignment = 1  # Center alignment
        title = Paragraph("Restoration Request for ...................", title_style)
        elements.append(title)
        elements.append(Spacer(2, 10))

        # Custom style for table cells
        custom_style = ParagraphStyle(name='CustomStyle', fontSize=10, alignment=1, leading=12)

        # Table data with "No" column
        data_table = [
            [
                Paragraph("No", custom_style),
                Paragraph("Branch Name", custom_style), 
                Paragraph("Branch Code", custom_style), 
                Paragraph("User Data", custom_style), 
                Paragraph("Report Name", custom_style), 
                Paragraph("Required Date", custom_style),
                Paragraph("Remarks", custom_style) 
            ]
        ]
        
        # Add row numbers and other data
        sorted_data = sorted(data, key=lambda x: x['Required Date'], reverse=True)
        for i, item in enumerate(sorted_data, start=1):
            data_table.append([
                Paragraph(str(i), custom_style),  # "No" column
                Paragraph(item['Branch Name'], custom_style), 
                Paragraph(item['Branch Code'], custom_style), 
                Paragraph(item['User Data'], custom_style), 
                Paragraph(item['Report Name'], custom_style), 
                Paragraph(item['Required Date'].strftime('%d/%m/%Y'), custom_style),
                # Paragraph(item.get('Remarks', ''), custom_style)  # Add Remarks field if needed
            ])
        
        # Column widths (adjusted to fit the "No" column)
        col_widths = [30, 100, 45, 70, 100, 68, 120]

        # Create table
        table = Table(data_table, colWidths=col_widths)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.white),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
        ]))

        elements.append(table)
        pdf.build(elements)
        messagebox.showinfo("Success", f"Data saved to {file_path}")

# Initialize the data list
data = []

# Create the main window
root = tk.Tk()
root.title("Spool FIle Request Data Entry Application")

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
table = ttk.Treeview(root, columns=columns, show='headings')

for col in columns:
    table.heading(col, text=col)
    table.column(col, minwidth=0, width=120)

table.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Set the initial focus to the first input field
entry_branch_name.focus_set()

# Start the main event loop
root.mainloop()


