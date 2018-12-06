---
title: Modifying Registry Values in a Device's Software Key
description: Modifying Registry Values in a Device's Software Key
ms.assetid: 4DBDB53D-CA64-4c19-84A5-FBE1529FD0C5
keywords:
- registry WDK device installations , modifying registry values in a device's software key
- modifying registry values WDK device installations , device software key
ms.date: 04/20/2017
ms.localizationpriority: medium
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

These device properties represent a device's installation state. Direct modification of these properties might invalidate the device's installation state. For example, changing information related to the [INF file](inf-files.md) invalidates information about driver files that are associated with such properties as device and driver signing information. Changing driver version or driver date might break Windows Update functionality.

**Note**  Starting with Windows Vista, the operating system imposes "installation-time only" access restrictions for these properties. Values can be replicated for compatibility, and direct modification of values during device installation does not affect internal state.

 

To safely modify the values of other registry entries in a device's software key, follow these guidelines:

-   Use [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) and [**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163) to retrieve and set standard or custom properties.

    For more information, see [Accessing Device Driver Properties](accessing-device-driver-properties.md).

-   Set only those device properties that are not reserved by the operating system.

    For example, to change the name of the device as displayed to the user, change its [**DEVPKEY_Device_FriendlyName**](https://msdn.microsoft.com/library/windows/hardware/ff542502) device property.

 

 





