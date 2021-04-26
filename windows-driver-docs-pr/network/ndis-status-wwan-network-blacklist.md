---
title: NDIS_STATUS_WWAN_NETWORK_BLACKLIST
description: Miniport drivers use the NDIS_STATUS_WWAN_NETWORK_BLACKLIST notification to inform the mobile broadband (MB) service about the completion of a previous OID_WWAN_NETWORK_BLACKLIST Query or Set request.
ms.date: 08/21/2018
keywords: 
 -NDIS_STATUS_WWAN_NETWORK_BLACKLIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS_STATUS_WWAN_NETWORK_BLACKLIST

> [!IMPORTANT]
> ### Bias-free communication
>
> Microsoft supports a diverse and inclusive environment. This article contains references to terminology that the Microsoft [style guide for bias-free communication](/style-guide/bias-free-communication) recognizes as exclusionary. The word or phrase is used in this article for consistency because it currently appears in the software. When the software is updated to remove the language, this article will be updated to be in alignment.

Miniport drivers use the **NDIS_STATUS_WWAN_NETWORK_BLACKLIST** notification to inform the mobile broadband (MB) service about the completion of a previous [OID_WWAN_NETWORK_BLACKLIST](oid-wwan-network-blacklist.md) Query or Set request.

Unsolicited events are sent if any of the blacklist states have changed from actuated to not actuated, or vice versa. For example, if a SIM is inserted whose provider matches the SIM provider blacklist.

This notification uses the [**NDIS_WWAN_NETWORK_BLACKLIST**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_network_blacklist) structure.

## Requirements

**Version**: Windows 10, version 1703
**Header**: Ntddndis.h (include Ndis.h)

## See also

[MB Network Blacklist Operations](./mb-network-blacklist-operations.md)

[OID_WWAN_NETWORK_BLACKLIST](oid-wwan-network-blacklist.md)

[**NDIS_WWAN_NETWORK_BLACKLIST**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_network_blacklist)
