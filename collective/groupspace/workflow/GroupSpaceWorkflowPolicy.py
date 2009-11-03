"""
A workflow policy definition respecting the default workflow
"""

from Acquisition import aq_base
from App.class_init import InitializeClass
from zope.interface import implements
from AccessControl import ClassSecurityInfo
from Products.CMFCore.permissions import ManagePortal
from Products.CMFPlacefulWorkflow.DefaultWorkflowPolicy import DefaultWorkflowPolicyDefinition
from Products.CMFPlacefulWorkflow.PlacefulWorkflowTool import addWorkflowPolicyFactory
from Products.CMFPlacefulWorkflow.interfaces.portal_placeful_workflow import IWorkflowPolicyDefinition

DEFAULT_CHAIN = '(Default)'
_MARKER = '_MARKER'

class GroupSpaceWorkflowPolicyDefinition(DefaultWorkflowPolicyDefinition):
    """
    A workflow policy that respects the default workflow
    """
    implements(IWorkflowPolicyDefinition)

    meta_type = 'GroupSpaceWorkflowPolicy'
    id = 'groupspace_workflow_policy'

    security = ClassSecurityInfo()
    
    security.declareProtected( ManagePortal, 'getChainFor')
    def getChainFor(self, obj, managescreen=False):
        """Returns the chain that applies to the object.

        If chain doesn't exist we return None to get a fallback from
        portal_workflow.

        @parm managescreen: If True return the special tuple
                            ('default') instead of the actual default
                            chain (hack).
        """
        cbt = self._chains_by_type
        if type(obj) == type(''):
            portal_type = obj
        elif hasattr(aq_base(obj), '_getPortalTypeName'):
            portal_type = obj._getPortalTypeName()
        else:
            portal_type = None

        if portal_type is None:
            return None

        chain = None
        if cbt is not None:
            chain = cbt.get(portal_type, _MARKER)

        # Backwards compatibility: before chain was a string, not a list
        if chain is not _MARKER and type(chain) == type(''):
            chain = [x.strip() for x in chain.split(',')]

        if chain is _MARKER or chain is None:
            # Enforcing a default chain in absence of a definition
            if managescreen:
                chain = DEFAULT_CHAIN
            else:
                chain = self.getDefaultChain(obj)            
        elif len(chain) == 1 and chain[0] == DEFAULT_CHAIN:
            chain = self.getDefaultChain(obj)
            if chain and managescreen:
                chain = DEFAULT_CHAIN
            else:
                chain = None

        return chain

    security.declareProtected( ManagePortal, 'getDefaultChain')
    def getDefaultChain(self, obj):
        """ Returns the default chain."""
        # A default chain must be available, otherwise we can't control 
        # access to GroupSpace content.
        assert(not self._default_chain is None)        
        return self._default_chain

InitializeClass(GroupSpaceWorkflowPolicyDefinition)

addWorkflowPolicyFactory(GroupSpaceWorkflowPolicyDefinition, 
                         title='GroupSpace Policy')

