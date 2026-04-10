import re

# Token patterns (updated)
TOKEN_SPEC = [
    ('KEYWORD',     r'\b(if|else|while|return|int|float|char|for|void|printf)\b'),
    ('IDENTIFIER',  r'\b[A-Za-z_]\w*\b'),
    ('NUMBER',      r'\b\d+(\.\d+)?\b'),
    ('STRING',      r'"[^"\n]*"'),
    ('OPERATOR',    r'==|!=|<=|>=|&&|\|\||[+\-*/=<>]'),
    ('SEPARATOR',   r'[(){},;]'),
    ('COMMENT',     r'//.*?$|/\*.*?\*/'),
    ('NEWLINE',     r'\n'),
    ('SKIP',        r'[ \t]+'),
    ('MISMATCH',    r'.')
]

# Compile regex
TOK_REGEX = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC)
token_re = re.compile(TOK_REGEX, re.MULTILINE | re.DOTALL)

def tokenize(code):
    tokens = []
    line_num = 1

    for mo in token_re.finditer(code):
        kind = mo.lastgroup
        value = mo.group()

        if kind == 'NEWLINE':
            line_num += 1
        elif kind in ('SKIP', 'COMMENT'):
            continue
        elif kind == 'MISMATCH':
            print(f"⚠️ Error at line {line_num}: Unexpected '{value}'")
        else:
            tokens.append((kind, value, line_num))

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