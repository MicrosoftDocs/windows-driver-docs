---
title: Peer-to-Peer
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
description: Information about NFC forum defined peer-to-peer standards and protocols that ensure devices are able to interact using NFC.
ms.date: 01/11/2024
---

# Peer-to-peer

To ensure that two devices are able to interact using NFC, the driver MUST transmit and receive data via the following NFC Forum defined peer-to-peer standards and protocols:

- LLCP v1.1
- SNEP v1.0

## Driver Requirements

The Driver MUST support the default SNEP server running over LLCP to exchange NDEF messages:

- On arrival of a remote P2P device, the driver MUST establish a client SNEP connection with the remote device's default SNEP server (followed by which the "DeviceArrived" subscriptions is triggered).
- The driver MUST also be able to accept connections on its default SNEP server from a remote device's SNEP client connection.
- All NDEF messages received on the SNEP server MUST be translated into message types as defined in this document.
- All message types to be published MUST be translated into NDEF messages and sent to the remote device as defined above. Once the message is transmitted, the **[IOCTL_NFP_GET_NEXT_TRANSMITTED_MESSAGE](/windows-hardware/drivers/ddi/nfpdev/ni-nfpdev-ioctl_nfp_get_next_transmitted_message)** is completed as defined in this document.

## Related topics

- [Near field communications (NFC) API reference](/windows-hardware/drivers/ddi/_nfpdrivers/)
