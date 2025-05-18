# Quản lý danh sách sản phẩm:
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from typing import Optional 

app=FastAPI()

class Product(BaseModel):
    id: Optional [int] = None
    name: str
    price: float
    description: Optional[str]= None

products =[]
current_id= 1

@app.get("/product", response_model= List[Product])
async def get_products():
    return products

@app.post("/products", response_model= Product)
async def create_product(product: Product): 
    global current_id   
    product.id = current_id  # Gán ID tự động cho sản phẩm vừa nhận
    current_id +=1
    products.append(product)
    return product

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Biến toàn cục: Khai báo bên ngoài tất cả các hàm → dùng được ở mọi nơi.
# dùng global khi: Bạn muốn thay đổi giá trị của một biến khai báo bên ngoài hàm.
# Biến toàn cục current_id được dùng để tự động tăng ID cho sản phẩm;
# Cần khai báo global để cập nhật biến bên ngoài hàm.
# Từ khóa global trong Python được dùng khi bạn muốn thay đổi giá trị của 
# một biến toàn cục (global variable) từ bên trong một hàm.
