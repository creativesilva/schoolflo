"""English to Spanish strings for the PVHS Digital Media site.

Keys are English text segments exactly as they appear on the page (whitespace collapsed).
A key written "page.html::Text" applies only on that page and wins over the plain key
(used where a title is split over two lines and Spanish word order differs).
KEEP lists segments that stay the same in both languages (names, brands, links).
Student facing Spanish uses "tu" and plain, clear wording.
Never use em or en dashes in either language."""

KEEP = {
    "PVHS Digital Media", "Pioneer Valley High School", "SkillsUSA", "Light Writerz", "SchoolFlo",
    "EN", "ES", "F", "Language / Idioma", "Santa Maria, CA", "· Santa Maria, CA",
    "UC / CSU a-g", "a-g “F”",
    "Chris Silva", "Laura Garcia", "Rileigh Mankin",
    "Ella Naoe", "Gregorio Calleja", "Julio Marquez", "Davina Royall Showalter", "Jessica Valdez",
    "www.creativesilva.com", "www.chrisandlaura.com",
}

ES = {
    # ---------- Split titles (page specific word order)
    "index.html::Digital": "Medios",
    "index.html::Media": "Digitales",
    "digital-photography.html::Digital": "Fotografía",
    "digital-photography.html::Photography": "Digital",
    "digital-arts.html::Digital": "Artes",
    "digital-arts.html::Arts": "Digitales",
    "teachers.html::Our": "Nuestros",
    "teachers.html::Teachers": "Maestros",

    # ---------- Page titles and descriptions
    "PVHS Digital Media | Pioneer Valley High School": "PVHS Digital Media | Pioneer Valley High School",
    "Digital Photography | PVHS Digital Media": "Fotografía Digital | PVHS Digital Media",
    "Digital Arts | PVHS Digital Media": "Artes Digitales | PVHS Digital Media",
    "Our Teachers | PVHS Digital Media": "Nuestros Maestros | PVHS Digital Media",
    "Sign Up | PVHS Digital Media": "Inscríbete | PVHS Digital Media",
    "Digital Media at Pioneer Valley High School: Digital Photography and Digital Arts. Career Technical Education in Arts, Media, and Entertainment.":
        "Medios Digitales en Pioneer Valley High School: Fotografía Digital y Artes Digitales. Educación Técnica Profesional en Artes, Medios y Entretenimiento.",
    "Photography 1 and Photography 2 at Pioneer Valley High School: Manual mode, RAW, Lightroom Classic, lighting, and studio work.":
        "Fotografía 1 y Fotografía 2 en Pioneer Valley High School: modo manual, RAW, Lightroom Classic, iluminación y trabajo de estudio.",
    "Digital Arts 1 and Digital Arts 2 at Pioneer Valley High School: design foundations, Adobe Illustrator and Photoshop, branding, and portfolio work.":
        "Artes Digitales 1 y Artes Digitales 2 en Pioneer Valley High School: bases del diseño, Adobe Illustrator y Photoshop, identidad de marca y portafolio.",
    "Meet the Digital Media teachers at Pioneer Valley High School: Chris Silva, Laura Garcia, and Rileigh Mankin.":
        "Conoce a los maestros de Medios Digitales de Pioneer Valley High School: Chris Silva, Laura Garcia y Rileigh Mankin.",
    "Interest form for Digital Photography and Digital Arts at Pioneer Valley High School.":
        "Formulario de interés para Fotografía Digital y Artes Digitales en Pioneer Valley High School.",

    # ---------- Header, nav, footer
    "Skip to content": "Saltar al contenido",
    "PVHS Digital Media home": "Inicio de PVHS Digital Media",
    "Pioneer Valley High School Panthers logo": "Logotipo de los Panthers de Pioneer Valley High School",
    "Main": "Principal",
    "Open menu": "Abrir menú",
    "Menu": "Menú",
    "Digital Media": "Medios Digitales",
    "Digital Photography": "Fotografía Digital",
    "Digital Arts": "Artes Digitales",
    "Our Teachers": "Nuestros Maestros",
    "Sign Up": "Inscríbete",
    "Sign up": "Inscríbete",
    "Learn it. Make it.": "Apréndelo. Créalo.",
    "Present it.": "Preséntalo.",
    "Career Technical Education in Arts, Media, and Entertainment at Pioneer Valley High School. Design, Visual, and Media Arts pathway.":
        "Educación Técnica Profesional en Artes, Medios y Entretenimiento en Pioneer Valley High School. Trayectoria de Diseño, Artes Visuales y Medios.",
    "Program Overview": "Resumen del programa",
    "Courses": "Clases",
    "Connect": "Conecta",
    "Light Writerz Photo Club": "Club de fotografía Light Writerz",
    "PVHS Digital Media · Pioneer Valley High School": "PVHS Digital Media · Pioneer Valley High School",
    "Hosted on": "Alojado en",
    "Staff login": "Acceso para el personal",

    # ---------- Course and program names
    "Photography": "Fotografía",
    "Photography 1": "Fotografía 1",
    "Photography 2": "Fotografía 2",
    "Photography 1 & 2": "Fotografía 1 y 2",
    "Digital Arts 1": "Artes Digitales 1",
    "Digital Arts 2": "Artes Digitales 2",
    "Digital Arts 1 & 2": "Artes Digitales 1 y 2",
    "Photography 1 & 2 · Digital Arts 1": "Fotografía 1 y 2 · Artes Digitales 1",
    "Photography & Digital Arts": "Fotografía y Artes Digitales",
    "Sign up for Photography 1": "Inscríbete en Fotografía 1",
    "Sign up for Photography 2": "Inscríbete en Fotografía 2",
    "Sign up for Digital Arts 1": "Inscríbete en Artes Digitales 1",
    "Sign up for Digital Arts 2": "Inscríbete en Artes Digitales 2",

    # ---------- Home
    "Pioneer Valley High School · CTE Pathway": "Pioneer Valley High School · Trayectoria CTE",
    "Real cameras. Industry software. Professional habits. Taught by CTE teachers with real industry experience, and it counts as your a-g “F” fine art.":
        "Cámaras reales. Programas profesionales. Hábitos de trabajo profesionales. Con maestros de CTE con experiencia real en la industria, y cuenta como tu arte “F” de a-g.",
    "Meet the team": "Conoce al equipo",
    "The PVHS photo club": "El club de fotografía de PVHS",
    "About the program": "Sobre el programa",
    "Hands on, not lectures": "Aprender haciendo, no solo escuchando",
    "Digital Media at Pioneer Valley is a Career Technical Education program in the Arts, Media, and Entertainment sector, inside the Design, Visual, and Media Arts pathway.":
        "Medios Digitales en Pioneer Valley es un programa de Educación Técnica Profesional (CTE) del sector de Artes, Medios y Entretenimiento, dentro de la trayectoria de Diseño, Artes Visuales y Medios.",
    "Students learn industry standard tools and professional habits through hands on projects. By the end of the pathway, a student can operate real equipment, run a professional edit and deliver workflow, and present finished creative work.":
        "Los estudiantes aprenden herramientas profesionales y buenos hábitos de trabajo con proyectos prácticos. Al terminar la trayectoria, un estudiante sabe usar equipo real, editar y entregar su trabajo como un profesional, y presentar obras creativas terminadas.",
    "Bilingual materials.": "Materiales bilingües.",
    "Project directions and handouts are offered in English and Spanish, and students may submit their work in either language.":
        "Las instrucciones de los proyectos y las hojas de trabajo están en inglés y en español, y los estudiantes pueden entregar su trabajo en cualquiera de los dos idiomas.",
    "A Mac lab.": "Un laboratorio de Mac.",
    "Students work on Macs, with a school iPad that doubles as a scanner for sketches and hand done work.":
        "Los estudiantes trabajan en computadoras Mac, con un iPad de la escuela que también sirve como escáner para bocetos y trabajos hechos a mano.",
    "Fine arts credit.": "Crédito de bellas artes.",
    "Courses satisfy the UC and CSU a-g “F” Visual and Performing Arts requirement.":
        "Las clases cumplen con el requisito “F” de Artes Visuales y Escénicas de a-g para UC y CSU.",
    "Open to everyone.": "Abierto para todos.",
    "Photography 1 and Digital Arts 1 need no experience.": "Fotografía 1 y Artes Digitales 1 no requieren experiencia.",
    "Student work: a student in a blue sweater surrounded by loops of light, a light painting photograph":
        "Trabajo estudiantil: un estudiante con suéter azul rodeado de líneas de luz, una fotografía de pintura con luz",
    "Student work: writing with light, a long exposure project.": "Trabajo estudiantil: escribir con luz, un proyecto de exposición larga.",
    "Visual & Performing Arts": "Artes Visuales y Escénicas",
    "College ready elective": "Optativa que te prepara para la universidad",
    "The “F” in a-g": "La “F” de a-g",
    "Our Photography and Digital Arts courses satisfy the UC and CSU a-g “F” Visual and Performing Arts requirement.":
        "Nuestras clases de Fotografía y Artes Digitales cumplen con el requisito “F” de Artes Visuales y Escénicas de a-g para UC y CSU.",
    "To be eligible for the University of California and California State University, students need a year of Visual and Performing Arts. Digital Media covers that fine art requirement while building real career skills on industry tools, so one elective works toward college and career at the same time.":
        "Para poder entrar a la Universidad de California (UC) y a la Universidad Estatal de California (CSU), los estudiantes necesitan un año de Artes Visuales y Escénicas. Medios Digitales cumple ese requisito de bellas artes mientras desarrollas habilidades reales para una carrera con herramientas profesionales. Así, una sola optativa te prepara para la universidad y para una carrera al mismo tiempo.",
    "College:": "Universidad:",
    "counts as fine art (“F”) for UC and CSU admission.": "cuenta como bellas artes (“F”) para la admisión a UC y CSU.",
    "Career:": "Carrera:",
    "a CTE pathway in Arts, Media, and Entertainment, with SkillsUSA.": "una trayectoria CTE en Artes, Medios y Entretenimiento, con SkillsUSA.",
    "Years of industry experience": "Años de experiencia en la industria",
    "Fine arts credit": "Crédito de bellas artes",
    "Student organization": "Organización estudiantil",
    "Two Pathways, Four Courses": "Dos trayectorias, cuatro clases",
    "Start with level 1, grow into level 2": "Empieza con el nivel 1 y avanza al nivel 2",
    "Student light painting photograph": "Fotografía estudiantil de pintura con luz",
    "Student magazine cover designs": "Diseños estudiantiles de portadas de revista",
    "Program 01": "Programa 01",
    "Program 02": "Programa 02",
    "Foundation · no experience needed": "Básico · no necesitas experiencia",
    "Advanced · lighting and studio": "Avanzado · iluminación y estudio",
    "Advanced · brand and portfolio": "Avanzado · marca y portafolio",
    "Operate a real camera on Manual, see like a photographer, shape light on purpose, and finish images in Adobe Lightroom Classic and Photoshop.":
        "Usa una cámara real en modo manual, aprende a ver como fotógrafo, controla la luz con intención y termina tus imágenes en Adobe Lightroom Classic y Photoshop.",
    "Learn the elements and principles of design, then use Adobe Illustrator and Photoshop to make clean, intentional graphics, brands, and portfolio work.":
        "Aprende los elementos y principios del diseño, y luego usa Adobe Illustrator y Photoshop para crear gráficos limpios y con intención, marcas y trabajos para tu portafolio.",
    "Explore Photography": "Explora Fotografía",
    "Explore Digital Arts": "Explora Artes Digitales",
    "Career Technical Student Organization": "Organización estudiantil de Educación Técnica Profesional",
    "PVHS Digital Media is associated with SkillsUSA for both the Digital Photography and Digital Arts pathways.":
        "PVHS Digital Media está asociado con SkillsUSA en las trayectorias de Fotografía Digital y de Artes Digitales.",
    "SkillsUSA is a national organization for career and technical students. It helps students build leadership, teamwork, and workplace skills, and gives them a place to show their technical work beyond the classroom.":
        "SkillsUSA es una organización nacional para estudiantes de carreras técnicas. Ayuda a los estudiantes a desarrollar liderazgo, trabajo en equipo y habilidades para el trabajo, y les da un lugar para mostrar su trabajo técnico fuera del salón.",
    "Visit SkillsUSA": "Visita SkillsUSA",
    "Pathway status": "Nivel en la trayectoria",
    "Concentrator": "Concentrador",
    "A student who builds depth in one pathway by moving past the first course, for example Photography 1 into Photography 2, or Digital Arts 1 into Digital Arts 2.":
        "Un estudiante que profundiza en una trayectoria al pasar de la primera clase a la siguiente, por ejemplo de Fotografía 1 a Fotografía 2, o de Artes Digitales 1 a Artes Digitales 2.",
    "Completer": "Completador",
    "A student who finishes the full course sequence in a pathway. Completers leave with a body of finished work and real industry skills.":
        "Un estudiante que termina toda la secuencia de clases de una trayectoria. Los completadores salen con un conjunto de trabajos terminados y habilidades reales de la industria.",
    "How Every Project Runs": "Cómo funciona cada proyecto",
    "The same five steps in every course": "Los mismos cinco pasos en todas las clases",
    "Learn the concept": "Aprende el concepto",
    "A short, plain language overview introduces the idea and its key vocabulary.":
        "Una explicación corta y sencilla presenta la idea y su vocabulario clave.",
    "Make or capture": "Crea o captura",
    "Photograph with a camera kit, or build a design in Adobe software.":
        "Toma fotografías con un equipo de cámara o crea un diseño en los programas de Adobe.",
    "Edit and finish": "Edita y termina",
    "Cull, edit, and export the work to a professional standard.":
        "Selecciona, edita y exporta tu trabajo con calidad profesional.",
    "Turn it in": "Entrégalo",
    "Each step submits a clear deliverable to Canvas: a photo, a contact sheet, a design file, a high resolution export.":
        "Cada paso tiene una entrega clara en Canvas: una foto, una hoja de contactos, un archivo de diseño o una exportación en alta resolución.",
    "Reflect": "Reflexiona",
    "A short written reflection: what I did, what I learned, what I would change.":
        "Una reflexión corta por escrito: qué hice, qué aprendí y qué cambiaría.",
    "Students are graded on following the process and meeting the standard for each deliverable, not on being a “natural.” Clear, repeatable expectations are the point.":
        "La calificación se basa en seguir el proceso y cumplir el estándar de cada entrega, no en tener “talento natural.” Lo importante son expectativas claras que se pueden repetir.",
    "35 years of combined industry experience ·": "35 años de experiencia combinada en la industria ·",
    "14 years industry experience": "14 años de experiencia en la industria",
    "7 years industry experience": "7 años de experiencia en la industria",
    "Learn the concept. Make the work.": "Aprende el concepto. Crea el trabajo.",
    "Present it like a professional.": "Preséntalo como un profesional.",
    "The PVHS Digital Media standard": "El estándar de PVHS Digital Media",
    "Interested? Fill out the sign up form so our teachers can follow up, and ask your counselor about adding the class to your schedule.":
        "¿Te interesa? Llena el formulario de inscripción para que nuestros maestros se comuniquen contigo, y pregúntale a tu consejero cómo agregar la clase a tu horario.",

    # ---------- Course pages (shared)
    "Digital Media · Program 01": "Medios Digitales · Programa 01",
    "Digital Media · Program 02": "Medios Digitales · Programa 02",
    "Foundation": "Básico",
    "Advanced": "Avanzado",
    "Level 1 · Foundation": "Nivel 1 · Básico",
    "Level 2 · Advanced": "Nivel 2 · Avanzado",
    "a-g credit": "Crédito a-g",
    "UC / CSU “F” Visual and Performing Arts": "UC / CSU “F” Artes Visuales y Escénicas",
    "Taught by": "Maestros",
    "Who it is for": "Para quién es",
    "Cameras": "Cámaras",
    "Software": "Programas",
    "Lab": "Laboratorio",
    "Lighting gear": "Equipo de iluminación",
    "What students will be able to do": "Lo que los estudiantes podrán hacer",
    "Core units": "Unidades principales",
    "Example projects": "Proyectos de ejemplo",
    "How the year builds": "Cómo avanza el año",
    "Learn more": "Más información",
    "SkillsUSA · Concentrators & Completers": "SkillsUSA · Concentradores y completadores",
    "Student Work": "Trabajos estudiantiles",

    # ---------- Digital Photography
    "From Manual mode to studio lighting. Two courses that teach students to see, capture, and finish photographs on purpose.":
        "Del modo manual a la iluminación de estudio. Dos clases que enseñan a los estudiantes a ver, capturar y terminar fotografías con intención.",
    "Operate a real camera on Manual, see like a photographer, and finish images with professional editing software. Open to all students.":
        "Usa una cámara real en modo manual, aprende a ver como fotógrafo y termina tus imágenes con programas profesionales de edición. Abierta para todos los estudiantes.",
    "Move from a good exposure to controlling light and telling a story on purpose, with flash, studio work, and a personal style.":
        "Pasa de una buena exposición a controlar la luz y contar una historia con intención, con flash, trabajo de estudio y un estilo personal.",
    "The foundation photography course. Students learn to operate a real camera on Manual, see like a photographer, and finish their images with professional editing software.":
        "La clase básica de fotografía. Los estudiantes aprenden a usar una cámara real en modo manual, a ver como fotógrafos y a terminar sus imágenes con programas profesionales de edición.",
    "Open to all students, no experience required. The entry point to the photography pathway.":
        "Abierta para todos los estudiantes, no se requiere experiencia. Es el punto de entrada a la trayectoria de fotografía.",
    "Canon mirrorless camera kits: body, lenses, battery, charger, memory card.":
        "Equipos de cámaras Canon sin espejo: cuerpo, lentes, batería, cargador y tarjeta de memoria.",
    "Adobe Lightroom Classic, plus Adobe Photoshop near the end of the year.":
        "Adobe Lightroom Classic, y Adobe Photoshop hacia el final del año.",
    "Mac computers, with the school iPad as a scanner.": "Computadoras Mac, con el iPad de la escuela como escáner.",
    "Operate a camera in Manual mode and capture in RAW, controlling aperture, shutter speed, and ISO.":
        "Usar una cámara en modo manual y capturar en RAW, controlando la apertura, la velocidad de obturación y el ISO.",
    "Read and use available light, and balance exposure across different settings.":
        "Leer y aprovechar la luz disponible, y equilibrar la exposición en diferentes lugares.",
    "Apply composition: framing, the rule of thirds, leading lines, and point of view.":
        "Aplicar la composición: encuadre, regla de los tercios, líneas guía y punto de vista.",
    "Import, cull, and edit a set of photos, and build contact sheets of the full take and the final selections.":
        "Importar, seleccionar y editar un grupo de fotos, y crear hojas de contactos de todas las tomas y de la selección final.",
    "Export finished, high resolution images and present them cleanly.":
        "Exportar imágenes terminadas en alta resolución y presentarlas de forma limpia.",
    "Camera fundamentals": "Bases de la cámara",
    "Manual mode, RAW, exposure (aperture, shutter, ISO), focus, and lens choice.":
        "Modo manual, RAW, exposición (apertura, obturador, ISO), enfoque y elección de lente.",
    "Seeing & composition": "Ver y componer",
    "Framing, the rule of thirds, leading lines, perspective, and finding images where others see none.":
        "Encuadre, regla de los tercios, líneas guía, perspectiva y encontrar imágenes donde otros no ven nada.",
    "Editing workflow": "Proceso de edición",
    "Import, cull, edit for exposure and color, export, and contact sheets.":
        "Importar, seleccionar, editar la exposición y el color, exportar y hacer hojas de contactos.",
    "Creative projects": "Proyectos creativos",
    "Themed photo walks and studio style challenges that put the skills to work.":
        "Caminatas fotográficas con tema y retos de estudio para poner en práctica lo aprendido.",
    "Intro to compositing": "Introducción a la composición digital",
    "A first Photoshop project that combines finished photos into one piece.":
        "Un primer proyecto en Photoshop que combina fotos terminadas en una sola pieza.",
    "Self-Portrait": "Autorretrato",
    "Composition Concepts": "Conceptos de composición",
    "Leading Lines Photo Walk": "Caminata fotográfica de líneas guía",
    "Image Series Photo Walk": "Caminata fotográfica de serie de imágenes",
    "Lightroom Editing": "Edición en Lightroom",
    "Tiny Things": "Cosas pequeñas",
    "Balloon Pop": "Globo que revienta",
    "Aperture Portrait": "Retrato con apertura",
    "Exposure Balance": "Equilibrio de exposición",
    "Spell Your Name Photo Walk": "Caminata fotográfica: escribe tu nombre",
    "Early projects teach one skill at a time: composition first, then the editing workflow, then a single camera control. Later projects combine skills. The year closes by moving finished photos into Photoshop, which sets up Photography 2 and the Digital Arts courses.":
        "Los primeros proyectos enseñan una habilidad a la vez: primero la composición, luego el proceso de edición y después un control de la cámara. Los proyectos posteriores combinan habilidades. El año termina llevando fotos terminadas a Photoshop, lo que prepara para Fotografía 2 y para las clases de Artes Digitales.",
    "The advanced photography course. Students move from “getting a good exposure” to controlling light and telling a story on purpose.":
        "La clase avanzada de fotografía. Los estudiantes pasan de “lograr una buena exposición” a controlar la luz y contar una historia con intención.",
    "Students who completed Photography 1, or who can show the fundamentals: Manual mode, RAW, and the Lightroom workflow.":
        "Estudiantes que terminaron Fotografía 1, o que pueden demostrar lo básico: modo manual, RAW y el proceso en Lightroom.",
    "Speedlites and off camera flash, modifiers, backdrops, tripods, reflectors, and a studio setup.":
        "Flashes Speedlite y flash fuera de la cámara, modificadores de luz, fondos, trípodes, reflectores y un estudio.",
    "Everything in Photography 1, plus camera kits reserved for the advanced course.":
        "Todo lo de Fotografía 1, más equipos de cámara reservados para la clase avanzada.",
    "Shape light on purpose: off camera flash, studio lighting, and mixed or available light.":
        "Controlar la luz con intención: flash fuera de la cámara, iluminación de estudio y luz mixta o disponible.",
    "Plan and direct a session, and work with a subject to make an intentional portrait.":
        "Planear y dirigir una sesión, y trabajar con una persona para crear un retrato con intención.",
    "Build and apply their own editing presets for a consistent personal style.":
        "Crear y aplicar sus propios ajustes preestablecidos de edición para un estilo personal constante.",
    "Hold a higher creative bar: natural only constraints, series that read as a body of work, and refined final edits.":
        "Mantener un nivel creativo más alto: retos solo con elementos naturales, series que se ven como un conjunto de obra y ediciones finales cuidadas.",
    "Lighting": "Iluminación",
    "Off camera flash, studio sessions, modifiers, and controlling the look of light.":
        "Flash fuera de la cámara, sesiones de estudio, modificadores y control del aspecto de la luz.",
    "Advanced exposure & lenses": "Exposición y lentes avanzados",
    "Deliberate aperture and depth of field choices across the full lens kit.":
        "Decisiones intencionales de apertura y profundidad de campo con todos los lentes.",
    "Style & workflow": "Estilo y proceso",
    "Building custom presets and developing a consistent personal edit.":
        "Crear ajustes preestablecidos propios y desarrollar una edición personal constante.",
    "Concept & series": "Concepto y serie",
    "Themed bodies of work with a tighter creative constraint.":
        "Conjuntos de obra con tema y con un reto creativo más exigente.",
    "Portraiture": "Retrato",
    "Working with a subject, posing, and direction.": "Trabajar con una persona, posar y dirigir.",
    "Composition Photo Walk": "Caminata fotográfica de composición",
    "Off-Camera Flash": "Flash fuera de la cámara",
    "Studio Session": "Sesión de estudio",
    "Build Your Own Preset": "Crea tu propio ajuste preestablecido",
    "Same rhythm, higher ceiling": "El mismo ritmo, un nivel más alto",
    "Photography 1 teaches one control at a time. Photography 2 adds lighting, often requires natural only or self directed work, and expects students to run the full capture to delivery pipeline on their own.":
        "Fotografía 1 enseña un control a la vez. Fotografía 2 agrega iluminación, muchas veces pide trabajo solo con elementos naturales o dirigido por el estudiante, y espera que los estudiantes hagan todo el proceso, de la captura a la entrega, por su cuenta.",
    "The Digital Photography pathway is associated with SkillsUSA. Students who continue past level 1 become pathway concentrators, and students who finish the full sequence become pathway completers.":
        "La trayectoria de Fotografía Digital está asociada con SkillsUSA. Los estudiantes que continúan después del nivel 1 se vuelven concentradores de la trayectoria, y los que terminan toda la secuencia se vuelven completadores.",
    "Writing with light and multiple exposures": "Escribir con luz y exposiciones múltiples",
    "Ribbons of light spiral around a student standing in the dark": "Cintas de luz giran alrededor de un estudiante parado en la oscuridad",
    "Dense scribbles of light across a dark frame, a face glowing behind them": "Trazos densos de luz sobre un fondo oscuro, con un rostro iluminado detrás",
    "A student in a blue sweater surrounded by loops of light": "Un estudiante con suéter azul rodeado de líneas de luz",
    "Writing with Light": "Escribir con luz",
    "Long exposure light painting": "Pintura con luz de exposición larga",
    "Portrait of a student in a striped sweater under violet light": "Retrato de un estudiante con suéter a rayas bajo luz violeta",
    "Black and white multiple exposure portrait of a student": "Retrato de exposición múltiple en blanco y negro de un estudiante",
    "Multiple exposure portrait of a student with glasses in violet and red": "Retrato de exposición múltiple de un estudiante con lentes, en violeta y rojo",
    "Multiples": "Múltiples",
    "Multiple exposure portrait": "Retrato de exposición múltiple",
    "See more in the Light Writerz gallery": "Mira más en la galería de Light Writerz",

    # ---------- Digital Arts
    "Design with intention. Two courses that build from the elements of art to brand systems and portfolio quality work in Adobe Illustrator and Photoshop.":
        "Diseña con intención. Dos clases que van de los elementos del arte a sistemas de marca y trabajos de calidad para portafolio en Adobe Illustrator y Photoshop.",
    "The elements and principles of design, plus the industry standard Adobe tools to make clean, intentional graphics. Open to all students.":
        "Los elementos y principios del diseño, más las herramientas profesionales de Adobe para crear gráficos limpios y con intención. Abierta para todos los estudiantes.",
    "Move from exercises to real, portfolio quality design work: brand systems, campaigns, layouts, and client briefs.":
        "Pasa de ejercicios a trabajos de diseño reales y de calidad para portafolio: sistemas de marca, campañas, diagramación y encargos de clientes.",
    "The foundation design course. Students learn the elements and principles of design and the industry standard Adobe tools to make clean, intentional graphics.":
        "La clase básica de diseño. Los estudiantes aprenden los elementos y principios del diseño y las herramientas profesionales de Adobe para crear gráficos limpios y con intención.",
    "Open to all students, no experience required. The entry point to the design and graphic arts pathway.":
        "Abierta para todos los estudiantes, no se requiere experiencia. Es el punto de entrada a la trayectoria de diseño y artes gráficas.",
    "Adobe Illustrator for vector art, logos, and type. Adobe Photoshop for image editing, compositing, and mockups.":
        "Adobe Illustrator para arte vectorial, logotipos y tipografía. Adobe Photoshop para editar imágenes, composiciones digitales y maquetas.",
    "Mac computers, with the school iPad as a scanner for sketches and hand done work.":
        "Computadoras Mac, con el iPad de la escuela como escáner para bocetos y trabajos hechos a mano.",
    "Use the elements and principles of art and design on purpose: line, shape, color, form, balance, contrast, and type.":
        "Usar con intención los elementos y principios del arte y el diseño: línea, figura, color, forma, equilibrio, contraste y tipografía.",
    "Work the core Adobe tools: the Illustrator workspace, drawing and pen tools, type, layers, and exporting, plus Photoshop layers and placement.":
        "Manejar las herramientas principales de Adobe: el espacio de trabajo de Illustrator, las herramientas de dibujo y pluma, texto, capas y exportación, además de capas y colocación en Photoshop.",
    "Take an idea from sketch to finished digital artwork, by vector tracing or by compositing.":
        "Llevar una idea de un boceto a una obra digital terminada, con trazado vectorial o con composición digital.",
    "Apply color theory and typography to communicate a clear message.":
        "Aplicar la teoría del color y la tipografía para comunicar un mensaje claro.",
    "Produce finished, export ready graphics at a stated size and format.":
        "Producir gráficos terminados y listos para exportar en un tamaño y formato indicados.",
    "Design foundations": "Bases del diseño",
    "The elements and principles of art, color theory, and typography.":
        "Los elementos y principios del arte, la teoría del color y la tipografía.",
    "Illustrator skills": "Habilidades en Illustrator",
    "Workspace, drawing and pen tools, shapes, type, layers, and sketch to vector.":
        "Espacio de trabajo, herramientas de dibujo y pluma, figuras, texto, capas y de boceto a vector.",
    "Photoshop skills": "Habilidades en Photoshop",
    "Layers, placing and sizing images, simple compositing, and export.":
        "Capas, colocar y ajustar el tamaño de imágenes, composición digital sencilla y exportación.",
    "Applied projects": "Proyectos aplicados",
    "Posters, covers, pictograms and icons, character design, and brand graphics.":
        "Carteles, portadas, pictogramas e íconos, diseño de personajes y gráficos de marca.",
    "Communication": "Comunicación",
    "Making work that reads clearly and serves a purpose or a client.":
        "Crear trabajos que se entienden con claridad y que sirven a un propósito o a un cliente.",
    "Pictograms": "Pictogramas",
    "Color Theory": "Teoría del color",
    "Sketchbook Cover Art": "Portada para cuaderno de bocetos",
    "Motivational Poster": "Cartel motivacional",
    "Live Stream Graphic": "Gráfico para transmisión en vivo",
    "Elements of Art / Character Design": "Elementos del arte / Diseño de personajes",
    "Character Design (Form and Color)": "Diseño de personajes (forma y color)",
    "Get to Know Illustrator": "Conoce Illustrator",
    "Start with design fundamentals and tool familiarity, then short applied projects that each target one or two principles. The year builds toward projects that combine skills into a finished, presentable piece.":
        "Empieza con las bases del diseño y el manejo de las herramientas, y luego proyectos cortos que trabajan uno o dos principios a la vez. El año avanza hacia proyectos que combinan habilidades en una pieza terminada y lista para presentar.",
    "The advanced design course. Students move from exercises to real, portfolio quality design work and brand projects.":
        "La clase avanzada de diseño. Los estudiantes pasan de ejercicios a trabajos de diseño reales, de calidad para portafolio, y a proyectos de marca.",
    "Students who completed Digital Arts 1, or who can show the fundamentals and comfort with Illustrator and Photoshop.":
        "Estudiantes que terminaron Artes Digitales 1, o que pueden demostrar lo básico y manejan bien Illustrator y Photoshop.",
    "Illustrator and Photoshop together at a higher level, plus print and output tools.":
        "Illustrator y Photoshop juntos a un nivel más alto, además de herramientas de impresión y salida.",
    "Design complete, multi piece projects: a brand system, a campaign, a layout set.":
        "Diseñar proyectos completos de varias piezas: un sistema de marca, una campaña o un conjunto de diagramaciones.",
    "Work from a brief or a client’s needs, make deliberate design choices, and explain them.":
        "Trabajar a partir de un encargo o de las necesidades de un cliente, tomar decisiones de diseño con intención y explicarlas.",
    "Combine Illustrator and Photoshop in a professional workflow, and prepare files for screen and print.":
        "Combinar Illustrator y Photoshop en un proceso profesional, y preparar archivos para pantalla e impresión.",
    "Build a portfolio of finished work that shows range and craft.":
        "Crear un portafolio de trabajos terminados que muestre variedad y calidad.",
    "Branding & identity": "Marca e identidad",
    "Logo systems, color and type systems, and a consistent visual language.":
        "Sistemas de logotipo, sistemas de color y tipografía, y un lenguaje visual constante.",
    "Layout & production": "Diagramación y producción",
    "Multi page and multi piece layouts, print and digital output, and file preparation.":
        "Diagramación de varias páginas y piezas, salida impresa y digital, y preparación de archivos.",
    "Client & brief work": "Trabajo con clientes y encargos",
    "Designing to a real or simulated client’s needs and constraints.":
        "Diseñar según las necesidades y límites de un cliente real o simulado.",
    "Advanced technique": "Técnica avanzada",
    "More complex Illustrator and Photoshop work, mockups, and presentation.":
        "Trabajo más complejo en Illustrator y Photoshop, maquetas y presentación.",
    "Portfolio": "Portafolio",
    "Curating and presenting a body of finished work.": "Seleccionar y presentar un conjunto de trabajos terminados.",
    "Brief driven, portfolio focused": "Basado en encargos, enfocado en el portafolio",
    "Digital Arts 2 runs as a set of larger, brief driven projects that apply and deepen the Digital Arts 1 foundations. Same rhythm: concept, make, refine, deliver, reflect, with a higher bar on craft, independence, and finish.":
        "Artes Digitales 2 funciona con proyectos más grandes basados en encargos, que aplican y profundizan las bases de Artes Digitales 1. El mismo ritmo: concepto, crear, mejorar, entregar y reflexionar, con un nivel más alto de calidad, independencia y acabado.",
    "The Digital Arts pathway is associated with SkillsUSA. Students who continue past level 1 become pathway concentrators, and students who finish the full sequence become pathway completers.":
        "La trayectoria de Artes Digitales está asociada con SkillsUSA. Los estudiantes que continúan después del nivel 1 se vuelven concentradores de la trayectoria, y los que terminan toda la secuencia se vuelven completadores.",
    "Magazine covers: photography meets design": "Portadas de revista: la fotografía se une al diseño",
    "Vogue magazine cover by Ella Naoe": "Portada de la revista Vogue por Ella Naoe",
    "Rolling Stone magazine cover by Gregorio Calleja": "Portada de la revista Rolling Stone por Gregorio Calleja",
    "Time magazine cover by Julio Marquez": "Portada de la revista Time por Julio Marquez",
    "Sports Illustrated magazine cover by Davina Royall Showalter": "Portada de la revista Sports Illustrated por Davina Royall Showalter",
    "People magazine cover by Jessica Valdez": "Portada de la revista People por Jessica Valdez",
    "Vogue cover": "Portada de Vogue",
    "Rolling Stone cover": "Portada de Rolling Stone",
    "Time cover": "Portada de Time",
    "Sports Illustrated cover": "Portada de Sports Illustrated",
    "People cover": "Portada de People",

    # ---------- Teachers
    "Every Digital Media teacher is a CTE teacher with real industry experience: 35 combined years of commercial and fine art work, brought into the classroom.":
        "Cada maestro de Medios Digitales es un maestro de CTE con experiencia real en la industria: 35 años combinados de trabajo comercial y de bellas artes, llevados al salón de clases.",
    "Chris Silva is a fine art photographer and visual arts educator based in Santa Maria, California. He teaches Photography and Digital Arts at Pioneer Valley High School. Working mostly in black and white, across film, digital, and hybrid workflows, he makes documentary work, environmental portraits, and experimental images rooted in place and lived experience.":
        "Chris Silva es fotógrafo de bellas artes y educador de artes visuales en Santa Maria, California. Enseña Fotografía y Artes Digitales en Pioneer Valley High School. Trabaja sobre todo en blanco y negro, con película, digital y procesos híbridos, y crea trabajo documental, retratos en su entorno e imágenes experimentales basadas en el lugar y en la experiencia vivida.",
    "Capturing light since age 13 on 35mm film, Chris studied Applied Arts and Design at Allan Hancock College and earned a BA in Photography from Southern New Hampshire University. He co-owns Cris & Laura Inspired EYE Images and co-founded Light Writerz, the PVHS photography club.":
        "Captura la luz desde los 13 años con película de 35 mm. Chris estudió Artes Aplicadas y Diseño en Allan Hancock College y obtuvo una licenciatura (BA) en Fotografía de Southern New Hampshire University. Es copropietario de Cris & Laura Inspired EYE Images y cofundador de Light Writerz, el club de fotografía de PVHS.",
    "Laura Garcia is a professional photographer, photography educator, and co-founder of Light Writerz. Laura co-owns Cris & Laura Inspired EYE Images, bringing years of professional industry experience to the next generation of Light Writers.":
        "Laura Garcia es fotógrafa profesional, educadora de fotografía y cofundadora de Light Writerz. Laura es copropietaria de Cris & Laura Inspired EYE Images y comparte años de experiencia profesional en la industria con la nueva generación de Light Writers.",
    "Laura earned an Associate of Arts (A.A.) from Santa Barbara City College and a Bachelor of Arts (B.A.) in Photography from Southern New Hampshire University.":
        "Laura obtuvo un título técnico en Artes (Associate of Arts, A.A.) de Santa Barbara City College y una licenciatura en Artes (Bachelor of Arts, B.A.) en Fotografía de Southern New Hampshire University.",
    "As a Light Writerz advisor, Laura helps students build the discipline, technical skill, and creative confidence it takes to make photographs with intention.":
        "Como asesora de Light Writerz, Laura ayuda a los estudiantes a desarrollar la disciplina, la técnica y la confianza creativa que se necesitan para crear fotografías con intención.",
    "Hi there, nice to meet you! I’m Rileigh. I’m a tenacious designer who specializes in brand identity, apparel design, and pattern design. I thrive under pressure and strive to create meaningful designs through authentic storytelling.":
        "¡Hola, mucho gusto! Soy Rileigh. Me dedico al diseño con tenacidad y me especializo en identidad de marca, diseño de ropa y diseño de patrones. Trabajo muy bien bajo presión y me esfuerzo por crear diseños significativos que cuenten historias auténticas.",
    "Outside of design, I love exploring and competing. You can find me traveling, camping, hiking, or challenging friends and family to a new board game.":
        "Fuera del diseño, me encanta explorar y competir. Me puedes encontrar viajando, acampando, haciendo senderismo o retando a mis amigos y familia a un nuevo juego de mesa.",
    "I studied at Corvin University and Laguna College of Art and Design, where I earned my bachelor’s degree, and I now teach Digital Arts at Pioneer Valley High School.":
        "Estudié en Corvin University y en Laguna College of Art and Design, donde obtuve mi licenciatura, y ahora enseño Artes Digitales en Pioneer Valley High School.",
    "Combined years in industry": "Años combinados en la industria",
    "Want to join a class?": "¿Quieres tomar una clase?",
    "Photography 1 and Digital Arts 1 are open to every PVHS student, no experience needed, and they count toward the a-g “F” fine art requirement. Fill out the sign up form, then ask your counselor to add one to your schedule.":
        "Fotografía 1 y Artes Digitales 1 están abiertas para todos los estudiantes de PVHS, sin necesidad de experiencia, y cuentan para el requisito “F” de bellas artes de a-g. Llena el formulario de inscripción y luego pídele a tu consejero que agregue la clase a tu horario.",
    "Explore the program": "Explora el programa",

    # ---------- Sign up page
    "Interest Form": "Formulario de interés",
    "Want to take Digital Photography or Digital Arts next school year? Fill out this short form and our teachers will follow up with you.":
        "¿Quieres tomar Fotografía Digital o Artes Digitales el próximo año escolar? Llena este formulario corto y nuestros maestros se comunicarán contigo.",
    "Full name": "Nombre completo",
    "First and last name": "Nombre y apellido",
    "Student ID number": "Número de identificación estudiantil",
    "6 digits": "6 dígitos",
    "Your 6 digit PVHS student ID.": "Tu número de estudiante de PVHS de 6 dígitos.",
    "What grade will you be in next school year?": "¿En qué grado estarás el próximo año escolar?",
    "9th grade": "9.º grado",
    "10th grade": "10.º grado",
    "11th grade": "11.º grado",
    "12th grade": "12.º grado",
    "Which classes are you interested in?": "¿Qué clases te interesan?",
    "Choose one or more.": "Elige una o más.",
    "Advanced · after Photography 1": "Avanzado · después de Fotografía 1",
    "Advanced · after Digital Arts 1": "Avanzado · después de Artes Digitales 1",
    "Questions or comments": "Preguntas o comentarios",
    "(optional)": "(opcional)",
    "Website": "Sitio web",
    "Send my sign up": "Enviar mi inscripción",
    "This is an interest form, not your official schedule. Your counselor makes the final schedule.":
        "Este es un formulario de interés, no tu horario oficial. Tu consejero hace el horario final.",
    "Sent": "Enviado",
    "You are on the list!": "¡Ya estás en la lista!",
    "Our teachers will follow up with you. Remember to also ask your counselor about adding the class to your schedule.":
        "Nuestros maestros se comunicarán contigo. Recuerda también pedirle a tu consejero que agregue la clase a tu horario.",
    "Back to Digital Media": "Volver a Medios Digitales",
    "Sign up another student": "Inscribir a otro estudiante",
    "Good to know": "Es bueno saber",
    "Photography 1 and Digital Arts 1 are open to everyone. No experience needed.":
        "Fotografía 1 y Artes Digitales 1 están abiertas para todos. No necesitas experiencia.",
    "Every class counts toward the UC and CSU a-g “F” fine art requirement.":
        "Todas las clases cuentan para el requisito “F” de bellas artes de a-g para UC y CSU.",
}
