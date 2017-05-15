---
title: Using CVS
description: Using CVS
ms.assetid: 4ad1202e-0be5-4adc-af8b-6b8d7cb34b04
keywords: ["Concurrent Versions System (CVS)", "source servers, CVS", "SrcSrv, CVS", "Concurrent Versions System (CVS), overview"]
---

# Using CVS


The CVS module for Source Server was developed using Concurrent Versions System (CVS) 1.11.17 (client). It has not been tested with any other versions of CVS. Furthermore, the current version of the module is a beta version.

### <span id="cvsroot"></span><span id="CVSROOT"></span>CVSROOT

On the computer on which you source index the build, CVSROOT cannot contain password and user information. Use cvs.exe to set your credentialing information.

To prepare the [Srcsrv.ini](the-srcsrv-ini-file.md) file for CVS indexing you must enter an alias for your repository that uniquely distinguishes it from any others in your network. This repository must match the value of CVSROOT in your environment. There is no need to set this value in the copy of Srcsrv.ini that you keep with your debugger clients because the alias is defined in the source indexed .pdb file.

### <span id="client_computer"></span><span id="CLIENT_COMPUTER"></span>Client Computer

The client computer that extracts files during debugging does not need a CVS sandbox or CVSROOT set. It does need CVS binaries in the path, and if the repository is locked, you must set the username and password with Cvs.exe.

### <span id="revision_tags"></span><span id="REVISION_TAGS"></span>Revision Tags

CVS is unable to extract a file by its version number. Instead, it must be done using what is known as a *tag*. When indexing a CVS-based system, you must ensure that all changes are checked into the repository and then apply a tag using the "cvs tag" command. Then, when indexing the file, make certain you use the "label" command-line parameter to specify the tag that you want to associate with the build you are indexing. You can achieve the same result by setting CVS\_LABEL in the environment. Other values can be set from the environment or the command line. Use the **-??** command-line option with SSIndex to examine your choices and to verify that all was configured correctly:

```
ssindex.cmd -system=cvs -??
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20CVS%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




