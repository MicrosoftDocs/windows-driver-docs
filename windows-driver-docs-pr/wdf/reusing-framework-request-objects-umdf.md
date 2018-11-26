---
title: Reusing Framework Request Objects in UMDF
description: Reusing Framework Request Objects in UMDF
ms.assetid: 804efc94-a7df-4ebd-a42e-82d1c5376e19
keywords:
- I/O requests WDK UMDF , reusing objects
- request processing WDK UMDF , reusing I/O request objects
- User-Mode Driver Framework WDK , reusing I/O request objects
- UMDF WDK , reusing I/O request objects
- user-mode drivers WDK UMDF , reusing I/O request objects
- reusing I/O request objects WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reusing Framework Request Objects in UMDF


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

To improve driver performance, framework-based drivers that create and send many nearly identical asynchronous requests to an I/O target can reuse request objects instead of creating a new request object for each request. A driver can reuse a request object after the request has been completed.

If a driver has created a request object by calling [**IWDFDevice::CreateRequest**](https://msdn.microsoft.com/library/windows/hardware/ff557021), it can reuse the request by calling [**IWDFIoRequest2::Reuse**](https://msdn.microsoft.com/library/windows/hardware/ff559048). A driver can also reuse request objects that it has received from the framework in its I/O queues.

If your driver provides an [**IRequestCallbackRequestCompletion::OnCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff556905) callback function for a request object that it reuses, the driver must call [**IWDFIoRequest::SetCompletionCallback**](https://msdn.microsoft.com/library/windows/hardware/ff559153) after it calls [**Reuse**](https://msdn.microsoft.com/library/windows/hardware/ff559048).

 

 





