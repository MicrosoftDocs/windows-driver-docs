---
title: Registry Trees and Keys for Devices and Drivers
description: Registry Trees and Keys for Devices and Drivers
ms.assetid: 8f6ac7c1-f31a-4d14-8ba7-b432615db073
---

# Registry Trees and Keys for Devices and Drivers


The operating system, drivers, and device installation components store information about drivers and devices in the registry. In general, drivers and device installation components should use the registry to store data that must be maintained across restarts of the system. For information about how a driver accesses registry information, see [Using the Registry in a Driver](https://msdn.microsoft.com/library/windows/hardware/ff565537).

Registry contents should always be treated as untrusted, modifiable information. If one of your driver components writes information to the registry and another component reads it later, do not assume that the information has not been modified in the meantime. After reading information from the registry, your driver components should always validate the information before using it.

For more information about the registry in general, see the Microsoft Windows SDK documentation.

This section contains the following topics which describe the use of registry keys to store information about drivers and devices:

[Registry Trees for Devices and Drivers](overview-of-registry-trees-and-keys.md)

[RunOnce Registry Key](runonce-registry-key.md)

[DeviceOverrides Registry Key](deviceoverrides-registry-key.md)

Drivers must access Plug and Play (PnP) keys in the registry using system routines such as [**IoGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff549203) or [**IoOpenDeviceRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff549443). User-mode setup components should use device installation functions such as [**SetupDiGetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551967) or [**SetupDiOpenDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552079). The registry can be accessed from INF files by using [**INF AddReg directives**](inf-addreg-directive.md).

**Important**  *Drivers must not access these registry trees and keys directly.* This discussion of registry information in this section is solely for debugging a device installation or configuration problem.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Registry%20Trees%20and%20Keys%20for%20Devices%20and%20Drivers%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




