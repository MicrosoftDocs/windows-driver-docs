---
title: OID_GEN_CO_MEDIA_SUPPORTED
description: This topic describes the OID_GEN_CO_MEDIA_SUPPORTED object identifier (OID).
ms.assetid: 688d5054-f92d-4054-bf6e-dcf43fcfeb06
keywords:
- OID_GEN_CO_MEDIA_SUPPORTED
ms.date: 11/02/2017
ms.localizationpriority: medium
---

# OID_GEN_CO_MEDIA_SUPPORTED

A complete list of the media types the NIC supports, as a proper subset of the following system-defined values:

**NdisMedium802_3**  
Ethernet (802.3).

**NdisMedium802_5**  
Token Ring (802.5).

**NdisMediumFddi**  
FDDI.

**NdisMediumWan**  
WAN.

**NdisMediumLocalTalk**  
LocalTalk.

**NdisMediumDix**  
DEC/Intel/Xerox (DIX) Ethernet.

**NdisMediumArcnetRaw**  
ARCNET (raw).

**NdisMediumArcnet878_2**  
ARCNET (878.2).

**NdisMediumWirelessWan**  
Various types of NdisWirelessXxx media.

**NdisMediumAtm**  
ATM.

**NdisMediumIrda**  
Reserved for future use on Windows 2000 and later platforms.

## Remarks

A LAN-emulation driver for ATM networks declares its medium as **NdisMedium802_3** , rather than **NdisMediumAtm**. Such a driver emulates Ethernet to higher-level NDIS drivers, complies with the ATM Forum's LANE, and provides UNI signaling support.

A wireless-WAN NIC driver must report its medium type as **NdisMediumWirelessWan**. However, such a miniport driver also must provide **NdisWWDIXEthernetFrames** header format to any bound protocol that selects this format, and the miniport driver can provide its NIC's native header format as well. To support existing LAN-based protocols, the driver writer can provide an NDIS intermediate driver to "translate" a wireless NIC's native header formats and medium-specific information into a form understood by existing protocols.

If the underlying miniport driver returns **NULL** for this query or if an experimental media type is used, the driver must indicate receives with [NdisMCoIndicateReceivePacket](https://msdn.microsoft.com/library/windows/hardware/ff553455).


## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

