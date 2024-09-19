from fasthtml.common import *
#ola
app, rt = fast_app()

# Estilos actualizados incluyendo botones modernos para skills
css = '''
    /* ... (estilos anteriores sin cambios) ... */

    .container {
        max-width: 800px;
        width: 100%;
    }

    .terminal {
        border: 2px solid #00ff00;
        padding: 30px;
        margin: 40px auto;
        max-width: 800px;
        text-align: center;
        box-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 30px #00ff00;
        animation: neon-pulse 1.5s ease-in-out infinite alternate;
        border-radius: 15px;
        overflow: hidden;
    }

    .section {
        font-size: 1.5em;
        margin-top: 40px;
        margin-bottom: 20px;
    }

    /* ... (resto de los estilos sin cambios) ... */
    /* ... (estilos anteriores sin cambios) ... */

    .terminal {
        border: 2px solid #00ff00;
        padding: 20px;
        margin: 20px auto;
        max-width: 800px;
        text-align: center;
        box-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 30px #00ff00;
        animation: neon-pulse 1.5s ease-in-out infinite alternate;
    }

    @keyframes neon-pulse {
        from {
            box-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 30px #00ff00;
        }
        to {
            box-shadow: 0 0 20px #00ff00, 0 0 30px #00ff00, 0 0 40px #00ff00;
        }
    }

    /* ... (resto de los estilos sin cambios) ... */

    :root { 
        --pico-font-size: 90%;
        --pico-font-family: 'Courier New', monospace; 
    }
    body {
        background-color: #0f0f0f;
        color: #00ff00;
        font-family: var(--pico-font-family);
        display: flex;
        justify-content: center;
        padding: 20px;
    }
    .container {
        max-width: 800px;
        width: 100%;
    }
    a {
        color: #00ff00;
        text-decoration: none;
    }
       .terminal {
        border: 2px solid #00ff00;
        padding: 20px;
        margin: 20px auto;
        max-width: 800px;
        text-align: center;
    }

    /* Para mantener el alineado a la izquierda en ciertos elementos dentro de .terminal */
    .terminal ul, .terminal p {
        text-align: left;
    }
    .header {
        text-align: center;
        font-size: 2em;
        margin-bottom: 20px;
    }
    .section {
        font-size: 1.5em;
        margin-top: 20px;
    }
    .skills-list {
        list-style-type: none;
        padding: 0;
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
    }
    .skill-item {
        background-color: #003300;
        color: #00ff00;
        border: 1px solid #00ff00;
        border-radius: 20px;
        padding: 8px 16px;
        font-size: 0.9em;
        transition: all 0.3s ease;
    }
    .skill-item:hover {
        background-color: #00ff00;
        color: #000000;
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0, 255, 0, 0.1);
    }

      .projects-list {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 20px;
        padding: 0;
        list-style-type: none;
    }
    .project-item {
        background-color: #001100;
        border: 1px solid #00ff00;
        border-radius: 8px;
        padding: 15px;
        transition: all 0.3s ease;
    }
    .project-item:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(0, 255, 0, 0.2);
    }
    .project-image {
        width: 100%;
        height: 150px;
        object-fit: cover;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .project-title {
        color: #00ff00;
        font-size: 1.2em;
        margin-bottom: 10px;
    }
    .project-description {
        color: #00cc00;
        font-size: 0.9em;
        margin-bottom: 15px;
    }
    .project-links {
        display: flex;
        justify-content: space-between;
    }
    .project-link {
        display: inline-block;
        background-color: #003300;
        color: #00ff00;
        padding: 5px 10px;
        border-radius: 5px;
        text-decoration: none;
        transition: background-color 0.3s ease;
    }
    .project-link:hover {
        background-color: #004400;
    }

        .glitch {
        position: relative;
        color: #00ff00;
        font-size: 2em;
        letter-spacing: 0.1em;
        animation: glitch-skew 1s infinite linear alternate-reverse;
    }
    .glitch::before,
    .glitch::after {
        content: attr(data-text);
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
    .glitch::before {
        left: 2px;
        text-shadow: -2px 0 #ff00ff;
        clip: rect(44px, 450px, 56px, 0);
        animation: glitch-anim 5s infinite linear alternate-reverse;
    }
    .glitch::after {
        left: -2px;
        text-shadow: -2px 0 #00ffff;
        clip: rect(44px, 450px, 56px, 0);
        animation: glitch-anim2 5s infinite linear alternate-reverse;
    }
    @keyframes glitch-anim {
        0% {
            clip: rect(10px, 9999px, 82px, 0);
            transform: skew(0.55deg);
        }
        5% {
            clip: rect(54px, 9999px, 59px, 0);
            transform: skew(0.07deg);
        }
        10% {
            clip: rect(62px, 9999px, 7px, 0);
            transform: skew(0.05deg);
        }
        /* ... (más keyframes) ... */
        100% {
            clip: rect(100px, 9999px, 94px, 0);
            transform: skew(0.32deg);
        }
    }
    @keyframes glitch-anim2 {
        0% {
            clip: rect(65px, 9999px, 100px, 0);
            transform: skew(0.4deg);
        }
        5% {
            clip: rect(93px, 9999px, 74px, 0);
            transform: skew(0.61deg);
        }
        10% {
            clip: rect(23px, 9999px, 94px, 0);
            transform: skew(0.05deg);
        }
        /* ... (más keyframes) ... */
        100% {
            clip: rect(53px, 9999px, 25px, 0);
            transform: skew(0.6deg);
        }
    }
    @keyframes glitch-skew {
        0% {
            transform: skew(-2deg);
        }
        10% {
            transform: skew(-1deg);
        }
        20% {
            transform: skew(0deg);
        }
        /* ... (más keyframes) ... */
        100% {
            transform: skew(1deg);
        }
               .social-icons {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 20px;
    }
    .social-icon {
        transition: transform 0.3s ease;
    }
    .social-icon:hover {
        transform: scale(10.1);
    }
'''

