---
title: KSEVENTSETID\_Clock
description: Clients can request to be notified of clock state events on a clock by registering these events with the clock's file object KSEVENT\_CLOCK\_INTERVAL\_MARKKSEVENT\_CLOCK\_POSITION\_MARKWhen a client submits the IOCTL\_KS\_ENABLE\_EVENT request to register for event notification, it submits as a data buffer the structure documented in the EventData section of each event reference page.
ms.assetid: a411f83a-0361-4db6-9617-7c8588739cb4
keywords: ["KSEVENTSETID_Clock Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENTSETID_Clock
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSEVENTSETID\_Clock


Clients can request to be notified of clock state events on a clock by registering these events with the clock's file object:

[**KSEVENT\_CLOCK\_INTERVAL\_MARK**](ksevent-clock-interval-mark.md)

[**KSEVENT\_CLOCK\_POSITION\_MARK**](ksevent-clock-position-mark.md)

When a client submits the IOCTL\_KS\_ENABLE\_EVENT request to register for event notification, it submits as a data buffer the structure documented in the **EventData** section of each event reference page.

 

 





