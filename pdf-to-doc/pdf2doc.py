import os
import cloudconvert
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('CLOUDCONVERT_API_KEY')
if not API_KEY:
    raise ValueError("CLOUDCONVERT_API_KEY no está configurada en el archivo .env")

pdf_folder = 'pdfs'
doc_folder = 'docs'

cloudconvert.configure(api_key=API_KEY, sandbox=False)

# Por si se borra o algo yo ke se
os.makedirs(doc_folder, exist_ok=True)

# Más sencillo que el programa lo mire y haga todo solo
for pdf_filename in os.listdir(pdf_folder):
    if not pdf_filename.lower().endswith('.pdf'):
        continue

    base_name = os.path.splitext(pdf_filename)[0]
    docx_filename = base_name + '.docx'
    docx_path = os.path.join(doc_folder, docx_filename)

    # Si ya existe el archivo .docx, saltar
    if os.path.exists(docx_path):
        print(f'Saltando "{pdf_filename}" (ya convertido).')
        continue

    print(f'Convirtiendo "{pdf_filename}"...')
    
    pdf_path = os.path.join(pdf_folder, pdf_filename)
    
    job = cloudconvert.Job.create(payload={
        "tasks": {
            'import-my-file': {
                'operation': 'import/upload',
                'name': 'Import PDF File',
                'filename': 'pasos_tipos_graficos.pdf'
            },
            'convert-my-file': {
                'operation': 'convert',
                'input': 'import-my-file',
                'input_format': 'pdf',
                'output_format': 'docx',
            },
            'export-my-file': {
                'operation': 'export/url',
                'input': 'convert-my-file'
            }
        }
    })
    # Gracias API por no tener la operación export/download
    upload_task_id = job['tasks'][0]['id']
    upload_task = cloudconvert.Task.find(id=upload_task_id)
    res = cloudconvert.Task.upload(file_name=pdf_path,  task=upload_task)

    cloudconvert.Job.wait(id=job['id'])

    job_result = cloudconvert.Job.find(id=job['id'])
    export_task = next(task for task in job_result['tasks'] if task['name'] == 'export-my-file')
    file_url = export_task['result']['files'][0]['url']

    response = requests.get(file_url)
    output_path = os.path.join(doc_folder, docx_filename)
    with open(output_path, 'wb') as f:
        f.write(response.content)

    print(f'Documento descargado en: {output_path}')