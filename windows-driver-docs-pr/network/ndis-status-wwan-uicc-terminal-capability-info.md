---
title: NDIS_STATUS_WWAN_UICC_TERMINAL_CAPABILITY_INFO
description: NDIS_STATUS_WWAN_UICC_TERMINAL_CAPABILITY_INFO is sent to inform the MB host of the last terminal capability objects sent to the modem.
keywords:
- NDIS_STATUS_WWAN_UICC_TERMINAL_CAPABILITY_INFO
ms.date: 03/02/2022
ms.localizationpriority: medium
---

# NDIS_STATUS_WWAN_UICC_TERMINAL_CAPABILITY_INFO

The NDIS_STATUS_WWAN_UICC_TERMINAL_CAPABILITY_INFO status notification is sent by a modem miniport adapter to inform the MB host of the last terminal capability objects sent to the modem. This notification is sent in response to [OID_WWAN_UICC_TERMINAL_CAPABILITY](oid-wwan-uicc-terminal-capability.md) query and set requests.

This notification uses the [**NDIS_WWAN_UICC_TERMINAL_CAPABILITY_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_uicc_terminal_capability_info) structure.

## Requirements

**Version**: Windows 10, version 1607
**Header**: Ndis.h

## See also

[OID_WWAN_UICC_TERMINAL_CAPABILITY](oid-wwan-uicc-terminal-capability.md)

[**NDIS_WWAN_UICC_TERMINAL_CAPABILITY_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_uicc_terminal_capability_info)

[MB low level UICC access](mb-low-level-uicc-access.md)
