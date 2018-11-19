---
title: NDIS_STATUS_WWAN_NETWORK_BLACKLIST
description: Miniport drivers use the NDIS_STATUS_WWAN_NETWORK_BLACKLIST notification to inform the mobile broadband (MB) service about the completion of a previous OID_WWAN_NETWORK_BLACKLIST Query or Set request.
ms.assetid: 38ED7C51-D352-4B48-BF80-433A7C4642AB
ms.date: 08/21/2018
keywords: 
 -NDIS_STATUS_WWAN_NETWORK_BLACKLIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS_STATUS_WWAN_NETWORK_BLACKLIST

Miniport drivers use the **NDIS_STATUS_WWAN_NETWORK_BLACKLIST** notification to inform the mobile broadband (MB) service about the completion of a previous [OID_WWAN_NETWORK_BLACKLIST](oid-wwan-network-blacklist.md) Query or Set request.

Unsolicited events are sent if any of the blacklist states have changed from actuated to not actuated, or vice versa. For example, if a SIM is inserted whose provider matches the SIM provider blacklist.

This notification uses the [**NDIS_WWAN_NETWORK_BLACKLIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_network_blacklist) structure.

## Requirements

|   |   |
| --- | --- |
| Version | Windows 10, version 1703 |
| Header | Ntddndis.h (include Ndis.h) |

## See also

[MB Network Blacklist Operations](https://docs.microsoft.com/windows-hardware/drivers/network/mb-network-blacklist-operations)

[OID_WWAN_NETWORK_BLACKLIST](oid-wwan-network-blacklist.md)

[**NDIS_WWAN_NETWORK_BLACKLIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_network_blacklist)
