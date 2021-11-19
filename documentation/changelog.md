# Changelog
## v2.0.0a
### Changes
- [x] Seperate the `toHtml()` function into `toHtml()`, `parseSite()`, and `parseTag()`
- [X] Remove `$content` & `$variables` headers.
- [X] Add brand-new document types. `$script` for scripts & `$site` for websites and other digital content.
- [X] Improve Escaping
### Known Errors
- div elements still do not work. This will be changed shortly with the new engine.
### Fixed Errors
- Improve escaping system
### Language Changes
- Merge Variables and Tags into one section (removes `$variables` & `$content`)
- Add new `$script` & `$site` headers to determine doctype
### Notes
- Engine v2 is still a work-in-progress. The `daze` tool will soon have a command to test the beta.

## v1.2.0a
### Changes
- [x] Add new option to output partial html to the engine
- [x] Allow setting variables to variables
- [x] Merge `meta` and `variables` section and change the meta configuration.
- [x] Add comment support (see language changes)
- [x] Add support for `(img)` tags
- [x] Add support for JavaScript
- [x] Add support for CSS
### Known Errors
- div elements do not work. This should be fixed by v1.4.0
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