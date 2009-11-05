"""
Setup handlers for collective.groupspace.workflow
"""
from StringIO import StringIO
from Products.CMFCore.utils import getToolByName
from collective.groupspace.workflow.config import CONTENT_POLICY
from collective.groupspace.workflow.config import GROUPSPACE_POLICY

def setup_various(context):
    """Import steps that are not handled by GS import/export handlers
    """
    out = StringIO()
    portal = context.getSite()
    
    print >> out, add_content_policy(portal)
    print >> out, add_groupspace_policy(portal)
    print >> out, augment_permissions(portal)
    
    logger = context.getLogger("Plone")
    logger.info(out.getvalue())

def add_content_policy(portal):
    """Add the placeful workflow policy for content of GroupSpaces.
    """
    out = StringIO()
    
    placeful_workflow = getToolByName(portal, 'portal_placeful_workflow', None)
    
    if placeful_workflow is None:
        print >> out, "Error: CMFPlacefulWorkflow is not installed"
    elif CONTENT_POLICY not in placeful_workflow.objectIds():
        wpt = 'groupspace_workflow_policy (GroupSpace Policy)'
        placeful_workflow.manage_addWorkflowPolicy(CONTENT_POLICY,
                                                   workflow_policy_type=wpt)
        policy = placeful_workflow.getWorkflowPolicyById(CONTENT_POLICY)
        policy.setTitle('GroupSpace content workflows')
        policy.setDefaultChain(('groupspace_content_workflow',))
        print >> out, "Installed workflow policy %s" % CONTENT_POLICY
    else:
        print >> out, "Workflow policy %s already installed" % CONTENT_POLICY
        
    return out.getvalue()
    
def add_groupspace_policy(portal):
    """Add the placeful workflow policy for the GroupSpaces.
    """
    out = StringIO()
    
    placeful_workflow = getToolByName(portal, 'portal_placeful_workflow', None)
    
    if placeful_workflow is None:
        print >> out, "Error: CMFPlacefulWorkflow is not installed"
    elif GROUPSPACE_POLICY not in placeful_workflow.objectIds():
        wpt = 'groupspace_workflow_policy (GroupSpace Policy)'
        placeful_workflow.manage_addWorkflowPolicy(GROUPSPACE_POLICY, 
                                                   workflow_policy_type=wpt)
        policy = placeful_workflow.getWorkflowPolicyById(GROUPSPACE_POLICY)
        policy.setTitle('GroupSpace workflows')
        policy.setDefaultChain(('groupspace_workflow',))
        print >> out, "Installed workflow policy %s" % GROUPSPACE_POLICY
    else:
        print >> out, "Workflow policy %s already installed" % GROUPSPACE_POLICY
        
    return out.getvalue()
        
        
def augment_permissions(portal):
    """
    Augment the permissions for the group roles so these are available
    on the Plone site and don't have to be redundantly defined on the local
    workflows.
    """
    out = StringIO()

    r2p = {"GroupAdmin": ["ATContentTypes: Add Document",
                          "ATContentTypes: Add Event",
                          "ATContentTypes: Add Favorite",
                          "ATContentTypes: Add File",
                          "ATContentTypes: Add Folder",
                          "ATContentTypes: Add Image",
                          "ATContentTypes: Add Large Plone Folder",
                          "ATContentTypes: Add Link",
                          "ATContentTypes: Add News Item",
                          "Access contents information",
                          "Add portal content",
                          "Add portal folders",
                          "CMFEditions: Access previous versions",
                          "CMFEditions: Apply version control",
                          "CMFEditions: Checkout to location",
                          "CMFEditions: Revert to previous versions",
                          "CMFEditions: Save new version",
                          "Delete objects",
                          "List folder contents",
                          "Manage properties",
                          "Modify portal content",
                          "Modify view template",
                          "Request review",
                          "View",
                          "iterate : Check in content",
                          "iterate : Check out content",
                         ],
           "GroupEditor":["Access contents information",
                          "CMFEditions: Access previous versions",
                          "CMFEditions: Apply version control",
                          "CMFEditions: Checkout to location",
                          "CMFEditions: Revert to previous versions",
                          "CMFEditions: Save new version",
                          "Delete objects",
                          "List folder contents",
                          "Manage properties",
                          "Modify portal content",
                          "Modify view template",
                          "Request review",
                          "View",
                          "iterate : Check in content",
                          "iterate : Check out content",
                          ],                      
           "GroupContributor":["ATContentTypes: Add Document",
                               "ATContentTypes: Add Event",
                               "ATContentTypes: Add Favorite",
                               "ATContentTypes: Add File",
                               "ATContentTypes: Add Folder",
                               "ATContentTypes: Add Image",
                               "ATContentTypes: Add Large Plone Folder",
                               "ATContentTypes: Add Link",
                               "ATContentTypes: Add News Item",
                               "Access contents information",
                               "Add portal content",
                               "Add portal folders",
                               "CMFEditions: Access previous versions",
                               "CMFEditions: Apply version control",
                               "CMFEditions: Save new version",
                               "List folder contents",
                               "View",
                            ],
           "GroupReader":["Access contents information",
                          "List folder contents",
                          "View",
                         ],
      }

    for role_to_manage in r2p.keys():
        permissions = r2p[role_to_manage]
        portal.manage_role(role_to_manage, permissions)
        
    return out.getvalue()
