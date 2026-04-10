import re

# Token patterns
TOKEN_SPEC = [
    ('KEYWORD',     r'\b(if|else|while|return|int|float|char|for)\b'),
    ('IDENTIFIER',  r'\b[A-Za-z_]\w*\b'),
    ('NUMBER',      r'\b\d+(\.\d+)?\b'),
    ('OPERATOR',    r'[+\-*/=<>!]=?|&&|\|\|'),
    ('SEPARATOR',   r'[(){},;]'),
    ('STRING',      r'"[^"]*"'),
    ('COMMENT',     r'//.*?$|/\*.*?\*/'),
    ('NEWLINE',     r'\n'),
    ('SKIP',        r'[ \t]+'),
    ('MISMATCH',    r'.')
]

# Compile into regex
TOK_REGEX = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC)
token_re = re.compile(TOK_REGEX, re.DOTALL | re.MULTILINE)

def tokenize(code):
    tokens = []
    for mo in token_re.finditer(code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NEWLINE' or kind == 'SKIP' or kind == 'COMMENT':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character: {value}')
        else:
            tokens.append((kind, value))
    return tokens

# Test
source_code = '''
int main() {
    float pi = 3.14;
    // Print something
    printf("Hello, World!");
    return 0;
}
'''

tokens = tokenize(source_code)
for t in tokens:
    print(t)
