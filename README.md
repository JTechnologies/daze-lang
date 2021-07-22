# Daze
A declarative langauge for building websites
# Basic Syntax
## Layouts
The layout of daze code is unique.
Here is the basic layout:
```daze
$variables
# Variables Here.
$content
# Webpage code here.
```
Here is a basic overview of these sections
### $variables
The `$variables` section is the place to declare all variables. Variables are declared using the syntax `+!variable=content`. You may have an unlimited amount of variables, although this may increase the compilation time.
An example `$variables` section would be:
```daze
$variables
!bestlanguage="Daze"
```
Variables may only store strings for the time. *This will change soon.*
Strings must be enclosed in ```"``` or ```'```. Variables do not support key/value sets or lists for the moment. Basic logical programming and addition will be comming soon (tm). You may set variables to other variables, but wherever you reference a variable with `!`, you must make sure to follow the variable name with a space. Additionally, metavariables may be used to store basic information about the site. All variables here are put into Meta tags, excluding the `%title` variable, which gets inserted into a `<title>` tag at compilation. Metavariables follow the rules of variables with the addition of being able to reference metavariables using % instead of a !.
### $content
The `$content` section contains all the visible content on the site. Variables may not be declared here. You can use any normal HTML tags here. Here is the syntax:
`(tag: content)`. Pretty simple, right? Content must be enclosed in quotes, and you may only reference variables inside of the quotes. Make sure to follow all the variable references with a space. But there is a catch to this aproach: There is no area for attributes. There is a solution. After each tag, you can place an attribute. The syntax for this is almost identical to the syntax for declaring a variable. Here it is: `+attribute=content`. Like the variables, these may only store strings enclosed in `""` or `''`. This will not change in the future. You cannot reference variables in attributes.
# Compilation
Compilation is easy with the `daze` tool installed. This tool is currently available as a standalone tool (available in the releases). The only requirement to install the tool is to have `python` installed. This requirement will be removed soon, as a bianary package is in the works. Here is the syntax for the daze tool:
`daze compile <input .daze file> <output .daze file>`
## Installation
### AUR (Arch Linux/Manjaro)
#### Arch
With Yay or your favorite AUR helper:
`yay -S daze`
#### Manjaro
With AUR support enabled from Add/Remove Software:
`pamac install daze`
### From Source
Download the daze file from releases. Add this file to PATH. The `daze` command should be available after relaunching the terminal. An installation script is comming soon along with a Debian package.
