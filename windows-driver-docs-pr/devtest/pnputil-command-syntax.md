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

**/disable-device** <em><instance ID> [/reboot]</em>

Disable devices on the system. 

```
/reboot - reboot system if needed to complete the operation.
```

**/enable-device** <em><instance ID> [/reboot]</em>

Enable devices on the system.  

```
/reboot - reboot system if needed to complete the operation.
```

**/restart-device** <em><instance ID> [/reboot]</em>

Restart devices devices on the system. 

```
/reboot - reboot system if needed to complete the operation.
```

**/remove-device** <em><instance ID> [/subtree] [/reboot]</em>

Attempt to remove a device from the system. 

```
/subtree - remove entire device subree, including any child devices.
/reboot - reboot system if needed to complete the operation.
```

**/scan-devices** <em> [/instanceid <instance ID>] [/async]</em>

Scan the system for any device hardware changes. 

```
/instanceid <instance ID> - scan device subtree for changes.
/async - scan for changes asynchronously.
```
**/enum-devices** <em> [/connected] [/disconnected] [instanceid <instance ID>] [/class <name | GUID>] [/problem [<code>]] [/ids] [/relations] [/drivers] </em>

Enumerate all devices on the system.

```
/connected | /disconnected - filter by connected devices or filter by disconnected devices.
/instanceid <instance ID> - filter by device instance ID.
/class <name | GUID> - filter by device class name or GUID.
/problem [<code>] - filter by devices with problems or filter by specific problem code.
/ids - display hardware IDs and compatible IDs.
/relations - display parent and child device relations.
/drivers - display matching and installed drivers.
```

**/enum-interfaces** <em> [/enabled | /disabled] [/class <name | GUID>] </em>

Enumerate all device interfaces on the system.

```
/enabled | /disabled - filter by enabled interfaces or filter by disabled interfaces.
/class <GUID> - filter by interface class GUID.
```

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

 

 





