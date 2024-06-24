import pandas as pd

import pandas as pd

# Importar las preguntas desde el archivo de entrada
input_file_path = r"C:\Users\vhgar\OneDrive\Desktop\ScriptTutorLSM\Entrada.xlsx"
preguntas = pd.read_excel(input_file_path)

# Crear una lista para almacenar las filas formateadas
formatted_data = []

# Añadir la fila de encabezado fija
header = ["settings", "TÍTULO DE LA LECCIÓN", "RESUMEN DE LA LECCIÓN", 0, "minutes", "", 0, 80, 10, "", "", "rand", 200]
formatted_data.append(header)

# Iterar sobre las filas del DataFrame de entrada y formatearlas
for idx, row in preguntas.iterrows():
    question_row = [
        "question", 
        row['PREGUNTA'], 
        "<p>" + row['DESCRIPCIÓN DE LA PREGUNTA'] + "</p>", 
        "single_choice", 
        1, 
        idx + 1, 
        "", 
        1, 
        "",  
        '<p><br data-mce-bogus="1"></p>'
    ]
    formatted_data.append(question_row)

    # Crear filas de respuestas (4 filas)
    for j in range(4):
        answer_row = [
            "answer", 
            row['OPCION CORRECTA'] if j == 0 else row[f'OPCION INCORRECTA.{j-1}' if j > 1 else 'OPCION INCORRECTA'], 
            "text", 
            1 if j == 0 else "", 
            0, 
            "", 
            j + 1, 
            "", 
            "", 
            "", 
            "", 
            "", 
            ""
        ]
        formatted_data.append(answer_row)

# Convertir la lista formateada en un DataFrame de pandas
#columns = ["settings", "TÍTULO DE LA LECCIÓN", "RESUMEN DE LA LECCIÓN", 0, "minutes", "", 0, 80, 10, "", "", "rand", 200]
df_output = pd.DataFrame(formatted_data)

# Guardar el DataFrame de salida en un archivo Excel
output_file_path = r"C:\Users\vhgar\OneDrive\Desktop\ScriptTutorLSM\tutor-quiz-formateado.csv"
df_output.to_csv(output_file_path, index=False, header=False)

print(f"Nuevo archivo Excel creado en: {output_file_path}")
