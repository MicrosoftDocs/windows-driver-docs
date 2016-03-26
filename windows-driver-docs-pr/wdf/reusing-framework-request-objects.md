---
title: Reusing Framework Request Objects
description: Reusing Framework Request Objects
ms.assetid: 9e3090a9-62d0-48b3-9f3b-7171dc6d2766
keywords: ["request processing WDK KMDF , reusing request objects", "request objects WDK KMDF , reusing", "reusing request objects WDK KMDF"]
---

# Reusing Framework Request Objects


## <a href="" id="ddk-reusing-framework-request-objects-df"></a>


To improve performance, framework-based drivers that create and send lots of nearly identical asynchronous requests to an I/O target can reuse request objects instead of creating a new request object for each request. A driver can reuse a request object after the request has been completed.

If a driver has created a request object by calling [**WdfRequestCreate**](https://msdn.microsoft.com/library/windows/hardware/ff549951) or [**WdfRequestCreateFromIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549953), it can reuse the request by calling [**WdfRequestReuse**](https://msdn.microsoft.com/library/windows/hardware/ff550026). A driver can also reuse request objects that it has received from the framework in its I/O queues, but it cannot change the IRP that the received request object contains.

If you are careful to avoid situations that cause the unsuccessful return values described in [**WdfRequestReuse**](https://msdn.microsoft.com/library/windows/hardware/ff550026), your driver can call **WdfRequestReuse** from within a [*CompletionRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff540745) callback function. (The *CompletionRoutine* callback function has a VOID return value and therefore cannot report errors.)

If your driver provides a [*CompletionRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff540745) callback function for a request object that it reuses, the driver must call [**WdfRequestSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff550030) after calling [**WdfRequestReuse**](https://msdn.microsoft.com/library/windows/hardware/ff550026).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Reusing%20Framework%20Request%20Objects%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




