#!/usr/bin/env python

import subprocess
import errno
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


def make_sure_path_exists(path, mode):
    try:
        os.makedirs(path, mode=mode)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def run_jenkins(vars):
    jenkins_home = vars['JENKINS']['HOME_DIR']
    jenkins_lib = vars['JENKINS']['LIB_DIR']
    jenkins_http_port = vars['JENKINS']['HTTP_PORT']
    jenkins_log_dir = vars['LOGS']['DIR']
    jenkins_pid_name = vars['LOGS']['PID']
    jenkins_pid_file = '{0}/{1}'.format(jenkins_log_dir, jenkins_pid_name)

    make_sure_path_exists(jenkins_log_dir, 0755)

    # set jenkins home dir
    os.environ['JENKINS_HOME'] = '{0}/.jenkins'.format(jenkins_home)

    cmd = ['{0}/bin/java'.format(os.environ['JAVA_HOME']),
           '-Djava.awt.headless=true',
           '-Dhudson.model.DownloadService.noSignatureCheck=true',
           '-Djenkins.install.runSetupWizard=false',
           '-jar',
           jenkins_lib,
           '--httpPort={0}'.format(jenkins_http_port)]

    # run jenkins
    jenkins = subprocess.Popen(cmd)

    # write pid
    jenkins_pid = open(jenkins_pid_file, "w")
    jenkins_pid.write(str(jenkins.pid))
    jenkins_pid.close()

    return jenkins.pid


if __name__ == '__main__':
    # read global variables
    jenkins_vars = read_jenkins_vars(sys.argv[1])
    # first start jenkins
    pid = run_jenkins(jenkins_vars)
