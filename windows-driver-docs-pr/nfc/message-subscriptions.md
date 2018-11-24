---
title: NFP message subscriptions
description: NFP message subscriptions
ms.assetid: ECE9C495-978F-4BD7-95BC-B68432F9B81E
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NFP message subscriptions


A subscription is represented as a unique open handle within the driver. A subscription is made active by opening a handle into the “Subs\\” device namespace. The type of the subscription is defined to be everything following the “Subs\\” prefix.

A callback on message reception is given through a completed [**IOCTL\_NFP\_GET\_NEXT\_SUBSCRIBED\_MESSAGE**](https://msdn.microsoft.com/library/windows/hardware/jj853319).

A subscription can be temporarily disabled via an [**IOCTL\_NFP\_DISABLE**](https://msdn.microsoft.com/library/windows/hardware/jj853315).

A subscription can be re-enabled via an [**IOCTL\_NFP\_ENABLE**](https://msdn.microsoft.com/library/windows/hardware/jj853316).

## Handles


A client that wants to subscribe to a message type will first open a new handle to the driver. Handles from prior publications, subscriptions, and so on, cannot be reused. If they are no longer needed, they will be closed by a well-behaved client.

In opening the handle, a client sets the type of the message subscription. This is the same mechanism as used with publishing, except that the type is prefixed with “Subs\\” instead of “Pubs\\”.

There is no facility to read back the type.

### Required Actions

-   The driver MUST parse the protocol component (before the first ‘.’). Any unrecognized protocol MUST complete with STATUS\_OBJECT\_PATH\_NOT\_FOUND
-   If the string is not NULL-terminated within the buffer length, the driver MUST complete the IOCTL with STATUS\_INVALID\_PARAMETER.
-   If the protocol requires a subtype and the subtype component of the string buffer is less than one (1) character or longer than 250 characters, the driver MUST complete the IOCTL with STATUS\_INVALID\_PARAMETER.
-   If the protocol component of the string buffer is longer than 250 characters, the driver MUST complete the IOCTL with STATUS\_INVALID\_PARAMETER.
-   The driver MUST interpret the first NULL as the end of the string.
-   The driver MAY recognize the “Pairing:Bluetooth” type for subscriptions.
-   The driver MUST recognize the “WindowsUri” type.
-   The driver MUST recognize the “DeviceArrived” type for subscriptions only.
-   The driver MUST recognize the “DeviceDeparted” type for subscriptions only.
-   The driver MUST recognize the “WindowsMime” type for subscriptions only.
-   The driver MUST recognize the “WindowsMime.” type.
-   If the protocol should only be recognized for subscriptions, and the IOCTL specifies “Pubs\\”, the driver MUST complete the IOCTL with STATUS\_OBJECT\_PATH\_NOT\_FOUND.
-   If the protocol should only be recognized for publications, and the IOCTL specifies “Subs\\”, the driver MUST complete the IOCTL with STATUS\_OBJECT\_PATH\_NOT\_FOUND.
-   Some protocols (namespaces) are reserved. Unless explicitly specified in this document, the driver MUST NOT recognize any protocols that begin with:
    -   "Windows”
    -   "Device”
    -   "Pairing”
    -   "NDEF”
-   Two open handles to the same type MUST represent two distinct entities.
-   If *CreateFile* succeeds, the handle is now a “subscription handle”, and MUST NOT be changed into any other type of handle.
-   After this IOCTL succeeds, and before the handle is closed, every time a message is received via the proximity technology that matches the type of this subscription then that message’s data MUST be attached to the file handle for delivery to the client.

## Unsubscribe


The client will close the subscription handle in order to stop receiving messages. If a client process terminates, the system will close all open file handles on behalf of the client.

### Required Actions

When the handle is closed, the driver MUST reclaim all memory used by the subscription:

-   The driver MUST reclaim the type string data.
-   The received queue MUST be purged and reclaimed.
-   Any pended IOCTL MUST be completed with STATUS\_CANCELLED.

## Malicious Peers


If a malicious peer device attempts a denial of service (DOS) attack via the proximity technology, it’s possible that a client could be unable to drain the “Received” queue fast enough to prevent excessive memory use by the driver.

### Required Actions

The driver MUST NOT queue or deliver a given message to the client if that message is received when 50 messages are currently in the “Received” queue (the newest messages are dropped).

## Unresponsive or Misbehaving Clients


If a client stops draining the “Received” queue by failing to send the required [**IOCTL\_NFP\_GET\_NEXT\_SUBSCRIBED\_MESSAGE**](https://msdn.microsoft.com/library/windows/hardware/jj853319) request for a period of ten to twenty seconds \[10-20sec\], the driver should assume that the client is gone. Under normal circumstances, clients should refresh their requests well within one second \[1s\]. If this occurs, the driver must set the “CompleteEventImmediately” counter to zero and must not increment the counter until the client wakes up and sends the required IRP.

### Required Actions

The driver must set the “CompleteEventImmediately” counter to zero and must not increment the counter if the client has not sent a replacement [**IOCTL\_NFP\_GET\_NEXT\_SUBSCRIBED\_MESSAGE**](https://msdn.microsoft.com/library/windows/hardware/jj853319) within 10 - 20 seconds of the prior IOCTL completion.

## Malformed Messages


The client is likely to drop or ignore all errors (except STATUS\_BUFFER\_OVERFLOW) returned from [**IOCTL\_NFP\_GET\_NEXT\_SUBSCRIBED\_MESSAGE**](https://msdn.microsoft.com/library/windows/hardware/jj853319). Therefore, the driver shouldn’t complete these with error conditions merely because a malformed message was received.

### Required Actions

-   The driver MUST NOT deliver messages that are larger than the maximum permitted message size to the client.
-   The driver SHOULD NOT deliver zero-length messages to the client.
-   The driver MUST NOT deliver partial messages to subscribers.
-   The driver MUST NOT deliver messages to the client that have failed a strong CRC.

    **Note**  NFC Forum Certification guarantees this for NFC-enabled NFP providers.

     

-   The driver MUST use a strongly reliable transport and/or attempt retransmission of messages that fail a strong CRC.

    **Note**  NFC Forum Certification guarantees this for NFC-enabled NFP providers.

     

## Duplicate Subscriptions


The driver should assume that if the client subscribes for a message type twice, it is because the client wants to receive the message twice when the message is received.

### Required Actions

The driver MUST accept and report duplicate subscriptions, even if subscribed by the same client.

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[Near field proximity DDI reference](https://msdn.microsoft.com/library/windows/hardware/jj866056)  

