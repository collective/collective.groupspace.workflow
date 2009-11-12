import unittest
from base import PloneTestCase
from collective.groupspace.workflow.handlers import add_local_groupspace_workflow
from Products.CMFPlacefulWorkflow.PlacefulWorkflowTool import WorkflowPolicyConfig_id
from collective.groupspace.workflow.config import CONTENT_POLICY
from collective.groupspace.workflow.config import GROUPSPACE_POLICY
from collective.groupspace.workflow.setuphandlers import add_content_policy
from collective.groupspace.workflow.setuphandlers import add_groupspace_policy

class TestAddLocalGroupspaceWorkflow(PloneTestCase):

    def afterSetUp(self):
        add_content_policy(self.portal)
        add_groupspace_policy(self.portal)
      
    def test_add_local_groupspace_workflow(self):
        obj = self.folder.aq_explicit
        event = None
        add_local_groupspace_workflow(obj, event)
        policy = getattr(self.folder.aq_explicit, WorkflowPolicyConfig_id)
        self.failUnless(policy.getPolicyInId() == GROUPSPACE_POLICY)
        self.failUnless(policy.getPolicyBelowId() == CONTENT_POLICY)

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestAddLocalGroupspaceWorkflow))
    return suite

if __name__ == '__main__':
    unittest.main()
