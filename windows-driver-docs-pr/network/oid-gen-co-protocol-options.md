---
title: OID_GEN_CO_PROTOCOL_OPTIONS
description: This topic describes the OID_GEN_CO_PROTOCOL_OPTIONS object identifier (OID).
ms.assetid: 5c1212e4-1fd2-435a-ae8c-9f75522cbca6
keywords:
- OID_GEN_CO_PROTOCOL_OPTIONS
ms.date: 11/02/2017
ms.localizationpriority: medium
---

# OID_GEN_CO_PROTOCOL_OPTIONS

A bitmask that defines optional properties of the protocol driver. A protocol informs NDIS of its properties, which can optionally take advantage of them. If the protocol driver does not set its flags on a binding, NDIS assumes they are all clear.

The following flags are currently defined:

NDIS_PROT_OPTION_ESTIMATED_LENGTH  
Indicates that packets can be indicated at the worst-case estimate of packet size, instead of an exact value, to this protocol.

NDIS_PROT_OPTION_NO_LOOPBACK  
The protocol does not require loopback support on the binding.

NDIS_PROT_OPTION_NO_RSVD_ON_RCVPKT  
The protocol does not use the **ProtocolReserved** section of indicated receive packets. This allows NDIS to indicate a receive packet to more than one protocol.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

