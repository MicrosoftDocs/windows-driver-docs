---
title: DispatchDeviceControl in Lowest-Level Drivers
description: DispatchDeviceControl in Lowest-Level Drivers
ms.assetid: 51caacd3-c9e0-450e-9060-f308ab46b5a0
keywords: ["dispatch routines WDK kernel , DispatchDeviceControl routine", "dispatch DispatchDeviceControl routine", "IRP_MJ_DEVICE_CONTROL I/O function code", "device control dispatch routines WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# DispatchDeviceControl in Lowest-Level Drivers





An [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) request for a lowest-level driver requires that the driver either change the state of its device or provide information about the state of its device. Because most kinds of drivers are required to handle a number of I/O control codes, their [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287) routines usually contain a **switch** statement somewhat like the following:

```cpp
    :    : 
switch (irpSp->Parameters.DeviceIoControl.IoControlCode)
{ 
    case IOCTL_DeviceType_XXX: 
    case IOCTL_DeviceType_YYY: 
        if (irpSp->Parameters.DeviceIoControl.InputBufferLength < 
                (sizeof(IOCTL_XXXYYY_STRUCTURE)))
        { 
            status = STATUS_BUFFER_TOO_SMALL; 
            break; 
        } else { 
            IoMarkIrpPending(Irp); 
     :    : // pass IRP on for further processing 
    case ... 
     :    :
```

As this code fragment shows, a *DispatchDeviceControl* routine also checks parameters, sometimes on each I/O control code that the driver must support, sometimes on groups of these I/O control codes.

Consider the following implementation guidelines for device drivers' *DispatchDeviceControl* routines:

-   *DispatchDeviceControl* must check the parameters for validity, and immediately complete IRPs with parameter errors, as described in [Completing IRPs](completing-irps.md).

-   Grouping I/O control codes in a **case** statement (where practical) when testing for valid parameters is economical in terms of driver performance and size and in code maintenance. As the preceding code fragment suggests, I/O control codes that use a common structure are natural candidates for such a **case** group.

-   Switching first on any I/O control codes for which the *DispatchDeviceControl* routine can satisfy and complete the IRP improves performance because the driver can return control faster.

-   Switching later on I/O control codes that specify infrequently requested operations also can improve the driver's performance in processing **IRP\_MJ\_DEVICE\_CONTROL** requests.

-   For better performance, every lowest-level device driver's *DispatchDeviceControl* routine should satisfy any device control request that it can, without queuing the IRP to other driver routines.

If the *DispatchDeviceControl* routine can complete the IRP, it should call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) with a *PriorityBoost* of IO\_NO\_INCREMENT. If the *DispatchDeviceControl* routine must queue the IRP for further processing, it must call [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422) and return STATUS\_PENDING.

 

 




