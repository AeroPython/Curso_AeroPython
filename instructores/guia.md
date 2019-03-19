# Introducción



# Configuración

- Instalar Anaconda: generalmente, el curso se imparte con la última versión de Ananconda disponible en https://www.anaconda.com/distribution/. Esto debe confirmarse con el resto de instructores y con las personas encargadas de la instalación en los ordenadores que vayan a utilizarse.
- Instalar git: git no es necesario para los alumnos. No obstante, es necesario que los instructores dispongan de él para poder modificar y adaptar el contenido del curso. Se puede bajar en: https://git-scm.com/downloads. Un tutorial sencillo se puede seguir en: http://gitimmersion.com/.
- Tener una cuenta en https://github.com/ para poder publicar los cambios, abrir issues, editar la wiki...
- El usuario debe pertencer al grupo instructors en la organización aeropython: https://github.com/orgs/AeroPython/teams/instructors/ Ese permiso pueden proporcionarlo los administradores del repo. Si no dispones del mismo ponte en contacto con ellos o abre un issue: https://github.com/AeroPython/Curso_AeroPython/issues
- Al menos uno de los instructores tendrá permiso para fusionar Pull Requests a la rama master durante el desarrollo del curso.


# Descargando el material

- El primer paso consiste en clonar el rpeositorio oficial del curso: https://github.com/AeroPython/Curso_AeroPython

```
$ git clone git@github.com:AeroPython/Curso_AeroPython.git
```

- Si ya clonaste el material en otra ocasión o quieres actualizarlo debes ejecutar:

`$ git fetch origin`
`$ git merge --ff-only origin master`

# Preparando un curso

- Asegurarse de que existe una release para la edición anterior del curso: https://github.com/AeroPython/Curso_AeroPython/releases
- Añadir la nueva edición al readme
- Añadir a los nuevos colaboradores al readme
- Opcional: crear un nuevo proyecto https://github.com/AeroPython/Curso_AeroPython/projects
- Establecer el calendario y el horario.
- Asignar a cada día los notebooks que se utilizarán
- Crear un issue por día en el que figuren: fecha, notebooks asignados al día, persona asignada a cada notebook, otras tareas relacionadas con la sesión.
  - El título sugerido es día/mes Nombre de la clase.
  - Las tareas asociadas pueden crearse en nuevos issues si tienen entidad suficiente
  - Los issues se utilizarán para marcar el progreso, hacer preguntas para coordinar la clase, remarcar aspectos que se resaltarán sobre la clase...


# Preparando una clase

En el funcionamiento típico del curso, cada sesión la imparten dos personas (como mínimo). Cada una estará encargada de la revisión de unos notebooks (normalmente la mitad cada uno).

- El primer paso siempre es actualizar el repositorio local:

`$ git fetch origin`
`$ git checkout master`
`$ git merge --ff-only origin master`

- Para la revisión de la parte asignada el primer paso será crear una rama desde la master:

`$ git checkout -b nombre-rama`

Se recomienda que el nombre de la rama incluya la fecha de la clase seguido de `a` si es la primera parte o `b` si es la segunda parte de la sesión

- Se trabajará siempre sobre la carpeta notebooks_completos
- Se realizarán los cambios deseados en el notebook de la sesión teniendo en cuenta que:
   - El curso debe evolucionar con el lenguaje. Debe evitarse que aparezcan formas arcaicas de hacer las cosas cuando existen nuevas alternativas más sencillas o ha cambiado el estándar, deben evitarse los DeprecationWarning...
   - Se deben releer las explicaciones que acompañan el código. Nunca es un mal momento para corregir erratas, hacer acalraciones extra, añadir enlaces...
   - Se debe intentar no borrar material: es preferible dejarlo completo y saltarlo durante la clase. Si hay gran cantidad de material en esta situación quizá convenga partir el notebook en dos o plantearse si realmente quiere trabajarse ese material con los alumnos.
   - Al generar los notebooks vacíos (ver más abajo) todas las celdas de código se vaciarán al final excepto las que comiencen con `# aeropython: preserve`. No se eliminarán las líneas comentadas de ninguna celda. Una parte importante del proceso de preparación consiste en elegir, qué se escribe en directo con los alumnos y qué se deja ya relleno para tan solo ejecutarlo.

