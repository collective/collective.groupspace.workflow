import unittest
from base import PloneTestCase
from collective.groupspace.workflow.setuphandlers import setup_various
from collective.groupspace.workflow.setuphandlers import require_placeful_workflow
from collective.groupspace.workflow.setuphandlers import add_content_policy
from collective.groupspace.workflow.setuphandlers import add_groupspace_policy
from collective.groupspace.workflow.setuphandlers import augment_permissions

class TestSetupVarious(PloneTestCase):
    def test_setup_various(self):
        class DummyLogger:
            def info(self, msg):
                pass
        class Dummy:
            def getSite(self):
                return self._portal
            def getLogger(self, name):
                return DummyLogger()
        obj = Dummy()
        obj._portal = self.portal
        expected = None
        self.assertEqual(expected, setup_various(obj))

class TestRequirePlacefulworkflow(PloneTestCase):
    def test_require_place_fulworkflow(self):
        self.failUnlessRaises(AttributeError, require_placeful_workflow, self.portal, None)
        
class TestAddContentPolicy(PloneTestCase):
    def test_add_content_policy(self):
        expected = 'Workflow policy groupspace_content_placeful_workflow already installed\n'
        self.assertEqual(expected, add_content_policy(self.portal))
        
class TestAddGroupspacePolicy(PloneTestCase):
    def test_add_groupspace_policy(self):
        expected = 'Workflow policy groupspace_placeful_workflow already installed\n'
        self.assertEqual(expected, add_groupspace_policy(self.portal))
        
class TestAugmentPermissions(PloneTestCase):
    def test_augment_permissions(self):
        expected = ''
        self.assertEqual(expected, augment_permissions(self.portal))
        
def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestSetupVarious))
    suite.addTest(makeSuite(TestRequirePlacefulworkflow))
    suite.addTest(makeSuite(TestAddContentPolicy))
    suite.addTest(makeSuite(TestAddGroupspacePolicy))
    suite.addTest(makeSuite(TestAugmentPermissions))
    return suite

if __name__ == '__main__':
    unittest.main()
