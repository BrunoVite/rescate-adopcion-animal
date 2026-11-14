# Informe académico — Actividad #1: Sistema de Control de Rescate y Adopción Animal

Estudiante: Bruno Duvan Vite Santos — Paralelo A — UTM
Repositorio: https://github.com/BrunoVite/rescate-adopcion-animal

## 1. Introducción

Este informe documenta el análisis y el diseño orientado a objetos de un sistema de control de rescate y adopción animal. El sistema permite registrar casos de rescate reportados por ciudadanos, categorizarlos por especie, asignar personal (voluntarios o veterinarios), dar seguimiento al estado del caso y gestionar la adopción. El diseño se modela con UML (casos de uso y clases), aplica patrones de diseño y registra su evolución en GitHub con el flujo de trabajo Gitflow.

## 2. Análisis del escenario

Actores:
- Ciudadano/Reportante: reporta un animal en situación de rescate y consulta el estado de su caso.
- Voluntario/Veterinario: recibe notificaciones de nuevos rescates, registra y categoriza al animal y actualiza el estado del caso.
- Administrador del Refugio: asigna personal, gestiona las adopciones y administra usuarios y reportes.

Requerimientos funcionales (RF):
- RF1: crear un caso de rescate.
- RF2: categorizar la especie del animal (perro, gato, fauna silvestre).
- RF3: asignar un voluntario o veterinario al caso.
- RF4: cambiar el estado del caso (Rescatado, En tratamiento, En adopción, Adoptado).
- RF5: notificar al personal cuando se registra un nuevo caso.
- RF6: consultar el estado de un caso.

Requerimientos no funcionales (RNF):
- Escalabilidad: poder agregar nuevas especies o tipos de personal sin modificar el código existente.
- Mantenibilidad: bajo acoplamiento y responsabilidades separadas (MVC y SOLID).
- Trazabilidad: historial de versiones y de cambios mediante Gitflow.

## 3. Diagrama de casos de uso

El diagrama está en docs/casos_de_uso.dot. Los casos de uso por actor son:
- Reportante: Reportar rescate; Consultar estado del caso.
- Voluntario: Recibir notificación de nuevo rescate; Actualizar estado del caso; Registrar y categorizar animal.
- Administrador: Asignar voluntario o veterinario; Gestionar adopción; Administrar usuarios y reportes.

## 4. Diagrama de clases

El diagrama está en docs/clases.dot. Las clases principales son:
- Expediente (abstracta), con los atributos id, nombre y estado, y los métodos cambiar_estado() y obtener_protocolo().
- ExpedientePerro, ExpedienteGato y ExpedienteFauna, que heredan de Expediente.
- ExpedienteFactory, que crea los expedientes según la especie.
- GestorCasos (Singleton), que gestiona los expedientes y notifica a los observadores.
- Sujeto y Personal (Observer), donde Personal es el observador concreto.
- CasoController y CasoView (MVC), que separan la lógica de presentación de la lógica de negocio.

Se aplican los principios SOLID: responsabilidad única (cada clase hace una cosa), abierto/cerrado (nuevas especies sin modificar la lógica existente), sustitución de Liskov (cualquier subclase de Expediente se usa donde se espera un Expediente) e inversión de dependencias (el controlador depende de abstracciones).

## 5. Patrones de diseño implementados

Se implementan cuatro patrones, uno por encima del mínimo de tres exigido:

| Patrón | Tipo | Archivo | Problema que resuelve |
|---|---|---|---|
| Factory Method (fábrica) | Creacional | src/patterns/factory.py | Crear el expediente correcto según la especie |
| Singleton | Creacional | src/patterns/singleton.py | Garantizar una única instancia del gestor de casos |
| Observer | Comportamiento | src/patterns/observer.py | Notificar al personal cuando se registra un caso |
| MVC | Arquitectónico | src/controller/caso_controller.py | Separar modelo, vista y controlador |

## 6. Justificación de la clasificación de la fábrica basada en diccionario

La fábrica ExpedienteFactory se clasifica como un patrón creacional, en la variante de fábrica parametrizada (Simple Factory) que sigue la intención del Factory Method: delegar la creación de objetos de una jerarquía (Expediente) para que el cliente no dependa de las clases concretas. En lugar de usar una cadena de condicionales if/elif, la fábrica usa un diccionario (TIPOS) que asocia el nombre de la especie con su clase concreta.

Por qué se eligió el diccionario:
- Cumple abierto/cerrado: para soportar una especie nueva basta con agregar una clase y una entrada en el diccionario, sin modificar la lógica de creación.
- Elimina la complejidad de condicionales anidados y hace la búsqueda directa, en tiempo constante.
- Es adecuada para este dominio, porque todos los expedientes se construyen con los mismos parámetros (id y nombre) y solo cambia la clase concreta. Por ello no se justifica una jerarquía paralela de creadores como en el Factory Method clásico de GoF, que añadiría clases sin aportar valor.
- Mantiene al controlador desacoplado de las clases concretas: solo conoce ExpedienteFactory.crear(especie, id, nombre) y trabaja con la abstracción Expediente (polimorfismo).
- Facilita la trazabilidad y las pruebas, ya que el catálogo de especies queda en un único lugar visible.

Limitaciones y alternativa: la versión con diccionario no es el Factory Method puro de GoF, que usa subclases creadoras. Si en el futuro cada especie requiriera parámetros o lógica de construcción distintos, se evolucionaría a creadores por especie. Una mejora inmediata es lanzar un error claro cuando la especie no exista en el diccionario y permitir el registro dinámico de nuevas especies.

## 7. Flujo de trabajo Gitflow

El repositorio usa ramas main (versión estable), develop (integración), feature/* (patron-singleton, patron-mvc, entre otras), release/1.0.0 y las ramas de apoyo. Cada patrón se desarrolló en su rama feature, se integró mediante pull request y la versión 1.0.0 se publicó mediante la rama de release (archivo VERSION). Este informe se publica en la rama feature/informe-academico y se integra mediante pull request.

## 8. Conclusiones

El diseño propuesto cubre los requerimientos funcionales y no funcionales del caso, se modela con UML y aplica cuatro patrones que reducen el acoplamiento y facilitan la extensión del sistema. La fábrica basada en diccionario ofrece un equilibrio entre simplicidad y extensibilidad adecuado para el tamaño del dominio, y Gitflow deja un registro trazable del avance del diseño.
