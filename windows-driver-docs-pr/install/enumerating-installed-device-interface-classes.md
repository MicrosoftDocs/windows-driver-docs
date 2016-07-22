---
title: Enumerating Installed Device Interfaces
description: Enumerating Installed Device Interfaces
ms.assetid: 14A9E6DD-58A9-4af0-B469-7CCF4596BE27
keywords: ["enumerating installed device interfaces WDK", "installed device interfaces WDK", "installed device interfaces WDK , enumerating", "device interfaces WDK device installations , enumerating"]
---

# Enumerating Installed Device Interfaces


You must not enumerate the device interface classes in a system by directly accessing registry keys. As with any registry key, the location, name, or format of the key might change between different versions of Windows.

Use the following guidelines to safely discover the attributes of device interfaces:

-   User-mode applications should follow these steps:

    1.  Use [**SetupDiGetClassDevs**](https://msdn.microsoft.com/library/windows/hardware/ff551069) or [**SetupDiGetClassDevsEx**](https://msdn.microsoft.com/library/windows/hardware/ff551072) to retrieve the devices that support interfaces for the specified device interface class. You must set the DIGCF\_DEVICEINTERFACE flag in the *Flags* parameter, and you must set the *Enumerator* parameter to a specific device instance identifier.

        To include only device interfaces that are present in a system, set the DIGCF\_PRESENT flag in the *Flags* parameter.

    2.  Use [**SetupDiEnumDeviceInterfaces**](https://msdn.microsoft.com/library/windows/hardware/ff551015) to enumerate interfaces that are registered for a device interface class. This interface class is specified through the *InterfaceClassGuid* parameter.

-   Kernel-mode drivers should use [**IoGetDeviceInterfaces**](https://msdn.microsoft.com/library/windows/hardware/ff549186) to enumerate the device interface classes that are installed in the system.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Enumerating%20Installed%20Device%20Interfaces%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




