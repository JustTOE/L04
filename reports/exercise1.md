# Bug reports for exercise1.py

Line: 3  
Problem: The function `is_even(n)` returns `True` when `n % 2 == 1`, which is incorrect because `n % 2 == 1` means the number is odd, not even.  
Example: is_even(4) returns False, but it should return True since 4 is even.  
Fix: Change `n % 2 == 1` to `n % 2 == 0`

Line: 8  
Problem: The function `rectangle_area(width, height)` returns the sum of width and height, not the product, which is the correct formula for area.  
Example: rectangle_area(5, 3) returns 8, but the correct area should be 15.  
Fix: Change `return width + height` to `return width * height`

Line: 12  
Problem: The function `double(n)` adds 2 to `n`, but the docstring says "twice the number n", which means it should return `n * 2`.  
Example: double(5) returns 7, but it should return 10.  
Fix: Change `return n + 2` to `return n * 2`
