---
title: NDIS_STATUS_WWAN_UICC_BINARY_RESPONSE
ms.topic: reference
description: Miniport drivers use the NDIS_STATUS_WWAN_UICC_BINARY_RESPONSE notification to inform the mobile broadband (MB) service about the completion of a previous OID_WWAN_UICC_ACCESS_BINARY Query request.
ms.date: 03/02/2023
keywords: 
 -NDIS_STATUS_WWAN_UICC_BINARY_RESPONSE Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# NDIS_STATUS_WWAN_UICC_BINARY_RESPONSE

Miniport drivers use the **NDIS_STATUS_WWAN_UICC_BINARY_RESPONSE** notification to inform the mobile broadband (MB) service about the completion of a previous [OID_WWAN_UICC_ACCESS_BINARY](oid-wwan-uicc-access-binary.md) Query or Set request.

Unsolicited events are not applicable.

This notification uses the [**NDIS_WWAN_UICC_RESPONSE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_uicc_response) structure.

## Requirements

**Version**: Windows 10, version 1903
**Header**: Ntddndis.h (include Ndis.h)

## See also

[MB UICC application and file system access](mb-uicc-application-and-file-system-access.md)

[OID_WWAN_UICC_ACCESS_BINARY](oid-wwan-uicc-access-binary.md)

[**NDIS_WWAN_UICC_RESPONSE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_uicc_response)
