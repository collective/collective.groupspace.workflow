from base import PloneTestCase
import unittest
from collective.groupspace.workflow.policy import GroupSpaceWorkflowPolicyDefinition

class TestGroupSpaceWorkflowPolicyDefinition(PloneTestCase):

    def setUp(self):
        PloneTestCase.setUp(self)

        class Dummy:
            pass
        self.obj = Dummy()

        self.policy = GroupSpaceWorkflowPolicyDefinition(self.obj)

        _chains_by_type = {'Document': ('(Default)',), 
                           'Image': ('(Default)',), 
                           'Topic': ('intranet_folder_workflow',), 
                           'Link': ('(Default)',), 
                           'File': ('(Default)',), 
                           'Large Plone Folder': ('intranet_folder_workflow',), 
                           'Folder': ('intranet_folder_workflow',), 
                           'News Item': ('(Default)',), 
                           'Event': ('(Default)',)}

        self.policy._chains_by_type = _chains_by_type                   
        self.policy._default_chain = ('groupspace_content_workflow',)

    def test_getChainFor(self):
        """
        When the object has no identifiable portal_type, the chain is None.
        """
        self.assertEqual(None, self.policy.getChainFor(self.obj))

    def test_getChainFor_1(self):
        """
        When there is a no portal_type, and the management screen is shown, 
        an empty string is returned.
        """
        self.assertEqual('', self.policy.getChainFor(self.obj, managescreen=True))

    def test_getChainFor_2(self):
        """
        As soon as there is a portal_type, the default chain is returned.
        """
        class Dummy:
            def _getPortalTypeName(self):
                return "GroupSpace"
        self.obj = Dummy()
        expected = ('groupspace_content_workflow',)
        self.assertEqual(expected, self.policy.getChainFor(self.obj))

    def test_getChainFor_3(self):
        """
        In the management screen, when the type is not in the _chains_by_type 
        dictionary, the default chain is returned.
        """
        class Dummy:
            def _getPortalTypeName(self):
                return "GroupSpace"
        self.obj = Dummy()
        expected = '(Default)'
        self.assertEqual(expected, self.policy.getChainFor(self.obj, managescreen=True))

    def test_getChainFor_4(self):
        """
        When there is a portal_type, and the chain by type is '(Default)', 
        the default chain is returned.
        """
        class Dummy:
            def _getPortalTypeName(self):
                return "Event"
        self.obj = Dummy()
        self.assertEqual(('groupspace_content_workflow',), self.policy.getChainFor(self.obj))

    def test_getChainFor_5(self):
        """
        In the managament screen when there is a portal_type, and the chain by 
        type is '(Default)', the default chain is returned.
        """
        class Dummy:
            def _getPortalTypeName(self):
                return "Event"
        self.obj = Dummy()
        self.assertEqual('(Default)', self.policy.getChainFor(self.obj, managescreen=True))

    def test_getChainFor_6(self):
        """
        Test backwards compatibility.
        In the managament screen when there is a portal_type, and the chain by 
        type is '(Default)', the default chain is returned.
        """
        self.policy._chains_by_type = {'Backwards': 'workflow1, workflow2'}
        class Dummy:
            def _getPortalTypeName(self):
                return "Backwards"
        self.obj = Dummy()
        self.assertEqual(('workflow1', 'workflow2'), self.policy.getChainFor(self.obj))

    def test_getDefaultChain(self):
        expected = ('groupspace_content_workflow',)
        self.assertEqual(expected, self.policy.getDefaultChain(self.obj))

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestGroupSpaceWorkflowPolicyDefinition))
    return suite
    
if __name__ == '__main__':
    unittest.main()
