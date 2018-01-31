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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
```/subdirs - traverse sub directories for driver packages.  
/install - install/update drivers on any matching devices.  
/reboot - reboot system if needed to complete the operation.  
```

  **/delete-driver** *<oem#.inf> [/uninstall] [/force] [/reboot]*

Delete driver package from the driver store.  

```/uninstall - uninstall driver package from any devices using it.  
/force - delete driver package even when it is in use by devices.  
/reboot - reboot system if needed to complete the operation.  
```

**/export-driver** *<oem#.inf | *> <target directory>*

Export driver package(s) from the driver store into a target directory.

**/enum-drivers**

Enumerate all 3rd party driver packages in the driver store.

**/?**

Displays the command-line syntax.

## Legacy Command Mapping

```
  [-i] -a <filename.inf> ==> /add-driver <filename.inf> [/install]

  [-f] -d <oem#.inf>     ==> /delete-driver <oem#.inf> [/force]

  -e                     ==> /enum-drivers
```
 

###  Comments



For examples of how to use the PnPUtil tool, see [PnPUtil Examples](pnputil-examples.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20PnPUtil%20Command%20Syntax%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




