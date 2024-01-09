import io

import pandas as pd


def custom_parser(x):
    parts = x.split("/")
    if len(parts) == 1:
        return pd.Series({"ip": parts[0], "ip_range": None})
    else:
        return pd.Series({"ip": parts[0], "ip_range": parts[1]})


def split_dest_port(x):
    parts = x.split("/")
    if len(parts) == 1:
        return pd.Series({"dest_port": parts[0], "protocol": None})
    else:
        return pd.Series({"dest_port": parts[0], "protocol": parts[1].upper()})


def parse_to_df(data):
    df = pd.read_csv(
        io.StringIO(data),
        delim_whitespace=True,
        converters={
            # "source_ip": custom_parser,
            # "dest_ip": custom_parser,
            "dest_port": split_dest_port,
        },
    )

    # Split 'source_ip' and 'dest_ip' into two separate columns
    # df[["source_ip", "source_ip_range"]] = df["source_ip"].apply(pd.Series)
    # df[["dest_ip", "dest_ip_range"]] = df["dest_ip"].apply(pd.Series)
    df[["dest_port", "dest_port_type"]] = df["dest_port"].apply(pd.Series)
    df = df.loc[df["dest_port"] != "ALL"]

    return df


def list_to_string(lst):
    return "[" + ", ".join(map(str, lst)) + "]"


def parse_group_input(df):
    a = (
        df.groupby(["source_ip", "dest_ip", "dest_port_type"])[["dest_port"]]
        .agg(list)
        .reset_index()
    )
    b = a.map(lambda x: list_to_string(x) if isinstance(x, list) else x)
    c = b.groupby(["dest_port", "dest_ip", "dest_port_type"]).agg(list).reset_index()
    return c


def parse_file(data):
    df = parse_to_df(data)
    df = parse_group_input(df)
    import ast

    df["dest_port"] = (
        df["dest_port"]
        .apply(lambda x: ast.literal_eval(x))
        .apply(lambda x: list(map(lambda y: str(y), x)))
    )

    df.to_json("df.json", orient="records")

    return "ok"


if __name__ == "__main__":
    with open("config.txt") as config:
        data = config.read()
        parse_file(data)
