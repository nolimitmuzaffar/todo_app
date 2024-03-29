from app import app

def test1():
    """
    Function test1 tests that the flask app has a correct
    response code when the application goes live
    """
    response = app.test_client().get("/")
    assert response.status_code ==200
    
def test2():
    """  A dummy docstring """
    response = app.test_client().get("/edit")
    assert response.status_code ==200
    
    
    
    
    
def test3():
    """ A dummy docstring  """
    response = app.test_client().get("/edit")
    assert b"To Do App" in response.data 
    """ check if byte or "to do app" exists on the page edit """
    assert b"Todo Title" in response.data
    assert b"Add" in response.data
    