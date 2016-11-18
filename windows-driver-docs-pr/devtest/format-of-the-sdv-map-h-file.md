---
title: Format of the Sdv-map.h File
description: Format of the Sdv-map.h File
ms.assetid: 1b9e2b8d-04b8-4288-9d63-e7d84d75a9c6
keywords: ["Sdv-map.h WDK Static Driver Verifier , formats", "formats WDK Static Driver Verifier"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Format%20of%20the%20Sdv-map.h%20File%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




