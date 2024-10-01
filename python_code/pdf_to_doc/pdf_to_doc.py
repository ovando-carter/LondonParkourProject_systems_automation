# pip install pdf2docx


# Import the required modules
from pdf2docx import Converter

# Keeping the PDF's location in a separate variable
pdf_file = r&quot;C:/Users/apple/Documents/corporate_organisation/systems_automation/program/python_code/pdf_to_doc Invoice_Test.pdf&quot

# Maintaining the Document's path in a separate variable
docx_file = r&quot;C:/Users/apple/Documents/corporate_organisation/systems_automation/program/python_code/pdf_to_doc Invoice_Test.doc&quot

# Using the built-in function, convert the PDF file to a document file by saving it in a variable.
cv = Converter(pdf_file)

# Storing the Document in the variable's initialised path
cv.convert(docx_file)

# Conversion closure through the function close()
cv.close()
