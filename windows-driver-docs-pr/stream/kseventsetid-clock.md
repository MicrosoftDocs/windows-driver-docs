---
title: KSEVENTSETID_Clock
description: Clients can request to be notified of clock state events on a clock by registering these events with the clock's file object KSEVENT\_CLOCK\_INTERVAL\_MARKKSEVENT\_CLOCK\_POSITION\_MARKWhen a client submits the IOCTL\_KS\_ENABLE\_EVENT request to register for event notification, it submits as a data buffer the structure documented in the EventData section of each event reference page.
keywords: ["KSEVENTSETID_Clock Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSEVENTSETID_Clock
api_type:
- NA
ms.date: 11/28/2017
---

# KSEVENTSETID\_Clock


Clients can request to be notified of clock state events on a clock by registering these events with the clock's file object:

[**KSEVENT\_CLOCK\_INTERVAL\_MARK**](ksevent-clock-interval-mark.md)

[**KSEVENT\_CLOCK\_POSITION\_MARK**](ksevent-clock-position-mark.md)

When a client submits the IOCTL\_KS\_ENABLE\_EVENT request to register for event notification, it submits as a data buffer the structure documented in the **EventData** section of each event reference page.

 

 





