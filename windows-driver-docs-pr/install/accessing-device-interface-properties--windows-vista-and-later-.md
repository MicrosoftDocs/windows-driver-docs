---
title: Accessing Device Interface Properties
description: Accessing Device Interface Properties
ms.assetid: 8a46816b-56c5-49e9-8250-9ede037ae2b5
---

# Accessing Device Interface Properties


In Windows Vista and later versions of Windows, applications and installers can access [device interface properties](https://msdn.microsoft.com/library/windows/hardware/ff541409) by calling the following SetupAPI functions:

-   [**SetupDiGetDeviceInterfacePropertyKeys**](https://msdn.microsoft.com/library/windows/hardware/ff551959)

    The **SetupDiGetDeviceInterfacePropertyKeys** function retrieves an array of the device interface property keys that identify the device interface properties that are currently set for a device interface instance. For information about how to determine what properties are set for a device interface, see [Determining Which Properties are Set for a Device Interface](determining-which-properties-are-set-for-a-device-interface.md).

-   [**SetupDiGetDeviceInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551122)

    The **SetupDiGetDeviceInterfaceProperty** function [retrieves a device interface property](retrieving-a-device-interface-property-value.md) that is set for a device interface.

-   [**SetupDiSetDeviceInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552158)

    The **SetupDiSetDeviceInterfaceProperty** function [sets a device interface property](setting-a-device-interface-property-value.md) for a device interface.

For information about how to access device interface properties on Windows Server 2003, Windows XP, and Windows 2000, see Accessing Device Interface Properties.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Accessing%20Device%20Interface%20Properties%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




