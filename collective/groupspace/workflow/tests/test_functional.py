from zope.testing import doctest
from unittest import TestSuite
from utils import optionflags
from Testing.ZopeTestCase import FunctionalDocFileSuite
from base import FunctionalTestCase

def test_suite():
    tests = ['placefulworkflowpolicy.txt',]
    suite = TestSuite()
    for test in tests:
        suite.addTest(FunctionalDocFileSuite(test,
            optionflags=optionflags,
            package="collective.groupspace.workflow.tests",
            test_class=FunctionalTestCase))
    return suite
