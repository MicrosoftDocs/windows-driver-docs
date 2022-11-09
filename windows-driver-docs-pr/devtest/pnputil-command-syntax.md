---
title: PnPUtil Command Syntax
description: How to run PnPUtil, including syntax and parameters. 
keywords:
- PnPUtil Command Syntax Driver Development Tools
topic_type:
- apiref
api_name:
- PnPUtil
api_type:
- NA
ms.date: 11/09/2022
---

# PnPUtil Command Syntax


To run PnPUtil, open a Command Prompt window (**Run as Administrator**) and type a command using the following syntax and parameters.

**Note**  PnPUtil (PnPUtil.exe) is included in every version of Windows, starting with Windows Vista (in the %windir%\\system32 directory).

**PNPUTIL** \[/add-driver <...> | /delete-driver <...> | /export-driver <...> | /enum-drivers | /enum-devices \[<...>\] | /enum-interfaces \[<...>\] | /disable-device <...> | /enable-device <...> | /restart-device <...> | /remove-device <...> | /scan-devices \[<...>\] | /enum-classes \[<...>\] | /?\]

## Commands

### **/add-driver** *\<filename.inf | \*.inf\> \[/subdirs] \[/install] \[/reboot]*

**Available starting in Windows 10, version 1607.**

Add driver package(s) into the driver store.  

/subdirs - traverse sub directories for driver packages.  

/install - install/update drivers on any matching devices.  

/reboot - reboot system if needed to complete the operation.  


### **/delete-driver** *\<oem#.inf\> \[/uninstall] \[/force] \[/reboot]*

**Available starting in Windows 10, version 1607.**

Delete driver package from the driver store.  

/uninstall - uninstall driver package from any devices using it.  

/force - delete driver package even when it is in use by devices.  

/reboot - reboot system if needed to complete the operation.  


### **/export-driver** *\<oem#.inf | \*\> \<target directory\>*

**Available starting in Windows 10, version 1607.**

Export driver package(s) from the driver store into a target directory.


### **/enum-drivers** *\[/class \<name | GUID\>] \[/files]*

**Available starting in Windows 10, version 1607.**

Enumerate all 3rd party driver packages in the driver store.

**Flags available starting in Windows 11, version 21H2.**

/class \<name | GUID\> - filter by driver class name or GUID.

**Flags available starting in Windows 11, version 22H2.**

/files - enumerate all driver package files.


### **/disable-device** *\[\<instance ID\> | /deviceid \<device ID\>] \[/class \<name | GUID\>] \[/bus \<name | GUID\>] \[/reboot] \[/force]*

**Available starting in Windows 10 Version 2004**

Disable devices on the system. 

/reboot - reboot system if needed to complete the operation.

**Flags available starting in Windows 11 Version 21H2**

/deviceid \<device ID\> - disable all devices with matching device ID.

**Flags available starting in Windows 11 Version 22H2**

/class \<name | GUID\> - filter by device class name or GUID.

/bus \<name | GUID\> - filter by bus enumerator name or bus type GUID.

/force - disable even if device provides critical system functionality.


### **/enable-device** *\[\<instance ID\> | /deviceid \<device ID\>] \[/class \<name | GUID\>] \[/bus \<name | GUID\>] \[/reboot]*

**Available starting in Windows 10 Version 2004**

Enable devices on the system.  

/reboot - reboot system if needed to complete the operation.

**Flags available starting in Windows 11 Version 21H2**

/deviceid \<device ID\> - enable all devices with matching device ID.

**Flags available starting in Windows 11 Version 22H2**

/class \<name | GUID\> - filter by device class name or GUID.

/bus \<name | GUID\> - filter by bus enumerator name or bus type GUID.


### **/restart-device** *\[\<instance ID\> | /deviceid \<device ID\>] \[/class \<name | GUID\>] \[/bus \<name | GUID\>] \[/reboot]*

**Available starting in Windows 10 Version 2004**

