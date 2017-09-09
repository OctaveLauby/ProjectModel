"""Utils to manage parameters and arguments"""


def read_params(params, dft_params):
    """Return parameters completed with default.

    Args:
        params      (dict): user parameters
        dft_params  (dict): dft parameters

    Returns:
        (dict): user parameters completed with defaults

    Raises:
        KeyError when user parameters are not all in dft parameters
    """
    res_params = dict(dft_params)

    unknown_keys = []
    for (key, value) in params.items():
        if key not in res_params:
            unknown_keys.append(key)
        elif value is not None:
            res_params[key] = value

    if unknown_keys:
        raise KeyError(
            "Unexpected keys in params: %s" % ", ".join(map(str, unknown_keys))
        )

    return res_params
