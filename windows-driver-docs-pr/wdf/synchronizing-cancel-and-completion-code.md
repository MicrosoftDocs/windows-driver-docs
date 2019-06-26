---
title: Synchronizing Cancel and Completion Code
description: Synchronizing Cancel and Completion Code
ms.assetid: 4c302fc5-cb14-46e5-80c8-8dbf62486905
keywords:
- request processing WDK KMDF , canceling requests
- I/O requests WDK KMDF , canceling
- synchronization WDK KMDF
- completing I/O requests WDK KMDF
- request processing WDK KMDF , synchronization
- I/O requests WDK KMDF , synchronization
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Synchronizing Cancel and Completion Code





If your driver calls [**WdfRequestMarkCancelable**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelable) or [**WdfRequestMarkCancelableEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestmarkcancelableex) to make an I/O request cancelable, there is potential for a synchronization problem. For example, your driver and device might perform device I/O operations asynchronously by means of [*EvtInterruptIsr*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_isr) and [*EvtInterruptDpc*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) callback functions, and both the *EvtInterruptDpc* and [*EvtRequestCancel*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nc-wdfrequest-evt_wdf_request_cancel) callback functions might contain calls to [**WdfRequestComplete**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestcomplete).

The driver must call [**WdfRequestComplete**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestcomplete) only once, to either complete or cancel the request. But if the [*EvtInterruptDpc*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) and [*EvtRequestCancel*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nc-wdfrequest-evt_wdf_request_cancel) callback functions are not synchronized with each other, the framework can call one while the other is executing.

Avoiding this problem is easy if your driver uses the framework's [automatic synchronization](using-automatic-synchronization.md), because automatic synchronization ensures that the callback functions will be called one at a time.

If your driver does not use the framework's automatic synchronization, it can use [framework locks](using-framework-locks.md) to synchronize cancel and completion code.

Whether the driver uses framework's automatic synchronization or provides its own synchronization, the driver's [*EvtRequestCancel*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nc-wdfrequest-evt_wdf_request_cancel) callback function must call [**WdfRequestComplete**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestcomplete) to cancel a request. The driver's [*EvtInterruptDpc*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) callback function should call [**WdfRequestUnmarkCancelable**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestunmarkcancelable) as follows:

```cpp
Status = WdfRequestUnmarkCancelable(Request);
if( Status != STATUS_CANCELLED ) {
    WdfRequestComplete(Request, RequestStatus);
    }
```

This code ensures that the driver does not call [**WdfRequestComplete**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestcomplete) to complete the request if the driver has already called it to cancel the request.

For more information about the rules that your driver must follow when it calls **WdfRequestUnmarkCancelable**, see [**WdfRequestUnmarkCancelable**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestunmarkcancelable).

 

 





