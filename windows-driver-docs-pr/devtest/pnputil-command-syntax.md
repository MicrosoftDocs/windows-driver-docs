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
ms.date: 11/14/2022
---

# PnPUtil Command Syntax

PnPUtil (PnPUtil.exe) is included in every version of Windows starting with Windows Vista, in the %windir%\\system32 directory.

To run PnPUtil, open a command prompt window (Run as Administrator) and type a command using the following syntax and parameters.

```syntax
PNPUTIL [/add-driver <...> | /delete-driver <...> |
         /export-driver <...> | /enum-drivers |
         /enum-devices [<...>] | /enum-interfaces [<...>] |
         /disable-device <...> | /enable-device <...> |
         /restart-device <...> | /remove-device <...> |
         /scan-devices [<...>] | /enum-classes [<...>] |
         /?]
```

## Commands

### /add-driver

Adds driver package(s) into the driver store. Command available starting in Windows 10, version 1607.

```syntax
PNPUTIL /add-driver <filename.inf | *.inf> [/subdirs] [/install] [/reboot]
```

Flags:

- `/subdirs` - traverse sub directories for driver packages
- `/install` - install/update drivers on any matching devices
- `/reboot` - reboot system if needed to complete the operation

### /delete-driver

Deletes a driver package from the driver store. Command available starting in Windows 10, version 1607.

```syntax
PNPUTIL /delete-driver <oem#.inf> [/uninstall] [/force] [/reboot]
```

Flags:

- `/uninstall` - uninstall driver package from any devices using it
- `/force` - delete driver package even when it is in use by devices
- `/reboot` - reboot system if needed to complete the operation

### /export-driver

Exports driver package(s) from the driver store into a target directory. Command available starting in Windows 10, version 1607.

```syntax
PNPUTIL /export-driver <oem#.inf | *> <target directory>
```

### /enum-drivers

Enumerates all third-party driver packages in the driver store. Command available starting in Windows 10, version 1607.

```syntax
PNPUTIL /enum-drivers [/class <name | GUID>] [/files]
```

Flags available starting in Windows 11, version 21H2:

- `/class <name | GUID>` - filter by driver class name or GUID

Flags available starting in Windows 11, version 22H2:

- `/files` - enumerate all driver package files

### /disable-device

Disables devices on the system. Command available starting in Windows 10 version 2004.

```syntax
PNPUTIL /disable-device [<instance ID> | /deviceid <device ID>]
                        [/class <name | GUID>]
                        [/bus <name | GUID>]
                        [/reboot] [/force]
```

Flags:

- `/reboot` - reboot system if needed to complete the operation

Flags available starting in Windows 11 version 21H2:

- `/deviceid <device ID>` - disable all devices with matching device ID

Flags available starting in Windows 11 version 22H2:

- `/class <name | GUID>` - filter by device class name or GUID
- `/bus <name | GUID>` - filter by bus enumerator name or bus type GUID
- `/force` - disable even if device provides critical system functionality

### /enable-device

Enables devices on the system. Command available starting in Windows 10 version 2004.

```syntax
PNPUTIL /enable-device [<instance ID> | /deviceid <device ID>]
                       [/class <name | GUID>] [/bus <name | GUID>]
                       [/reboot]
```

Flags:

- `/reboot` - reboot system if needed to complete the operation

Flags available starting in Windows 11 version 21H2:

- `/deviceid <device ID>` - enable all devices with matching device ID

Flags available starting in Windows 11 version 22H2:

- `/class <name | GUID>` - filter by device class name or GUID
- `/bus <name | GUID>` - filter by bus enumerator name or bus type GUID

### /restart-device

Restarts devices on the system. Command available starting in Windows 10 version 2004.

```syntax
PNPUTIL /restart-device [<instance ID> | /deviceid <device ID>]
                        [/class <name | GUID>] [/bus <name | GUID>]
                        [/reboot]
```

Flags:

- `/reboot` - reboot system if needed to complete the operation

Flags available starting in Windows 11 version 21H2:

