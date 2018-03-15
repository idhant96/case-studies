from recipies.loaders import Loader

data, shape = Loader.load_csv('data/diabetes.csv')
print(shape)