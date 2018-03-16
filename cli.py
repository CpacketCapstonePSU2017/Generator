"""
    This code is released under an MIT license
    A slightly beautiful Click CLI
    Author: Josh Garrison
"""
import click
from datetime import datetime
from generator_framework.generator_config import GeneratorConfig
from generator_framework.generator import Generator
config = GeneratorConfig()
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


# TODO fix this to be one function somehow.
def validate_date(ctx, param, value):
    try:
        date = datetime.strptime(value, "%Y-%m-%d")
        return date.date()
    except ValueError:
        raise click.BadParameter('Date must be in YYYY-MM-DD')


def parse_date(value):
    try:
        date = datetime.strptime(value, "%Y-%m-%d")
        return date.date()
    except ValueError:
        raise click.BadParameter('Date must be in YYYY-MM-DD')


# TODO Help prompts
@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--function-type', '-f', prompt=True, type=click.Choice(['poisson', 'weibull']),
              default=config.Func_Type.Name)
@click.option('--days', '-d', prompt=True, type=click.INT, default=config.Days, help='Fill me in...')
@click.option('--high-max', '-hm', prompt=True, default=config.High_Max, type=click.FLOAT)
@click.option('--high-min', default=config.High_Min, type=click.INT)
@click.option('--low-max', '-lm', prompt=True, default=config.Low_Max, type=click.FLOAT)
@click.option('--low-min', default=config.Low_Min, type=click.INT)
@click.option('--business-hours', prompt=True, default=config.Business_Hours, type=click.INT)
@click.option('--shape', '-sh', prompt=True, default=config.Shape, type=click.FLOAT)
@click.option('--work-hour', prompt=True, default=config.Work_Hour_Start, type=click.INT)
@click.option('--scale', prompt=True, default=config.Scale, type=click.INT)
@click.option('--start-date', '-sd', default=config.Start_Date.__str__(), callback=validate_date)
def cli(function_type, days, high_max, high_min, low_max, low_min, business_hours, shape, work_hour, scale, start_date):
    """
    Fill this amazing DOC string in.
    """
    config = GeneratorConfig()
    click.echo(datetime.today().date())
    if start_date == datetime.today().date():
        start_date = click.prompt('Enter a start date: ', value_proc=parse_date, default=datetime.today().date())
        click.echo(start_date)
    config.set_config(days=days, high_max=high_max, high_min=high_min, low_max=low_max, low_min=low_min,
                      business_hours=business_hours, shape=shape, start_date=start_date, work_hour_start=work_hour,
                      scale=scale, func_type=function_type)
    # print(config.get_config())
    # TODO add threaded loading indicator and a confirmation prompt here.
    click.echo('Running Generator...')
    gen = Generator(config)
    if click.confirm('Write to csv?', default=True):
        gen.write_data_to_csv()
    if click.confirm('Write to DB?'):
        gen.write_data_to_database()


if __name__ == '__main__':
    cli()
