---
title: Accessing Device Interface Properties
description: Accessing Device Interface Properties
ms.date: 04/04/2022
---

# Accessing Device Interface Properties

In Windows Vista and later versions of Windows, applications and installers can access [device interface properties](/previous-versions/ff541409(v=vs.85)) by calling the following functions.

> [!NOTE]
> SetupApi is not supported on all editions of Windows.  When possible, you should use lower layer APIs such as those available via [CfgMgr32.dll](/windows/win32/api/cfgmgr32/). See [Porting from SetupApi to CfgMgr32](porting-from-setupapi-to-cfgmgr32.md) for tips.

For information about how to access device interface properties on Windows Server 2003, Windows XP, and Windows 2000, see Accessing Device Interface Properties.

## Retrieving properties

Property APIs such as [**CM_Get_Device_Interface_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_propertyw) or [**SetupDiGetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertyw) can be used to retrieve a device interface property.

## Setting properties

Property APIs such as [**CM_Set_Device_Interface_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_set_device_interface_propertyw) or [**SetupDiSetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdeviceinterfacepropertyw) can be used to set a device interface property.

## Getting a list of available properties

Property APIs such as [**CM_Get_Device_Interface_Property_Keys**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_property_keysw) or [**SetupDiGetDeviceInterfacePropertyKeys**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertykeys) can be used to retrieve an array of the property keys that identify the properties that are currently set for a device interface. This can be used to determine the full set of properties set on a device interface. However, use of these functions, especially to then subsequently retrieve the value of all properties that these functions indicate are set on the device interface, should be used sparingly since the retrieval of the list of all properties and their values can be an expensive operation.