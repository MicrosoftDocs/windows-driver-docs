---
title: Guidelines for Writing Dispatch(Internal)DeviceControl Routines
description: Guidelines for Writing Dispatch(Internal)DeviceControl Routines
ms.assetid: e64ab28e-2904-41c2-a262-405bc129b9bb
keywords: ["dispatch routines WDK kernel , DispatchDeviceControl routine", "dispatch routines WDK kernel , DispatchInternalDeviceControl routine", "DispatchDeviceControl routine", "DispatchInternalDeviceControl routine", "IRP_MJ_DEVICE_CONTROL I/O function code", "IRP_MJ_INTERNAL_DEVICE_CONTROL I/O function code", "internal device control dispatch routines WDK kernel", "device control dispatch routines WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Guidelines for Writing Dispatch(Internal)DeviceControl Routines





Keep the following points in mind when writing a [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287) or [*DispatchInternalDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543326) routine:

At a minimum, a higher-level driver must copy the parameters for an [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) or [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766) request from its own I/O stack location in the IRP to the next-lower-level driver's I/O stack location. Then, it must call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) with a pointer to the next-lower driver's device object and the IRP.

The higher-level driver should propagate the status value returned by **IoCallDriver** or set it in the returned IRP's I/O status block when it returns control for a request that lower drivers handle synchronously.

The underlying device driver must process device control requests unless it has a closely coupled class driver that completes a subset of these requests on its behalf. A device driver's *DispatchDeviceControl* routine usually begins processing these requests by turning on the **Parameters.DeviceIoControl.IoControlCode** in its I/O stack location of each IRP.

A lower-level device driver should check the parameters passed in with the request and fail the IRP with an appropriate error if any parameter is invalid. The most common check on the validity of parameters to these requests has the form:

```cpp
    if (Irp->Parameters.DeviceIoControl.InputBufferLength < 
            (sizeof(IOCTL_SPECIFIC_STRUCTURE))) { 
        status = STATUS_XXX;
```

or
```cpp
    if (Irp->Parameters.DeviceIoControl.OutputBufferLength < 
            (sizeof(IOCTL_SPECIFIC_STRUCTURE))) { 
        status = STATUS_XXX; 
```

where the status value set is one of STATUS\_BUFFER\_TOO\_SMALL or STATUS\_INVALID\_PARAMETER.
Every device driver's *DispatchDeviceControl* or *DispatchInternalDeviceControl* routine must handle the receipt of an unrecognized I/O control code by setting the I/O status block with an appropriate NTSTATUS value, setting its **Information** field to zero, and completing the IRP with a *PriorityBoost* of IO\_NO\_INCREMENT.

The particular I/O control codes a device driver handles must include any device-type-specific, system-defined I/O control codes for the same type of device. See the device-specific sections of the Windows Driver Kit (WDK) for more information about the system requirements for each type of device and the corresponding (Windows SDK) header files, each beginning with the prefix *ntdd*, for declarations of the system-defined structures for these I/O control codes.

The class driver of a closely coupled class/port driver pair can process and complete a subset of device control requests without passing them on to the underlying port driver. However, such a class driver must pass on all valid device control requests that require a change of state for the device and those that require the return of volatile information about the device, such as its current baud rate, volume, or video mode.

 

 




