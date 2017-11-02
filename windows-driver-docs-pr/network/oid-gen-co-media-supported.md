---
title: OID_GEN_CO_MEDIA_SUPPORTED
author: windows-driver-content
description: This topic describes the OID_GEN_CO_MEDIA_SUPPORTED object identifier (OID).
ms.assetid: 688d5054-f92d-4054-bf6e-dcf43fcfeb06
keywords:
- OID_GEN_CO_MEDIA_SUPPORTED
ms.author: windowsdriverdev
ms.date: 11/02/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")