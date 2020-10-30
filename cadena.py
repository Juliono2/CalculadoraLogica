def proposicion(p):
	aux=''
	aux = p.replace('^', ' and ', p.count("^"))
	p = aux.replace('v', ' or ', p.count("v"))
	aux = p.replace('→', ' => ', p.count("→"))
	p = aux.replace('↔', ' = ', p.count("↔"))
	aux = p.replace('[', ' ( ', p.count("["))
	p = aux.replace(']', ' ) ', p.count("]"))
	return p

def variables(s):

	if("p" in s and "q" in s and "r" in s):
		variables = ['p', 'q' , 'r']
		return variables
	elif("p" in s and "q" in s):
		variables = ['p' , 'q']
		return variables
	elif("p" in s and "r" in s):
		variables = ['p' , 'r']
		return variables

def preposicionesConjugadas(p):
    preposiciones = []
    for i in p:

        if (i == "["):

            inicio = p.find("[") + 1
            range = p.rfind("]")


            preposiciones.append(proposicion(p[inicio:range]))
            p = p.replace(p[inicio-1:range+1], p[inicio:range])

        if (i == "("):

            inicio = p.find("(") + 1
            range = p.find(")")
            preposiciones.append(proposicion(p[inicio:range]))
            p = p.replace(p[inicio-1:range+1], p[inicio:range])

    return preposiciones
