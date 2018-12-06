---
title: Format of the Sdv-map.h File
description: Format of the Sdv-map.h File
ms.assetid: 1b9e2b8d-04b8-4288-9d63-e7d84d75a9c6
keywords:
- Sdv-map.h WDK Static Driver Verifier , formats
- formats WDK Static Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Format of the Sdv-map.h File


The Sdv-map.h file lists all of the function role types that have been declared in the driver and their associated callback functions and driver entry points.

The following shows the approved Sdv-map.h file for the KMDF sample driver, Fail\_Driver3.

```
//Approved=true
#define fun_WDF_DRIVER_DEVICE_ADD EvtDriverDeviceAdd
#define fun_WDF_IO_QUEUE_IO_READ EvtIoRead
#define fun_WDF_IO_QUEUE_IO_STOP EvtIoStop
#define fun_WDF_TIMER_1 EvtTimerFunc
#define fun_WDF_DRIVER_UNLOAD EvtDriverUnload
#define fun_WDF_REQUEST_CANCEL_1 EvtRequestCancel
#define fun_DriverEntry DriverEntry
#define fun_WDF_DEVICE_D0_ENTRY DeviceD0Entry
#define fun_WDF_IO_QUEUE_IO_WRITE EvtIoWrite
#define fun_WDF_IO_QUEUE_IO_DEVICE_CONTROL EvtIoDeviceControl
```

When SDV finds an entry point, it creates a **\#define** directive in the following format:

```
#define fun_Function_RoleType EntryPoint
```

 

 





