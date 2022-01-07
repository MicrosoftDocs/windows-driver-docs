---
title: Enumerating Installed Devices
description: Enumerating Installed Devices
keywords:
- enumerating installed devices WDK
- installed devices WDK , enumerating
ms.date: 04/20/2017
---

# Enumerating Installed Devices


You should not enumerate devices by using registry keys directly. Registry keys do not contain the required information to enumerate installed devices on the system. This information, such as whether the device is actually present or is a phantom device (one that is not plugged in), is held by the [Plug and Play (PnP) manager](pnp-manager.md). The PnP manager also performs additional filtering of registry information.

To enumerate installed devices safely, follow these steps:

1.  Use [**SetupDiGetClassDevs**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsw) or [**SetupDiGetClassDevsEx**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsexa) to retrieve information for a set of devices that belong to a specified device setup class. To retrieve information only for devices that are present in the system, set DIGCF_PRESENT in the *Flags* parameter.

2.  Use [**SetupDiEnumDeviceInfo**](/windows/win32/api/setupapi/nf-setupapi-setupdienumdeviceinfo) to enumerate the devices in the set.

3.  Use [**SetupDiGetDeviceInstanceId**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinstanceida) to retrieve unique [device instance identifiers (IDs)](device-instance-ids.md).

 

