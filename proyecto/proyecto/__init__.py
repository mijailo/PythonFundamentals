__version__ = '0.1.0'

from proyecto.covid19.covid import Covid19

if __name__ == '__main__':
    cov = Covid19()
    print(cov.algo())