- Una vez hechos los cambios se hará commit. Preferiblemente cada cambio irá acompañado de su commit en lugar de hacer un sólo commit para todos los cambios:

`$ git add notebooks_completos/nombre_del_notebook`
`$ git commit -m "descripción del cambio"`

- Una vez hechos todos los commits necesarios o cuando se quiera compartir el progreso con el resto de instructores se hará push al repositorio:

`$ git push origin/nombre-rama`

- Por último, generar la versión vacía de los notebooks. Situando el directorio activo en la carpeta principal del curso, ejecutar el archivo `empty_nb.py` situado en la carpeta `utils`:

`$ python utils/empty_nb.py`

Si todo va bien aparecerá una nueva versión vacía de todos los notebooks basada en la versión actual de los notebooks completos.


- Cuando se haya terminado el proceso de revisión, hará un Pull Request para incluir la rama que se ha creado en la master.

  - Ir a https://github.com/AeroPython/Curso_AeroPython y seleccionar la rama deseada.
  - Pulsar el botón de New Pull Request
  - Rellenar el título con la fecha de la clase y el título
  - Describir brevemente los cambios en la parte reservada para comentarios
  - Seleccionar como revisor a la persona con permisos para fusionar los cambios y a todo a aquel a quien se quiera implicar en la revisión
  - Si se está usando la opción de proyectos en GitHub, seleccionar el proyecto

- Al cerrar el PR, asegurarse de que se genreraron los notebooks vacíos, marcar como completados los puntos necesarios en el issue de la clase y cerrarlo si está todo terminado


# Impartiendo una clase

- Antes de empezar, actualizar el repositorio, bien descargando de nuevo el ZIP o haciendo pull con git. Es normal que se hayan incluido cambios de última hora y que la versión del ordenador personal o del aula no estén actualizadas.
- Pedir a los alumnos que descarguen de nuevo el material con cuidado de no reemplazar sus cambios personales del día anterior
- Prestar atención al paso anterior y al arranque del notebook. Mucha gente tiene dificultades aquí los primeros días
- Abrir siempre el notebook vacio

## Consejos
- Recueda que el mayor éxito del curso es que la gente haga cosas, no que escuche cosas.
- Si todo el mundo está muy callado y no responde a las preguntas, sobre todo al principio de la clase, trata de averiguar si les ha salido algún error y se encuentran atascados.
- Da tiempo a los alumnos para que copien lo que escribes.
- Tómate tiempo en explicar lo que has hecho, incentiva que te pregunten o te sugieran alternativas. Levántate si es posible para esta parte.
- Evita subir y bajar en el notebook todo el rato buscando cosas, marea a los alumnos.
- Evita copiar y pegar código, si tú lo reescribes, ellos tienen más tiempo de seguirte.
- Trata de dejar a los alumnos que resuelvan pequeños retos, paséate por la mesas para ver si progresan, si les salen errores o si ya han terminado. Discute con ellos otras posibles soluciones.
- 
- Si no eres el instructor principal:

  - Asegúrate de que la pantalla está lo suficientemente grande y se ve desde cualquier punto del aula
  - Hazle una señal al instructor principal si va demasiado rápido o si la mayoría del aula ha encontrado un problema que les impide seguir. Ten en cuenta que la mayoría de dificultades se producen al principio de la sesión.
  - Muévete por el aula mientras los alumnos siguen la clase para comprobar cómo van. En ocasiones, no te preguntarán nada si no te acercas tú primero.
  - Incentiva a los alumnos a que pregunten las dudas más generales en alto, si te preguntan una duda de este tipo, repítela en alto para todos.
