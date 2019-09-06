'''Deployment configuration

Author: Ukor, Jidechi
Orgainzation: Tedx Ebonyi State
Maintainers: []
'''
import multiprocessing

bind = 'localhost:51750'
workers = multiprocessing.cpu_count() * 2 + 1
