---
title: \ Registry Subkey
description: \ Registry Subkey
ms.assetid: 19b72c64-5a64-4655-b922-4a4bca162b32
---

# \* Registry Subkey


Beginning with Windows 7, the **\*** (asterisk) registry subkey specifies that a removable device capability override applies to all device nodes ([*devnodes*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) enumerated for the device identified through either the [HardwareID](hardwareid-registry-subkey.md) or [CompatibleID](compatibleid-registry-subkey.md) registry subkey. For more information about removable device capability overrides, see [DeviceOverrides Registry Key](deviceoverrides-registry-key.md).

The **\*** registry subkey applies the removable device capability override to all devnodes specified through the **HardwareID** or **CompatibleID** registry subkeys, based on the rules of the [LocationPaths](locationpaths-registry-subkey.md) or [ChildLocationPaths](childlocationpaths-registry-subkey.md) registry subkey specified for the override. For example, if the **\*** registry subkey is specified within a **LocationPaths** subkey, the removable device capability override applies to all parent devnodes for devices identified through the parent **HardwareID** or **CompatibleID** registry subkey.

The following table defines the format and requirements of the **\*** registry subkey.

| Registry subkey name | Required/optional | Format requirements | Parent subkey                                                                                                      | Child subkeys |
|----------------------|-------------------|---------------------|--------------------------------------------------------------------------------------------------------------------|---------------|
| \*                   | Optional          | None                | [LocationPaths](locationpaths-registry-subkey.md) or [ChildLocationPaths](childlocationpaths-registry-subkey.md) | None          |

 

Either the [LocationPath](locationpath-registry-subkey.md) or **\*** registry subkeys must be present to indicate the scope of the removable device capability override.

The \* registry subkey must contain a **Removable** DWORD value that specifies whether the device is removable or not. The following table defines the valid **Removable** values.

| Removable value | Explanation                                                 |
|-----------------|-------------------------------------------------------------|
| 0               | The applicable devnodes should be regarded as not removable |
| 1               | The applicable devnodes should be regarded as removable     |

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20*%20Registry%20Subkey%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




