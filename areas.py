from getgauge.python import step, before_scenario, Messages
class area:
    def area_of_triangle(self,a,b,c):
        a = int(a)
        b = int(b)
        c = int(c)
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        return round(area)

    def area_of_rectangle(self,a,b):
        a = int(a)
        b = int(b)
    
        return a * b
    
    def area_of_trapezoid(self, a,b,h):
        a = int(a)
        b = int(b)
        h = int(h)
        
        area = ((a+b)/2)*h
        
        return  round(area)
    
    def area_of_hexagon(self, a):
        a = int(a)
        area = ((3 * (3)**0.5)* (a * a))/2
        return round(area)

    
# --------------------------
# Gauge step implementations
# --------------------------
    
@step("The area of a triangle with sides <a>, <b>, <c> is <expected_area> after rounding off")
def assert_area_of_triangle(a,b,c,expected_area):
    t = area()
    actual_area = t.area_of_triangle(a,b,c)
    assert str(expected_area) == str(actual_area)
    
    
@step("The area of a rectangle with length <l> and breadth <b> is <expected_area> after rounding off.")
def assert_area_of_rectangle(l,b,expected_area):
    r = area()
    actual_area = r.area_of_rectangle(l,b)
    assert str(expected_area) == str(actual_area)
    
    
@step("Below is the table with the values of length and breadth <table>")
def assert_area_of_rect(table):
    r = area()
    a = table.get_column_values_with_name("length")
    b = table.get_column_values_with_name("breadth")
    actual = []
    for a1,b1 in zip(a,b):
        actual.append(str(r.area_of_rectangle(a1,b1)))
    #print(actual)
    expected = table.get_column_values_with_name("Area")
    #print(expected)
    assert expected == actual
    
@step("The area of a trapezoid with sides a = <a>, b = <b> and h = <h> after rounding off is <expected_area>")
def assert_area_of_trapezoid(a,b,h,expected_area):
    t = area()
    actual_area = t.area_of_trapezoid(a,b,h)
    assert str(expected_area) == str(actual_area)
    
@step("The area of a hexagon with side a = <a> is <expected_area>")
def assert_area_of_hexagon(a,expected_area):
    h = area()
    actual_area = h.area_of_hexagon(a)
    assert str(expected_area) == str(actual_area)