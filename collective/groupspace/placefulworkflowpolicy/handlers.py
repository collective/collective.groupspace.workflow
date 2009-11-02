"""
Handle the setting of policies when a groupspace is added
"""

from collective.groupspace.workflow.config import CONTENT_POLICY
from collective.groupspace.workflow.config import GROUPSPACE_POLICY
from Products.CMFPlacefulWorkflow.PlacefulWorkflowTool import WorkflowPolicyConfig_id

def add_local_groupspace_workflow(obj, event):
    """Apply the local workflow when a groupspace is added.
    """
    product = 'CMFPlacefulWorkflow'
    obj.manage_addProduct[product].manage_addWorkflowPolicyConfig()
    #
    # Calling getWorkflowPolicyConfig directly is not possible because of an 
    # explicit check in CMFPlacefulWorkflow for the permission "Manage portal",
    # which Contributors don't have. This would only make it possible for 
    # managers to add GroupSpaces, which doesn't make sense.
    #
    # config = placeful_workflow.getWorkflowPolicyConfig(groupspace)
    #
    # Instead need to do what the getWorkflowPolicyConfig method does after
    # the permission check:
    #
    config = getattr(obj.aq_explicit, WorkflowPolicyConfig_id)
    config.setPolicyIn(policy=GROUPSPACE_POLICY)
    config.setPolicyBelow(policy=CONTENT_POLICY)       
