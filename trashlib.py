trashVersion = "0.1.1-beta"
trashParserId = "lexer-rishit-khandelwal-1.7.2020"
trashParserIdShort = "rishit-khandelwal"

PWD = '~'

def trashParse(command):
    tmp = command
    argz = []
    tx = ''
    inString = False
    for letr in tmp:
        if letr == ' ' and not inString and tx != '':
            argz.append(tx)
            tx = ''
        if not inString and letr != ' ':
            tx += letr
        if letr == '"':
            inString = not inString
    argz.append(tx)
    return argz
    
prompt = f'trash-{trashVersion} running by {trashParserIdShort} | {PWD}>'