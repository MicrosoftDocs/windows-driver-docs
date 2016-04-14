---
title: Publishing messages
author: windows-driver-content
description: Publishing messages
ms.assetid: 44F8FB0B-6709-4A1C-886D-3788CA39A4D2
keywords: ["NFC", "near field communications", "proximity", "near field proximity", "NFP"]
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

------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20Publishing%20messages%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")
