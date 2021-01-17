
import uuid
def get_products():
    fake_response = [{
            "sku": uuid.uuid4(),
            "title":"Vanilla ice cream",
            "long_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam nec tellus in ante ornare luctus vitae a turpis. Duis pellentesque lacus ac est malesuada dapibus. Donec interdum efficitur lectus. Curabitur tristique lobortis iaculis. Morbi condimentum leo ullamcorper mi blandit fringilla. Donec aliquam ipsum nibh, tempor rutrum dui eleifend eu. Suspendisse velit metus, congue at nibh sed, interdum euismod dui. Aliquam id nisl non enim commodo dapibus. Mauris eget suscipit lorem. Donec egestas pharetra mauris. Aliquam erat volutpat. Quisque id nulla at neque hendrerit aliquet quis at felis. Mauris nisi nisl, maximus et tristique eu, accumsan eget massa. Aenean congue volutpat dapibus. Maecenas cursus, urna nec vehicula interdum, ex eros sollicitudin quam, a malesuada lorem ante et diam. Aenean tincidunt arcu orci, eu blandit tortor tempus et.",
            "price_euro": 1.5
            },{
            "sku": uuid.uuid4(),
            "title":"Lemon ice cream",
            "long_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam nec tellus in ante ornare luctus vitae a turpis. Duis pellentesque lacus ac est malesuada dapibus. Donec interdum efficitur lectus. Curabitur tristique lobortis iaculis. Morbi condimentum leo ullamcorper mi blandit fringilla. Donec aliquam ipsum nibh, tempor rutrum dui eleifend eu. Suspendisse velit metus, congue at nibh sed, interdum euismod dui. Aliquam id nisl non enim commodo dapibus. Mauris eget suscipit lorem. Donec egestas pharetra mauris. Aliquam erat volutpat. Quisque id nulla at neque hendrerit aliquet quis at felis. Mauris nisi nisl, maximus et tristique eu, accumsan eget massa. Aenean congue volutpat dapibus. Maecenas cursus, urna nec vehicula interdum, ex eros sollicitudin quam, a malesuada lorem ante et diam. Aenean tincidunt arcu orci, eu blandit tortor tempus et.",
            "price_euro": 0.5
            }]
    return fake_response

def create_product(sku, title, long_description, price_euro):
    '''Insertar todo esto en una bbdd '''
    print(f"Crear sku={sku} y title={title}")
