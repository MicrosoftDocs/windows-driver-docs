---
title: PnPUtil Command Syntax
description: How to run PnPUtil, including syntax and parameters. 
ms.assetid: f14ceb98-8d82-43dd-b06e-2595b59b6999
keywords:
- PnPUtil Command Syntax Driver Development Tools
topic_type:
- apiref
api_name:
- PnPUtil
api_type:
- NA
ms.date: 01/31/2018
ms.localizationpriority: medium
---

# PnPUtil Command Syntax


To run PnPUtil, open a Command Prompt window (**Run as Administrator**) and type a command using the following syntax and parameters.

**Note**  PnPUtil (PnPUtil.exe) is included in every version of Windows, starting with Windows Vista (in the %windir%\\system32 directory).

 

```
pnputil [/add-driver <...> | /delete-driver <...> |
         /export-driver <...> | /enum-drivers | /?]
```

## Commands

  **/add-driver** <filename.inf | *.inf> [/subdirs] [/install] [/reboot]

Add driver package(s) into the driver store.  
```
/subdirs - traverse sub directories for driver packages.  
/install - install/update drivers on any matching devices.  
/reboot - reboot system if needed to complete the operation.  
```

  **/delete-driver** *<oem#.inf> [/uninstall] [/force] [/reboot]*

Delete driver package from the driver store.  

```
/uninstall - uninstall driver package from any devices using it.  
/force - delete driver package even when it is in use by devices.  
/reboot - reboot system if needed to complete the operation.  
```

**/export-driver** <em><oem#.inf | *> <target directory></em>

Export driver package(s) from the driver store into a target directory.

**/enum-drivers**

Enumerate all 3rd party driver packages in the driver store.

**/?**

Displays the command-line syntax.

## Legacy Command Mapping

The following commands are still supported, but are legacy.  We recommend that you use the up-to-date syntax instead.

```
  -a [-i]  <filename.inf> ==> /add-driver <filename.inf> [/install]

  -d [-f]  <oem#.inf>     ==> /delete-driver <oem#.inf> [/force]

  -e                     ==> /enum-drivers
```
 

###  Comments



For examples of how to use the PnPUtil tool, see [PnPUtil Examples](pnputil-examples.md).

 

 