glitch_script = '''
    function glitchEffect() {
        const glitch = document.querySelector('.glitch');
        const text = glitch.textContent;
        glitch.setAttribute('data-text', text);
    }
    window.addEventListener('load', glitchEffect);
'''

@rt('/')
def get():
    cv_path = "CV_JoseJuanGallegosSuarez.pdf"
    cv_exists = os.path.exists(cv_path)
    
    return Html(
        Head(
            Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"),
            Style(css),
            Script(glitch_script)
        ),
        Body(
            Div(
                Div(
                    H2("Sobre mí", _class="section", style="text-align: left; margin-bottom: 20px;"),
                    Div(
                        Div(
                            Img(src="https://avatars.githubusercontent.com/u/162421825?v=4", alt="Mi foto", style="width: 200px; height: 200px; border-radius: 50%; object-fit: cover;"),
                            style="flex: 0 0 auto; margin-right: 20px;"
                        ),
                        Div(
                            H3('José Juan Gallegos Suarez', _class="header glitch"),
                            P("Desarrollador Full-Stack", style="margin-top: 0; font-style: italic;"),
                            P("Ingeniero en Sistemas Computacionales con pasión por la tecnología y la innovación."),
                            P("Especializado en desarrollo de software, mantenimiento de equipos, y soluciones tecnológicas."),
                            style="flex: 1; text-align: justify;"
                        ),
                        style="display: flex; align-items: center;"
                    ),
                    _class="terminal",
                    style="border-radius: 15px; overflow: hidden; padding: 20px; margin-bottom: 60px;"
                ),
                Div(
                    Div(
                        I(_class="fas fa-envelope", style="position: absolute; left: 10px; top: 50%; transform: translateY(-50%); color: #00ff00;"),
                        Input(
                            type="text",
                            value="ing.josejuangallegos@gmail.com",
                            readonly=True,
                            style="background-color: #001100; color: #00ff00; border: 1px solid #00ff00; padding: 10px 10px 10px 35px; border-radius: 5px; width: 300px; box-sizing: border-box;"
                        ),
                        style="position: relative; display: inline-block; margin-right: 10px;"
                    ),
                    Button(
                        I(_class="fas fa-envelope", style="font-size: 18px;"),
                        onclick="sendEmail()",
                        style="margin-right: 10px; padding: 10px 15px; background-color: #003300; color: #00ff00; border: 1px solid #00ff00; border-radius: 5px; cursor: pointer; transition: all 0.3s ease;"
                    ),
                    Button(
                        I(_class="fas fa-copy", style="font-size: 18px;"),
                        onclick="copyEmail()",
                        style="margin-right: 10px; padding: 10px 15px; background-color: #003300; color: #00ff00; border: 1px solid #00ff00; border-radius: 5px; cursor: pointer; transition: all 0.3s ease;"
                    ),
                    A(
                        I(_class="fas fa-download", style="font-size: 18px;"),
                        href="https://drive.google.com/file/d/1PA1w04EWNXn1GJahCaWf13pZPhgdlNwj/view?usp=drive_link", 
                        download="CV_JoseJuanGallegosSuarez.pdf", 
                        _class="download-cv-btn",
                        style="padding: 10px 15px; background-color: #003300; color: #00ff00; border: 1px solid #00ff00; border-radius: 5px; text-decoration: none; transition: all 0.3s ease;"
                    ),
                    style="display: flex; align-items: center; justify-content: center; margin: 60px 0;",
                    _class="terminal",
                ),
                Div(
                    H2("Skills", _class="section"),
                    Ul(
                        Li("Python", _class="skill-item"),
                        Li("JavaScript", _class="skill-item"),
                        Li("Dart", _class="skill-item"),
                        Li("Docker", _class="skill-item"),
                        Li("SQL Server", _class="skill-item"),
                        Li("MySQL", _class="skill-item"),
                        Li("PostgreSQL", _class="skill-item"),
                        Li("MongoDB", _class="skill-item"),
                        Li("Git", _class="skill-item"),
                        Li("GitHub", _class="skill-item"),
                        Li("PHP", _class="skill-item"),
                        Li("Laravel", _class="skill-item"),
                        Li("Astro", _class="skill-item"),
                        Li("React", _class="skill-item"),
                        Li("Next.js", _class="skill-item"),
                        Li("Tailwind CSS", _class="skill-item"),
                        Li("Bootstrap", _class="skill-item"),
                        _class="skills-list"
                    ),
                    _class="skills terminal",
                    style="border-radius: 15px; overflow: hidden; padding: 20px; margin-bottom: 60px;"
                ),
                Div(
                    H2("Projects", _class="section"),
                    Ul(
                        Li(
                            Div(
                                Img(src="https://via.placeholder.com/300x150", alt="Proyecto 1", _class="project-image"),
                                H3("Automatización de Sincronización de Datos y Seguridad", _class="project-title"),
                                P("Sistema automatizado para sincronizar datos entre plataformas y mejorar la seguridad.", _class="project-description"),
                                Div(
                                    A("Web", href="#", _class="project-link"),
                                    A("GitHub", href="https://github.com/tuusuario/proyecto1", _class="project-link"),
                                    _class="project-links"
                                ),
                                style="border-radius: 10px; overflow: hidden;"
                            ),
                            _class="project-item"
                        ),
                        Li(
                            Div(
                                Img(src="https://via.placeholder.com/300x150", alt="Proyecto 2", _class="project-image"),
                                H3("Desarrollo de Aplicaciones Móviles", _class="project-title"),
                                P("Aplicaciones móviles innovadoras para Android e iOS utilizando tecnologías modernas.", _class="project-description"),
                                Div(
                                    A("Web", href="#", _class="project-link"),
                                    A("GitHub", href="https://github.com/tuusuario/proyecto2", _class="project-link"),
                                    _class="project-links"
                                ),
                                style="border-radius: 10px; overflow: hidden;"
                            ),
                            _class="project-item"
                        ),
                        Li(
                            Div(
                                Img(src="https://via.placeholder.com/300x150", alt="Proyecto 3", _class="project-image"),
                                H3("Gestión de Infraestructura con Docker y Kubernetes", _class="project-title"),
                                P("Implementación de soluciones de contenedores para mejorar la escalabilidad y el despliegue.", _class="project-description"),
                                Div(
                                    A("Web", href="#", _class="project-link"),
                                    A("GitHub", href="https://github.com/tuusuario/proyecto3", _class="project-link"),
                                    _class="project-links"
                                ),
                                style="border-radius: 10px; overflow: hidden;"
                            ),
                            _class="project-item"
                        ),
                        _class="projects-list"
                    ),
                    _class="projects terminal",
                    style="border-radius: 15px; overflow: hidden; padding: 20px; margin-bottom: 60px;"
                ),
                Div(
                    H2("Contact", _class="section"),
                    Div(
                        A(Img(src="img/link.svg", alt="LinkedIn", _class="social-icon", width="40", height="40"), 
                          href="https://www.linkedin.com/in/jose-juan-gallegos-su%C3%A1rez-89148b293?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app", target="_blank"),
                        A(Img(src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MCIgaGVpZ2h0PSI0MCIgdmlld0JveD0iMCAwIDI0IDI0Ij48cGF0aCBmaWxsPSIjMDBmZjAwIiBkPSJNMTIuMDAxIDJjLTUuNTI1IDAtMTAgNC40NzUtMTAgMTBhOS45OSA5Ljk5IDAgMCAwIDYuODM3IDkuNDg4Yy41LjA4Ny42ODgtLjIxMy42ODgtLjQ3NmMwLS4yMzctLjAxMy0xLjAyNC0uMDEzLTEuODYyYy0yLjUxMi40NjMtMy4xNjItLjYxMi0zLjM2Mi0xLjE3NWMtLjExMy0uMjg4LS42LTEuMTc1LTEuMDI1LTEuNDEzYy0uMzUtLjE4Ny0uODUtLjY1LS4wMTMtLjY2MmMuNzg4LS4wMTMgMS4zNS43MjUgMS41MzggMS4wMjVjLjkgMS41MTIgMi4zMzcgMS4wODcgMi45MTIuODI1Yy4wODgtLjY1LjM1LTEuMDg3LjYzOC0xLjMzN2MtMi4yMjUtLjI1LTQuNTUtMS4xMTMtNC41NS00LjkzOGMwLTEuMDg4LjM4Ny0xLjk4NyAxLjAyNS0yLjY4N2MtLjEtLjI1LS40NS0xLjI3NS4xLTIuNjVjMCAwIC44MzctLjI2MyAyLjc1IDEuMDI0YTkuMyA5LjMgMCAwIDEgMi41LS4zMzdjLjg1IDAgMS43LjExMiAyLjUuMzM3YzEuOTEzLTEuMyAyLjc1LTEuMDI0IDIuNzUtMS4wMjRjLjU1IDEuMzc1LjIgMi40LjEgMi42NWMuNjM3LjcgMS4wMjUgMS41ODcgMS4wMjUgMi42ODdjMCAzLjgzOC0yLjMzNyA0LjY4OC00LjU2MiA0LjkzOGMuMzYyLjMxMi42NzUuOTEyLjY3NSAxLjg1YzAgMS4zMzctLjAxMyAyLjQxMi0uMDEzIDIuNzVjMCAuMjYyLjE4OC41NzQuNjg4LjQ3NEExMC4wMiAxMC4wMiAwIDAgMCAyMiAxMmMwLTUuNTI1LTQuNDc1LTEwLTEwLTEwIi8+PC9zdmc+", alt="GitHub", _class="social-icon"), 
                          href="https://github.com/Giuseppe-Giovanni-Ingegnere-Sistemi", target="_blank"),
                        A(Img(src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MCIgaGVpZ2h0PSI0MCIgdmlld0JveD0iMCAwIDI0IDI0Ij48cGF0aCBmaWxsPSIjMDBmZjAwIiBkPSJNMTkuMDUgNC45MUE5LjgyIDkuODIgMCAwIDAgMTIuMDQgMmMtNS40NiAwLTkuOTEgNC40NS05LjkxIDkuOTFjMCAxLjc1LjQ2IDMuNDUgMS4zMiA0Ljk1TDIuMDUgMjJsNS4yNS0xLjM4YzEuNDUuNzkgMy4wOCAxLjIxIDQuNzQgMS4yMWM1LjQ2IDAgOS45MS00LjQ1IDkuOTEtOS45MWMwLTIuNjUtMS4wMy01LjE0LTIuOS03LjAxbS03LjAxIDE1LjI0Yy0xLjQ4IDAtMi45My0uNC00LjItMS4xNWwtLjMtLjE4bC0zLjEyLjgybC44My0zLjA0bC0uMi0uMzFhOC4yNiA4LjI2IDAgMCAxLTEuMjYtNC4zOGMwLTQuNTQgMy43LTguMjQgOC4yNC04LjI0YzIuMiAwIDQuMjcuODYgNS44MiAyLjQyYTguMTggOC4xOCAwIDAgMSAyLjQxIDUuODNjLjAyIDQuNTQtMy42OCA4LjIzLTguMjIgOC4yM200LjUyLTYuMTZjLS4yNS0uMTItMS40Ny0uNzItMS42OS0uODFjLS4yMy0uMDgtLjM5LS4xMi0uNTYuMTJjLS4xNy4yNS0uNjQuODEtLjc4Ljk3Yy0uMTQuMTctLjI5LjE5LS41NC4wNmMtLjI1LS4xMi0xLjA1LS4zOS0xLjk5LTEuMjNjLS43NC0uNjYtMS4yMy0xLjQ3LTEuMzgtMS43MmMtLjE0LS4yNS0uMDItLjM4LjExLS41MWMuMTEtLjExLjI1LS4yOS4zNy0uNDNzLjE3LS4yNS4yNS0uNDFjLjA4LS4xNy4wNC0uMzEtLjAyLS40M3MtLjU2LTEuMzQtLjc2LTEuODRjLS4yLS40OC0uNDEtLjQyLS41Ni0uNDNoLS40OGMtLjE3IDAtLjQzLjA2LS42Ni4zMWMtLjIyLjI1LS44Ni44NS0uODYgMi4wN3MuODkgMi40IDEuMDEgMi41NmMuMTIuMTcgMS43NSAyLjY3IDQuMjMgMy43NGMuNTkuMjYgMS4wNS40MSAxLjQxLjUyYy41OS4xOSAxLjEzLjE2IDEuNTYuMWMuNDgtLjA3IDEuNDctLjYgMS42Ny0xLjE4Yy4yMS0uNTguMjEtMS4wNy4xNC0xLjE4cy0uMjItLjE2LS40Ny0uMjgiLz48L3N2Zz4=", alt="Email", _class="social-icon"), 
                          href="https://wa.me/qr/U7C3KCW53O3XB1"),
                        A(Img(src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MCIgaGVpZ2h0PSI0MCIgdmlld0JveD0iMCAwIDI0IDI0Ij48cGF0aCBmaWxsPSIjMDBmZjAwIiBkPSJNMjAgMThoLTJWOS4yNUwxMiAxM0w2IDkuMjVWMThINFY2aDEuMmw2LjggNC4yNUwxOC44IDZIMjBtMC0ySDRjLTEuMTEgMC0yIC44OS0yIDJ2MTJhMiAyIDAgMCAwIDIgMmgxNmEyIDIgMCAwIDAgMi0yVjZhMiAyIDAgMCAwLTItMiIvPjwvc3ZnPg==", alt="Email", _class="social-icon"), 
                          href="mailto:ing.josejuangallegos@gmail.com"),
                        _class="social-icons"
                    ),
                    _class="contact terminal",
                    style="border-radius: 15px; overflow: hidden; padding: 20px; margin-bottom: 60px;"
                ),
                _class="container"
            )
        )
    )

serve()