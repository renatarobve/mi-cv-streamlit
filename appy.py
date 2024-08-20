import streamlit as st



#Foto del CV
col1, col2 = st.columns([1, 2.2]) # The ratio [1, 2] means col2 is twice as wide as col1.

with col1:
    
    st.image("Foto tamaño pasaporte.png", width=160)
    st.subheader("Información de Contacto")
    st.write("""
    **Nombre:** Renata Sofía Robles Velasco  
    **Celular:** +52 3317888053   
    **Email:** renatarobve@gmail.com  
    **LinkedIn:** [renata-roblesv](http://linkedin.com/in/renata-roblesv)
    """)
    st.subheader("Idiomas")
    st.write("""
             * Nivel de Inglés: C1
             * Nivel de Frances: B2
             * Nivel de Italiano: A2
             """)
    
    st.subheader("Habilidades")
    st.write("""
             * Excel: Nivel Intermedio
             * Elaboración de Estados Financieros
             * Elaboración de declaraciones Anuales
             * Manejo de Microsoft Office
             * Presupuestación
             * Manejo de PowerBi para análisis de datos y conciliación
             """)

with col2:
    # Basic Info
    st.title("Estudiante de Administración y Finanzas")
    

    # Summary or Objective
    st.header("Aptitudes")
    st.write("""
    * Trabajo colaborativo
    * Resolución de problemas 
    * Actitud proactiva e iniciativa
    * Gran capacidad de comunicación
    * Adaptación al cambio
    * Buena capacidad de análisis y organización para poder llevar a cabo las tareas pendientes
    """)

    # Work Experience
    st.header("Experiencia Laboral")
    st.subheader("Financial Strategy Intern")
    st.write("""
    *Wispok, Guadalajara Jalisco*  
    *Mayo 2023 - Febrero 2024*  
    * Elaboración de estudios macroeconómicos
    * Elaboración de proyecciones financieras para rondas de levantamiento de capital (Venture Capital)
    * Estudios de viabilidad económica, legal y técnica para productos de financiamiento y método de pago
    * Conciliación de pagos
    * Elaboración y métricas operativas del funcionamiento de la empresa (KPIs)
    * Perfilación de transacciones y estudio de bases de datos para identificación de transacciones inusuales
    """)

    st.subheader("Elaboración de declaraciones anuales y mensuales")
    st.write("""
    *Negocio familiar, Guadalajara Jalisco*  
    *2020 - Actualidad*  
    * Elaboración de declaraciones anuales para el negocio familiar 
    * Conocimiento de contabilidad para elaboración y entendimiento de los estados financieros
    """)

    # Education
    st.header("Historial Académico")
    st.subheader("Especialidad en Gestión de Carteras")
    st.write("""
    *Afi Escuela, Madrid España*  
    *Julio 2024*  
    Técnicas de gestión de carteras y patrimonio mediante análisis macroeconómico de mercado, con investigación en distintos vehículos de inversión que se adapten a las necesidades de cada perfil de inversionista. 
    """)

    st.subheader("Semestre de Intercambio en Universidad de Florencia")
    st.write("""
    *Universidad de Estudios de Florencia, Florencia Italia*  
    *Junio 2024*  
    """)


    st.subheader("Licenciatura en Administración y Finanzas")
    st.write("""
    *Universidad Panamericana, Campus Guadalajara*  
    *Agosto 2021 - Actualidad*  
    """)


    # Footer
    st.write("### ¡Gracias por revisar mi CV!")

