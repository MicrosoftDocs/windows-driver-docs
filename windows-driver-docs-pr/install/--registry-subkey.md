---
title: '* Registry Subkey'
description: '* Registry Subkey'
ms.assetid: 19b72c64-5a64-4655-b922-4a4bca162b32
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# \* Registry Subkey


Beginning with Windows 7, the **\\*** (asterisk) registry subkey specifies that a removable device capability override applies to all device nodes ([*devnodes*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) enumerated for the device identified through either the [HardwareID](hardwareid-registry-subkey.md) or [CompatibleID](compatibleid-registry-subkey.md) registry subkey. For more information about removable device capability overrides, see [DeviceOverrides Registry Key](deviceoverrides-registry-key.md).

The **\\*** registry subkey applies the removable device capability override to all devnodes specified through the **HardwareID** or **CompatibleID** registry subkeys, based on the rules of the [LocationPaths](locationpaths-registry-subkey.md) or [ChildLocationPaths](childlocationpaths-registry-subkey.md) registry subkey specified for the override. For example, if the **\\*** registry subkey is specified within a **LocationPaths** subkey, the removable device capability override applies to all parent devnodes for devices identified through the parent **HardwareID** or **CompatibleID** registry subkey.

The following table defines the format and requirements of the **\\*** registry subkey.

| Registry subkey name | Required/optional | Format requirements | Parent subkey                                                                                                      | Child subkeys |
|----------------------|-------------------|---------------------|--------------------------------------------------------------------------------------------------------------------|---------------|
| \*                   | Optional          | None                | [LocationPaths](locationpaths-registry-subkey.md) or [ChildLocationPaths](childlocationpaths-registry-subkey.md) | None          |

 

Either the [LocationPath](locationpath-registry-subkey.md) or **\\*** registry subkeys must be present to indicate the scope of the removable device capability override.

The \* registry subkey must contain a **Removable** DWORD value that specifies whether the device is removable or not. The following table defines the valid **Removable** values.

| Removable value | Explanation                                                 |
|-----------------|-------------------------------------------------------------|
| 0               | The applicable devnodes should be regarded as not removable |
| 1               | The applicable devnodes should be regarded as removable     |

 

 

 





