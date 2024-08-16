#python create compiled version of module so that whenever we import module
#it import compile version for fast performance.
# By defining __init__.py in sub directory python treat is as package.

from sales import caltax, calshipping # import module
# importing package
import ecommerace.sales  
from ecommerace.sales import calshipping, caltax

calshipping()

# Calling with module
sales.calshipping()
sales.caltax()

#calling with package
ecommerace.sales.calshipping()
ecommerace.sales.caltax()