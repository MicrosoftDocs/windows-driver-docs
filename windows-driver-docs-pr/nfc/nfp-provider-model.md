---
title: NFP provider model
author: windows-driver-content
description: The Near Field Proximity (NFP) provider driver model provides a common surface for Windows to use NFP capabilities and to enable NFP scenarios and use cases.
ms.assetid: AD8DC80F-5CE2-4547-B951-A82A280F18ED
---

# NFP provider model


The Near Field Proximity (NFP) provider driver model provides a common surface for Windows to use NFP capabilities and to enable NFP scenarios and use cases.

To expose these capabilities to Windows, the implementer of a compatible device must provide a device driver that implements the **GUID\_DEVINTERFACE\_NFP** device interface. This driver works with the underlying NFP technology implemented in software and/or hardware on the device to form an NFP provider.

The **GUID\_DEVINTERFACE\_NFP** device interface enables Windows to use various NFP technologies. The most common functionality exposed by implementers of this device interface is generic and not specific to any underlying NFP technology. Apps programming to this common functionality to communicate with other Windows apps should be able to use any NFP provider without modifying the app’s code. Because NFC is a leading standard in the NFP space, the device interface supports specific NFC behavior by giving an NFP provider the ability to handle native NDEF packets. An app may take a dependency on this NFC-specific functionality and restrict its own functionality to NFC-enabled NFP providers only.

Two PCs with incompatible NFP providers will not be able to communicate through their NFP providers. This specification provides guidelines sufficient to support interoperation of two certified Windows systems because support for at least one NFC-enabled provider is a requirement for Windows system certification.

NFP providers pre-stage their communication using a pub/sub model whose transmission is triggered by a proximate event of the underlying NFP technology. Messages are published and subscribed to based on a message type. When two devices become proximate according to the NFP technology, the proximity state is triggered and all currently published messages are transmitted to current subscribers on the other device. This mechanism provides a model where the user sets some context on his device, then taps it with another device to complete the scenario in an easy way.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20NFP%20provider%20model%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




