#!/usr/bin/env python

import subprocess
import yaml
import sys
import os


def read_jenkins_vars(vars_path):
    with open(vars_path, 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            sys.exit(1)


def run_jenkins(vars):
    jenkins_home = vars['JENKINS']['HOME_DIR']
    jenkins_lib = vars['JENKINS']['LIB_DIR']
    jenkins_http_port = vars['JENKINS']['HTTP_PORT']
    jenkins_log_dir = vars['LOGS']['DIR']
    jenkins_log_name = vars['LOGS']['LOG_NAME']
    jenkins_pid_name = vars['LOGS']['PID']
    jenkins_log_file = '{0}/{1}'.format(jenkins_log_dir, jenkins_log_name)
    jenkins_pid_file = '{0}/{1}'.format(jenkins_log_dir, jenkins_pid_name)

    # set jenkins home dir
    os.environ['JENKINS_HOME'] = '{0}/.jenkins'.format(jenkins_home)

    cmd = ['{0}/bin/java'.format(os.environ['JAVA_HOME']),
           '-jar',
           jenkins_lib,
           '--httpPort={0}'.format(jenkins_http_port)]

    # run jenkins
    jenkins = subprocess.Popen(cmd, stdout=file(jenkins_log_file, 'ab'))
    # write pid file
    subprocess.call(['echo', jenkins.pid, ">", jenkins_pid_file])


if __name__ == '__main__':
    jenkins_vars = read_jenkins_vars(sys.argv[1])

    run_jenkins(jenkins_vars)
