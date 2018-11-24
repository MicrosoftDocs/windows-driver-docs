---
title: Reusing Framework Request Objects
description: Reusing Framework Request Objects
ms.assetid: 9e3090a9-62d0-48b3-9f3b-7171dc6d2766
keywords:
- request processing WDK KMDF , reusing request objects
- request objects WDK KMDF , reusing
- reusing request objects WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reusing Framework Request Objects





To improve performance, framework-based drivers that create and send lots of nearly identical asynchronous requests to an I/O target can reuse request objects instead of creating a new request object for each request. A driver can reuse a request object after the request has been completed.

If a driver has created a request object by calling [**WdfRequestCreate**](https://msdn.microsoft.com/library/windows/hardware/ff549951) or [**WdfRequestCreateFromIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549953), it can reuse the request by calling [**WdfRequestReuse**](https://msdn.microsoft.com/library/windows/hardware/ff550026). A driver can also reuse request objects that it has received from the framework in its I/O queues, but it cannot change the IRP that the received request object contains.

If you are careful to avoid situations that cause the unsuccessful return values described in [**WdfRequestReuse**](https://msdn.microsoft.com/library/windows/hardware/ff550026), your driver can call **WdfRequestReuse** from within a [*CompletionRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff540745) callback function. (The *CompletionRoutine* callback function has a VOID return value and therefore cannot report errors.)

If your driver provides a [*CompletionRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff540745) callback function for a request object that it reuses, the driver must call [**WdfRequestSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff550030) after calling [**WdfRequestReuse**](https://msdn.microsoft.com/library/windows/hardware/ff550026).

 

 





