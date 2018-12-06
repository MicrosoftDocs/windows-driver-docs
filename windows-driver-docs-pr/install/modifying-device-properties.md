---
title: Rules for Modifying Device Properties
description: Rules for Modifying Device Properties
ms.assetid: EB554B5C-310A-4b2c-A2D5-22A113415400
keywords:
- device properties WDK device installations , rules for modifying
- device properties WDK device installations , modifying
- modifying device properties WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Rules for Modifying Device Properties


Many [device properties](device-properties.md) have complex dependencies on other properties or device state. For example, the values of [**DEVPKEY_Device_Class**](https://msdn.microsoft.com/library/windows/hardware/ff542385) and [**DEVPKEY_Device_ClassGuid**](https://msdn.microsoft.com/library/windows/hardware/ff542388) must be consistent with one another.

Direct modification of reserved properties could invalidate device installation state. For example, if the [**DEVPKEY_Device_DeviceDesc**](https://msdn.microsoft.com/library/windows/hardware/ff542407) is changed, system functionality (such as backup, driver rollback, and Windows Update) could break.

The following properties are read-only and can never be set with [**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163):

-   [**DEVPKEY_Device_Address**](https://msdn.microsoft.com/library/windows/hardware/ff542359)

-   [**DEVPKEY_Device_BusNumber**](https://msdn.microsoft.com/library/windows/hardware/ff542364)

-   [**DEVPKEY_Device_BusTypeGuid**](https://msdn.microsoft.com/library/windows/hardware/ff542371)

-   [**DEVPKEY_Device_Capabilities**](https://msdn.microsoft.com/library/windows/hardware/ff542373)

-   [**DEVPKEY_Device_EnumeratorName**](https://msdn.microsoft.com/library/windows/hardware/ff542489)

-   [**DEVPKEY_Device_LegacyBusType**](https://msdn.microsoft.com/library/windows/hardware/ff542541)

-   [**DEVPKEY_Device_PDOName**](https://msdn.microsoft.com/library/windows/hardware/ff542580)

-   [**DEVPKEY_Device_PowerData**](https://msdn.microsoft.com/library/windows/hardware/ff542586)

-   [**DEVPKEY_Device_RemovalPolicy**](https://msdn.microsoft.com/library/windows/hardware/ff542597)

-   [**DEVPKEY_Device_RemovalPolicyDefault**](https://msdn.microsoft.com/library/windows/hardware/ff542603)

-   [**DEVPKEY_Device_UINumber**](https://msdn.microsoft.com/library/windows/hardware/ff542660)

The following properties are writable. However, they are reserved for use by the operating system and must not be set directly:

-   [**DEVPKEY_Device_Class**](https://msdn.microsoft.com/library/windows/hardware/ff542385)

-   [**DEVPKEY_Device_ClassGuid**](https://msdn.microsoft.com/library/windows/hardware/ff542388)

-   [**DEVPKEY_Device_Driver**](https://msdn.microsoft.com/library/windows/hardware/ff542427)

-   [**DEVPKEY_Device_DriverDesc**](https://msdn.microsoft.com/library/windows/hardware/ff542436)

-   [**DEVPKEY_Device_Manufacturer**](https://msdn.microsoft.com/library/windows/hardware/ff542558)

**Note**  [*Class installers*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-class-installer) and [*co-installers*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-co-installer) must not change device properties except for the friendly name ([**DEVPKEY_Device_FriendlyName**](https://msdn.microsoft.com/library/windows/hardware/ff542502)) and the upper and lower filter drivers for the device ([**DEVPKEY_Device_UpperFilters**](https://msdn.microsoft.com/library/windows/hardware/ff542667) and [**DEVPKEY_Device_LowerFilters**](https://msdn.microsoft.com/library/windows/hardware/ff542554)). For more information, see [Accessing Device Instance Properties](accessing-device-instance-properties--windows-vista-and-later-.md).

 

 

 





