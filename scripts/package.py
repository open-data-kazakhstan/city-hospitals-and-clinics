from datapackage import Package

# Creating a new package
package = Package(base_path='C:/Users/polat/Desktop/city-hospitals-and-clinics/data')
package.infer('med_institutions.csv')

# Saving the package to 'datapackage.json'
package.save('../datapackage.json')
