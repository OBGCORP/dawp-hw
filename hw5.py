from itertools import product

def product_of_sums_to_sum_of_products(expression):
    groups = [group.split('+') for group in expression.replace(')', '').split('(') if group.strip()]

    expanded_terms = product(*groups)

    result = ' + '.join([''.join(term.strip() for term in terms) for terms in expanded_terms])

    return result

if __name__ == "__main__":
    expressions = [
        "(x + y)(z + t)",
        "(x + y + z)(f + r + e)",
        "(a + b)(c + d)",
        "(a + b)(c + d)(e + f)"
    ]

    for expression in expressions:
        result = product_of_sums_to_sum_of_products(expression)
        print(f"{expression} -> {result}")