---
title: Accessing Device Setup Class Properties
description: Accessing Device Setup Class Properties
ms.date: 04/05/2022
---

# Accessing Device Setup Class Properties

In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) includes the following:
* Device setup class properties that correspond to the CM_CRP_Xxx identifiers that are defined in *cfgmgr32.h* or SPCRP_Xxx identifiers that are defined in *Setupapi.h*.
* Properties that do not have CM_CRP_Xxx or SPCRP_Xxx identifiers, but do have corresponding ways to query the values.

## Properties that correspond to CM_CRP_Xxx or SPCRP_Xxx identifiers

In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) supports the [device setup class](overview-of-device-setup-classes.md) properties that correspond to the CM_CRP_Xxx identifiers that are defined in *cfgmgr32.h* and the SPCRP_Xxx identifiers that are defined in *Setupapi.h*. These properties characterize a [device setup class](./overview-of-device-setup-classes.md). The unified device property model uses [property keys](property-keys.md) to represent these properties. Windows Server 2003, Windows XP, and Windows 2000 also support most of these device setup class properties. However, these earlier versions of Windows do not support the property keys of the unified device property model. Instead, these versions of Windows versions use the CM_CRP_*Xxx* or SPCRP_*Xxx* identifiers to represent and access the device setup class properties.

To maintain compatibility with earlier versions of Windows, Windows Vista and later versions also support using CM_CRP_Xxx or SPCRP_*Xxx* identifiers to access device setup class properties. However, you should use the property keys of the unified device property model to access device setup class properties.

For a list of the system-defined device setup class properties that have corresponding CM_CRP_Xxx or SPCRP_Xxx identifiers, see the following table.

|Unified property model property | CM_CRP_Xxx value | SPCRP_Xxx value |
| --- | --- | ---|
| [**DEVPKEY_DeviceClass_Security**](devpkey-deviceclass-security.md) | CM_CRP_SECURITY | SPCRP_SECURITY |
| [**DEVPKEY_DeviceClass_SecuritySDS**](devpkey-deviceclass-securitysds.md) | CM_CRP_SECURITY_SDS | SPCRP_SECURITY_SDS |
| [**DEVPKEY_DeviceClass_DevType**](devpkey-deviceclass-devtype.md) | CM_CRP_DEVTYPE | SPCRP_DEVTYPE |
| [**DEVPKEY_DeviceClass_Exclusive**](devpkey-deviceclass-exclusive.md) | CM_CRP_EXCLUSIVE | SPCRP_EXCLUSIVE |
| [**DEVPKEY_DeviceClass_Characteristics**](devpkey-deviceclass-characteristics.md) | CM_CRP_CHARACTERISTICS | SPCRP_CHARACTERISTICS |

For information about how to access device setup class properties in Windows Vista and later versions, see [Accessing Device Class Properties (Windows Vista and Later)](accessing-device-class-properties--windows-vista-and-later-.md).

### Accessing a Device Setup Class Property

To access device setup class properties that correspond to the CM_CRP_*Xxx* or SPCRP_*Xxx* identifiers on Windows Server 2003, Windows XP, and Windows 2000, use the following functions:

-   [**CM_Get_Class_Registry_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_class_registry_propertyw) or [**SetupDiGetClassRegistryProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassregistrypropertyw) to retrieve a property.

-   [**CM_Set_Class_Registry_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_set_class_registry_propertyw) or [**SetupDiSetClassRegistryProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetclassregistrypropertyw) to set a property.

## Properties that do not have CM_CRP_Xxx or SPCRP_Xxx identifiers

For information about how to access the corresponding device setup class properties on Windows Server 2003, Windows XP, and Windows 2000, see the following topics:

[Accessing the Friendly Name and Class Name of a Device Setup Class](accessing-the-friendly-name-and-class-name-of-a-device-setup-class.md)

[Accessing Icon Properties of a Device Setup Class](accessing-icon-properties-of-a-device-setup-class.md)
