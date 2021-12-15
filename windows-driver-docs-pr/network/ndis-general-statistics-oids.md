---
title: NDIS general statistics OIDs
description: This section describes general statistics OIDs for all NDIS drivers
keywords: ["NDIS general statistics OIDs", "WDK NDIS general statistics OIDs", "WDK general statistics OIDs"]
ms.date: 04/20/2017
---

# NDIS general statistics OIDs

A driver should respond to a query of a statistics OID with complete information so that the driver can supply the operating system and applications with information that they need to monitor network status, respond to security issues, and diagnose problems. If statistics counters are in hardware, the driver should read the appropriate statistics value from hardware each time that a statistics OID is queried.

## Miniport driver support for 64-bit counters

All one-Gbps and faster miniport drivers must support 64-bit counters for the following statistics OIDs. In addition, Microsoft recommends that all 100Mbps and faster miniport drivers support 64-bit counters for the following statistics OIDs:

- [OID_GEN_STATISTICS](./oid-gen-statistics.md)
- [OID_GEN_BYTES_RCV](./oid-gen-bytes-rcv.md)
- [OID_GEN_BYTES_XMIT](./oid-gen-bytes-xmit.md)
- [OID_GEN_RCV_DISCARDS](./oid-gen-rcv-discards.md)
- [OID_GEN_XMIT_DISCARDS](./oid-gen-xmit-discards.md)
- [OID_GEN_XMIT_OK](./oid-gen-xmit-ok.md)
- [OID_GEN_RCV_OK](./oid-gen-rcv-ok.md)
- [OID_GEN_XMIT_ERROR](./oid-gen-xmit-error.md)
- [OID_GEN_RCV_ERROR](./oid-gen-rcv-error.md)
- [OID_GEN_RCV_NO_BUFFER](./oid-gen-rcv-no-buffer.md)
- [OID_GEN_DIRECTED_BYTES_XMIT](./oid-gen-directed-bytes-xmit.md)
- [OID_GEN_DIRECTED_FRAMES_XMIT](./oid-gen-directed-frames-xmit.md)
- [OID_GEN_MULTICAST_BYTES_XMIT](./oid-gen-multicast-bytes-xmit.md)
- [OID_GEN_MULTICAST_FRAMES_XMIT](./oid-gen-multicast-frames-xmit.md)
- [OID_GEN_BROADCAST_BYTES_XMIT](./oid-gen-broadcast-bytes-xmit.md)
- [OID_GEN_BROADCAST_FRAMES_XMIT](./oid-gen-broadcast-frames-xmit.md)
- [OID_GEN_DIRECTED_BYTES_RCV](./oid-gen-directed-bytes-rcv.md)
- [OID_GEN_DIRECTED_FRAMES_RCV](./oid-gen-directed-frames-rcv.md)
- [OID_GEN_MULTICAST_BYTES_RCV](./oid-gen-multicast-bytes-rcv.md)
- [OID_GEN_MULTICAST_FRAMES_RCV](./oid-gen-multicast-frames-rcv.md)
- [OID_GEN_BROADCAST_BYTES_RCV](./oid-gen-broadcast-bytes-rcv.md)
- [OID_GEN_BROADCAST_FRAMES_RCV](./oid-gen-broadcast-frames-rcv.md)
- [OID_GEN_RCV_CRC_ERROR](./oid-gen-rcv-crc-error.md)
- [OID_GEN_TRANSMIT_QUEUE_LENGTH](./oid-gen-transmit-queue-length.md)
- [OID_GEN_INIT_TIME_MS](./oid-gen-init-time-ms.md)
- [OID_GEN_RESET_COUNTS](./oid-gen-reset-counts.md)
- [OID_GEN_MEDIA_SENSE_COUNTS](./oid-gen-media-sense-counts.md)

Miniport drivers can also support 64-bit counters for other statistics OIDs, such as OIDs that indicate transmit or receive errors.

System support for 64-bit counters is available in Windows XP and later operating systems.

>[!NOTE]
> If an NDIS MUX driver exposes multiple miniport instances, querying the following general statistics OIDs should return data specific to that miniport instance. For example, if a MUX driver implements virtual local area network (VLAN) filtering and exposes one miniport per VLAN, the statistics values returned from the following OIDs are expected to be per VLAN.
> - [OID_GEN_STATISTICS](./oid-gen-statistics.md)
> - [OID_GEN_RCV_OK](./oid-gen-rcv-ok.md)
> - [OID_GEN_XMIT_OK](./oid-gen-xmit-ok.md)
