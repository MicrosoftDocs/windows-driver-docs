---
title: Accessing Device Instance Properties (Prior to Windows Vista)
description: Accessing Device Instance SPDRP_Xxx Properties
ms.date: 04/04/2022
---

# Accessing Device Instance Properties (Prior to Windows Vista)

In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) supports the device instance properties that correspond to the CM_DRP_Xxx identifiers that are defined in *cfgmgr32.h* and the SPDRP_Xxx identifiers that are defined in *Setupapi.h*. These properties characterize the configuration of a device instance. The unified device property model uses [property keys](property-keys.md) to represent these properties. Windows Server 2003, Windows XP, and Windows 2000 also support these device properties. However, these earlier versions of Windows do not support the property keys of the unified device property model. Instead, these earlier Windows versions use the CM_DRP_*Xxx* or SPDRP_*Xxx* identifiers to represent and access the device instance properties.

To maintain compatibility with these earlier versions of Windows, Windows Vista and later versions also support using CM_DRP_Xxx or SPDRP_Xxx identifiers to access device instance properties. However, you should use the corresponding property keys to access these properties on Windows Vista and later versions of Windows.

For a list of the system-defined device instance properties that have corresponding CM_DRP_Xxx or SPDRP_Xxx identifiers, see the following table.

|Unified property model property | CM_DRP_Xxx value | SPDRP_Xxx value |
| --- | --- | ---|
| [**DEVPKEY_Device_DeviceDesc**](devpkey-device-devicedesc.md) | CM_DRP_DEVICEDESC | SPDRP_DEVICEDESC |
| [**DEVPKEY_Device_HardwareIds**](devpkey-device-hardwareids.md) | CM_DRP_HARDWAREID | SPDRP_HARDWAREID |
| [**DEVPKEY_Device_CompatibleIds**](devpkey-device-compatibleids.md) | CM_DRP_COMPATIBLEIDS | SPDRP_COMPATIBLEIDS |
| [**DEVPKEY_Device_Service**](devpkey-device-service.md) | CM_DRP_SERVICE | SPDRP_SERVICE |
| [**DEVPKEY_Device_Class**](devpkey-device-class.md) | CM_DRP_CLASS | SPDRP_CLASS |
| [**DEVPKEY_Device_ClassGuid**](devpkey-device-classguid.md) | CM_DRP_CLASSGUID | SPDRP_CLASSGUID |
| [**DEVPKEY_Device_ConfigFlags**](devpkey-device-configflags.md) | CM_DRP_CONFIGFLAGS | SPDRP_CONFIGFLAGS |
| [**DEVPKEY_Device_Manufacturer**](devpkey-device-manufacturer.md) | CM_DRP_MFG | SPDRP_MFG |
| [**DEVPKEY_Device_FriendlyName**](devpkey-device-friendlyname.md) | CM_DRP_FRIENDLYNAME | SPDRP_FRIENDLYNAME |
| [**DEVPKEY_Device_LocationInfo**](devpkey-device-locationinfo.md) | CM_DRP_LOCATION_INFORMATION | SPDRP_LOCATION_INFORMATION |
| [**DEVPKEY_Device_PDOName**](devpkey-device-pdoname.md) | CM_DRP_PHYSICAL_DEVICE_OBJECT_NAME | SPDRP_PHYSICAL_DEVICE_OBJECT_NAME |
| [**DEVPKEY_Device_Capabilities**](devpkey-device-capabilities.md) | CM_DRP_CAPABILITIES | SPDRP_CAPABILITIES |
| [**DEVPKEY_Device_UINumber**](devpkey-device-uinumber.md) | CM_DRP_UI_NUMBER | SPDRP_UI_NUMBER |
| [**DEVPKEY_Device_BusTypeGuid**](devpkey-device-bustypeguid.md) | CM_DRP_BUSTYPEGUID | SPDRP_BUSTYPEGUID |
| [**DEVPKEY_Device_LegacyBusType**](devpkey-device-legacybustype.md)] | CM_DRP_LEGACYBUSTYPE | SPDRP_LEGACYBUSTYPE |
| [**DEVPKEY_Device_BusNumber**](devpkey-device-busnumber.md) | CM_DRP_BUSNUMBER | SPDRP_BUSNUMBER |
| [**DEVPKEY_Device_EnumeratorName**](devpkey-device-enumeratorname.md) | CM_DRP_ENUMERATOR_NAME | SPDRP_ENUMERATOR_NAME |
| [**DEVPKEY_Device_Security**](devpkey-device-security.md) | CM_DRP_SECURITY | SPDRP_SECURITY |
| [**DEVPKEY_Device_SecuritySDS**](devpkey-device-securitysds.md) | CM_DRP_SECURITY_SDS | SPDRP_SECURITY_SDS |
| [**DEVPKEY_Device_DevType**](devpkey-device-devtype.md) | CM_DRP_DEVTYPE | SPDRP_DEVTYPE |
| [**DEVPKEY_Device_Exclusive**](devpkey-device-exclusive.md) | CM_DRP_EXCLUSIVE | SPDRP_EXCLUSIVE |
| [**DEVPKEY_Device_Characteristics**](devpkey-device-characteristics.md) | CM_DRP_CHARACTERISTICS | SPDRP_CHARACTERISTICS |
| [**DEVPKEY_Device_Address**](devpkey-device-address.md) | CM_DRP_ADDRESS | SPDRP_ADDRESS |


For information about how to use property keys to access device instance properties in Windows Vista and later versions of Windows, see [Accessing Device Instance Properties (Windows Vista and Later)](accessing-device-instance-properties--windows-vista-and-later-.md).

## Accessing a Device Property

To access device instance properties that correspond to the CM_DRP_*Xxx* or SPDRP_*Xxx* identifiers on Windows Server 2003, Windows XP, and Windows 2000, use the following functions:

-   [**CM_Get_DevNode_Registry_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_registry_propertyw) or [**SetupDiGetDeviceRegistryProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceregistrypropertya) to retrieve a property.

-   [**CM_Set_DevNode_Registry_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_set_devnode_registry_propertyw) or [**SetupDiSetDeviceRegistryProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdeviceregistrypropertya) to set a property.
