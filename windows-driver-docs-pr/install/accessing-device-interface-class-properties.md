---
title: Accessing Device Interface Class Properties
description: Accessing Device Interface Class Properties
ms.date: 04/05/2022
---

# Accessing Device Interface Class Properties

In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) includes device interface class properties that characterize a device interface class. The unified device property model uses [property keys](property-keys.md) to represent these properties. For information about how to use property keys to access device setup class properties in Windows Vista and later versions, see [Accessing Device Class Properties (Windows Vista and Later)](accessing-device-class-properties--windows-vista-and-later-.md).

Windows Server 2003, Windows XP, and Windows 2000 also support most of these device interface class properties. However, these earlier versions of Windows do not support the property keys of the unified device property model. Instead, you can represent and access the corresponding property information on these versions of Windows by using the following method.

## Accessing the Default Interface for a Device Interface Class

To retrieve the default interface for a device interface class, call [**SetupDiGetClassDevs**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsw) and supply the following parameter values:

-   Set *ClassGuid* to the GUID that represents the device interface class for which to retrieve the default interface.

-   Set *Enumerator* to **NULL**.

-   Set *hwndParent* to **NULL**.

-   Set *Flags* to (DIGCF_DEVICEINTERFACE | DIGCF_DEFAULT).

This call will return a device information set that contains a device information element. The device information element that is returned represents the device that supports the default interface for the specified device interface class.

To set the default interface for a device interface class, call [**SetupDiSetDeviceInterfaceDefault**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdeviceinterfacedefault) and supply the following parameters values:

-   Set *DeviceInfoSet* to a handle to the device information set that contains the device interface to set as the default for a device interface class.

-   Set *DeviceInterfaceData* to a pointer to an [**SP_DEVICE_INTERFACE_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_device_interface_data) structure that specifies the device interface in *DeviceInfoSet*.
