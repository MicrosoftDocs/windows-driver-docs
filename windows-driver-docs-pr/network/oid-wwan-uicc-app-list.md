---
title: OID_WWAN_UICC_APP_LIST
description: OID_WWAN_UICC_APP_LIST retrieves a list of applications in a UICC and information about them.
ms.date: 04/08/2019
keywords: 
 -OID_WWAN_UICC_APP_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# OID_WWAN_UICC_APP_LIST

OID_WWAN_UICC_APP_LIST retrieves a list of applications in a UICC and information about them.

Miniport drivers must process Query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request before later sending an [NDIS_STATUS_WWAN_UICC_UICC_APP_LIST](ndis-status-wwan-uicc-app-list.md) status notification containing an [**NDIS_WWAN_UICC_APP_LIST**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_uicc_app_list) structure that describes the app list for the UICC.

Set requests are not applicable.

## Remarks

When the UICC in the modem is fully initialized and ready to register with the mobile operator, a UICC application must be selected for registration and a Query request with this OID should return the selected application in the **ActiveAppIndex** field of the [**WWAN_UICC_APP_LIST**](/windows-hardware/drivers/ddi/wwan/ns-wwan-_wwan_uicc_app_list) structure used in response.

For more information about usage of this OID, see [MB UICC application and file system access](mb-uicc-application-and-file-system-access.md).

## Requirements

**Version**: Windows 10, version 1903
**Header**: Ntddndis.h (include Ndis.h)

## See also

[MB UICC application and file system access](mb-uicc-application-and-file-system-access.md)

[NDIS_STATUS_WWAN_UICC_UICC_APP_LIST](ndis-status-wwan-uicc-app-list.md)

[**NDIS_WWAN_UICC_APP_LIST**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_uicc_app_list)

[**WWAN_UICC_APP_LIST**](/windows-hardware/drivers/ddi/wwan/ns-wwan-_wwan_uicc_app_list)
