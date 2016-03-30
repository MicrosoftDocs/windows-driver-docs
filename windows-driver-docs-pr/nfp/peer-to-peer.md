---
title: Peer-to-Peer
ms.assetid: 0234BA57-477E-408C-94C8-8DD8922FD386
description: 
---

# Peer-to-Peer


To ensure that two devices are able to interact using NFC, the driver MUST transmit and receive data via the following NFC Forum defined peer-to-peer standards and protocols:

-   LLCP v1.1
-   SNEP v1.0

## Driver Requirements


The Driver MUST support the default SNEP server running over LLCP to exchange NDEF messages:

-   On arrival of a remote P2P device, the driver MUST establish a client SNEP connection with the remote device’s default SNEP server (followed by which the “DeviceArrived” subscriptions is triggered).
-   The driver MUST also be able to accept connections on its default SNEP server from a remote device’s SNEP client connection.
-   All NDEF messages received on the SNEP server MUST be translated into message types as defined in this document.
-   All message types to be published MUST be translated into NDEF messages and sent to the remote device as defined above. Once the message is transmitted, the [**IOCTL\_NFP\_GET\_NEXT\_TRANSMITTED\_MESSAGE**](https://msdn.microsoft.com/library/windows/hardware/jj853320) is completed as defined in this document.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20Peer-to-Peer%20%20RELEASE:%20%283/30/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




