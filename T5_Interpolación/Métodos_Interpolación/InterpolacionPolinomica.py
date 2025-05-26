def main():
    # Valores conocidos (x, y)
    x = [1, 2, 3]
    y = [1, 8, 27]

    # Valor donde se desea interpolar
    x_bus = 2.5

    # Valor real conocido en x = 2.5 (por ejemplo, para f(x) = x^3)
    valor_real = 15.625

    # Realizar interpolación
    resultado = interpolar_polinomio(x, y, x_bus)

    # Mostrar resultado de interpolación
    print(f"Valor Interpolado en x = {x_bus:.1f}: {resultado:.4f}")

    # Calcular y mostrar errores
    error_abs = calcular_error(valor_real, resultado)
    error_porcentual = calcular_error_porcentual(valor_real, resultado)
    print(f"Cuota de error estimada: {error_abs:.4f}")
    print(f"Error Porcentual: {error_porcentual:.2f}%")

    # Mostrar puntos utilizados
    print("\nPuntos Utilizados:")
    for i in range(len(x)):
        print(f"x = {x[i]:.1f}, y = {y[i]:.1f}")

if __name__ == "__main__":
    main()