- `/deviceid <device ID>` - restart all devices with matching device ID

Flags available starting in Windows 11 version 22H2:

- `/class <name | GUID>` - filter by device class name or GUID
- `/bus <name | GUID>` - filter by bus enumerator name or bus type GUID.

### /remove-device

Attempts to remove a device from the system. Command available starting in Windows 10 version 2004.

```syntax
PNPUTIL /remove-device [<instance ID> | /deviceid <device ID>]
                       [/class <name | GUID>] [/bus <name | GUID>]
                       [/subtree] [/reboot] [/force]
```

Flags:

- `/subtree` - remove entire device subtree, including any child devices
- `/reboot` - reboot system if needed to complete the operation

Flags available starting in Windows 11 version 21H2:

- `/deviceid <device ID>` - remove all devices with matching device ID

Flags available starting in Windows 11 version 22H2:

- `/class <name | GUID>` - filter by device class name or GUID
- `/bus <name | GUID>` - filter by bus enumerator name or bus type GUID
- `/force` - remove even if device provides critical system functionality

### /scan-devices

Scans the system for any device hardware changes. Command available starting in Windows 10 version 2004.

```syntax
/scan-devices [/instanceid <instance ID>] [/async]
```

Flags:

- `/instanceid <instance ID>` - scan device subtree for changes
- `/async` - scan for changes asynchronously

### /enum-devices

Enumerate all devices on the system. Command available starting in Windows 10 version 1903.

```syntax
PNPUTIL /enum-devices [/connected | /disconnected]
                      [/instanceid <instance ID> | /deviceid <device ID>]
                      [/class <name | GUID>] [/problem [<code>]]
                      [/bus [<name | GUID>]] [/deviceids] [/relations]
                      [/services] [/stack] [/drivers] [/interfaces]
                      [/properties] [/resources]
```

Flags:

- `/connected` - filter by connected devices
- `/disconnected` - filter by disconnected devices
- `/instanceid <instance ID>` - filter by device instance ID
- `/class <name | GUID>` - filter by device class name or GUID
- `/problem [<code>]` - filter by devices with problems or filter by specific problem code
- `/relations` - display parent and child device relations
- `/drivers` - display matching and installed drivers

Flags available starting in Windows 11 version 21H2:

- `/bus [<name | GUID>]` - display bus enumerator name and bus type GUID or filter by bus enumerator name or bus type GUID
- `/deviceids` - display hardware and compatible IDs
- `/services` - display device services
- `/stack` - display effective device stack information
- `/interfaces` - display device interfaces
- `/properties` - display all device properties

Flags available starting in Windows 11 version 22H2:

- `/deviceid <device ID>` - filter by device hardware and compatible ID
- `/resources` - display device resources

### /enum-interfaces

Enumerates all device interfaces on the system. Command available starting in Windows 10 version 1903.

```syntax
PNPUTIL /enum-interfaces [/enabled | /disabled] [/class <GUID>] [/properties]
```

Flags:

- `/enabled` - filter by enabled interfaces
- `/disabled` - filter by disabled interfaces
- `/class <GUID>` - filter by interface class GUID

Flags available starting in Windows 11, version 22H2:

- `/properties` - display all interface properties

### /enum-classes

Enumerates all device classes on the system. Command available starting in Windows 11, version 22H2.

```syntax
PNPUTIL /enum-classes [/class <name | GUID>] [/services]
```

Flags:

- `/class <name | GUID>` - filter by device class name or GUID
- `/services` - display device class services

### /?

Displays the command-line syntax.

```syntax
PNPUTIL /?
```

## Legacy Command Mapping

The following commands are still supported, but are legacy.  We recommend that you use the up-to-date syntax instead.

```syntax
  -a [-i]  <filename.inf> ==> /add-driver <filename.inf> [/install]

  -d [-f]  <oem#.inf>     ==> /delete-driver <oem#.inf> [/force]

  -e                      ==> /enum-drivers
```

## Examples

For examples of how to use the PnPUtil tool, see [PnPUtil Examples](pnputil-examples.md).
