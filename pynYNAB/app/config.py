import logging
import os

import configargparse
from appdirs import AppDirs

myAppdir = AppDirs('pynYNAB').user_config_dir
configfile = os.path.join(myAppdir, 'ynab.conf')

parser = configargparse.getArgumentParser('pynYNAB', default_config_files=[configfile], add_config_file_help=False)
group = parser.add_argument_group('command line or config file arguments')
group.add_argument('--email', metavar='Email', type=str, required=False,
                   help='The Email User ID for nYNAB')
group.add_argument('--password', metavar='Password', type=str, required=False,
                   help='The Password for nYNAB')
group.add_argument('--level', metavar='LoggingLevel', type=str.lower, required=False, default='error',
                   choices=['critical', 'error', 'warn', 'warning', 'info', 'debug'],
                   help='Logging Level')
group.add_argument('-echo', required=False, action='store_true',
                   help='echoes all tracking (warning, very verbose)')
group.add_argument('-echodb', required=False, action='store_true',
                   help='echoes all client db accesses (warning, very verbose)')

group.add_argument('--budgetname', metavar='BudgetName', type=str, required=False,
                   help='The nYNAB budget to use')

args = parser.parse_known_args()[0]
echo = args.echo if args else False
echodb = args.echodb if args else False

def get_logger(args=None):
    args = parser.parse_known_args()[0] if args is None else args
    logginglevel = args.level.upper()
    logger = logging.getLogger('pynYNAB')
    logging.basicConfig()
    logger.setLevel(logginglevel)
    return logger


def test_common_args(args):
    if args.email is None:
        get_logger().error('No email user ID provided, please specify it at the command line or in %s' % (configfile,))
        exit(-1)
    if args.password is None:
        get_logger().error('No password provided, please specify it at the command line or in %s' % (configfile,))
        exit(-1)
    if args.budgetname is None:
        get_logger().error('No budget name provided, please specify it at the command line or in %s' % (configfile,))
        exit(-1)


def alert_quit_badconfig():
    print('Please modify ynab.conf situated in %s' % myAppdir)
    import shutil

    shutil.copy('ynab.conf.format', os.path.join(myAppdir, 'ynab.conf'))
    exit(-1)