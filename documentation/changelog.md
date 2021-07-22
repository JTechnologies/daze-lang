# Changelog
## v0.2.0a
### Changes
- [x] Add new option to output partial html to the engine
- [x] Allow setting variables to variables
- [x] Merge `meta` and `variables` section and change the meta configuration.
- [x] Add comment support (see language changes)
- [x] Add support for `(img)` tags
- [x] Add support for JavaScript
- [x] Add support for CSS
### Known Errors
- div elements do not work. This should be fixed by v0.4.0
### Fixed Errors
*none*
### Language Changes
- Declaring a variable is now done with `+!`
- Metavariables may be set to variables
- Variables may be set to other variables
- Declaring a metavariable is now done with `+%`
- Tags must now have quotes surrounding the content, making `(h1: Hi)` `(h1: "Hi")`
### Notes
*none*
