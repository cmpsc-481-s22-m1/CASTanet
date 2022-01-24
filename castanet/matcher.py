import libcst as cst

def try_matchers(cst_dict):
    for file in cst_dict:
        cast = cst_dict[file]
        functions = match.findall(cast, match.FunctionDef())
