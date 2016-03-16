---
title: Synchronizing Cancel and Completion Code
description: Synchronizing Cancel and Completion Code
ms.assetid: 4c302fc5-cb14-46e5-80c8-8dbf62486905
keywords: ["request processing WDK KMDF canceling requests", "I/O requests WDK KMDF canceling", "synchronization WDK KMDF", "completing I/O requests WDK KMDF", "request processing WDK KMDF synchronization", "I/O requests WDK KMDF synchronization"]
---

# Synchronizing Cancel and Completion Code


## <a href="" id="ddk-synchronizing-cancel-and-completion-code-df"></a>


If your driver calls [**WdfRequestMarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff549983) or [**WdfRequestMarkCancelableEx**](https://msdn.microsoft.com/library/windows/hardware/ff549984) to make an I/O request cancelable, there is potential for a synchronization problem. For example, your driver and device might perform device I/O operations asynchronously by means of [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) and [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback functions, and both the *EvtInterruptDpc* and [*EvtRequestCancel*](https://msdn.microsoft.com/library/windows/hardware/ff541817) callback functions might contain calls to [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945).

The driver must call [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945) only once, to either complete or cancel the request. But if the [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) and [*EvtRequestCancel*](https://msdn.microsoft.com/library/windows/hardware/ff541817) callback functions are not synchronized with each other, the framework can call one while the other is executing.

Avoiding this problem is easy if your driver uses the framework's [automatic synchronization](using-automatic-synchronization.md), because automatic synchronization ensures that the callback functions will be called one at a time.

If your driver does not use the framework's automatic synchronization, it can use [framework locks](using-framework-locks.md) to synchronize cancel and completion code.

Whether the driver uses framework's automatic synchronization or provides its own synchronization, the driver's [*EvtRequestCancel*](https://msdn.microsoft.com/library/windows/hardware/ff541817) callback function must call [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945) to cancel a request. The driver's [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback function should call [**WdfRequestUnmarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff550035) as follows:

```
Status = WdfRequestUnmarkCancelable(Request);
if( Status != STATUS_CANCELLED ) {
    WdfRequestComplete(Request, RequestStatus);
    }
```

This code ensures that the driver does not call [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945) to complete the request if the driver has already called it to cancel the request.

For more information about the rules that your driver must follow when it calls **WdfRequestUnmarkCancelable**, see [**WdfRequestUnmarkCancelable**](https://msdn.microsoft.com/library/windows/hardware/ff550035).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Synchronizing%20Cancel%20and%20Completion%20Code%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




