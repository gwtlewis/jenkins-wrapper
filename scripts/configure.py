#!/usr/bin/env python

import os
import sys
import bootstrap


def kill_jenkins(jenkins_pid):
    os.kill(jenkins_pid, 9)


def disable_secure(vars):
    jenkins_config = "{0}/.jenkins/config.xml".format(vars['JENKINS']['HOME_DIR'])

    if os.path.exists(jenkins_config):
        os.system("python {0}/disable_secure.py {1}".format(vars['SCRIPTS']['DIR'], jenkins_config))
    else:
        print("Jenkins config file not found")
        sys.exit(1)


if __name__ == '__main__':

    jenkins_vars = bootstrap.read_jenkins_vars(sys.argv[1])

    kill_jenkins(int(sys.argv[2]))

    disable_secure(jenkins_vars)

