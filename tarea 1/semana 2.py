# Código en C# con comentarios explicativos
codigo_csharp = """
// Clase para representar un Circulo
public class Circulo
{
    // Campo privado para almacenar el radio del circulo
    private double radio;

    // Constructor que inicializa el valor del radio
    public Circulo(double radio)
    {
        this.radio = radio;
    }

    // CalcularArea es un método que devuelve un valor double. 
    // Se utiliza para calcular el área de un círculo. No requiere argumentos adicionales.
    public double CalcularArea()
    {
        // Formula: Area = PI * radio^2
        return Math.PI * Math.Pow(radio, 2);
    }

    // CalcularPerimetro es un método que devuelve un valor double.
    // Se utiliza para calcular el perímetro del círculo. No requiere argumentos adicionales.
    public double CalcularPerimetro()
    {
        // Formula: Perímetro = 2 * PI * radio
        return 2 * Math.PI * radio;
    }
}

// Clase para representar un Rectángulo
public class Rectangulo
{
    // Campos privados para almacenar las dimensiones del rectángulo
    private double largo; // Longitud del rectángulo
    private double ancho; // Anchura del rectángulo

    // Constructor que inicializa los valores de largo y ancho
    public Rectangulo(double largo, double ancho)
    {
        this.largo = largo;
        this.ancho = ancho;
    }

    // CalcularArea es un método que devuelve un valor double.
    // Se utiliza para calcular el área del rectángulo. No requiere argumentos adicionales.
    public double CalcularArea()
    {
        // Formula: Area = largo * ancho
        return largo * ancho;
    }

    // CalcularPerimetro es un método que devuelve un valor double.
    // Se utiliza para calcular el perímetro del rectángulo. No requiere argumentos adicionales.
    public double CalcularPerimetro()
    {
        // Formula: Perímetro = 2 * (largo + ancho)
        return 2 * (largo + ancho);
    }
}
"""

# Imprimir el código en consola
print(codigo_csharp)
