Introduction
============

Implements a placeful workflow policy needed for the GroupSpace content type that makes sure that, unless otherwise defined, all content types use the default workflow as defined by the placeful workflow policy.

groupspace.placefulworkflowpolicy Installation
----------------------------------------------

To install groupspace.placefulworkflowpolicy into the global Python environment (or a workingenv),
using a traditional Zope 2 instance, you can do this:

* When you're reading this you have probably already run 
  ``easy_install groupspace.placefulworkflowpolicy``. Find out how to install setuptools
  (and EasyInstall) here:
  http://peak.telecommunity.com/DevCenter/EasyInstall

* Create a file called ``groupspace.placefulworkflowpolicy-configure.zcml`` in the
  ``/path/to/instance/etc/package-includes`` directory.  The file
  should only contain this::

    <include package="groupspace.placefulworkflowpolicy" />


Alternatively, if you are using zc.buildout and the plone.recipe.zope2instance
recipe to manage your project, you can do this:

* Add ``groupspace.placefulworkflowpolicy`` to the list of eggs to install, e.g.:

    [buildout]
    ...
    eggs =
        ...
        groupspace.placefulworkflowpolicy
       
* Tell the plone.recipe.zope2instance recipe to install a ZCML slug:

    [instance]
    recipe = plone.recipe.zope2instance
    ...
    zcml =
        groupspace.placefulworkflowpolicy
      
* Re-run buildout, e.g. with:

    $ ./bin/buildout
        
You can skip the ZCML slug if you are going to explicitly include the package
from another package's configure.zcml file.
