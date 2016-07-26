---
title: Modifying Registry Values in a Device's Software Key
description: Modifying Registry Values in a Device's Software Key
ms.assetid: 4DBDB53D-CA64-4c19-84A5-FBE1529FD0C5
keywords: ["registry WDK device installations , modifying registry values in a device's software key", "modifying registry values WDK device installations , device software key"]
---

# Modifying Registry Values in a Device's Software Key


You must not modify the values of the following registry entries (*device properties*) in a device's [*software key*](https://msdn.microsoft.com/library/windows/hardware/ff556336#wdkgloss-software-key):

-   DriverDate

-   DriverDateData

-   DriverDesc

-   DriverVersion

-   InfPath

-   InfSection

-   InfSectionExt

-   MatchingDeviceId

-   ProviderName

-   EnumPropPages32

These device properties represent a device?s installation state. Direct modification of these properties might invalidate the device?s installation state. For example, changing information related to the [INF file](inf-files.md) invalidates information about driver files that are associated with such properties as device and driver signing information. Changing driver version or driver date might break Windows Update functionality.

**Note**  Starting with Windows Vista, the operating system imposes "installation-time only" access restrictions for these properties. Values can be replicated for compatibility, and direct modification of values during device installation does not affect internal state.

 

To safely modify the values of other registry entries in a device's software key, follow these guidelines:

-   Use [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) and [**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163) to retrieve and set standard or custom properties.

    For more information, see [Accessing Device Driver Properties](accessing-device-driver-properties.md).

-   Set only those device properties that are not reserved by the operating system.

    For example, to change the name of the device as displayed to the user, change its [**DEVPKEY\_Device\_FriendlyName**](https://msdn.microsoft.com/library/windows/hardware/ff542502) device property.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Modifying%20Registry%20Values%20in%20a%20Device's%20Software%20Key%20%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




