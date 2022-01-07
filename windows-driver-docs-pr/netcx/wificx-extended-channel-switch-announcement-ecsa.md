---
title: WiFiCx Extended channel switch announcement (ECSA)
description: This section provides suggested driver/firmware changes to implement Extended Channel Switch Announcement (ECSA) for WiFiCx
ms.date: 09/30/2021
---

# WiFiCx Extended channel switch announcement (ECSA)


To minimize the cases where the Wi-Fi Direct port causes the system to operate in Multi-Channel mode, multi-channel uses cases are not as performant as single channel use cases. We recommend that the device (driver/firmware) implements ECSA. This feature should exist completely on the IHV side.

Here are the suggested driver/firmware changes.

- Support bi-directional ECSA on the Wi-Fi Direct port.

- When the device is the Group Owner (GO) and is in Multi-Channel mode:
  - The driver must detect if the remote peer supports ECSA.
  - If the remote peer supports ECSA, engage ECSA to move the peer into the channel configuration that yields a single channel.

- When device is a GO & connected to a single Client:
  - If the remote peer sends the P2P Operating Channel Preference frame and there is no STA connectivity, then the driver should engage in eCSA to move the peer into a requested channel.


- When the device is the Client and is in Multi-Channel mode:
  - If the remote peer supports eCSA, then send the P2P Operating Channel Preference frame to request that the remote GO initiates eCSA. GO may not initiate eCSA if it would cause the GO to go into MC.
  - If an ECSA request comes from the remote peer, then support it.

- Send channel change notifications to the operating system with [NDIS\_STATUS\_WDI\_INDICATION\_P2P\_GROUP\_OPERATING\_CHANNEL](./ndis-status-wdi-indication-p2p-group-operating-channel.md).

 

