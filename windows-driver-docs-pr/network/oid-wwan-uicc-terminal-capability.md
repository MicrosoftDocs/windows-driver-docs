---
title: OID_WWAN_UICC_TERMINAL_CAPABILITY
description: The mobile broadband host sends OID_WWAN_UICC_TERMINAL_CAPABILITY to inform the modem about the terminal capabilities of the host. 
keywords:
- MB UICC terminal capability, Mobile Broadband UICC terminal capability, Mobile Broadband miniport driver UICC terminal capability
ms.date: 06/24/2022
ms.localizationpriority: medium
---

# OID_WWAN_UICC_TERMINAL_CAPABILITY

The mobile broadband host sends OID_WWAN_UICC_TERMINAL_CAPABILITY to a modem miniport adapter to inform the modem about the terminal capabilities of the host.

If the device supports dual SIM slots, the host can set terminal capability on either the active or  inactive SIM slot to inform the modem of the host OS's capabilities. The host can also query the terminal capability that persisted in the modem from a previous SIM insertion/reset.

For query requests, this OID's payload contains an [**NDIS_WWAN_QUERY_UICC_TERMINAL_CAPABILITY**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_query_uicc_terminal_capability) structure, which in turn contains a [**WWAN_QUERY_UICC_TERMINAL_CAPABILITY**](/windows-hardware/drivers/ddi/wwan/ns-wwan-wwan_query_uicc_terminal_capability) structure that specifies the slot ID.  Modem miniport drivers must process query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request before later sending an [NDIS_STATUS_WWAN_UICC_TERMINAL_CAPABILITY_INFO](ndis-status-wwan-uicc-terminal-capability-info.md) notification containing an [**NDIS_WWAN_UICC_TERMINAL_CAPABILITY_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_uicc_terminal_capability_info) structure, which in turn contains a [**WWAN_UICC_TERMINAL_CAPABILITY_INFO**](/windows-hardware/drivers/ddi/wwan/ns-wwan-wwan_uicc_terminal_capability_info) structure that represents the terminal capabilities.

For set requests, OID_WWAN_UICC_TERMINAL_CAPABILITY uses the [**NDIS_WWAN_SET_UICC_TERMINAL_CAPABILITY**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_set_uicc_terminal_capability) structure, which in turn contains a [**WWAN_SET_UICC_TERMINAL_CAPABILITY**](/windows-hardware/drivers/ddi/wwan/ns-wwan-wwan_set_uicc_terminal_capability) structure that represents the terminal capabilities and specifies the slot ID. The miniport driver responds with the NDIS_STATUS_WWAN_UICC_TERMINAL_CAPABILITY_INFO notification, which in turn contains an **NDIS_WWAN_UICC_TERMINAL_CAPABILITY_INFO** structure.

Unsolicited events are not applicable.

For more information, see [MB low level UICC access](mb-low-level-uicc-access.md).

## Requirements

**Version**: Windows 10, version 1607

**Header**: Ntddndis.h (include Ndis.h)

## See also

[NDIS_STATUS_WWAN_UICC_TERMINAL_CAPABILITY_INFO](ndis-status-wwan-uicc-terminal-capability-info.md)

[**NDIS_WWAN_UICC_TERMINAL_CAPABILITY_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_uicc_terminal_capability_info)

[**WWAN_UICC_TERMINAL_CAPABILITY_INFO**](/windows-hardware/drivers/ddi/wwan/ns-wwan-wwan_uicc_terminal_capability_info)

[**NDIS_WWAN_SET_UICC_TERMINAL_CAPABILITY**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_set_uicc_terminal_capability)

[**WWAN_SET_UICC_TERMINAL_CAPABILITY**](/windows-hardware/drivers/ddi/wwan/ns-wwan-wwan_set_uicc_terminal_capability)

[MB low level UICC access](mb-low-level-uicc-access.md)
