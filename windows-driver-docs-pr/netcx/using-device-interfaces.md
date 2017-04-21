---
title: Using Device Interfaces
---

# Using Device Interfaces

To receive IOCTLs from user mode, the client driver calls [**WdfDeviceCreateDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff545935) with a reference string, as shown here:

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

When an user-mode application sends requests to a handle opened on a device interface with a reference string, your client driver receives the I/O requests.  You can use [WDF queue objects](../wdf/framework-queue-objects.md) to handle the incoming I/O requests. If your device interface does not have a reference string, all the requests will be intercepted by NDIS.

For more info, see [Using WDF Device Interfaces](../wdf/using-device-interfaces.md).
