---
title: Mandatory OIDs for miniport drivers
description: This topic describes mandatory OIDs for miniport drivers 
ms.assetid: e4a620b4-de8f-4c1a-be94-b0ec97fa9791
keywords:
- Mandatory OIDs for miniport drivers, mandatory NDIS OIDs, mandatory OIDs WDK, mandatory OIDs networking
ms.date: 11/01/2017
ms.localizationpriority: medium
---

# Mandatory OIDs for miniport drivers

The following table lists the OIDs that are mandatory for all miniport drivers. Your miniport driver will be required to support additional OIDs, depending on its NDIS version and the services that it supports, such as:

- Connection-Oriented Objects 
- CoNDIS  
- Ethernet statistics OIDs 
- Header-Data Split OIDs 
- Hyper-V Extensible Switch OIDs 
- IPsec Offload Version 2 OIDs 
- MB OIDs 
- Native 802.11 Wireless LAN OIDs 
- NDIS TCP/IP Offload OIDs 
- NDKPI OIDs 
- Operational Power Management OIDs 
- Overview of Receive Filter OIDs 
- Receive Filter OIDs 
- Receive Side Scaling OIDs 
- Remote NDIS OIDs 
- Required and Optional OIDs for Power Management 
- SR-IOV OIDs 
- Statistical Power Management OIDs 
- Task Offload Objects 
- VMQ OIDs

In the "O/M" columns in the table: 

- "M" means "mandatory" and "O" means "optional."
- "N/A" in the "O/M for Query" column means that NDIS handles the OID query request and does not send it to the miniport driver, so the miniport driver only needs to support the OID set request. 
- If there is no entry in the "O/M for Query" column, this OID is a set-only OID.
- If there is no entry in the "O/M for Set" column, this OID is a query-only OID.

| OID | O/M for Query | O/M for Set | Comments |
| --- | --- | --- | --- |
| [OID_GEN_CURRENT_LOOKAHEAD](oid-gen-current-lookahead.md) | N/A | M | NDIS handles query and unsuccessful Set requests for the miniport driver. NDIS sends valid Set requests to the miniport driver. You can obtain the same information with [OID_GEN_RECEIVE_BLOCK_SIZE](oid-gen-receive-block-size.md). |
| [OID_GEN_CURRENT_PACKET_FILTER](oid-gen-current-packet-filter.md) | N/A | M | Query is not mandatory. Set is mandatory. |
| [OID_GEN_INTERRUPT_MODERATION](oid-gen-interrupt-moderation.md) | M | M |   |
| [OID_GEN_LINK_PARAMETERS](oid-gen-link-parameters.md) |   | M |   |
| [OID_GEN_MAXIMUM_TOTAL_SIZE](oid-gen-maximum-total-size.md) | M |   | There is no other way to get this information. |
| [OID_GEN_RCV_OK](oid-gen-rcv-ok.md) | M |   | NDIS does not handle this OID for miniport drivers and [OID_GEN_STATISTICS](oid-gen-statistics.md) does not include this information. **Note**: Statistics OIDs are mandatory unless NDIS handles them. |
| [OID_GEN_RECEIVE_BLOCK_SIZE](oid-gen-receive-block-size.md) | M |   | NDIS does not handle this OID for miniport drivers. |
| [OID_GEN_RECEIVE_BUFFER_SPACE](oid-gen-receive-buffer-space.md) | M |   | There is no other way to get this information. |
| [OID_GEN_STATISTICS](oid-gen-statistics.md) | M |   |   |
| [OID_GEN_TRANSMIT_BLOCK_SIZE](oid-gen-transmit-block-size.md) | M |   | There is no other way to get this information. |
| [OID_GEN_TRANSMIT_BUFFER_SPACE](oid-gen-transmit-buffer-space.md) | M |   | There is no other way to get this information. |
| [OID_GEN_VENDOR_DESCRIPTION](oid-gen-vendor-description.md) | M |   | There is no other way to get this information. |
| [OID_GEN_VENDOR_DRIVER_VERSION](oid-gen-vendor-driver-version.md) | M |   | There is no other way to get this information. |
| [OID_GEN_VENDOR_ID](oid-gen-vendor-id.md) | M |   | There is no other way to get this information. Independent hardware vendor's filter drivers or intermediate drivers might query this OID. |
| [OID_GEN_XMIT_OK](oid-gen-xmit-ok.md) | M |   | NDIS does not handle this OID and [OID_GEN_STATISTICS](oid-gen-statistics.md) does not include this information. **Note**: Statistics OIDs are mandatory unless NDIS handles them. |

