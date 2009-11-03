"""
Defining a local groupspace workflow interface
"""

from zope.interface import Interface

class ILocalGroupSpaceWorkflow(Interface):
    """
    ILocalGroupSpaceWorkflow interface

    When this interface is implemented on a GroupSpace, a local workflow policy
    is added when the object is created. This is a special workflow policy
    that makes sure the default workflow is really chosen, and differs from
    the default workflow policy in CMFPlacefulWorkflow in this respect. 
    """                                                  
