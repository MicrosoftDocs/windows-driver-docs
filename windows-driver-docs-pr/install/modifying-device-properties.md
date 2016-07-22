---
title: Rules for Modifying Device Properties
description: Rules for Modifying Device Properties
ms.assetid: EB554B5C-310A-4b2c-A2D5-22A113415400
keywords: ["device properties WDK device installations , rules for modifying", "device properties WDK device installations , modifying", "modifying device properties WDK device installations"]
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Rules%20for%20Modifying%20Device%20Properties%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




