---
title: NDIS_STATUS_WWAN_UICC_RECORD_RESPONSE
description: Miniport drivers use the NDIS_STATUS_WWAN_UICC_RECORD_RESPONSE notification to inform the mobile broadband (MB) service about the completion of a previous OID_WWAN_UICC_ACCESS_RECORD Query request.
ms.date: 04/10/2019
keywords: 
 -NDIS_STATUS_WWAN_UICC_RECORD_RESPONSE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# NDIS_STATUS_WWAN_UICC_RECORD_RESPONSE

Miniport drivers use the **NDIS_STATUS_WWAN_UICC_RECORD_RESPONSE** notification to inform the mobile broadband (MB) service about the completion of a previous [OID_WWAN_UICC_ACCESS_RECORD](oid-wwan-uicc-access-record.md) Query or Set request.

Unsolicited events are not applicable.

This notification uses the [**NDIS_WWAN_UICC_RESPONSE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_uicc_response) structure.

## Requirements

**Version**: Windows 10, version 1903
**Header**: Ntddndis.h (include Ndis.h)

## See also

[MB UICC application and file system access](mb-uicc-application-and-file-system-access.md)

[OID_WWAN_UICC_ACCESS_RECORD](oid-wwan-uicc-access-record.md)

[**NDIS_WWAN_UICC_RESPONSE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_uicc_response)
