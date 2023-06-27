import click
import configobj
from configobj import ConfigObj


def read_config():
    return configobj.ConfigObj('config.ini', create_empty=True)


def config_value(key: str):
    cfg = read_config()
    current = cfg.get(key, "")

    if not current:
        command, configuration = key.split('.')
        click.echo(f"{key} not configured. Run `oncall-analysis {command} configure` to configure")

    return current


def configure_key(key: str, hide: bool = False):
    cfg = read_config()
    current = cfg.get(key, "")

    if current:
        hidden = "****" + current[-2:] if hide else current
        result = click.prompt(f"Enter {key} (current: {hidden})", hide_input=hide, default="")
    else:
        result = click.prompt(f"Enter {key}", hide_input=hide, default="")

    if result:
        cfg[key] = result
        cfg.write()

    return result or current
