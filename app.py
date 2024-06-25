import streamlit as st
import pandas as pd

def formatear_preguntas(input_file):
    # Leer las preguntas desde el archivo de entrada
    preguntas = pd.read_excel(input_file)

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
            ("<p>" + row['DESCRIPCIÓN DE LA PREGUNTA'] + "</p>") if row['DESCRIPCIÓN DE LA PREGUNTA'] != "" else " ", 
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
    df_output = pd.DataFrame(formatted_data)
    
    return df_output

# Interfaz de Streamlit
st.title("Formato Quizes TutorLMS - IQ-Est Academy")

# Cargar el archivo de entrada
uploaded_file = st.file_uploader("Sube el archivo de preguntas en formato Excel", type=["xlsx"])

if uploaded_file is not None:
    # Formatear las preguntas
    df_output = formatear_preguntas(uploaded_file)

    # Mostrar el DataFrame formateado
    st.write("Archivo formateado:")
    st.dataframe(df_output)
    
    # Descargar el archivo de salida
    st.download_button(
        label="Descargar archivo formateado",
        data=df_output.to_csv(index=False, header=False).encode('utf-8'),
        file_name='tutor-quiz-formateado.csv',
        mime='text/csv'
    )
