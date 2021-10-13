---
title: OID_WWAN_NETWORK_BLACKLIST
description: OID_WWAN_NETWORK_BLACKLIST gets or sets information about network blacklists for a mobile broadband (MBB) device.
ms.date: 08/21/2018
keywords: 
 -OID_WWAN_NETWORK_BLACKLIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID_WWAN_NETWORK_BLACKLIST

> [!IMPORTANT]
> ### Bias-free communication
>
> Microsoft supports a diverse and inclusive environment. This article contains references to terminology that the Microsoft [style guide for bias-free communication](/style-guide/bias-free-communication) recognizes as exclusionary. The word or phrase is used in this article for consistency because it currently appears in the software. When the software is updated to remove the language, this article will be updated to be in alignment.

OID_WWAN_NETWORK_BLACKLIST gets or sets information about network blacklists for a mobile broadband (MBB) device.

Miniport drivers must process Query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request before later sending an [NDIS_STATUS_WWAN_NETWORK_BLACKLIST](ndis-status-wwan-network-blacklist.md) status notification containing an [**NDIS_WWAN_NETWORK_BLACKLIST**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_network_blacklist) structure that describes the current network blacklists.

For Set requests, this OID's payload contains an [**NDIS_WWAN_SET_NETWORK_BLACKLIST**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_set_network_blacklist) structure that specifies a list of MNC/MCC combinations that should be ignored by the modem.

## Remarks

After each Query or Set request, the miniport driver should return an [**NDIS_WWAN_NETWORK_BLACKLIST**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_network_blacklist) structure that contains information about the current network blacklist information.

For more information about usage of this OID, see [MBIM_CID_MS_NETWORK_BLACKLIST](./mb-network-blacklist-operations.md#mbim_cid_ms_network_blacklist).

## Requirements

**Version**: Windows 10, version 1703
**Header**: Ntddndis.h (include Ndis.h)

## See also

[MB Network Blacklist Operations](./mb-network-blacklist-operations.md)

[NDIS_STATUS_WWAN_NETWORK_BLACKLIST](ndis-status-wwan-network-blacklist.md)

[**NDIS_WWAN_NETWORK_BLACKLIST**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_network_blacklist)

[**NDIS_WWAN_SET_NETWORK_BLACKLIST**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_set_network_blacklist)
