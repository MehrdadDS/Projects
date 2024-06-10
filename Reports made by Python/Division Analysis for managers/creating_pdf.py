import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

def create_chart(data, title):
    plt.figure(figsize=(6, 4))
    plt.plot(data)
    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Save the chart as an image
    file_path = f"{title.lower().replace(' ', '_')}.png"
    plt.savefig(file_path)
    plt.close()
    return file_path

def create_pdf_with_charts(file_path):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # Add title
    c.setFont("Helvetica-Bold", 24)
    c.drawString(100, height - 50, "Meeting Agenda")

    # Add agenda items with links
    c.setFont("Helvetica", 12)
    agenda_items = [
        ("1. Division Level", "division_level"),
        ("2. Terminal Level", "terminal_level"),
        ("3. Customer Level", "customer_level"),
        ("4. Call Outs", "call_outs")
    ]
    
    y_position = height - 100
    for item, link in agenda_items:
        c.drawString(100, y_position, item)
        c.linkRect("", link, (100, y_position - 5, 200, y_position + 5))
        y_position -= 20

    # Create content sections with charts
    sections = [
        ("Division Level", "division_level", [1, 2, 3, 4, 5]),
        ("Terminal Level", "terminal_level", [2, 3, 4, 5, 6]),
        ("Customer Level", "customer_level", [3, 4, 5, 6, 7]),
        ("Call Outs", "call_outs", [4, 5, 6, 7, 8])
    ]

    for title, bookmark, data in sections:
        c.bookmarkPage(bookmark)
        c.showPage()
        c.setFont("Helvetica-Bold", 18)
        c.drawString(100, height - 50, title)

        # Create and add the chart image
        chart_path = create_chart(data, title)
        chart = ImageReader(chart_path)
        c.drawImage(chart, 100, height - 350, width=400, height=300, preserveAspectRatio=True)

    # Save the PDF
    c.save()

# Specify the file path
file_path = "meeting_agenda_with_charts.pdf"
create_pdf_with_charts(file_path)
