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
        if type(obj) == type(''):
            portal_type = obj
        elif hasattr(aq_base(obj), '_getPortalTypeName'):
            portal_type = obj._getPortalTypeName()
        else:
            portal_type = None

        if portal_type is None:
            # Objects that don't have a portal type are not handled
            if managescreen:
                # In the ZMI management screen, a None value does not look good
                return ''
            else:
                return None
            
        # The defined chains for portal types are stored in the _chains_by_type
        # dictionary on the workflow policy definition
        cbt = self._chains_by_type
        chain = None
        if cbt is not None:
            # Get the chains for the content type, or mark the chain as not
            # existing in the cbt.
            chain = cbt.get(portal_type, _MARKER)

        # Backwards compatibility: before chain was a string, not a tuple
        if chain is not _MARKER and type(chain) == type(''):
            chain = tuple([x.strip() for x in chain.split(',')])

        if chain in (_MARKER, None, (DEFAULT_CHAIN,)):
            # The chain is either
            #
            # * Not defined in the cbt, and has been marked: _MARKER
            #
            # * Undefined, because there is no cbt: None
            #
            # * Defined as the default chain in the cbt: (DEFAULT_CHAIN,)
            #
            # In all these cases, use the default chain
            if managescreen:
                # In the ZMI management screen show "(Default)"
                chain = DEFAULT_CHAIN
            else:
                # Return the default chain tuple 
                chain = self.getDefaultChain(obj)            

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

