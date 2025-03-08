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

# @strawberry.type
# class ClientData:
    


@strawberry.type
class Query:
    @strawberry.field
    def get_products(self) -> list[ProductData]:
        products = df.to_dict(orient="records")
        return [ProductData(**product) for product in products]
    
    @strawberry.field
    def get_product(self, id: int) -> ProductData:
        product = df[df["id_producto"] == id].iloc[0].to_dict()
        return ProductData(**product)
    
    @strawberry.field
    def get_product_by_name(self, name: str) -> ProductData:
        product = df[df["nombre_producto"] == name].iloc[0].to_dict()
        return ProductData(**product)
    
    @strawberry.field
    def get_product_by_sku(self, sku: str) -> ProductData:
        product = df[df["sku_producto"] == sku].iloc[0].to_dict()
        return ProductData(**product)
    
    @strawberry.field
    def get_products_by_client(self, id: int) -> list[ProductData]:
        products = df[df["id_cliente"] == id].to_dict(orient="records")
        return [ProductData(**product) for product in products]
    
    @strawberry.field
    def get_products_by_date(self, date: date) -> list[ProductData]:
        products = df[df["fecha"] == date].to_dict(orient="records")
        return [ProductData(**product) for product in products]
    
    @strawberry.field
    def get_products_from_date(self, start_date: date) -> list[ProductData]:
        products = df[df['fecha'] >= start_date].to_dict(orient="records")
        return [ProductData(**product) for product in products]
    

    
    

schema = strawberry.Schema(query=Query, scalar_overrides={int: BigInt})
