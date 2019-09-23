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


Many [device properties](device-properties.md) have complex dependencies on other properties or device state. For example, the values of [**DEVPKEY_Device_Class**](https://docs.microsoft.com/windows-hardware/drivers/install/devpkey-device-class) and [**DEVPKEY_Device_ClassGuid**](https://docs.microsoft.com/windows-hardware/drivers/install/devpkey-device-classguid) must be consistent with one another.

Direct modification of reserved properties could invalidate device installation state. For example, if the [**DEVPKEY_Device_DeviceDesc**](https://docs.microsoft.com/windows-hardware/drivers/install/devpkey-device-devicedesc) is changed, system functionality (such as backup, driver rollback, and Windows Update) could break.

The following properties are read-only and can never be set with [**SetupDiSetDeviceProperty**](https://docs.microsoft.com/windows/desktop/api/setupapi/nf-setupapi-setupdisetdevicepropertyw):

-   [**DEVPKEY_Device_Address**](https://docs.microsoft.com/windows-hardware/drivers/install/devpkey-device-address)

-   [**DEVPKEY_Device_BusNumber**](https://docs.microsoft.com/windows-hardware/drivers/install/devpkey-device-busnumber)

-   [**DEVPKEY_Device_BusTypeGuid**](https://docs.microsoft.com/windows-hardware/drivers/install/devpkey-device-bustypeguid)

-   [**DEVPKEY_Device_Capabilities**](https://docs.microsoft.com/windows-hardware/drivers/install/devpkey-device-capabilities)

-   [**DEVPKEY_Device_EnumeratorName**](https://docs.microsoft.com/windows-hardware/drivers/install/devpkey-device-enumeratorname)

-   [**DEVPKEY_Device_LegacyBusType**](https://docs.microsoft.com/windows-hardware/drivers/install/devpkey-device-legacybustype)

-   [**DEVPKEY_Device_PDOName**](https://docs.microsoft.com/windows-hardware/drivers/install/devpkey-device-pdoname)

-   [**DEVPKEY_Device_PowerData**](https://docs.microsoft.com/windows-hardware/drivers/install/devpkey-device-powerdata)

-   [**DEVPKEY_Device_RemovalPolicy**](https://docs.microsoft.com/windows-hardware/drivers/install/devpkey-device-removalpolicy)

-   [**DEVPKEY_Device_RemovalPolicyDefault**](https://docs.microsoft.com/windows-hardware/drivers/install/devpkey-device-removalpolicydefault)

-   [**DEVPKEY_Device_UINumber**](https://docs.microsoft.com/windows-hardware/drivers/install/devpkey-device-uinumber)

The following properties are writable. However, they are reserved for use by the operating system and must not be set directly:

-   [**DEVPKEY_Device_Class**](https://docs.microsoft.com/windows-hardware/drivers/install/devpkey-device-class)

-   [**DEVPKEY_Device_ClassGuid**](https://docs.microsoft.com/windows-hardware/drivers/install/devpkey-device-classguid)

-   [**DEVPKEY_Device_Driver**](https://docs.microsoft.com/windows-hardware/drivers/install/devpkey-device-driver)

-   [**DEVPKEY_Device_DriverDesc**](https://docs.microsoft.com/windows-hardware/drivers/install/devpkey-device-driverdesc)

-   [**DEVPKEY_Device_Manufacturer**](https://docs.microsoft.com/windows-hardware/drivers/install/devpkey-device-manufacturer)

**Note**  *Class installers* and *co-installers* must not change device properties except for the friendly name ([**DEVPKEY_Device_FriendlyName**](https://docs.microsoft.com/windows-hardware/drivers/install/devpkey-device-friendlyname)) and the upper and lower filter drivers for the device ([**DEVPKEY_Device_UpperFilters**](https://docs.microsoft.com/windows-hardware/drivers/install/devpkey-device-upperfilters) and [**DEVPKEY_Device_LowerFilters**](https://docs.microsoft.com/windows-hardware/drivers/install/devpkey-device-lowerfilters)). For more information, see [Accessing Device Instance Properties](accessing-device-instance-properties--windows-vista-and-later-.md).

 

 

 