Restart devices devices on the system. 

/reboot - reboot system if needed to complete the operation.

**Flags available starting in Windows 11 Version 21H2**

/deviceid \<device ID\> - restart all devices with matching device ID.

**Flags available starting in Windows 11 Version 22H2**

/class \<name | GUID\> - filter by device class name or GUID.

/bus \<name | GUID\> - filter by bus enumerator name or bus type GUID.


### **/remove-device** *\[\<instance ID\> | /deviceid \<device ID\>] \[/class \<name | GUID\>] \[/bus \<name | GUID\>] \[/subtree] \[/reboot] \[/force]*

**Available starting in Windows 10 Version 2004**

Attempt to remove a device from the system. 

/subtree - remove entire device subree, including any child devices.

/reboot - reboot system if needed to complete the operation.

**Flags available starting in Windows 11 Version 21H2**

/deviceid \<device ID\> - remove all devices with matching device ID.

**Flags available starting in Windows 11 Version 22H2**

/class \<name | GUID\> - filter by device class name or GUID.

/bus \<name | GUID\> - filter by bus enumerator name or bus type GUID.

/force - remove even if device provides critical system functionality.


### **/scan-devices** *\[/instanceid \<instance ID\>] \[/async]*

**Available starting in Windows 10 Version 2004**

Scan the system for any device hardware changes. 

/instanceid \<instance ID\> - scan device subtree for changes.

/async - scan for changes asynchronously.


### **/enum-devices** *\[/connected] | /disconnected] \[/instanceid \<instance ID\> | /deviceid \<device ID\>] \[/class \<name | GUID\>] \[/problem \[\<code\>]] \[/bus \[\<name | GUID\>]] \[/deviceids] \[/relations] \[/services] \[/stack] \[/drivers] \[/interfaces] \[/properties] \[/resources]*

**Available starting in Windows 10 Version 1903**

Enumerate all devices on the system.

/connected | /disconnected - filter by connected devices or filter by disconnected devices.

/instanceid \<instance ID\> - filter by device instance ID.

/class \<name | GUID\> - filter by device class name or GUID.

/problem \[\<code\>] - filter by devices with problems or filter by specific problem code.

/relations - display parent and child device relations.

/drivers - display matching and installed drivers.

**Flags available starting in Windows 11 Version 21H2**

/bus \[\<name | GUID\>] - display bus enumerator name and bus type GUID or filter by bus enumerator name or bus type GUID.

/deviceids - display hardware and compatible IDs.

/services - display device services.

/stack - display effective device stack information.

/interfaces - display device interfaces.

/properties - display all device properties.

**Flags available starting in Windows 11 Version 22H2**

/deviceid \<device ID\> - filter by device hardware and compatible ID.

/resources - display device resources.


### **/enum-interfaces** *\[/enabled | /disabled] \[/class \<GUID\>] \[/properties]*

**Available starting in Windows 10 Version 1903**

Enumerate all device interfaces on the system.

/enabled | /disabled - filter by enabled interfaces or filter by disabled interfaces.

/class \<GUID\> - filter by interface class GUID.

**Available starting in Windows 11, version 22H2.**

/properties - display all interface properties.


### **/enum-classes** *\[/class \<name | GUID\>] \[/services]*

**Available starting in Windows 11, version 22H2.**

Enumerate all device classes on the system.

/class \<name | GUID\> - filter by device class name or GUID.

/services - display device class services.


### **/?**

Displays the command-line syntax.

## Legacy Command Mapping

The following commands are still supported, but are legacy.  We recommend that you use the up-to-date syntax instead.

```
  -a [-i]  <filename.inf> ==> /add-driver <filename.inf> [/install]

  -d [-f]  <oem#.inf>     ==> /delete-driver <oem#.inf> [/force]

  -e                     ==> /enum-drivers
```
 

##  Examples

For examples of how to use the PnPUtil tool, see [PnPUtil Examples](pnputil-examples.md).