---
title: Initializing a General I/O Target
description: Initializing a General I/O Target
keywords:
- general I/O targets WDK KMDF , initializing
- initializing general I/O targets WDK KMDF
ms.date: 04/20/2017
---

# Initializing a General I/O Target





The framework initializes a driver's local I/O target for a device when the driver calls [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate). To retrieve a handle to a device's local I/O target, the driver calls [**WdfDeviceGetIoTarget**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicegetiotarget).

Most drivers send requests only to their local I/O target.

To initialize a remote I/O target for a device, the driver must:

1.  Call [**WdfIoTargetCreate**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetcreate) to create an I/O target object.

2.  Call [**WdfIoTargetOpen**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetopen) to open an I/O target so that the driver can send requests to it.

When the driver calls [**WdfIoTargetOpen**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetopen), it typically identifies the remote I/O target by supplying a Unicode string that represents an [object name](../kernel/object-names.md). This name can identify a device, file, or device interface. The framework sends I/O requests to the top of the driver stack that supports the object name.

Rarely, a driver might identify a remote I/O target by supplying a pointer to a Windows Driver Model (WDM) [**DEVICE\_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_object) structure. This pointer identifies a different driver within the calling driver's stack. Framework-based drivers rarely use this technique because they rarely have access to other drivers' **DEVICE\_OBJECT** structures.

The following example shows how the Ndisedge sample driver uses the above technique to create and open a remote I/O target:

```cpp
status = WdfIoTargetCreate(Adapter->WdfDevice,
                        WDF_NO_OBJECT_ATTRIBUTES,
                        &Adapter->IoTarget);
    if (!NT_SUCCESS(status)) {
        DEBUGP(MP_ERROR, ("WdfIoTargetCreate failed 0x%x\n",
               status));
        return status;
    }

    WDF_IO_TARGET_OPEN_PARAMS_INIT_CREATE_BY_NAME(&openParams,
                                &fileName,
                                STANDARD_RIGHTS_ALL
                                );

    status = WdfIoTargetOpen(Adapter->IoTarget,
                        &openParams);
    if (!NT_SUCCESS(status)) {
        DEBUGP(MP_ERROR, ("WdfIoTargetOpen failed 0x%x\n", status));
        return status;
    }
```

 

