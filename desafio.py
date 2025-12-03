def total_sales(sales, department):

    if not sales:
        return [0, 0.0]
    
    first = sales[0]
    parts = first.split(',')
    
    if len(parts) < 4:
        return total_sales(sales[1:], department)
    
    try:
        price = float(parts[2])
    except ValueError:
        price = 0.0
    
    dept = parts[3].strip()
    
    rest_count, rest_total = total_sales(sales[1:], department)
    
    if dept == department:
        return [rest_count + 1, rest_total + price]
    else:
        return [rest_count, rest_total]


def print_result(result):
    count, total = result
    print(f"{count} VENDAS")
    print(f"TOTAL = $ {total:.2f}")


if __name__ == "__main__":
    vendas = [
        "8349,14/09/2024,899.9,ESPORTE",
        "4837,17/09/2024,530.0,VESTUARIO",
        "15281,21/09/2024,1253.99,ESPORTE",
        "15344,27/09/2024,1000.9,VESTUARIO",
        "18317,04/10/2024,250.4,VESTUARIO",
        "18972,11/10/2024,385.5,JARDINAGEM"
    ]

    print("Departamento: VESTUARIO")
    resultado1 = total_sales(vendas, "VESTUARIO")
    print_result(resultado1)

    print("\nDepartamento: ESPORTE")
    resultado2 = total_sales(vendas, "ESPORTE")
    print_result(resultado2)
