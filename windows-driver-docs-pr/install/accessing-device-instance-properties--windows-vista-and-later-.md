---
title: Accessing Device Instance Properties
description: Accessing Device Instance Properties
ms.assetid: b571201a-e765-45d0-993b-5855041b4697
---

# Accessing Device Instance Properties


In Windows Vista and later versions of Windows, applications and installers can access [device instance properties](https://msdn.microsoft.com/library/windows/hardware/ff541334) by calling the following SetupAPI functions:

-   [**SetupDiGetDevicePropertyKeys**](https://msdn.microsoft.com/library/windows/hardware/ff551965)

    The **SetupDiGetDevicePropertyKeys** function retrieves an array of the device property keys that identify the device properties that are currently set for a device instance. For information about how to determine what properties are set for a device, see [Determining Which Properties Are Set for a Device Instance](determining-which-properties-are-set-for-a-device-instance.md).

-   [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

    The **SetupDiGetDeviceProperty** function [retrieves a device property that is set for a device instance](retrieving-a-device-instance-property-value.md).

-   [**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163)

    The **SetupDiSetDeviceProperty** function [sets a device property for a device instance](setting-a-device-instance-property-value.md).

For information about how to access device properties on Windows Server 2003, Windows XP, and Windows 2000, see [Using SetupAPI and Configuration Manager to Access Device Properties](using-setupapi-and-configuration-manager-to-access-device-properties.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Accessing%20Device%20Instance%20Properties%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




