# Tutorial de Markdown

Markdown es una forma sencilla y fácil de dar formato al texto en la web. En este tutorial, aprenderemos los conceptos básicos de Markdown y cómo utilizarlo para crear documentos bien formateados.

## 1. Encabezados

Los encabezados se crean utilizando el símbolo `#` seguido de un espacio y el texto del encabezado. Cuantos más `#` coloques, menor será el tamaño del encabezado.

```markdown
# Encabezado 1
## Encabezado 2
### Encabezado 3
```

**Explicación:**
- Utiliza uno, dos o tres `#` para crear encabezados de diferentes niveles.
- Cuanto más alto sea el número de `#`, menor será el tamaño del encabezado.

## 2. Estilo de texto

Puedes dar formato al texto de diversas maneras:

- **Negrita**: `**Texto**` o `__Texto__`
- *Cursiva*: `*Texto*` o `_Texto_`
- ~~Tachado~~: `~~Texto~~`

**Explicación:**
- Usa `**` o `__` para negrita, `*` o `_` para cursiva, y `~~` para tachado.

## 3. Listas

### Lista no ordenada

```markdown
- Elemento 1
- Elemento 2
  - Elemento anidado
- Elemento 3
```

### Lista ordenada

```markdown
1. Elemento 1
2. Elemento 2
   1. Elemento anidado
3. Elemento 3
```

**Explicación:**
- Utiliza `-` o `*` para listas no ordenadas.
- Utiliza números seguidos de un punto para listas ordenadas.
- Puedes anidar listas usando espacios.

## 4. Enlaces

```markdown
[Texto del enlace](URL)
```

Ejemplo:

```markdown
[Google](https://www.google.com)
```

**Explicación:**
- Coloca el texto del enlace entre corchetes y la URL entre paréntesis.

## 5. Imágenes

```markdown
![Texto alternativo](URL de la imagen)
```

Ejemplo:

```markdown
![Logo de Markdown](https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Markdown-mark.svg/250px-Markdown-mark.svg.png)
```

**Explicación:**
- Similar a los enlaces, pero con un signo de exclamación al principio.

## 6. Citas

```markdown
> Esto es una cita.
```

**Explicación:**
- Utiliza el símbolo `>` seguido de un espacio para citas.

## 7. Bloques de código

Puedes resaltar el código usando comillas invertidas simples (\`) para código en línea o triples (\`\`\`) para bloques de código.

Código en línea: \`Código\`

Bloque de código:

\```python
def saludar():
    print("¡Hola, Markdown!")
\```

**Explicación:**
- Utiliza comillas invertidas para resaltar código en línea.
- Utiliza triples comillas invertidas para bloques de código, con la opción de especificar el lenguaje.

## 8. Línea horizontal

Puedes agregar una línea horizontal para separar secciones utilizando tres guiones (-), tres asteriscos (*), o tres guiones bajos (_).

```markdown
---
```

**Explicación:**
- Utiliza tres guiones, asteriscos o guiones bajos en una línea para crear una línea horizontal.