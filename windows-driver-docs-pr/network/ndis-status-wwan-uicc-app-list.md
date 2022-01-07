---
title: NDIS_STATUS_WWAN_UICC_APP_LIST
description: Miniport drivers use the NDIS_STATUS_WWAN_UICC_APP_LIST notification to inform the mobile broadband (MB) service about the completion of a previous OID_WWAN_UICC_APP_LIST Query request.
ms.date: 04/08/2019
keywords: 
 -NDIS_STATUS_WWAN_UICC_APP_LIST Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# NDIS_STATUS_WWAN_UICC_APP_LIST

Miniport drivers use the **NDIS_STATUS_WWAN_UICC_APP_LIST** notification to inform the mobile broadband (MB) service about the completion of a previous [OID_WWAN_UICC_APP_LIST](oid-wwan-uicc-app-list.md) Query request.

Unsolicited events are not applicable.

This notification uses the [**NDIS_WWAN_UICC_APP_LIST**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_uicc_app_list) structure.

## Requirements

**Version**: Windows 10, version 1903
**Header**: Ntddndis.h (include Ndis.h)

## See also

[MB UICC application and file system access](mb-uicc-application-and-file-system-access.md)

[OID_WWAN_UICC_APP_LIST](oid-wwan-uicc-app-list.md)

[**NDIS_WWAN_UICC_APP_LIST**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_uicc_app_list)
