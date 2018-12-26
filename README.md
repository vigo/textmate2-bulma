![Version](https://img.shields.io/badge/version-0.2.0-orange.svg)
![Bulma](https://img.shields.io/badge/bulma-0.7.2-green.svg)
![Fontawesome](https://img.shields.io/badge/fontawesome-5.3.1-green.svg)
![Plaftorm](https://img.shields.io/badge/platform-TextMate-blue.svg)

# TextMate Bulma CSS framework bundle

Un-official Bulma CSS helper bundle for you with ❤️ You can visit Bulma’s
web site via https://bulma.io

All the example snippets are borrowed from Bulma’s examples!

---

## Installation

```bash
$ cd "$HOME/Library/Application Support/TextMate/Bundles/"
$ git clone https://github.com/vigo/textmate2-bulma.git Bulma.tmbundle
```

Reload TextMate If It’s needed.

---

## List of TAB Triggers

| Trigger                | Information                                 |
|:-----------------------|:--------------------------------------------|
| `new` + <kbd>⇥</kbd>  | Generates basic html starter page template. |
| `hlp` + <kbd>⇥</kbd>  | Helper classes                              |
| `col` + <kbd>⇥</kbd>  | Column helper                               |
| `cole` + <kbd>⇥</kbd> | Column examples                             |
| `lay` + <kbd>⇥</kbd>  | Layout helper                               |
| `laye` + <kbd>⇥</kbd> | Layout examples                             |
| `frm` + <kbd>⇥</kbd>  | Form helpers                                |
| `faw` + <kbd>⇥</kbd>  | Fontawesome helpers                         |

---

### `new`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>${1:Title}</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.2/css/bulma.min.css">
    <script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>
</head>
<body>
    <section class="section">
        <div class="container">
            <h1 class="title">Hello World</h1>
            <p class="subtitle">My first website with <strong>Bulma</strong>!</p>
        </div>
    </section>
</body>
</html>
```

---

### `hlp`

#### Color Helpers

Covers text and background colors. Prefixes are:

- `has-text-`
- `has-background-`


#### Typography Helpers

Covers typography related; text sizes, alignments, text transformations,
weights and font family. Prefixes are:

- `is-size-`
- `is-size-` + responsive prefixes (*mobile, tablet etc...*)
- `has-text-`
- `has-text-` + responsive prefixes (*mobile, tablet, -only etc...*)
- `is-` + transformations (*lowercase etc...*)
- `is-` + weights (*bold etc...*)
- `is-family-` + families (*monospace etc...*)

#### Responsive Visibility Helpers

`block`:

- `is-block-mobile`
- `is-block-touch`
- `is-block-tablet`
- `is-block-tablet-only`
- `is-block-desktop`
- `is-block-desktop-only`
- `is-block-widescreen`
- `is-block-widescreen-only`
- `is-block-fullhd`

`flex`:

- `is-flex-mobile`
- `is-flex-touch`
- `is-flex-tablet`
- `is-flex-tablet-only`
- `is-flex-desktop`
- `is-flex-desktop-only`
- `is-flex-widescreen`
- `is-flex-widescreen-only`
- `is-flex-fullhd`

`inline`:

- `is-inline-mobile`
- `is-inline-touch`
- `is-inline-tablet`
- `is-inline-tablet-only`
- `is-inline-desktop`
- `is-inline-desktop-only`
- `is-inline-widescreen`
- `is-inline-widescreen-only`
- `is-inline-fullhd`

`inline-block`:

- `is-inline-block-mobile`
- `is-inline-block-touch`
- `is-inline-block-tablet`
- `is-inline-block-tablet-only`
- `is-inline-block-desktop`
- `is-inline-block-desktop-only`
- `is-inline-block-widescreen`
- `is-inline-block-widescreen-only`
- `is-inline-block-fullhd`

`inline-flex`:

- `is-inline-flex-mobile`
- `is-inline-flex-touch`
- `is-inline-flex-tablet`
- `is-inline-flex-tablet-only`
- `is-inline-flex-desktop`
- `is-inline-flex-desktop-only`
- `is-inline-flex-widescreen`
- `is-inline-flex-widescreen-only`
- `is-inline-flex-fullhd`

`hidden`:

- `is-hidden-touch`
- `is-hidden-mobile`
- `is-hidden-tablet`
- `is-hidden-tablet-only`
- `is-hidden-dektop`
- `is-hidden-desktop-only`
- `is-hidden-widescreen`
- `is-hidden-widescreen-only`
- `is-hidden-fullhd`

#### Floating, Spacing and More

Floating;

- `is-clearfix`
- `is-pulled-left`
- `is-pulled-right`

Spacing;

- `is-marginless`
- `is-paddingless`

And more...

- `is-overlay`
- `is-clipped`
- `is-radiusless`
- `is-shadowless`
- `is-unselectable`
- `is-invisible`
- `is-sr-only`

---

### `col`

Covers column related snippets and class names.

- Column/Columns wrapper
- Column/Columns sizes and responsive (*three-quarters, two-thirds + mobile,tablet etc...*)
- 12 Columns system (`is-1` *etc...*)
- Offset, Gaps, Multiline, Vertical/Horizontal alignment prefixes
- Narrow column and responsive helpers

---

### `cole`

Example snippets for column helpers.

- 2,3,4,6,8 Columns
- Auto Columns
- 12 Column 1 to 12
- 4 Columns responsive
- 3 + 1 Columns responsive and variable sizes
- Vertical centered and multi lines
- Multine in a single row for mobile
- Centerin Colums

---

### `lay`

Covers layout helpers.

- Container
- Container Fluid / Responsive
- Level
- Level Item, Left/Right
- Media
- Media Content, Left/Right
- Hero variations (*color, gradient, size, three parts etc*)
- Section
- Footer

---

### `laye`

Examples snippets for layout helpers

Level Examples

- Complex Navbar
- Centered Level
- Mobile Level

Media Examples

- Tweet
- Disqus

Tile Examples

- 2 Different titles
- 3 and 4 Columns

---

### `frm`

Covers form helpers

- Control Classes (*label, input etc...*)
- Field variations
- Control variations (*sizes, loading etc..*)
- Input
- Button

---

### `faw`

Choose Fontawesome icon from selection UI or auto-completion box. Selection UI
uses AppleScript to build UI. It takes a bit time for building 1400+ options.
If you now the icon, try **Class Only** edition for much much faster.

---

### TODO

- Form missing items (*Textarea, Select etc...*)
- Elements (*Box, Content etc...*)
- Components (*Breadcrumb, Card etc...*)

---

## Screenshots

- [Fontawesome selector](Screenshots/fontawesome.png)
- [Layout Helper](Screenshots/layout.png)
- [Form Helper](Screenshots/form.png)
- [Helper Classes](Screenshots/helpers.png)

---

## Contributer(s)

* [Uğur "vigo" Özyılmazel](https://github.com/vigo) - Creator, maintainer


---


## Contribute

All PR’s are welcome!

1. `fork` (https://github.com/vigo/textmate2-bulma/fork)
1. Create your `branch` (`git checkout -b my-features`)
1. `commit` yours (`git commit -am 'added killer options'`)
1. `push` your `branch` (`git push origin my-features`)
1. Than create a new **Pull Request**!


---


## License

This project is licensed under MIT

