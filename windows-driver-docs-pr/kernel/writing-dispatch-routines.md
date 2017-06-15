---
title: Writing Dispatch Routines
author: windows-driver-content
description: Writing Dispatch Routines
MS-HAID:
- 'DrvComps\_789564ee-c57a-4b5c-841f-ef40bee3c23e.xml'
- 'kernel.writing\_dispatch\_routines'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 84eb9372-2ef7-4cc2-94af-97e3399e69e0
keywords: ["dispatch routines WDK kernel", "standard driver routines WDK kernel , dispatch routines", "driver routines WDK kernel , dispatch routines", "routines WDK kernel , dispatch routines", "system-space memory allocations WDK kernel", "system resource storage WDK kernel", "storing system resources", "dispatch routines WDK kernel , about dispatch routines", "IRPs WDK kernel , dispatch routines", "multiple I/O function codes WDK kernel", "IRP major function codes WDK kernel", "major function codes WDK kernel", "function codes WDK kernel"]
---

# Writing Dispatch Routines


## <a href="" id="ddk-writing-dispatch-routines-kg"></a>


Processing any I/O request packet (IRP) begins in a dispatch routine that the driver registers to handle an [IRP major function code](https://msdn.microsoft.com/library/windows/hardware/ff550710) (**IRP\_MJ\_*XXX***). The driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine exports entry points for dispatch routines in a dispatch table within the driver's [**DRIVER\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff544174) structure.

A driver can provide a separate dispatch routine for each major I/O function code that it handles. Alternatively, dispatch routines can be written to handle multiple I/O function codes.

This section contains the following topics:

[Dispatch Routine Functionality](dispatch-routine-functionality.md)

[Required Dispatch Routines](required-dispatch-routines.md)

[Optional Dispatch Routines](optional-dispatch-routines.md)

[Dispatch Routines and IRQLs](dispatch-routines-and-irqls.md)

[When to Check the Driver's I/O Stack Location](when-to-check-the-driver-s-i-o-stack-location.md)

[DispatchCreate, DispatchClose, and DispatchCreateClose Routines](dispatchcreate--dispatchclose--and-dispatchcreateclose-routines.md)

[DispatchCleanup Routines](dispatchcleanup-routines.md)

[DispatchRead, DispatchWrite, and DispatchReadWrite Routines](dispatchread--dispatchwrite--and-dispatchreadwrite-routines.md)

[DispatchDeviceControl and DispatchInternalDeviceControl Routines](dispatchdevicecontrol-and-dispatchinternaldevicecontrol-routines.md)

[DispatchPnP Routines](dispatchpnp-routines.md)

[DispatchPower Routines](dispatchpower-routines.md)

[DispatchQueryInformation Routines](dispatchqueryinformation-routines.md)

[DispatchSetInformation Routines](dispatchsetinformation-routines.md)

[DispatchFlushBuffers Routines](dispatchflushbuffers-routines.md)

[DispatchShutdown Routines](dispatchshutdown-routines.md)

[DispatchSystemControl Routines](dispatchsystemcontrol-routines.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Writing%20Dispatch%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


