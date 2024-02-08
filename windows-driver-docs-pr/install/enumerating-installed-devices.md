---
title: Enumerate Installed Devices
description: Provides information about how to enumerate installed devices.
keywords:
- enumerate installed devices WDK
- installed devices WDK, enumerate
ms.date: 08/29/2022
---

# Enumerate installed devices

You should not enumerate devices by using registry keys directly. Registry keys do not contain the required information to enumerate installed devices on the system. This information, such as whether the device is actually present or is a phantom device (one that is not plugged in), is held by the [Plug and Play (PnP) manager](pnp-manager.md). The PnP manager also performs additional filtering of registry information.

To enumerate installed devices safely, follow these steps.

- Using [configuration manager](/windows/win32/api/cfgmgr32/) functions:

    1. Use [**CM_Get_Device_ID_List**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_id_listw) to retrieve a list of unique [device instance identifier (ID)](device-instance-ids.md) strings. To retrieve information only for devices that are present in the system, set CM_GETIDLIST_FILTER_PRESENT in the *ulFlags* parameter.

    1. You can use the unique device instance ID with [**CM_Locate_DevNode**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_locate_devnodew) to retrieve a *DEVINST* that represents the device to use with other configuration manager APIs.

- Using [SetupAPI](setupapi.md) functions:

    1. Use [**SetupDiGetClassDevs**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsw)  to retrieve information for a set of devices. To retrieve information only for devices that are present in the system, set DIGCF_PRESENT in the *Flags* parameter.

    1. Use [**SetupDiEnumDeviceInfo**](/windows/win32/api/setupapi/nf-setupapi-setupdienumdeviceinfo) to enumerate the devices in the set.

    1. You can use the *SP_DEVINFO_DATA* returned by **SetupDiEnumDeviceInfo** with other SetupApi APIs or use [**SetupDiGetDeviceInstanceId**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinstanceidw) to retrieve a unique [device instance identifier (ID)](device-instance-ids.md) for the device.
