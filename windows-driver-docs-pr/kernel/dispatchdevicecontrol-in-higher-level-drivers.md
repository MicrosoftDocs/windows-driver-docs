---
title: DispatchDeviceControl in Higher-Level Drivers
description: DispatchDeviceControl in Higher-Level Drivers
ms.assetid: baff49c4-8764-4b65-84f4-ce5e10d51ed2
keywords: ["dispatch routines WDK kernel , DispatchDeviceControl routine", "dispatch DispatchDeviceControl routine", "IRP_MJ_DEVICE_CONTROL I/O function code", "device control dispatch routines WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# DispatchDeviceControl in Higher-Level Drivers





Usually, the [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287) routine of a higher-level driver simply sets up the I/O stack location for the next-lower-level driver and passes the IRP on with [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336). The *DispatchDeviceControl* routine seldom checks the validity of parameters in the input IRP because the underlying device driver is assumed to have better information about how to handle each device-type-specific I/O control request.

A possible exception to this general rule is the *DispatchDeviceControl* routine in the class driver of a class/port driver pair. For more information about handling device control requests in paired class/port drivers, see [Dispatch(Internal)DeviceControl in Class/Port Drivers](dispatch-internal-devicecontrol-in-class-port-drivers.md).

Any new higher-level driver that is not closely associated with a particular device driver should simply set up the [I/O stack location](i-o-stack-locations.md) for the next-lower-level driver and pass the [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) request on for further processing.

A device control request is usually handled synchronously. That is, a higher-level driver's *DispatchDeviceControl* routine can frequently return control to the system as follows:

```cpp
        :    : 
    return IoCallDriver(DeviceObject->NextDeviceObject, Irp);
```

However, a higher-level driver cannot use the preceding technique if a lower driver might return STATUS\_PENDING for such a request. In that case, the higher-level driver should call [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679) to register an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine. When the *IoCompletion* routine is called, it can check the I/O status block to determine whether the IRP is still pending. If it is, the *IoCompletion* routine might retry the request or, possibly, call [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422) before it calls [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) and returns STATUS\_PENDING. A higher-level driver must not complete an IRP with STATUS\_PENDING unless it has called **IoMarkIrpPending** for that IRP first.

If the underlying device driver must process much data transferred from the device before it completes the request, then a higher-level driver might handle such a device control request asynchronously. That is, the higher-level driver might call [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679) to register an *IoCompletion* routine, pass the IRP on to lower drivers, and return control from its own *DispatchDeviceControl* routine.

Almost all system-defined I/O control codes require the underlying device driver to transfer only modest amounts of data, usually much less than a PAGE\_SIZE amount. As a general rule, higher-level drivers should handle these requests synchronously, as shown in the preceding code fragment, because the lower drivers return control so quickly. That is, the overhead of calling the higher-level driver's *IoCompletion* routine does not compensate for whatever additional IRP processing that driver can get done in such a short interval.

A higher-level driver that allocates IRPs with [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318) for an underlying device driver can handle these device control requests synchronously. The higher-level driver can wait for an optional event object to be passed to **IoBuildDeviceIoControlRequest** and associated with the driver-allocated IRP.

 

 




