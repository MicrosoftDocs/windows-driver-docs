---
title: The Srcsrv.ini File
description: The Srcsrv.ini File
ms.assetid: 5a3f5990-e43a-4c50-a16f-cbaa9f706ece
keywords: ["SrcSrv, Srcsrv.ini file", "Srcsrv.ini file", "SrcSrv, SRCSRV_INI_FILE environment variable", "SRCSRV_INI_FILE environment variable"]
---

# The Srcsrv.ini File


The Srcsrv.ini file is the master list of all source control servers. Each entry has the following format:

```
MYSERVER=ServerInfo
```

When using Perforce, the *ServerInfo* consists of the full network path to the server, followed by a colon, followed by the port number it uses. For example:

```
MYSERVER=machine.corp.company.com:1666
```

Srcsrv.ini is a required file when you are actually source indexing a build using the modules shipped with this package. This entry creates an alias that is used to describe the server info. The value should be unique for every server that you support.

This file can also be installed on the computer running the debugger. When SrcSrv starts, it looks at Srcsrv.ini for values; these values override the information contained in the .pdb file. This enables users to configure a debugger to use an alternative source control server at debug time. However, if you manage your servers well and do not rename them, there should be no need to include this file with your client debugger installations.

This file also serves other purposes on the client side. For more information, see the sample Srcsrv.ini file installed with SrcSrv tools.

### <span id="using_a_different_location_or_file_name"></span><span id="USING_A_DIFFERENT_LOCATION_OR_FILE_NAME"></span>Using a Different Location or File Name

By default, SrcSrv uses as its master configuration file the file named Srcsrv.ini, located in the srcsrv subdirectory of the Debugging Tools for Windows installation directory.

You can specify a different file for configuration by setting the SRCSRV\_INI\_FILE environment variable equal to the full path and file name of the desired file.

For example, if several people want to share a single configuration file, they could place it on a share accessible to all of their systems, and then set an environment variable like the following:

```
set SRCSRV_INI_FILE=\\ourserver\ourshare\bestfile.txt
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20The%20Srcsrv.ini%20File%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




