# Data to string formatter
def data_to_str(val, quotes=0):
    return 'null' if val is None else (
        str(val).lower() if isinstance(val, bool) else (
            f"'{str(val)}'" if quotes == 1 else str(val)))
