def cidades():
    return {
        'Manaus': {'Fortaleza': 2384, 'Cuiabá': 1453},
        'Fortaleza': {'Manaus': 2384, 'Brasília': 1600, 'Salvador': 1028},
        'Cuiabá': {'Rio de Janeiro': 1576, 'Manaus': 1453, 'Belo Horizonte': 1373},
        'Brasília': {'Fortaleza': 1600, 'Belo Horizonte': 600},
        'Salvador': {'São Paulo': 1454, 'Fortaleza': 1028},
        'Belo Horizonte': {'Cuiabá': 1373, 'Brasília': 600, 'São Paulo': 490, 'Rio de Janeiro': 340},
        'Rio de Janeiro': {'Cuiabá': 1576, 'Curitiba': 676, 'Belo Horizonte': 340},
        'São Paulo': {'Salvador': 1454, 'Belo Horizonte': 490, 'Curitiba': 339},
        'Curitiba': {'Rio de Janeiro': 676, 'São Paulo': 339, 'Florianópolis': 251},
        'Florianópolis': {'Porto Alegre': 376, 'Curitiba': 251},
        'Porto Alegre': {'São Paulo': 852, 'Florianópolis': 376},
    }
