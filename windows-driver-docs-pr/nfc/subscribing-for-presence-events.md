---
title: Subscribing for presence events
author: windows-driver-content
description: Subscribing for presence events
ms.assetid: 4AA6C7DA-5301-4356-8AF9-5567322FAB46
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20Subscribing%20for%20presence%20events%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




