---
title: The Srcsrv.ini File
description: The Srcsrv.ini File
ms.assetid: 5a3f5990-e43a-4c50-a16f-cbaa9f706ece
keywords: ["SrcSrv, Srcsrv.ini file", "Srcsrv.ini file", "SrcSrv, SRCSRV_INI_FILE environment variable", "SRCSRV_INI_FILE environment variable"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# The Srcsrv.ini File


The Srcsrv.ini file is the master list of all source control servers. Each entry has the following format:

```ini
MYSERVER=ServerInfo
```

When using Perforce, the *ServerInfo* consists of the full network path to the server, followed by a colon, followed by the port number it uses. For example:

```ini
MYSERVER=machine.corp.company.com:1666
```

Srcsrv.ini is a required file when you are actually source indexing a build using the modules shipped with this package. This entry creates an alias that is used to describe the server info. The value should be unique for every server that you support.

This file can also be installed on the computer running the debugger. When SrcSrv starts, it looks at Srcsrv.ini for values; these values override the information contained in the .pdb file. This enables users to configure a debugger to use an alternative source control server at debug time. However, if you manage your servers well and do not rename them, there should be no need to include this file with your client debugger installations.

This file also serves other purposes on the client side. For more information, see the sample Srcsrv.ini file installed with SrcSrv tools.

### <span id="using_a_different_location_or_file_name"></span><span id="USING_A_DIFFERENT_LOCATION_OR_FILE_NAME"></span>Using a Different Location or File Name

By default, SrcSrv uses as its master configuration file the file named Srcsrv.ini, located in the srcsrv subdirectory of the Debugging Tools for Windows installation directory.

You can specify a different file for configuration by setting the SRCSRV\_INI\_FILE environment variable equal to the full path and file name of the desired file.

For example, if several people want to share a single configuration file, they could place it on a share accessible to all of their systems, and then set an environment variable like the following:

```console
set SRCSRV_INI_FILE=\\ourserver\ourshare\bestfile.txt
```

 

 





