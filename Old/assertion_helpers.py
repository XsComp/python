
# ------------------------------------------------------------
# assertion_helpers.py
# Av: Andreas Andresen & C-mode
# Inneholder nyttige assert-funksjoner for type- og innholdssjekk
# ------------------------------------------------------------

def assert_is_str(value, var_name="Verdien"):
    assert type(value) is str, f"{var_name} må være en streng"

def assert_nonempty_str(value, var_name="Verdien"):
    assert_is_str(value, var_name)
    assert value.strip() != "", f"{var_name} må ikke være tom"

def assert_min_length(value, min_len, var_name="Verdien"):
    assert_is_str(value, var_name)
    actual_length = len(value.strip())
    assert actual_length >= min_len, (
        f"{var_name} må inneholde minst {min_len} tegn "
        f"(du skrev {actual_length})"
    )

def assert_positive_int(value, var_name="Verdien"):
    assert type(value) is int, f"{var_name} må være et heltall"
    assert value > 0, f"{var_name} må være større enn 0"

def assert_in_range(value, min_val, max_val, var_name="Verdien"):
    assert type(value) in (int, float), f"{var_name} må være et tall"
    assert min_val <= value <= max_val, (
        f"{var_name} må være mellom {min_val} og {max_val}"
    )

# Du kan legge til flere etter behov, f.eks. for e-post, tall, osv.
