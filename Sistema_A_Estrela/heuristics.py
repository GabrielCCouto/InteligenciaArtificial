def heuristic_destino_rj(node_name):
    heuristic_values = {
        'Porto Alegre': 1124,
        'Florianópolis': 748,
        'Curitiba': 676,
        'São Paulo': 357,
        'Rio de Janeiro': 0,
        'Belo Horizonte': 340,
        'Brasília': 933,
        'Cuiabá': 1576,
        'Salvador': 1210,
        'Fortaleza': 2190,
        'Manaus': 2849,
    }
    return heuristic_values[node_name]

def heuristic_destino_sp(node_name):
    heuristic_values = {
        'Porto Alegre': 852,
        'Florianópolis': 489,
        'Curitiba': 339,
        'São Paulo': 0,
        'Rio de Janeiro': 357,
        'Belo Horizonte': 490,
        'Brasília': 873,
        'Cuiabá': 1326,
        'Salvador': 1454,
        'Fortaleza': 2369,
        'Manaus': 2589,
    }
    return heuristic_values[node_name]

def heuristic_destino_bh(node_name):
    heuristic_values = {
        'Porto Alegre': 1341,
        'Florianópolis': 973,
        'Curitiba': 821,
        'São Paulo': 490,
        'Rio de Janeiro': 340,
        'Belo Horizonte': 0,
        'Brasília': 621,
        'Cuiabá': 1373,
        'Salvador': 964,
        'Fortaleza': 1893,
        'Manaus': 2446,
    }
    return heuristic_values[node_name]

def heuristic_destino_bsb(node_name):
    heuristic_values = {
        'Porto Alegre': 1621,
        'Florianópolis': 1315,
        'Curitiba': 1081,
        'São Paulo': 873,
        'Rio de Janeiro': 933,
        'Belo Horizonte': 621,
        'Brasília': 0,
        'Cuiabá': 880,
        'Salvador': 1059,
        'Fortaleza': 1688,
        'Manaus': 1939,
    }
    return heuristic_values[node_name]

def heuristic_destino_cuiaba(node_name):
    heuristic_values = {
        'Porto Alegre': 1679,
        'Florianópolis': 1544,
        'Curitiba': 1302,
        'São Paulo': 1326,
        'Rio de Janeiro': 1576,
        'Belo Horizonte': 1373,
        'Brasília': 880,
        'Cuiabá': 0,
        'Salvador': 1925,
        'Fortaleza': 2329,
        'Manaus': 1453,
    }
    return heuristic_values[node_name]

def heuristic_destino_salvador(node_name):
    heuristic_values = {
        'Porto Alegre': 2303,
        'Florianópolis': 1931,
        'Curitiba': 1784,
        'São Paulo': 1454,
        'Rio de Janeiro': 1210,
        'Belo Horizonte': 964,
        'Brasília': 1059,
        'Cuiabá': 1915,
        'Salvador': 0,
        'Fortaleza': 1028,
        'Manaus': 2606,
    }
    return heuristic_values[node_name]

def heuristic_destino_fortaleza(node_name):
    heuristic_values = {
        'Porto Alegre': 3241,
        'Florianópolis': 2858,
        'Curitiba': 2671,
        'São Paulo': 2369,
        'Rio de Janeiro': 2190,
        'Belo Horizonte': 1893,
        'Brasília': 1688,
        'Cuiabá': 2329,
        'Salvador': 1028,
        'Fortaleza': 0,
        'Manaus': 2384,
    }
    return heuristic_values[node_name]

def heuristic_destino_manaus(node_name):
    heuristic_values = {
        'Porto Alegre': 3132,
        'Florianópolis': 2982,
        'Curitiba': 2734,
        'São Paulo': 2589,
        'Rio de Janeiro': 2849,
        'Belo Horizonte': 2446,
        'Brasília': 1939,
        'Cuiabá': 1453,
        'Salvador': 2606,
        'Fortaleza': 2384,
        'Manaus': 0,
    }
    return heuristic_values[node_name]

def heuristic_destino_curitiba(node_name):
    heuristic_values = {
        'Porto Alegre': 547,
        'Florianópolis': 251,
        'Curitiba': 0,
        'São Paulo': 339,
        'Rio de Janeiro': 676,
        'Belo Horizonte': 821,
        'Brasília': 1081,
        'Cuiabá': 1302,
        'Salvador': 1784,
        'Fortaleza': 2671,
        'Manaus': 2734,
    }
    return heuristic_values[node_name]

def heuristic_destino_florianopolis(node_name):
    heuristic_values = {
        'Porto Alegre': 376,
        'Florianópolis': 0,
        'Curitiba': 251,
        'São Paulo': 489,
        'Rio de Janeiro': 748,
        'Belo Horizonte': 973,
        'Brasília': 1316,
        'Cuiabá': 1544,
        'Salvador': 1931,
        'Fortaleza': 2858,
        'Manaus': 2982,
    }
    return heuristic_values[node_name]

def heuristic_destino_porto_alegre(node_name):
    heuristic_values = {
        'Porto Alegre': 0,
        'Florianópolis': 376,
        'Curitiba': 547,
        'São Paulo': 852,
        'Rio de Janeiro': 1124,
        'Belo Horizonte': 1341,
        'Brasília': 1621,
        'Cuiabá': 1679,
        'Salvador': 2303,
        'Fortaleza': 3241,
        'Manaus': 3132,
    }
    return heuristic_values[node_name]