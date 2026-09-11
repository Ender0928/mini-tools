import requests

def buscar_libros_open_library(titulo):
    url = f"http://openlibrary.org/search.json"
    params = {'title': titulo}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        libros = response.json().get('docs', [])
        resultados = []
        for libro in libros:
            titulo_libro = libro.get('title', 'Sin título')
            autores = libro.get('author_name', ['Autor desconocido'])
            edicion_key = libro.get('key', '').split('/')[-1]
            enlace_lectura = f"https://openlibrary.org/books/{edicion_key}" if edicion_key else "No disponible"
            resultados.append({
                'titulo': titulo_libro,
                'autores': ', '.join(autores),
                'enlace_lectura': enlace_lectura
            })
        return resultados
    else:
        return []

# Ejemplo de uso
titulo_a_buscar = "Un mundo feliz"
libros = buscar_libros_open_library(titulo_a_buscar)
for i, libro in enumerate(libros, 1):
    print(f"{i}. Título: {libro['titulo']}\n   Autor(es): {libro['autores']}\n   Enlace de lectura: {libro['enlace_lectura']}\n")

