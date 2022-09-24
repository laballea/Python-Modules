kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

def display(var):
    for key, value in var.items():
        print(key + " was created by " + value)

display(kata)