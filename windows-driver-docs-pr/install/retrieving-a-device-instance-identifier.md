---
title: Retrieving a Device Instance Identifier
description: Retrieving a Device Instance Identifier
ms.date: 04/05/2022
---

# Retrieving a Device Instance Identifier

In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) supports a device property that represents the device instance identifier. The unified device property model uses the [**DEVPKEY_Device_InstanceId**](./devpkey-device-instanceid.md) [property key](property-keys.md) to represent this property.

Windows Server 2003, Windows XP, and Windows 2000 also support this property. However, these earlier Windows versions do not support the property key of the unified device property model. Instead, you can retrieve a device instance identifier on these earlier versions of Windows by calling [**CM_Get_Device_ID**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_idw) or [**SetupDiGetDeviceInstanceId**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinstanceidw). To maintain compatibility with these earlier versions of Windows, Windows Vista and later versions also support **CM_Get_Device_ID** and **SetupDiGetDeviceInstanceId**. However, you should use the corresponding property key to access this property on Windows Vista and later.

For information about how to use property keys to access device driver properties on Windows Vista and later versions, see [Accessing Device Instance Properties (Windows Vista and Later)](accessing-device-instance-properties--windows-vista-and-later-.md).

To retrieve a device instance identifier on Windows Server 2003, Windows XP, and Windows 2000, see the following examples.

Device instance identifier strings must be less than `MAX_DEVICE_ID_LEN` characters (including NULL) which is defined in *cfgmgr32.h*. You can use that assumption to query the device instance identifier with code like:

```cpp
WCHAR DeviceInstancePath[MAX_DEVICE_ID_LEN];

cr = CM_Get_Device_ID(DevInst,
                      DeviceInstancePath,
                      sizeof(DeviceInstancePath)/sizeof(DeviceInstancePath[0]),
                      0);

if (cr != CR_SUCCESS) {
    printf("Error 0x%08x retrieving device instance path.\n", cr);
} else {
    printf("Device instance path is %ws.\n", DeviceInstancePath);
}
```

or alternatively, if you want your buffer to be dynamically sized:

```cpp
ULONG DeviceInstancePathLength = 0;
PWSTR DeviceInstancePath = NULL;

cr = CM_Get_Device_ID_Size(&DeviceInstancePathLength,
                           DevInst,
                           0);

if (cr != CR_SUCCESS) {
    printf("Error 0x%08x retrieving device instance path size.\n", cr);
} else {
    DeviceInstancePath = (PWSTR)malloc(DeviceInstancePathLength * sizeof(WCHAR));

    if (DeviceInstancePath != NULL) {
        cr = CM_Get_Device_ID(DevInst,
                              DeviceInstancePath,
                              DeviceInstancePathLength,
                              0);

        if (cr != CR_SUCCESS) {
            printf("Error 0x%08x retrieving device instance path.\n", cr);
        } else {
            printf("Device instance path is %ws.\n", DeviceInstancePath);
        }
    }
}

```
