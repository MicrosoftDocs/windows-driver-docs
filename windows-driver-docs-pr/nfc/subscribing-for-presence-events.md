---
title: Subscribing for presence events
description: Subscribing for presence events
ms.assetid: 4AA6C7DA-5301-4356-8AF9-5567322FAB46
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Subscribing for presence events


A presence subscription is represented as a unique open handle within the driver. An event will be thrown to the client from the driver every time the NFP provider transitions from non-proximate to proximate or proximate to non-proximate.

**Note**  This interface does not currently provide the ability to tell which proximate device was removed or which subscriptions arrive from which proximate device when two devices are both proximate.

 

Presence events are implemented using the typical subscription path. Messages with protocol “DeviceArrived” or “DeviceDeparted” MUST be interpreted as special subscriptions. The arrival message MUST be the first message delivered immediately before delivering received messages. The departure message MUST be the last message delivered after no more messages are possible.

## Subscription


This looks just like a regular subscription except for the following specific requirements.

A proximity device and its driver are involved in the protocol flow of receiving messages from a proximate device.

### Required Actions

The driver MUST accept and report duplicate subscriptions, even if subscribed by the same client.

-   Just before the first message is received when proximate, the driver MUST act as if a virtual “DeviceArrived” message was just received.
-   When the provider transitions to being non-proximate the driver MUST act as if a virtual “DeviceDeparted” message was just received.
-   The “DeviceDeparted” message MUST NOT be delivered to the client before all other messages have been handled by that client.
-   The payload for a DeviceArrived message MUST be a single DWORD with the high 31 bits set to zero and the least significant bit set ONLY when the first device to become proximate is capable of sustained bi-directional communication.

    **Note**  For NFC, this equates to LLCP support.

     

-   If the first device to become proximate is merely a tag-type device (for example, an NFC Forum Tag), then the driver MUST clear the least-significant bit in the payload of the DeviceArrived message.

     

-   The payload for a DeviceDeparted message MUST be a single DWORD with a value of 0.

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[Near field proximity DDI reference](https://msdn.microsoft.com/library/windows/hardware/jj866056)  

