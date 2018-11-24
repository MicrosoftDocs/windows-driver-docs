---
title: NFP provider model
description: The Near Field Proximity (NFP) provider driver model provides a common surface for Windows to use NFP capabilities and to enable NFP scenarios and use cases.
ms.assetid: AD8DC80F-5CE2-4547-B951-A82A280F18ED
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NFP provider model


The Near Field Proximity (NFP) provider driver model provides a common surface for Windows to use NFP capabilities and to enable NFP scenarios and use cases.

To expose these capabilities to Windows, the implementer of a compatible device must provide a device driver that implements the **GUID\_DEVINTERFACE\_NFP** device interface. This driver works with the underlying NFP technology implemented in software and/or hardware on the device to form an NFP provider.

The **GUID\_DEVINTERFACE\_NFP** device interface enables Windows to use various NFP technologies. The most common functionality exposed by implementers of this device interface is generic and not specific to any underlying NFP technology. Apps programming to this common functionality to communicate with other Windows apps should be able to use any NFP provider without modifying the app’s code. Because NFC is a leading standard in the NFP space, the device interface supports specific NFC behavior by giving an NFP provider the ability to handle native NDEF packets. An app may take a dependency on this NFC-specific functionality and restrict its own functionality to NFC-enabled NFP providers only.

Two PCs with incompatible NFP providers will not be able to communicate through their NFP providers. This specification provides guidelines sufficient to support interoperation of two certified Windows systems because support for at least one NFC-enabled provider is a requirement for Windows system certification.

NFP providers pre-stage their communication using a pub/sub model whose transmission is triggered by a proximate event of the underlying NFP technology. Messages are published and subscribed to based on a message type. When two devices become proximate according to the NFP technology, the proximity state is triggered and all currently published messages are transmitted to current subscribers on the other device. This mechanism provides a model where the user sets some context on his device, then taps it with another device to complete the scenario in an easy way.

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[Near field proximity DDI reference](https://msdn.microsoft.com/library/windows/hardware/jj866056)  

