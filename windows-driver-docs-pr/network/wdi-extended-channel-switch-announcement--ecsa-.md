---
title: WDI Extended channel switch announcement (ECSA)
description: This section provides suggested driver/firmware changes to implement Extended Channel Switch Announcement (ECSA)
ms.assetid: 9C59C8A2-335F-4BA4-8682-6DFFB82E1CAF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDI Extended channel switch announcement (ECSA)


To minimize the cases where the Wi-Fi Direct port causes the system to operate in Multi-Channel mode, multi-channel uses cases are not as performant as single channel use cases. We recommend that the device (driver/firmware) implements ECSA. This feature should exist completely on the IHV side.

Here are the suggested driver/firmware changes.

-   Support bi-directional ECSA on the Wi-Fi Direct port.
-   When the device is the Group Owner and is in Multi-Channel mode:
    -   The driver must detect if the remote peer supports ECSA.
    -   If the remote peer supports ECSA, engage ECSA to move the peer into the channel configuration that yields a single channel.
-   When the device is the Client and is in Multi-Channel mode:
    -   If an ECSA request comes from the remote peer, then support it.
-   Send channel change notifications to the operating system with [NDIS\_STATUS\_WDI\_INDICATION\_P2P\_GROUP\_OPERATING\_CHANNEL](https://msdn.microsoft.com/library/windows/hardware/dn925643).

 

 





