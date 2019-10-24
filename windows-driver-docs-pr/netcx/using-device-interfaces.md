---
title: Using Device Interfaces
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Using Device Interfaces

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

To receive IOCTLs from user mode, the client driver calls [**WdfDeviceCreateDeviceInterface**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreatedeviceinterface) with a reference string, as shown here:

```cpp
DECLARE_CONST_UNICODE_STRING(c_RefString, L"MyRefString");
status = WdfDeviceCreateDeviceInterface(
            device, 
            &GUID_MY_DEVICE_INTERFACE, 
            &c_RefString);
if (!NT_SUCCESS(status)) {
    return status;
}
```

When a user-mode application sends requests to a handle opened on a device interface with a reference string, your client driver receives the I/O requests.  You can use [WDF queue objects](../wdf/framework-queue-objects.md) to handle the incoming I/O requests.  If you do not provide a reference string, NDIS intercepts I/O requests sent to the device interface.

For more info, see [Using WDF Device Interfaces](../wdf/using-device-interfaces.md).
