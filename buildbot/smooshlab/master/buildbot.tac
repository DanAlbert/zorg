# -*- Python -*-

from twisted.application import service
from buildbot.master import BuildMaster
import os

basedir = os.path.dirname(os.path.abspath(__file__))
configfile = r'master.cfg'

application = service.Application('buildmaster')
BuildMaster(basedir, configfile).setServiceParent(application)

