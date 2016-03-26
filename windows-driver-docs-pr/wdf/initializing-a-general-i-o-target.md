---
title: Initializing a General I/O Target
description: Initializing a General I/O Target
ms.assetid: c5d5b589-09a3-4f58-83bf-2876b37b0937
keywords: ["general I/O targets WDK KMDF , initializing", "initializing general I/O targets WDK KMDF"]
---

# Initializing a General I/O Target


## <a href="" id="ddk-initializing-a-general-i-o-target-df"></a>


The framework initializes a driver's local I/O target for a device when the driver calls [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926). To retrieve a handle to a device's local I/O target, the driver calls [**WdfDeviceGetIoTarget**](https://msdn.microsoft.com/library/windows/hardware/ff546017).

Most drivers send requests only to their local I/O target.

To initialize a remote I/O target for a device, the driver must:

1.  Call [**WdfIoTargetCreate**](https://msdn.microsoft.com/library/windows/hardware/ff548591) to create an I/O target object.

2.  Call [**WdfIoTargetOpen**](https://msdn.microsoft.com/library/windows/hardware/ff548634) to open an I/O target so that the driver can send requests to it.

When the driver calls [**WdfIoTargetOpen**](https://msdn.microsoft.com/library/windows/hardware/ff548634), it typically identifies the remote I/O target by supplying a Unicode string that represents an [object name](https://msdn.microsoft.com/library/windows/hardware/ff557762). This name can identify a device, file, or device interface. The framework sends I/O requests to the top of the driver stack that supports the object name.

Rarely, a driver might identify a remote I/O target by supplying a pointer to a Windows Driver Model (WDM) [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) structure. This pointer identifies a different driver within the calling driver's stack. Framework-based drivers rarely use this technique because they rarely have access to other drivers' **DEVICE\_OBJECT** structures.

The following example shows how the Ndisedge sample driver uses the above technique to create and open a remote I/O target:

```
status = WdfIoTargetCreate(Adapter->WdfDevice,
                        WDF_NO_OBJECT_ATTRIBUTES,
                        &amp;Adapter->IoTarget);
    if (!NT_SUCCESS(status)) {
        DEBUGP(MP_ERROR, ("WdfIoTargetCreate failed 0x%x\n",
               status));
        return status;
    }

    WDF_IO_TARGET_OPEN_PARAMS_INIT_CREATE_BY_NAME(&amp;openParams,
                                &amp;fileName,
                                STANDARD_RIGHTS_ALL
                                );

    status = WdfIoTargetOpen(Adapter->IoTarget,
                        &amp;openParams);
    if (!NT_SUCCESS(status)) {
        DEBUGP(MP_ERROR, ("WdfIoTargetOpen failed 0x%x\n", status));
        return status;
    }
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Initializing%20a%20General%20I/O%20Target%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




