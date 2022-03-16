---
title: OID_WWAN_UICC_ATR
description: An OID_WWAN_UICC_ATR query request is sent to a modem miniport adapter to get the UICC smart card's Answer to Reset (ATR) information.
keywords:
- MB UICC reset, Mobile Broadband UICC reset, Mobile Broadband miniport driver UICC reset
ms.date: 02/24/2022
ms.localizationpriority: medium
---

# OID_WWAN_UICC_ATR

An OID_WWAN_UICC_ATR query request is sent by the mobile broadband host to a modem miniport adapter to get the UICC smart card's Answer to Reset (ATR) information. The ATR is the first string of bytes sent by the UICC after a reset has been performed. It describes the capabilities of the card, such as the number of logical channels that it supports.

The host can query the ATR information from either the active SIM slot or the inactive SIM slot in the device if the device supports dual SIM slots. This OID's payload contains an [**NDIS_WWAN_QUERY_ATR_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_query_atr_info) structure, which in turn contains a [**WWAN_QUERY_ATR_INFO**](/windows-hardware/drivers/ddi/wwan/ns-wwan-wwan_query_atr_info) structure that specifies the UICC slot ID. 

Modem miniport drivers must process query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request before later sending an [NDIS_STATUS_WWAN_ATR_INFO](ndis-status-wwan-atr-info.md) notification containing a [**NDIS_WWAN_ATR_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_atr_info) structure, which in turn contains a [**WWAN_QUERY_ATR_INFO**](/windows-hardware/drivers/ddi/wwan/ns-wwan-wwan_atr_info) structure that represents the passthrough status of the adapter.

Unsolicited events are not applicable.

For more info, see [MB low level UICC access](mb-low-level-uicc-access.md).

## Requirements

**Version**: Windows 10, version 1607
**Header**: Ntddndis.h (include Ndis.h)

## See also

[NDIS_STATUS_WWAN_ATR_INFO](ndis-status-wwan-atr-info.md)

[**NDIS_WWAN_QUERY_ATR_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_query_atr_info)

[**WWAN_QUERY_ATR_INFO**](/windows-hardware/drivers/ddi/wwan/ns-wwan-wwan_query_atr_info)

[**NDIS_WWAN_ATR_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_atr_info)

[**WWAN_ATR_INFO**](/windows-hardware/drivers/ddi/wwan/ns-wwan-wwan_atr_info)

[MB low level UICC access](mb-low-level-uicc-access.md)
