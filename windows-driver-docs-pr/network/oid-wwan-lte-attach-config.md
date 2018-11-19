---
title: OID_WWAN_LTE_ATTACH_CONFIG
description: OID_WWAN_LTE_ATTACH_CONFIG enables the operating system to query or set the default LTE attach context of the inserted SIM's provider (MCC/MNC pair).
ms.assetid: 7E753513-D6A2-4B67-9AED-83A695C39D3C
ms.date: 08/22/2018
keywords: 
 -OID_WWAN_LTE_ATTACH_CONFIG Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID_WWAN_LTE_ATTACH_CONFIG

OID_WWAN_LTE_ATTACH_CONFIG enables the operating system to query or set the default LTE attach context of the inserted SIM's provider (MCC/MNC pair).

Miniport drivers must process Query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request before later sending an [NDIS_STATUS_WWAN_LTE_ATTACH_CONFIG](ndis-status-wwan-lte-attach-config.md) status notification containing an [**NDIS_WWAN_LTE_ATTACH_CONTEXTS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_lte_attach_contexts) structure that describes the LTE attach configuration.

For Set requests, this OID's payload contains an [**NDIS_WWAN_SET_LTE_ATTACH_CONTEXT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_set_lte_attach_context) structure that describes LTE attach context information for the modem to set.

## Remarks

After each Query or Set request, the miniport driver should return an [NDIS_STATUS_WWAN_LTE_ATTACH_CONFIG](ndis-status-wwan-lte-attach-config.md) notification that describes the LTE attach configuration.

For more information about using this OID, see [MBIM_CID_MS_LTE_ATTACH_CONFIG](mb-lte-attach-operations.md).

## Requirements

|   |   |
| --- | --- |
| Version | Windows 10, version 1703 |
| Header | Ntddndis.h (include Ndis.h) |

## See also

[MB LTE Attach Operations](mb-lte-attach-operations.md)

[NDIS_STATUS_WWAN_LTE_ATTACH_CONFIG](ndis-status-wwan-lte-attach-config.md)

[**NDIS_WWAN_LTE_ATTACH_CONTEXTS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_lte_attach_contexts)

[**NDIS_WWAN_SET_LTE_ATTACH_CONTEXT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_set_lte_attach_context)
