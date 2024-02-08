---
title: Accessing Device Interface Properties Before Windows Vista
description: Accessing Device Interface Properties before Windows Vista
ms.date: 04/05/2022
---

# Accessing Device Interface Properties before Windows Vista

In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) includes device interface properties that characterize a device interface. The unified device property model uses [property keys](property-keys.md) to represent these properties. For information about how to use property keys to access device setup class properties in Windows Vista and later versions, see [Accessing Device Interface Properties (Windows Vista and Later)](accessing-device-interface-properties--windows-vista-and-later-.md).

Windows Server 2003, Windows XP, and Windows 2000 support most of these device interface class properties. However, these earlier versions of Windows do not support the property keys of the unified device property model. Instead, these versions of Windows use the following mechanisms to represent and access device interface properties.

## Using SetupDiEnumDeviceInterfaces to Retrieve Information About a Device Interface

A way to retrieve information about a device interface on Windows Server 2003, Windows XP, and Windows 2000 is by calling [**SetupDiEnumDeviceInterfaces**](/windows/win32/api/setupapi/nf-setupapi-setupdienumdeviceinterfaces) to retrieve an [**SP_DEVICE_INTERFACE_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_device_interface_data) structure for the interface. An SP_DEVICE_INTERFACE_DATA structure contains the following information:

-   The **Flags** member indicates whether a device interface is active or removed, and whether the device is the default interface for the interface class.

-   The **InterfaceClassGuild** member identifies the interface class GUID.
