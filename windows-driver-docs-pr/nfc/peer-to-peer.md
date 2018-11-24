---
title: Peer-to-peer
ms.assetid: 0234BA57-477E-408C-94C8-8DD8922FD386
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
description: Information about NFC forum defined peer-to-peer standards and protocols that ensure devices are able to interact using NFC.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Peer-to-peer


To ensure that two devices are able to interact using NFC, the driver MUST transmit and receive data via the following NFC Forum defined peer-to-peer standards and protocols:

-   LLCP v1.1
-   SNEP v1.0

## Driver Requirements


The Driver MUST support the default SNEP server running over LLCP to exchange NDEF messages:

-   On arrival of a remote P2P device, the driver MUST establish a client SNEP connection with the remote device’s default SNEP server (followed by which the “DeviceArrived” subscriptions is triggered).
-   The driver MUST also be able to accept connections on its default SNEP server from a remote device’s SNEP client connection.
-   All NDEF messages received on the SNEP server MUST be translated into message types as defined in this document.
-   All message types to be published MUST be translated into NDEF messages and sent to the remote device as defined above. Once the message is transmitted, the [**IOCTL\_NFP\_GET\_NEXT\_TRANSMITTED\_MESSAGE**](https://msdn.microsoft.com/library/windows/hardware/jj853320) is completed as defined in this document.

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[Near field proximity DDI reference](https://msdn.microsoft.com/library/windows/hardware/jj866056)  
