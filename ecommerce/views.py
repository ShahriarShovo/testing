from django.http import HttpResponse
from docx import Document

def open_docx(request, docx_path):
    # Replace 'docx_path' with the actual path to your DOCX file
    doc = Document(docx_path)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename="{docx_path}"'

    # Save the content of the DOCX file to the response
    doc.save(response)

    return response

