escapeProtect = "🵋"
def parseTag(line, skip=0):
    skipNext = skip
    split = line.replace("\:", "🵋")
    split = line.split(":")
    for i in range(len(split)-1):
        split[i] = split[i].replace("🵋", ":")
        split[i] = split[i].replace("\(", "🵋")
    split[0] = split[0].replace("(", "")
    for i in range(len(split)-1):
        split[i].replace("🵋", "(")
    if len(split) != 2:
        for i in range(1,len(split)):
            if skipNext!=0:
                skipNext = skipNext-1
                pass
            elif skipNext==0:
                split[i] = split[i].replace("\)", "🵋")
                split[i] = split[i].replace(")", "")
                split[i] = split[i].replace("🵋", ")")
                if split[i][0] == " ":
                    if split[i][1] == "'" or split[i][1] == '"':
                        split[i] = split[i][2:-1]
                    elif split[i][1] == "(":
                        this = split[i][1:]
                        next = split[i+1]
                        fl = True
                        c=1
                        p=next
                        while fl==True:
                            if p[0] == "(" or p[1] == "(":
                                next=f'{next}:{split[i+c]}'
                                p = split[i+c]
                                skipNext=skipNext+1
                                c=c+1
                            else:
                                skipNext=skipNext+1
                                fl = False
                        while next[-1] == ")":
                            if next[-1] == ")":
                                next = next[0:-1]
                        addBack = 0
                        for j in range(len(next)):
                            if(next[j] == "("):
                                addBack = addBack + 1
                        while addBack>0:
                            next=next+")"
                            addBack = addBack-1
                        split[i] = parseTag(f"{this}:{next}", skip=skipNext)
                elif split[i][0] == "'" or '"':
                    split[i] = split[1][2:-1]
                elif split[i][0] == "(":
                        this = split[i][1:]
                        next = split[i+1]
                        fl = True
                        c=1
                        p=next
                        while fl==True:
                            if p[0] == "(" or p[1] == "(":
                                next=f'{next}:{split[i+c]}'
                                p = split[i+c]
                                skipNext=skipNext+1
                                c=c+1
                            else:
                                skipNext=skipNext+1
                                fl = False
                        while next[-1] == ")":
                            if next[-1] == ")":
                                next = next[0:-1]
                        addBack = 0
                        for j in range(len(next)):
                            if(next[j] == "("):
                                addBack = addBack + 1
                        while addBack>0:
                            next=next+")"
                            addBack = addBack-1
                        split[i] = parseTag(f"{this}:{next}", skip=skipNext)
    else:
        split[1] = split[1].replace("\)", "🵋")
        split[1] = split[1].replace(")", "")
        split[1] = split[1].replace("🵋", ")")
        if split[1][0] == " ":
            if split[1][1] == "'" or '"':
                split[1] = split[1][2:-1]
            elif split[1][1] == "(":
                return("ERR 86")
        elif split[1][0] == "'" or '"':
            split[1] = split[1][2:-1]
        elif split[1][0] == "(":
            pass
    return [split[0],split[1]]
def parseSite(input):
    lines = []
    comments=[]
    variables={}
    metavariables={}
    tags=[]
    for line in input:
        lines.append(line)
    for line in lines:
        if line[:2] == "##":
            comments.append(line[2:])
        elif line[:2] == "+!":
            variable = line[2:].replace(" = ", "=").split("=")
            if variable[1][0] == "'" or variable[1][0] == '"':
                variable[1] =['str', variable[1][1:-1]]
            elif variable[1] == "True" or variable[1] == "False":
                variable[1]=['bol', variable[1]]
            elif int(variable[1]):
                variable[1]=['int', variable[1]]
            elif variable[1][0] == "!":
                variable[1]=variables[variable[1]]
            elif variable[1][0] == "%":
                variable[1]=metavariables[variable[1]]
            else:
                #TODO: GET CURRENT LINE NUMBER FOR ERROR
                return("!!Error on line (tba): Invalid Variable Type")
            variables[variable[0]]=variable[1]
        elif line[:2] == "+%":
            variable = line[2:].replace(" = ", "=").split("=")
            if variable[1][0] == "'" or variable[1][0] == '"':
                variable[1] =['str', variable[1][1:-1]]
            elif variable[1] == "True" or variable[1] == "False":
                variable[1]=['bol', variable[1]]
            elif int(variable[1]):
                variable[1]=['int', variable[1]]
            elif variable[1][0] == "!":
                variable[1]=variables[variable[1]]
            elif variable[1][0] == "%":
                variable[1]=metavariables[variable[1]]
            else:
                #TODO: GET CURRENT LINE NUMBER FOR ERROR
                return("!!Error on line (tba): Invalid MetaVariable Type")
            metavariables[variable[0]]=variable[1]
        elif line[0] == "(":
            tags.append(parseTag(line))
        elif line[0] == "$":
            pass
        elif line[0] == "+":
            working = line
            working = working[1:]
            working = working.replace(" = ", "=").split("=")
            if working[1][0] == "!":
                working[1]=variables[working[1][1:]][1]
            elif working[1][0] == "'" or working[1][0] == '"':
                working[1]=working[1][1:-1] 
            tag = tags[-1]
            if len(tag) == 2:
                tag.append([working])
            elif len(tag) == 3:
                tag[2].append(working)
            else:
                return("!!Error: Internal Error. Submit an issue with code 'r01:ev2:086'")
        else:
            return(f"!!Error on line (tba): Unknown line start. {line}")
    return comments, variables, metavariables, tags
def ptag2html(input):
    ptag=input
    tag="<"
    tag=tag+ptag[0]
    for attr in ptag[2]:
        tag = f"{tag} {attr[0]}='{attr[1]}'"
    tag = f"{tag}>"
    if type(ptag[1])!= str:
        tag=f"{tag}{ptag2html(ptag[1])}"
    else:
        tag=f"{tag}{ptag[1]}"
    tag=f"{tag}</{ptag[0]}>"
    return tag
def toHtml(input, part="all"):
    textInput = input
    input = input.replace("; ", "\n").replace(";", "\n")
    input = input.replace("\\\n", ";")
    input = input.splitlines()
    tags = []
    comments = []
    variables = {}
    metavariables = {}
    if input[0] == "$site":
        comments, variables, metavariables, tags = parseSite(input)
    elif input[0] == "$script":
        return "!!Error: Attempt to compile pure script into HTML"
    else:
        return f"!!Error on line 1: Unknown Daze type '{input[0]}'"
    parsedTags=""
    head=""
    for i in tags:
        parsedTags=f"{parsedTags}{ptag2html(i)}\n"    
    for i in metavariables.keys():
        o=""
        if not i in ['title']:
            # Create a standard meta tag && append it to the proccessed tags.
            o=f'<meta name="{i}" content="{metavariables[i][1]}">'
        else:
            o=f'<{i}>{metavariables[i][1]}</{i}>'
        head=f"{head}{o}\n"
    if part=="all":
        return f"""<!DOCTYPE html>
<html>
<head>

{head}
</head>
<body>

{parsedTags}
</body>
</html>"""
    elif part=="head":
        return f"""<head>

{head}
</head>"""  
    elif part=="body":
        return f"""<body>

{parsedTags}
</body>"""
    else:
        return f"!!Error: invalid part for toHtml '{part}'"