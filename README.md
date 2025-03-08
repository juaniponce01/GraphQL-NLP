# API GraphQL para Consultar Productos y Clientes

Esta es una API GraphQL que permite consultar información sobre productos y clientes, incluyendo compras, detalles del producto y estadísticas relacionadas.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/juaniponce01/GraphQL-NLP.git
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd repo
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

Para iniciar la API, ejecuta el siguiente comando:

```bash
uvicorn main:app --reload
```

La API estará disponible en `http://127.0.0.1:8000/docs`.

## Consultas GraphQL

Puedes acceder a la interfaz interactiva de GraphQL en `http://127.0.0.1:8000/graphql`.

A continuación, se describen las consultas disponibles:

### Consultas

#### `get_products`
Obtiene todos los productos registrados.

**Ejemplo de consulta:**
```graphql
query {
  getProducts {
    fecha
    id_cliente
    sku_producto
    nombre_producto
  }
}
```

#### `get_product(id: Int)`
Obtiene un producto específico por su `id_producto`.

**Ejemplo de consulta:**
```graphql
query {
  getProduct(id: 1) {
    fecha
    id_cliente
    sku_producto
    nombre_producto
  }
}
```

#### `get_product_by_name(name: String)`
Obtiene un producto por su nombre.

**Ejemplo de consulta:**
```graphql
query {
  getProductByName(name: "Producto 1") {
    fecha
    id_cliente
    sku_producto
    nombre_producto
  }
}
```

#### `get_product_by_sku(sku: String)`
Obtiene un producto por su SKU.

**Ejemplo de consulta:**
```graphql
query {
  getProductBySku(sku: "SKU123") {
    fecha
    id_cliente
    sku_producto
    nombre_producto
  }
}
```

#### `get_products_by_client(id: Int)`
Obtiene todos los productos comprados por un cliente, basado en su `id_cliente`.

**Ejemplo de consulta:**
```graphql
query {
  getProductsByClient(id: 1) {
    fecha
    id_cliente
    sku_producto
    nombre_producto
  }
}
```

#### `get_products_by_date(date: Date)`
Obtiene todos los productos comprados en una fecha específica.

**Ejemplo de consulta:**
```graphql
query {
  getProductsByDate(date: "2024-02-01") {
    fecha
    id_cliente
    sku_producto
    nombre_producto
  }
}
```

#### `get_products_from_date(start_date: Date)`
Obtiene todos los productos comprados a partir de una fecha específica.

**Ejemplo de consulta:**
```graphql
query {
  getProductsFromDate(startDate: "2024-01-01") {
    fecha
    id_cliente
    sku_producto
    nombre_producto
  }
}
```

## Estructura de Datos

### `ProductData`

Los productos se representan en el siguiente formato:

- `fecha`: La fecha de la compra (formato `YYYY-MM-DD`).
- `id_cliente`: ID único del cliente.
- `sku_producto`: SKU del producto.
- `nombre_producto`: Nombre del producto.
- Otros atributos opcionales como la marca, código, categoría, etc.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.


