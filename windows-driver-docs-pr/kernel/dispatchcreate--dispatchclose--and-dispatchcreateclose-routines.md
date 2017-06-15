---
title: DispatchCreate, DispatchClose, and DispatchCreateClose Routines
author: windows-driver-content
description: DispatchCreate, DispatchClose, and DispatchCreateClose Routines
MS-HAID:
- 'DrvComps\_9dfccb26-a4e0-441a-9c8e-7d73de9b1654.xml'
- 'kernel.dispatchcreate\_\_dispatchclose\_\_and\_dispatchcreateclose\_routines'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5c1c0036-71b1-4410-b157-f9ebe3b6ecfc
keywords: ["dispatch routines WDK kernel , DispatchCreate routine", "dispatch routines WDK kernel , DispatchClose routine", "dispatch routines WDK kernel , DispatchCreateClose routine", "DispatchCreateClose routine", "DispatchClose routine", "DispatchCreate routine", "IRP_MJ_CREATE I/O function code", "IRP_MJ_CLOSE I/O function code", "create dispatch routines WDK kernel", "close dispatch routines WDK kernel"]
---

# DispatchCreate, DispatchClose, and DispatchCreateClose Routines


## <a href="" id="ddk-dispatchcreate-dispatchclose-and-dispatchcreateclose-routines-kg"></a>


A driver's [*DispatchCreate*](https://msdn.microsoft.com/library/windows/hardware/ff543266) and [*DispatchClose*](https://msdn.microsoft.com/library/windows/hardware/ff543255) routines handle IRPs with I/O function codes of [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff550729) and [**IRP\_MJ\_CLOSE**](https://msdn.microsoft.com/library/windows/hardware/ff550720), respectively. Alternatively, a combined [*DispatchCreateClose*](https://msdn.microsoft.com/library/windows/hardware/ff543270) routine can handle IRPs for both of these I/O function codes.

A create request can originate either from a user-mode subsystem's attempt to get a handle to a file object representing a device (possibly on behalf of an application or subsystem-level driver) or in a higher-level driver's call to [**IoGetDeviceObjectPointer**](https://msdn.microsoft.com/library/windows/hardware/ff549198) or [**IoAttachDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548294).

A reciprocal close request originates from a user-mode subsystem's close of the file object handle associated with the driver's device object.

Each of these requests is inherently synchronous.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20DispatchCreate,%20DispatchClose,%20and%20DispatchCreateClose%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


