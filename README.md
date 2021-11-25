# Daze
A declarative langauge for building websites
# Basic Syntax
## Layouts
The layout of daze code is unique.
Here is the basic layout:
```daze
<type>
<content>
```
### Types
There are two types of daze. The first is a `$site`, which structures data for display, and the second is a `$script`, which is not implemented yet. Tags are only used in a site.
### Variables
Variables are declared using the syntax `+!variable=content`. You may have an unlimited amount of variables, although this may increase the compilation time.

Strings must be enclosed in ```"``` or ```'```. Variables do not support key/value sets or lists for the moment. Basic logical programming and addition will be comming soon (tm). You may set variables to other variables, but wherever you reference a variable with `!`, you must make sure to follow the variable name with a space. Additionally, metavariables may be used to store basic information about the site. All variables here are put into Meta tags, excluding the `%title` variable, which gets inserted into a `<title>` tag at compilation. Metavariables follow the rules of variables with the addition of being able to reference metavariables using % instead of a !.
### Tags
You can use any normal HTML tags here. Here is the syntax:
`(tag: 'content')`. Pretty simple, right? Content must be enclosed in quotes, and you may only reference variables inside of the quotes. Make sure to follow all the variable references with a space. But there is a catch to this aproach: There is no area for attributes. There is a solution. After each tag, you can place an attribute. The syntax for this is almost identical to the syntax for declaring a variable. Here it is: `+attribute=content`. Like the metavariables, these may only store strings enclosed in `""` or `''`. This will not change in the future. You can reference variables in attributes.
# Compilation
Compilation is easy with the `daze` tool installed. This tool is currently available as a standalone tool (available in the releases). The only requirement to install the tool is to have `python` installed. This requirement will be removed soon, as a bianary package is in the works. Here is the syntax for the daze tool:
`daze compile <input .daze file> <output .daze file>`