"""Base class for integration tests, based on ZopeTestCase and PloneTestCase.

Note that importing this module has various side-effects: it registers a set of
products with Zope, and it sets up a sandbox Plone site with the appropriate
products installed.
"""

from Testing import ZopeTestCase

# Import PloneTestCase - this registers more products with Zope as a side effect
from Products.PloneTestCase.PloneTestCase import PloneTestCase
from Products.PloneTestCase.PloneTestCase import FunctionalTestCase
from Products.PloneTestCase.PloneTestCase import setupPloneSite
from DateTime import DateTime

from Products.CMFPlacefulWorkflow.PlacefulWorkflowTool import WorkflowPolicyConfig_id

from Products.PloneTestCase import PloneTestCase as ptc

# Set up a Plone site - note that the portlets branch of CMFPlone applies
# a portlets profile.
setupPloneSite()

ptc.setupPloneSite(extension_profiles = ('Products.CMFPlacefulWorkflow:CMFPlacefulWorkflow',))

class WorkflowTestCase(PloneTestCase):
    """Base class for integration tests for plone.app.workflow. This may
    provide specific set-up and tear-down operations, or provide convenience
    methods.
    """
    
class WorkflowFunctionalTestCase(FunctionalTestCase):
    """Base class for functional integration tests for plone.app.workflow. 
    This may provide specific set-up and tear-down operations, or provide 
    convenience methods.
    """

    def afterSetUp(self):

        self.portal.acl_users._doAddUser('manager', 'secret', ['Manager',],[])
        self.portal.acl_users._doAddUser('member', 'secret', ['Member',],[])
        self.portal.acl_users._doAddUser('owner', 'secret', ['Owner',],[])
        self.portal.acl_users._doAddUser('reviewer', 'secret', ['Reviewer',],[])
        self.portal.acl_users._doAddUser('editor', 'secret', ['Editor',],[])
        self.portal.acl_users._doAddUser('reader', 'secret', ['Reader',],[])
        
        self.portal.acl_users._doAddUser('delegate_reader', 'secret', ['Member',],[]) 
        self.portal.acl_users._doAddUser('delegate_editor', 'secret', ['Member',],[])
        self.portal.acl_users._doAddUser('delegate_contributor', 'secret', ['Member',],[])
        self.portal.acl_users._doAddUser('delegate_reviewer', 'secret', ['Member',],[])
        #self.portal.acl_users._doAddUser('delegate_manager', 'secret', ['Member',],[])

        self.setRoles(('Manager',))
        self.folder.invokeFactory('News Item', 'newsitem1')
        self.newsitem = self.folder.newsitem1
        self.folder.invokeFactory('Event', 'event1')
        self.event = self.folder.event1
        self.folder.invokeFactory('Document', 'document1')
        self.document = self.folder.document1
        self.setRoles(('Member',))

        self.workflow = self.portal.portal_workflow 
        self.placeful_workflow = self.portal.portal_placeful_workflow

    def setUpDefaultWorkflowPolicy(self, defaultWorkflow=None):
        # Setup a default workflow policy
        if WorkflowPolicyConfig_id in self.folder.objectIds():
            # Remove any preexisting workflow policy
            self.folder.manage_delObjects(WorkflowPolicyConfig_id)
        self.placeful_workflow.manage_addWorkflowPolicy('default_placeful_workflow')
        policy = self.placeful_workflow.getWorkflowPolicyById('default_placeful_workflow')
        policy.setTitle('Default content workflows')
        policy.setDefaultChain((defaultWorkflow,))
        self.folder.manage_addProduct['CMFPlacefulWorkflow'].manage_addWorkflowPolicyConfig()
        config = getattr(self.folder.aq_explicit, WorkflowPolicyConfig_id)
        config.setPolicyBelow(policy='default_placeful_workflow')
        config.setPolicyIn(policy='default_placeful_workflow')
        self.document.reindexObjectSecurity()
        self.folder.reindexObjectSecurity()
        self.newsitem.reindexObjectSecurity()
        self.event.reindexObjectSecurity()
        
    def setUpGroupSpaceWorkflowPolicy(self, defaultWorkflow=None):
        # Setup a GroupSpace workflow policy
        if WorkflowPolicyConfig_id in self.folder.objectIds():
            # Remove any preexisting workflow policy
            self.folder.manage_delObjects(WorkflowPolicyConfig_id)
        self.placeful_workflow.manage_addWorkflowPolicy('groupspace_placeful_workflow', 
                                                   workflow_policy_type='groupspace_workflow_policy (GroupSpace Policy)',
                                                  )
        policy = self.placeful_workflow.getWorkflowPolicyById('groupspace_placeful_workflow')
        policy.setTitle('GroupSpace content workflows')
        policy.setDefaultChain((defaultWorkflow,))
        self.folder.manage_addProduct['CMFPlacefulWorkflow'].manage_addWorkflowPolicyConfig()
        config = getattr(self.folder.aq_explicit, WorkflowPolicyConfig_id)
        config.setPolicyBelow(policy='groupspace_placeful_workflow')
        config.setPolicyIn(policy='groupspace_placeful_workflow')
        self.document.reindexObjectSecurity()
        self.folder.reindexObjectSecurity()
        self.newsitem.reindexObjectSecurity()
        self.event.reindexObjectSecurity()
