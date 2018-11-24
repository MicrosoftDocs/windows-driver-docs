---
title: Publishing messages
description: Publishing messages
ms.assetid: 44F8FB0B-6709-4A1C-886D-3788CA39A4D2
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Publishing messages


Clients can publish messages with specific types but will have limited knowledge of who will receive the message or when the message has been received by another app or device. This allows clients to easily “advertise” information to anyone interested without the need to manage the timing of message transmission.

Clients of the Windows proximity API can request to publish messages. The publication lifetime is bound to the client. As long as the client is running, it can maintain the publication. At any time, the client can drop the publication (by unpublish). If the client stops running, the publication is removed.

When a message is unpublished it should no longer be transmitted when a device becomes proximate in the future.

The NFP model is intended to support short (and therefore quickly transmitted) messages, typically less than 512 bytes. NFP providers are only required to support messages up to and including 10 kilobytes (KB). Any client that wants to send larger messages with portable code across all providers must manually chunk messages or transmit messages out of band.

## Message Transmitted Callback


The Message Transmitted Callback allows clients to know when a message they have published has been transmitted to another device. One of the goals of the Message Transmitted Callback is to enable an app to unpublish a message as soon as it has been transmitted.

The model does not provide for knowledge of the receiving side actually processing the message. The only way to accomplish this is for the receiver to publish a message back to the client.

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[Near field proximity DDI reference](https://msdn.microsoft.com/library/windows/hardware/jj866056)  

