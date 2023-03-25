# Homework
1) @pytest.fixture:
The first and easiest way to instantiate some dataset is to use pytest fixtures.

pytest.fixture decorator makes it possible to inject the return value in the test functions whose have in their signature the decorated function name.
It’s really more hard to figure out than just seeing it in action:

def get_gender_heading(name):
    # super AI based algorithm (such 2018, much AI)
    # Return "Mr" or "Mrs" for a given name.
@pytest.fixture
def male_name():
    return 'Phil'
@pytest.fixture
def female_name():
    return 'Claire'
def test_male_prefix(male_name):
    assert 'Mr.' == get_gender_heading(male_name)
def test_female_prefix(female_name):
    assert 'Mrs.' == get_gender_heading(female_name)
*******************************************************    
2) @pytest.mark.parametrize : 
pytest.mark.parametrize to the rescue!
The above decorator is a very powerful functionality, it permits to call a test function multiple times, changing the parameters input at each iteration.
The first argument lists the decorated function’s arguments, with a comma separated string. The second argument is an iterable for call values.

Let’s see how it works.

@pytest.mark.parametrize('name', ['Claire', 'Gloria', 'Haley'])
def test_female_prefix_v2(name):
    assert 'Mrs.' == get_gender_heading(name)
******************************************************* 
3) @pytest.mark.skip :
The simplest way to skip a test function is to mark it with the skip decorator which may be passed an optional reason:
@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
******************************************************* 
4) @pytest.mark.dependency:
It is used to determine dependencies between tests.

@pytest.mark.dependency()
@pytest.mark.xfail(reason="deliberate fail")
def test_a():
    assert False
