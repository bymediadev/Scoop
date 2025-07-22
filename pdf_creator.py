from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_pdf(profile, path):
    c = canvas.Canvas(str(path), pagesize=letter)
    c.setFont("Helvetica", 12)
    y = 750

    def write_line(label, text, y_offset=15):
        nonlocal y
        c.drawString(50, y, f"{label}:")
        y -= y_offset
        for line in text.split('\n'):
            c.drawString(60, y, line)
            y -= y_offset
            if y < 50:
                c.showPage()
                y = 750

    write_line("Guest", profile['guest_name'])
    write_line("Company", profile['company'])
    write_line("Bio", profile['bio'])
    write_line("Insight Summary", profile['insight_summary'])
    write_line("Company Summary", profile['company_summary'])

    c.drawString(50, y, "Generated Questions:")
    y -= 20
    for q in profile['draft_questions']:
        c.drawString(60, y, f"- {q}")
        y -= 15
        if y < 50:
            c.showPage()
            y = 750

    c.save()
