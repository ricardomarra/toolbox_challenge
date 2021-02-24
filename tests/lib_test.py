from toolbox_challenge.lib import haversine

def test_type_haversine():
    assert type(haversine(2, 4, 2, 4)) == float
