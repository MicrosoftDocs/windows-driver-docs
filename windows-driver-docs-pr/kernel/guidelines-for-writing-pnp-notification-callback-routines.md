---
title: Guidelines for Writing PnP Notification Callback Routines
author: windows-driver-content
description: Guidelines for Writing PnP Notification Callback Routines
MS-HAID:
- 'PlugPlay\_db01ab93-de66-4f81-8905-1577fbe2e833.xml'
- 'kernel.guidelines\_for\_writing\_pnp\_notification\_callback\_routines'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2153b4c2-f60f-4ac9-8eee-66c5f3a9f414
keywords: ["notifications WDK PnP , callback routines", "callback routines WDK PnP"]
---

# Guidelines for Writing PnP Notification Callback Routines


## <a href="" id="ddk-guidelines-for-writing-pnp-notification-callback-routines-kg"></a>


The PnP manager calls notification callback routines at IRQL = PASSIVE\_LEVEL.

To ensure smooth operation of the PnP subsystem, a PnP notification callback routine must follow these guidelines:

1.  A notification callback routine must not block.

2.  A notification callback routine must not call, or cause a call to, synchronous routines that generate PnP events or any routine that blocks waiting for device installation or removal.

    Calling such routines during a notification callback can cause a system deadlock.

    For example, a driver must not call [**IoReportTargetDeviceChange**](https://msdn.microsoft.com/library/windows/hardware/ff549625) in a notification callback routine. Call [**IoReportTargetDeviceChangeAsynchronous**](https://msdn.microsoft.com/library/windows/hardware/ff549634) instead.

3.  A notification callback routine should return success for any events it does not explicitly fail.

    When a driver registers for notification on an event category, the PnP manager notifies the driver of all events in that category, present and future. If a driver returns an error status for events it does not handle, the driver risks failing a new query event by mistake.

    A driver correctly returns an error status when, for example, the driver fails a query notification to veto the event being proposed.

4.  A notification callback routine should be paged code.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Guidelines%20for%20Writing%20PnP%20Notification%20Callback%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


