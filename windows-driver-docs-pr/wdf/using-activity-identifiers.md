---
title: Using Activity Identifiers
description: Using Activity Identifiers
ms.date: 04/20/2017
---

# Using Activity Identifiers


In framework versions 1.11 and later, UMDF drivers can set and retrieve activity identifiers (IDs). Activity IDs allow you to associate multiple I/O requests, so that you can track them using Event Tracing for Windows (ETW) tracing. This topic describes some possible scenarios in which the driver might use activity IDs.

## Associating New Requests with an Existing Request


In your driver's I/O dispatch callback function, you might create multiple framework I/O requests as a result of an incoming request. The driver obtains the activity ID from the original request and sets it in the new requests by calling [**WdfRequestRetrieveActivityId**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveactivityid) and [**WdfRequestSetActivityId**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsetactivityid).

For a code example, see [**WdfRequestRetrieveActivityId**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveactivityid).

## Associating New Requests with an Existing Thread


A driver might create a new I/O request in a thread other than the I/O dispatch thread, or in a work item. You can set the activity ID for such a request from any corresponding request, or by using the activity ID associated with the I/O dispatch thread. The driver can retrieve the activity ID associated with the current thread by calling [**EventActivityIdControl**](/windows/win32/api/evntprov/nf-evntprov-eventactivityidcontrol) and then calling [**WdfRequestSetActivityId**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsetactivityid) to set the identifier for each new I/O request.

If the driver calls the Win32 API to send an I/O request, it can retrieve the activity ID from the original request and propagate it to the thread. The I/O manager then applies the activity ID that is associated with the thread to any I/O request packets (IRPs) that it generates in response to the request.

 

