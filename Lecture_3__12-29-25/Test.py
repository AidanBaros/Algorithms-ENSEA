def parse(ensea_code : str):
    if not ('[' in ensea_code):
        return Expression(ensea_code, [])
    symbol, args = ensea_code.split('[', maxsplit=1)
    args = args[:-1]
    parsed_args_list : list[Expression] = parse_comma(args)

    return Expression(symbol, parsed_args_list)

def parse_comma(args : str):
    args_list : list[str] = []
    current_arg : str = ""
    bracket_counter = 0

    for character in args:
        if character == '[':
            bracket_counter += 1
        
        elif character == ']':
            bracket_counter -= 1
        
        if character == ',' and bracket_counter == 0:
            args_list.append(current_arg)
            current_arg = ""
        
        else:
            current_arg += character
    
    args_list.append(current_arg)

    return [parse(arg) for arg in args_list]