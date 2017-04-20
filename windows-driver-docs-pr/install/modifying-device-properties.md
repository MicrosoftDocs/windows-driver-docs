---
title: Rules for Modifying Device Properties
description: Rules for Modifying Device Properties
ms.assetid: EB554B5C-310A-4b2c-A2D5-22A113415400
keywords:
- device properties WDK device installations , rules for modifying
- device properties WDK device installations , modifying
- modifying device properties WDK device installations
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Rules for Modifying Device Properties


Many [device properties](device-properties.md) have complex dependencies on other properties or device state. For example, the values of [**DEVPKEY\_Device\_Class**](https://msdn.microsoft.com/library/windows/hardware/ff542385) and [**DEVPKEY\_Device\_ClassGuid**](https://msdn.microsoft.com/library/windows/hardware/ff542388) must be consistent with one another.

Direct modification of reserved properties could invalidate device installation state. For example, if the [**DEVPKEY\_Device\_DeviceDesc**](https://msdn.microsoft.com/library/windows/hardware/ff542407) is changed, system functionality (such as backup, driver rollback, and Windows Update) could break.

The following properties are read-only and can never be set with [**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163):

-   [**DEVPKEY\_Device\_Address**](https://msdn.microsoft.com/library/windows/hardware/ff542359)

-   [**DEVPKEY\_Device\_BusNumber**](https://msdn.microsoft.com/library/windows/hardware/ff542364)

-   [**DEVPKEY\_Device\_BusTypeGuid**](https://msdn.microsoft.com/library/windows/hardware/ff542371)

-   [**DEVPKEY\_Device\_Capabilities**](https://msdn.microsoft.com/library/windows/hardware/ff542373)

-   [**DEVPKEY\_Device\_EnumeratorName**](https://msdn.microsoft.com/library/windows/hardware/ff542489)

-   [**DEVPKEY\_Device\_LegacyBusType**](https://msdn.microsoft.com/library/windows/hardware/ff542541)

-   [**DEVPKEY\_Device\_PDOName**](https://msdn.microsoft.com/library/windows/hardware/ff542580)

-   [**DEVPKEY\_Device\_PowerData**](https://msdn.microsoft.com/library/windows/hardware/ff542586)

-   [**DEVPKEY\_Device\_RemovalPolicy**](https://msdn.microsoft.com/library/windows/hardware/ff542597)

-   [**DEVPKEY\_Device\_RemovalPolicyDefault**](https://msdn.microsoft.com/library/windows/hardware/ff542603)

-   [**DEVPKEY\_Device\_UINumber**](https://msdn.microsoft.com/library/windows/hardware/ff542660)

The following properties are writable. However, they are reserved for use by the operating system and must not be set directly:

-   [**DEVPKEY\_Device\_Class**](https://msdn.microsoft.com/library/windows/hardware/ff542385)

-   [**DEVPKEY\_Device\_ClassGuid**](https://msdn.microsoft.com/library/windows/hardware/ff542388)

-   [**DEVPKEY\_Device\_Driver**](https://msdn.microsoft.com/library/windows/hardware/ff542427)

-   [**DEVPKEY\_Device\_DriverDesc**](https://msdn.microsoft.com/library/windows/hardware/ff542436)

-   [**DEVPKEY\_Device\_Manufacturer**](https://msdn.microsoft.com/library/windows/hardware/ff542558)

**Note**  [*Class installers*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-class-installer) and [*co-installers*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-co-installer) must not change device properties except for the friendly name ([**DEVPKEY\_Device\_FriendlyName**](https://msdn.microsoft.com/library/windows/hardware/ff542502)) and the upper and lower filter drivers for the device ([**DEVPKEY\_Device\_UpperFilters**](https://msdn.microsoft.com/library/windows/hardware/ff542667) and [**DEVPKEY\_Device\_LowerFilters**](https://msdn.microsoft.com/library/windows/hardware/ff542554)). For more information, see [Accessing Device Instance Properties](accessing-device-instance-properties--windows-vista-and-later-.md).

 

 

 





