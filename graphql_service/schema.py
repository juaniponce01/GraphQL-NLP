import strawberry
from typing import Optional
from graphql_service.database import df
from datetime import date

# Esto es necesario ya que GraphQL no soporta enteros en 64-bits, por lo que se debe usar un BigInt
BigInt = strawberry.scalar(
    int,
    serialize=lambda v: str(v),
    parse_value=lambda v: int(v)
)

@strawberry.type
class ProductData:
    """
    Representa la información del producto en la base de datos.

    Atributos:
        fecha: La fecha en la que se registró el producto (formato datetime.date).
        id_cliente: El ID del cliente que compró el producto.
        id_vista: El ID de la vista asociada al producto.
        id_tipo_dispositivo: El tipo de dispositivo utilizado para la compra.
        id_fuente_medio: El ID de la fuente o medio de adquisición del producto.
        sku_producto: El SKU (Stock Keeping Unit) del producto.
        agregado_carrito_cant: Cantidad del producto agregado al carrito.
        ingreso_producto_monto: Monto total de ingreso generado por el producto.
        detalle_producto_cant: Cantidad de producto en el detalle de la compra.
        producto_cant: Cantidad de productos comprados.
        flag_pipol: Indicador de si el producto pertenece a una promoción especial (Pipol).
        id_producto: El ID del producto en el sistema.
        nombre_producto: Nombre del producto.
        marca_producto: Marca del producto (puede ser NULL).
        cod_producto: Código del producto (puede ser NULL).
        categoria_producto: Categoría del producto (puede ser NULL).
        categoria_prod_principal: Categoría principal del producto (puede ser NULL).
    """
    fecha: date
    id_cliente: int
    id_vista: int
    id_tipo_dispositivo: int
    id_fuente_medio: int
    sku_producto: str
    agregado_carrito_cant: int
    ingreso_producto_monto: float
    detalle_producto_cant: int
    producto_cant: int
    flag_pipol: int
    id_producto: int
    nombre_producto: str
    marca_producto: Optional[str]
    cod_producto: Optional[float]
    categoria_producto: Optional[str]
    categoria_prod_principal: Optional[str]

@strawberry.type
class Query:
    """
    Define los resolutores para las consultas GraphQL relacionadas con productos.
    """

    @strawberry.field(description="Obtiene todos los productos en la base de datos.")
    def get_products(self) -> list[ProductData]:
        """
        Resuelve todos los productos registrados en la base de datos.
        """
        products = df.to_dict(orient="records")
        return [ProductData(**product) for product in products]

    @strawberry.field(description="Obtiene un producto por su ID.")
    def get_product(self, id: int) -> ProductData:
        """
        Resuelve un único producto a partir de su ID.
        """
        product = df[df["id_producto"] == id].iloc[0].to_dict()
        return ProductData(**product)

    @strawberry.field(description="Obtiene un producto por su nombre.")
    def get_product_by_name(self, name: str) -> ProductData:
        """
        Resuelve un único producto a partir de su nombre.
        """
        product = df[df["nombre_producto"] == name].iloc[0].to_dict()
        return ProductData(**product)

    @strawberry.field(description="Obtiene un producto por su SKU.")
    def get_product_by_sku(self, sku: str) -> ProductData:
        """
        Resuelve un único producto a partir de su SKU.
        """
        product = df[df["sku_producto"] == sku].iloc[0].to_dict()
        return ProductData(**product)

    @strawberry.field(description="Obtiene todos los productos comprados por un cliente a partir de su ID.")
    def get_products_by_client(self, id: int) -> list[ProductData]:
        """
        Resuelve todos los productos comprados por un cliente en base a su ID.
        """
        products = df[df["id_cliente"] == id].to_dict(orient="records")
        return [ProductData(**product) for product in products]

    @strawberry.field(description="Obtiene los productos que coinciden con una fecha específica.")
    def get_products_by_date(self, date: date) -> list[ProductData]:
        """
        Resuelve los productos comprados en una fecha específica.
        """
        products = df[df["fecha"] == date].to_dict(orient="records")
        return [ProductData(**product) for product in products]

    @strawberry.field(description="Obtiene todos los productos comprados a partir de una fecha.")
    def get_products_from_date(self, start_date: date) -> list[ProductData]:
        """
        Resuelve los productos comprados desde una fecha específica.
        """
        products = df[df['fecha'] >= start_date].to_dict(orient="records")
        return [ProductData(**product) for product in products]

# Crear el esquema de GraphQL
schema = strawberry.Schema(query=Query, scalar_overrides={int: BigInt})
