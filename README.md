![Version](https://img.shields.io/badge/version-0.1.0-orange.svg)
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
$ git clone https://github.com/vigo/textmate2-bulma.git textmate2-bulma.tmbundle
```

Reload TextMate If It’s needed.

---

## List of TAB Triggers

| Trigger                | Information                                 |
|:-----------------------|:--------------------------------------------|
| `new` + <kbd>⇥</kbd>  | Generates basic html starter page template. |
| `cl` + <kbd>⇥</kbd>   | Color helper                                |
| `typ` + <kbd>⇥</kbd>  | Typography helper                           |
| `col` + <kbd>⇥</kbd>  | Column helper                               |
| `cole` + <kbd>⇥</kbd> | Column examples                             |
| `lay` + <kbd>⇥</kbd>  | Layout helper                               |
| `laye` + <kbd>⇥</kbd> | Layout examples                             |

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


### `cl`

Covers text and background colors. Prefixes are:

- `has-text-`
- `has-background-`


### `typ`

Covers typography related; text sizes, alignments, text transformations,
weights and font family. Prefixes are:

- `is-size-`
- `is-size-` + responsive prefixes (*mobile, tablet etc...*)
- `has-text-`
- `has-text-` + responsive prefixes (*mobile, tablet, -only etc...*)
- `is-` + transformations (*lowercase etc...*)
- `is-` + weights (*bold etc...*)
- `is-family-` + families (*monospace etc...*)


### `col`

Covers column related snippets and class names.

- Column/Columns wrapper
- Column/Columns sizes and responsive (*three-quarters, two-thirds + mobile,tablet etc...*)
- 12 Columns system (`is-1` *etc...*)
- Offset, Gaps, Multiline, Vertical/Horizontal alignment prefixes
- Narrow column and responsive helpers


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


### `lay`

Covers layout helpers.

- Container
- Container Fluid / Responsive
- Level
- Level Item, Left/Right
- Media
- Media Content, Left/Right

### `laye`

Examples snippets for layout helpers

Level Examples

- Complex Navbar
- Centered Level
- Mobile Level

Media Example

- Tweet
- Disqus

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

