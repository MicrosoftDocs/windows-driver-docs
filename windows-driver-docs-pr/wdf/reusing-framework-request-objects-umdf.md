---
title: Reusing Framework Request Objects in UMDF
description: Reusing Framework Request Objects in UMDF
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


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

To improve driver performance, framework-based drivers that create and send many nearly identical asynchronous requests to an I/O target can reuse request objects instead of creating a new request object for each request. A driver can reuse a request object after the request has been completed.

If a driver has created a request object by calling [**IWDFDevice::CreateRequest**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-createrequest), it can reuse the request by calling [**IWDFIoRequest2::Reuse**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest2-reuse). A driver can also reuse request objects that it has received from the framework in its I/O queues.

If your driver provides an [**IRequestCallbackRequestCompletion::OnCompletion**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-irequestcallbackrequestcompletion-oncompletion) callback function for a request object that it reuses, the driver must call [**IWDFIoRequest::SetCompletionCallback**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-setcompletioncallback) after it calls [**Reuse**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest2-reuse).

 

