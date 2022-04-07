---
title: Accessing Device Class Properties
description: Accessing Device Class Properties
ms.date: 04/04/2022
---

# Accessing Device Class Properties

In Windows Vista and later versions of Windows, applications and installers can access [device setup class properties](/previous-versions/ff542239(v=vs.85)) and [device interface class properties](/previous-versions/ff541406(v=vs.85)) by calling the following functions.

> [!NOTE]
> SetupApi is not supported on all editions of Windows.  When possible, you should use lower layer APIs such as those available via [CfgMgr32.dll](/windows/win32/api/cfgmgr32/). See [Porting from SetupApi to CfgMgr32](porting-from-setupapi-to-cfgmgr32.md) for tips.

For information about how to access device class properties on Windows Server 2003, Windows XP, and Windows 2000, see [Accessing Device Setup Class Properties](accessing-device-setup-class-properties.md) and [Accessing Device Interface Class Properties](accessing-device-interface-class-properties.md).

## Retrieving properties

Property APIs such as [**CM_Get_Class_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_class_propertyw) or [**SetupDiGetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyw) can be used to retrieve a class property for a device setup class or a device interface class.

## Setting properties

Property APIs such as [**CM_Set_Class_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_set_class_propertyw) or [**SetupDiSetClassProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetclasspropertyw) can be used to set a class property for a device setup class or device interface class.

## Getting a list of available properties

Property APIs such as [**CM_Get_Class_Property_Keys**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_class_property_keys) or [**SetupDiGetClassPropertyKeys**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertykeys) can be used to retrieve an array of the property keys that identify the properties that are currently set for a device setup class or device interface class. This can be used to determine the full set of properties set on a class. However, use of these functions, especially to then subsequently retrieve the value of all properties that these functions indicate are set on the class, should be used sparingly since the retrieval of the list of all properties and their values can be an expensive operation.
