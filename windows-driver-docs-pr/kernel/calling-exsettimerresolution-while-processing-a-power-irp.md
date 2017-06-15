---
title: Calling ExSetTimerResolution While Processing a Power IRP
author: windows-driver-content
description: Calling ExSetTimerResolution While Processing a Power IRP
MS-HAID:
- 'PwrMgmt\_806fcb6e-792b-4cef-9bf4-b8c0d1a30d44.xml'
- 'kernel.calling\_exsettimerresolution\_while\_processing\_a\_power\_irp'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 999a76ab-1586-4157-bfa7-8cc5dd517c71
---

# Calling ExSetTimerResolution While Processing a Power IRP


During the processing of an [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784) request, the power manager holds a lock on a resource that [**ExSetTimerResolution**](https://msdn.microsoft.com/library/windows/hardware/ff545614) must acquire to complete. Consequently, a deadlock will occur if a driver directly or indirectly calls this routine while processing a power request, and then waits for the call to the routine to return before the driver completes the power request. While processing a power request, a driver can safely call **ExSetTimerResolution** only if the driver does not wait for the call to this routine to return before completing the power request. For example, a driver can create a worker thread that calls **ExSetTimerResolution**, as long as the driver then completes the power request without waiting for the call to this routine to return.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Calling%20ExSetTimerResolution%20While%20Processing%20a%20Power%20IRP%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


