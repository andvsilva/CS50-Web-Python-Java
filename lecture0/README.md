# Lecture 0 - HTML and CSS

To start, I will show a basic example to describe the structure of a webpage and explain the some details.

#### [webpage.html](webpage.html):

```bash
<!DOCTYPE html>
<!-- It is an information to the browser about the document type to expect -->

<html lang="en">
<!-- type of language: english -->

<head>
    <!-- Head of the page-->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HELLO</title>
    <!-- Title of the wepage-->
</head>

<body>
    <!-- Body of the webpage-->
    Hello.
</body>

</html>
<!-- end webpage-->
```

```bash
# To open this page in a web browser type in the terminal:
$ google-chrome webpage.html 
```

### Document Object Model:

A diagram to describe the webpage:

**NOTE**: 'mermaid' is not one functionality of the markdown in the GitHub. This
only works on [Visual Studio Code](https://code.visualstudio.com/).

```mermaid
graph TD;
    HTML-->HEAD;
    HTML-->BODY;
    HEAD-->TITLE;
    TITLE-->HELLO;
    BODY-->Hello;
```

![](figures/diagram_html_structure.png)

In this folder, we have basic examples of how to make html page and how to works with some elements as cited below (Quick and fast reference, for more information see [w3schools]((https://www.w3schools.com/html/))):

- [attribute](html/attribute.html)
- [descedant](html/descedant.html)
- [flexbox](html/flexbox.html)
- [font](html/font.html)
- [form](html/form.html)
- [formcolors](html/formcolors.html)
- [grid](html/grid.html)
- [image](html/image.html)
- [link](html/link.html)
- [lists](html/lists.html)
- [heading](html/heading.html)
- [table](html/table.html)

```bash
# compile css file
$ sass variables.scss:variables.css

# or to use 
$ sass --watch variables.scss:variables.css
```

## Useful References:

- [Lecture - HTML and CSS](https://cs50.harvard.edu/web/2020/notes/0/#:~:text=HTML%20and%20CSS)
- [HTML](https://www.w3schools.com/html/), [CSS](https://www.w3schools.com/css/)
