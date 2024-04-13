---
title: Accessing Device Instance Properties
description: Accessing Device Instance Properties
ms.date: 04/04/2022
---

# Accessing Device Instance Properties

In Windows Vista and later versions of Windows, applications and installers can access [device instance properties](/previous-versions/ff541334(v=vs.85)) that are part of the [unified property model](unified-device-property-model--windows-vista-and-later-.md) by calling the following functions.

> [!NOTE]
> SetupApi is not supported on all editions of Windows.  When possible, you should use lower layer APIs such as those available via [CfgMgr32.dll](/windows/win32/api/cfgmgr32/). See [Porting from SetupApi to CfgMgr32](porting-from-setupapi-to-cfgmgr32.md) for tips.

For information about how to access device properties on Windows Server 2003, Windows XP, and Windows 2000, see [Using SetupAPI and Configuration Manager to Access Device Properties](using-setupapi-and-configuration-manager-to-access-device-properties.md).

## Retrieving properties

Property APIs such as [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) can be used to retrieve a device property that is set for a device instance.  For example, here is a sample that is retrieving a property that is expected to be of type DEVPROP_TYPE_UINT32:

```cpp
DEVPROPTYPE PropertyType = DEVPROP_TYPE_EMPTY;
ULONG PropertySize = 0;
ULONG SomeValue = 0;

PropertySize = sizeof(SomeValue);
cr = CM_Get_DevNode_Property(DevInst,
                             &DEVPKEY_CustomProperty,
                             &PropertyType,
                             (PBYTE)&SomeValue,
                             &PropertySize,
                             0);

if (cr == CR_NO_SUCH_VALUE) {
    printf("Property was not found\n");
} else if (cr != CR_SUCCESS) {
    printf("Error 0x%08x retrieving property.\n", cr);
} else if ((PropertyType != DEVPROP_TYPE_UINT32) || (PropertySize != sizeof(SomeValue))) {
    printf("Property data was not of the expected type or size\n");
} else {
    printf("Property value: 0x%08x\n", SomeValue);
}
```

## Setting properties

Property APIs such as [**CM_Set_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_set_devnode_propertyw) or [**SetupDiSetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdevicepropertyw) can be used to set a device property for a device instance.  For example, here is a sample that is setting a property of type DEVPROP_TYPE_UINT32:

```cpp
ULONG SomeValue = 5;
cr = CM_Set_DevNode_Property(DevInst,
                             &DEVPKEY_CustomProperty,
                             DEVPROP_TYPE_UINT32,
                             (PBYTE)&SomeValue,
                             sizeof(SomeValue),
                             0);

if (cr != CR_SUCCESS) {
    printf("Error 0x%08x setting property.\n", cr);
}
```

## Getting a list of available properties

Property APIs such as [**CM_Get_DevNode_Property_Keys**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_property_keys) or [**SetupDiGetDevicePropertyKeys**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertykeys) can be used to retrieve an array of the device property keys that identify the device properties that are currently set for a device instance. This can be used to determine the full set of properties set on a device. However, use of these functions, especially to then subsequently retrieve the value of all properties that these functions indicate are set on the device instance, should be used sparingly since the retrieval of the list of all properties and their values can be an expensive operation.


