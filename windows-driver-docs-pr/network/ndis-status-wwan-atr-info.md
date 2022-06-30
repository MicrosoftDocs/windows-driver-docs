---
title: NDIS_STATUS_WWAN_ATR_INFO
description: Miniport drivers use the NDIS_STATUS_WWAN_ATR_INFO notification to respond to OID query requests of OID_WWAN_UICC_ATR.
keywords:
- NDIS_STATUS_WWAN_ATR_INFO
ms.date: 06/24/2022
ms.localizationpriority: medium
---

# NDIS_STATUS_WWAN_ATR_INFO

Miniport drivers use the NDIS_STATUS_WWAN_ATR_INFO notification to respond to OID query requests of [OID_WWAN_UICC_ATR](oid-wwan-uicc-atr.md).

This notification uses the [**NDIS_WWAN_ATR_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_atr_info) structure.

## Requirements

**Version**: Windows 10, version 1607

**Header**: Ntddndis.h (include Ndis.h)

## See also

[OID_WWAN_UICC_ATR](oid-wwan-uicc-atr.md)

[**NDIS_WWAN_ATR_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_atr_info)

[MB low level UICC access](mb-low-level-uicc-access.md)
