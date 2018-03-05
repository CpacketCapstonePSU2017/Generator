"""
    A slightly beautiful Click CLI
    Author: Josh Garrison
"""
import click
from datetime import datetime
from generator_framework.generator_config import GeneratorConfig
from generator_framework.generator import Generator
# TODO fix context to pull defaults from config
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def validate_date(ctx, param, value):
    try:
        date = datetime.strptime(value, "%Y-%m-%d")
        return date
    except ValueError:
        raise click.BadParameter('Date must be in YYYY-MM-DD')


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--function-type', '-f', prompt=True, type=click.Choice(['poisson', 'weibull']))
@click.option('--days', '-d', prompt=True, type=click.INT, help='Fill me in...')
@click.option('--high-max', '-hm', prompt=True, type=click.FLOAT)
@click.option('--high-min', default=0, type=click.INT)
@click.option('--low-max', '-lm', prompt=True, type=click.FLOAT)
@click.option('--low-min', default=0, type=click.INT)
@click.option('--business-hours', prompt=True, type=click.INT)
@click.option('--shape', '-sh', prompt=True, type=click.FLOAT)
@click.option('--work-hour', prompt=True, type=click.INT)
@click.option('--scale', prompt=True, type=click.INT)
@click.option('--start-date', '-sd', prompt=True, callback=validate_date)
def cli(function_type, days, high_max, high_min, low_max, low_min, business_hours, shape, work_hour, scale,
        start_date):
    """
    Fill this amazing DOC string in.
    """
    config = GeneratorConfig()
    config.set_config(days=days, high_max=high_max, high_min=high_min, low_max=low_max, low_min=low_min,
                      business_hours=business_hours, shape=shape, start_date=start_date, work_hour_start=work_hour,
                      scale=scale, func_type=function_type)
    # print(config.get_config())
    # TODO add threaded loading indicator.
    click.echo('Running Generator...')
    gen = Generator(config)
    if click.confirm('Write to csv?', default=True):
        gen.write_data_to_csv()
    if click.confirm('Write to DB?'):
        gen.write_data_to_database()


if __name__ == '__main__':
    # config = generator_config.GeneratorConfig()
    cli()
