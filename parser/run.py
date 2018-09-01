from config.options import Options
from lehigh.crime_log import CrimeLog

options: Options = Options.from_cli()
print(f'Options:\n{str(options)}')

crime_log: CrimeLog = CrimeLog(options)

print(f'Processing crime log...')
crime_log.process()

print(f'Writing crime log...')
crime_log.write()
