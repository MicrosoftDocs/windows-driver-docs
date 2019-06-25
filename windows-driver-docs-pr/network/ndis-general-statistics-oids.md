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

- [OID_GEN_STATISTICS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-statistics)
- [OID_GEN_BYTES_RCV](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-bytes-rcv)
- [OID_GEN_BYTES_XMIT](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-bytes-xmit)
- [OID_GEN_RCV_DISCARDS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-rcv-discards)
- [OID_GEN_XMIT_DISCARDS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-xmit-discards)
- [OID_GEN_XMIT_OK](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-xmit-ok)
- [OID_GEN_RCV_OK](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-rcv-ok)
- [OID_GEN_XMIT_ERROR](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-xmit-error)
- [OID_GEN_RCV_ERROR](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-rcv-error)
- [OID_GEN_RCV_NO_BUFFER](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-rcv-no-buffer)
- [OID_GEN_DIRECTED_BYTES_XMIT](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-directed-bytes-xmit)
- [OID_GEN_DIRECTED_FRAMES_XMIT](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-directed-frames-xmit)
- [OID_GEN_MULTICAST_BYTES_XMIT](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-multicast-bytes-xmit)
- [OID_GEN_MULTICAST_FRAMES_XMIT](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-multicast-frames-xmit)
- [OID_GEN_BROADCAST_BYTES_XMIT](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-broadcast-bytes-xmit)
- [OID_GEN_BROADCAST_FRAMES_XMIT](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-broadcast-frames-xmit)
- [OID_GEN_DIRECTED_BYTES_RCV](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-directed-bytes-rcv)
- [OID_GEN_DIRECTED_FRAMES_RCV](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-directed-frames-rcv)
- [OID_GEN_MULTICAST_BYTES_RCV](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-multicast-bytes-rcv)
- [OID_GEN_MULTICAST_FRAMES_RCV](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-multicast-frames-rcv)
- [OID_GEN_BROADCAST_BYTES_RCV](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-broadcast-bytes-rcv)
- [OID_GEN_BROADCAST_FRAMES_RCV](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-broadcast-frames-rcv)
- [OID_GEN_RCV_CRC_ERROR](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-rcv-crc-error)
- [OID_GEN_TRANSMIT_QUEUE_LENGTH](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-transmit-queue-length)
- [OID_GEN_INIT_TIME_MS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-init-time-ms)
- [OID_GEN_RESET_COUNTS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-reset-counts)
- [OID_GEN_MEDIA_SENSE_COUNTS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-media-sense-counts)

Miniport drivers can also support 64-bit counters for other statistics OIDs, such as OIDs that indicate transmit or receive errors.

System support for 64-bit counters is available in Windows XP and later operating systems.

>[!NOTE]
> If an NDIS MUX driver exposes multiple miniport instances, querying the following general statistics OIDs should return data specific to that miniport instance. For example, if a MUX driver implements virtual local area network (VLAN) filtering and exposes one miniport per VLAN, the statistics values returned from the following OIDs are expected to be per VLAN.
> - [OID_GEN_STATISTICS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-statistics)
> - [OID_GEN_RCV_OK](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-rcv-ok)
> - [OID_GEN_XMIT_OK](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-xmit-ok)


