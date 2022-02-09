from app import create_app


app = create_app()
print(dir(app))
print(app.__dict__)

