---
title: NDIS general statistics OIDs
description: This section describes general statistics OIDs for all NDIS drivers
keywords: ["NDIS general statistics OIDs", "WDK NDIS general statistics OIDs", "WDK general statistics OIDs"]
ms.assetid: 364BEF6E-489C-427A-9ACC-D18F29F22B0F
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS general statistics OIDs

A driver should respond to a query of a statistics OID with complete information so that the driver can supply the operating system and applications with information that they need to monitor network status, respond to security issues, and diagnose problems. If statistics counters are in hardware, the driver should read the appropriate statistics value from hardware each time that a statistics OID is queried.

## Miniport driver support for 64-bit counters

All one-Gbps and faster miniport drivers must support 64-bit counters for the following statistics OIDs. In addition, Microsoft recommends that all 100Mbps and faster miniport drivers support 64-bit counters for the following statistics OIDs:

- [OID_GEN_STATISTICS](https://msdn.microsoft.com/library/windows/hardware/ff569640)
- [OID_GEN_BYTES_RCV](https://msdn.microsoft.com/library/windows/hardware/ff569443)
- [OID_GEN_BYTES_XMIT](https://msdn.microsoft.com/library/windows/hardware/ff569445)
- [OID_GEN_RCV_DISCARDS](https://msdn.microsoft.com/library/windows/hardware/ff569628)
- [OID_GEN_XMIT_DISCARDS](https://msdn.microsoft.com/library/windows/hardware/ff569653)
- [OID_GEN_XMIT_OK](https://msdn.microsoft.com/library/windows/hardware/ff569656)
- [OID_GEN_RCV_OK](https://msdn.microsoft.com/library/windows/hardware/ff569632)
- [OID_GEN_XMIT_ERROR](https://msdn.microsoft.com/library/windows/hardware/ff569654)
- [OID_GEN_RCV_ERROR](https://msdn.microsoft.com/library/windows/hardware/ff569629)
- [OID_GEN_RCV_NO_BUFFER](https://msdn.microsoft.com/library/windows/hardware/ff569631)
- [OID_GEN_DIRECTED_BYTES_XMIT](https://msdn.microsoft.com/library/windows/hardware/ff569578)
- [OID_GEN_DIRECTED_FRAMES_XMIT](https://msdn.microsoft.com/library/windows/hardware/ff569580)
- [OID_GEN_MULTICAST_BYTES_XMIT](https://msdn.microsoft.com/library/windows/hardware/ff569612)
- [OID_GEN_MULTICAST_FRAMES_XMIT](https://msdn.microsoft.com/library/windows/hardware/ff569614)
- [OID_GEN_BROADCAST_BYTES_XMIT](https://msdn.microsoft.com/library/windows/hardware/ff569440)
- [OID_GEN_BROADCAST_FRAMES_XMIT](https://msdn.microsoft.com/library/windows/hardware/ff569442)
- [OID_GEN_DIRECTED_BYTES_RCV](https://msdn.microsoft.com/library/windows/hardware/ff569577)
- [OID_GEN_DIRECTED_FRAMES_RCV](https://msdn.microsoft.com/library/windows/hardware/ff569579)
- [OID_GEN_MULTICAST_BYTES_RCV](https://msdn.microsoft.com/library/windows/hardware/ff569611)
- [OID_GEN_MULTICAST_FRAMES_RCV](https://msdn.microsoft.com/library/windows/hardware/ff569613)
- [OID_GEN_BROADCAST_BYTES_RCV](https://msdn.microsoft.com/library/windows/hardware/ff569439)
- [OID_GEN_BROADCAST_FRAMES_RCV](https://msdn.microsoft.com/library/windows/hardware/ff569441)
- [OID_GEN_RCV_CRC_ERROR](https://msdn.microsoft.com/library/windows/hardware/ff569627)
- [OID_GEN_TRANSMIT_QUEUE_LENGTH](https://msdn.microsoft.com/library/windows/hardware/ff569646)
- [OID_GEN_INIT_TIME_MS](https://msdn.microsoft.com/library/windows/hardware/ff569588)
- [OID_GEN_RESET_COUNTS](https://msdn.microsoft.com/library/windows/hardware/ff569638)
- [OID_GEN_MEDIA_SENSE_COUNTS](https://msdn.microsoft.com/library/windows/hardware/ff569608)

Miniport drivers can also support 64-bit counters for other statistics OIDs, such as OIDs that indicate transmit or receive errors.

System support for 64-bit counters is available in Windows XP and later operating systems.

>[!NOTE]
> If an NDIS MUX driver exposes multiple miniport instances, querying the following general statistics OIDs should return data specific to that miniport instance. For example, if a MUX driver implements virtual local area network (VLAN) filtering and exposes one miniport per VLAN, the statistics values returned from the following OIDs are expected to be per VLAN.
> - [OID_GEN_STATISTICS](https://msdn.microsoft.com/library/windows/hardware/ff569640)
> - [OID_GEN_RCV_OK](https://msdn.microsoft.com/library/windows/hardware/ff569632)
> - [OID_GEN_XMIT_OK](https://msdn.microsoft.com/library/windows/hardware/ff569656)


