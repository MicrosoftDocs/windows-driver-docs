---
title: Revise Canceled Request Logic
description: Revise Canceled Request Logic
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Revise Canceled Request Logic


When an I/O request is canceled, a WDM driver must manage several difficult race conditions. A request might be canceled while it is in a queue or while the driver is processing it. In each case the driver must use a combination of locks to ensure that it cancels and completes the request only once.

The WDF queuing mechanism greatly simplifies cancellation. If a request is canceled while it is on a queue, the framework handles cancellation without notifying the driver. The driver can request notification by registering an [*EvtIoCanceledOnQueue*](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_canceled_on_queue) callback function. After the framework has delivered a request to the driver, the request is not cancelable by default. A driver can call [**WdfRequestIsCanceled**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestiscanceled) at any time to find out whether the request has been canceled.

For more information, see [Canceling I/O Requests](canceling-i-o-requests.md).

 

