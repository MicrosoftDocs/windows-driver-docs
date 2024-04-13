---
title: OID_WWAN_UICC_RESET
ms.topic: reference
description: OID_WWAN_UICC_RESET is sent by the mobile broadband host to a modem miniport adapter to reset a UICC smart card.
keywords:
- MB UICC reset, Mobile Broadband UICC reset, Mobile Broadband miniport driver UICC reset
ms.date: 06/24/2022
ms.localizationpriority: medium
---

# OID_WWAN_UICC_RESET

OID_WWAN_UICC_RESET is sent by the mobile broadband host to a modem miniport adapter to reset a UICC smart card and specify the UICC's passthrough status after reset, or query the passthrough state of the adapter.

The host can query the passthrough state from either the active SIM slot or inactive SIM slot in the device if the device supports dual SIM slots. This OID's payload for query requests contains an [**NDIS_WWAN_QUERY_UICC_RESET**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_query_uicc_reset) structure, which in turn contains a [**WWAN_QUERY_UICC_RESET**](/windows-hardware/drivers/ddi/wwan/ns-wwan-wwan_query_uicc_reset) structure that specifies the UICC slot ID.

Modem miniport drivers must process query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request before later sending an [NDIS_STATUS_WWAN_UICC_RESET_INFO](ndis-status-wwan-uicc-reset-info.md) notification containing a [**NDIS_WWAN_UICC_RESET_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_uicc_reset_info) structure, which in turn contains a [**WWAN_UICC_RESET_INFO**](/windows-hardware/drivers/ddi/wwan/ns-wwan-_wwan_uicc_reset_info) structure that represents the passthrough status of the adapter.

The host can reset either the active SIM slot or inactive SIM slot in the device if the device supports dual SIM slots. For set requests, OID_WWAN_UICC_RESET uses the [**NDIS_WWAN_SET_UICC_RESET**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_set_uicc_reset) structure, which in turn contains a [**WWAN_SET_UICC_RESET**](/windows-hardware/drivers/ddi/wwan/ns-wwan-_wwan_set_uicc_reset) structure that represents the passthrough action the host specifies for the miniport adapter after it resets the UICC. After reset is complete, the miniport adapter responds with the NDIS_STATUS_WWAN_UICC_RESET_INFO notification, which in turn contains a [**NDIS_WWAN_UICC_RESET_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_uicc_reset_info) structure, to indicate its passthrough status.

Unsolicited events are not applicable.

For more info about passthrough actions and passthrough status, see [MB low level UICC access](mb-low-level-uicc-access.md).

## Requirements

**Version**: Windows 10, version 1709

**Header**: Ntddndis.h (include Ndis.h)

## See also

[**NDIS_WWAN_QUERY_UICC_RESET**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_query_uicc_reset)

[**WWAN_QUERY_UICC_RESET**](/windows-hardware/drivers/ddi/wwan/ns-wwan-wwan_query_uicc_reset)

[**NDIS_WWAN_UICC_RESET_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_uicc_reset_info)

[**WWAN_UICC_RESET_INFO**](/windows-hardware/drivers/ddi/wwan/ns-wwan-_wwan_uicc_reset_info)

[**NDIS_WWAN_SET_UICC_RESET**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_set_uicc_reset)

[**WWAN_SET_UICC_RESET**](/windows-hardware/drivers/ddi/wwan/ns-wwan-_wwan_set_uicc_reset)

[NDIS_STATUS_WWAN_UICC_RESET_INFO](ndis-status-wwan-uicc-reset-info.md)

[MB low level UICC access](mb-low-level-uicc-access.md)
