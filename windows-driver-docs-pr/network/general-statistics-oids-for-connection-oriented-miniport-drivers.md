---
title: General statistics OIDs for connection-oriented miniport drivers
author: windows-driver-content
description: This topic describes general statistics OIDs for connection-oriented objects.
ms.assetid: 1967ebb9-0cc9-46ca-b9db-fc505f41c38e
keywords:
- General statistics OIDs connection-oriented miniport drivers
ms.author: windowsdriverdev
ms.date: 11/02/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# General statistics OIDs for connection-oriented miniport drivers

The following table summarizes the OIDs used to get or set the general statistics characteristics of connection-oriented miniport drivers and/or their NICs.

> [!TIP] 
> A connection-oriented miniport driver handles such requests in its [MiniportCoOidRequest](https://msdn.microsoft.com/library/windows/hardware/ff559362) callback function.

In this table, M indicates an OID is mandatory, while O indicates it is optional.

| Length | Query | Set | Name |
| --- | --- | --- | --- |
| 4 or 8 | O |   | [OID_GEN_CO_BYTES_RCV](oid-gen-co-bytes-rcv.md) |
| 4 or 8 | O |   | [OID_GEN_CO_BYTES_XMIT](oid-gen-co-bytes-xmit.md) |
| 4 or 8 | O |   | [OID_GEN_CO_BYTES_XMIT_OUTSTANDING](oid-gen-co-bytes-xmit-outstanding.md) |
| 4 or 8 | O |   | [OID_GEN_CO_NETCARD_LOAD](oid-gen-co-netcard-load.md) |
| 4 or 8 | O |   | [OID_GEN_CO_RCV_CRC_ERROR](oid-gen-co-rcv-crc-error.md) |
| 4 or 8 | M |   | [OID_GEN_CO_RCV_PDUS_ERROR](oid-gen-co-rcv-pdus-error.md) |
| 4 or 8 | M |   | [OID_GEN_CO_RCV_PDUS_NO_BUFFER](oid-gen-co-rcv-pdus-no-buffer.md) |
| 4 or 8 | M |   | [OID_GEN_CO_RCV_PDUS_OK](oid-gen-co-rcv-pdus-ok.md) |
| 4 or 8 | O |   | [OID_GEN_CO_TRANSMIT_QUEUE_LENGTH](oid-gen-co-transmit-queue-length.md) |
| 4 or 8 | M |   | [OID_GEN_CO_XMIT_PDUS_ERROR](oid-gen-co-xmit-pdus-error.md) |
| 4 or 8 | M |   | [OID_GEN_CO_XMIT_PDUS_OK](oid-gen-co-xmit-pdus-ok.md) |

## Miniport driver support for 64-bit counters

All one-Gbps and faster connection-oriented miniport drivers must support 64-bit counters for the following statistics OIDs. In addition, Microsoft recommends that all 100Mbps and faster connection-oriented miiniport drivers support 64-bit counters for the following statistics OIDs:

[OID_GEN_CO_XMIT_PDUS_OK](oid-gen-co-xmit-pdus-ok.md)

[OID_GEN_CO_RCV_PDUS_OK](oid-gen-co-rcv-pdus-ok.md)

[OID_GEN_CO_BYTES_XMIT](oid-gen-co-bytes-xmit.md)

[OID_GEN_CO_BYTES_RCV](oid-gen-co-bytes-rcv.md)

Such miniport drivers can also support 64-bit counters for other statistics OIDs, such as OIDs that indicate transmit or receive errors.

System support for 64-bit counters is available in Windows XP and later versions.

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")