---
title: OID_WWAN_UICC_ACCESS_BINARY
description: OID_WWAN_UICC_ACCESS_BINARY accesses a UICC binary file, the structure type of which is WwanUiccFileStructureTransparent or WwanUiccFileStructureBerTLV.
ms.date: 04/10/2019
keywords: 
 -OID_WWAN_UICC_ACCESS_BINARY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# OID_WWAN_UICC_ACCESS_BINARY

OID_WWAN_UICC_ACCESS_BINARY accesses a UICC binary file, the structure type of which is **WwanUiccFileStructureTransparent** or **WwanUiccFileStructureBerTLV**.

Query requests read a binary file. Query payloads contain an [**NDIS_WWAN_UICC_ACCESS_BINARY**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_uicc_access_binary) structure specifying information about the file to read. Miniport drivers must process Query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request before later sending an [NDIS_STATUS_WWAN_UICC_BINARY_RESPONSE](ndis-status-wwan-uicc-binary-response.md) status notification containing an [**NDIS_WWAN_UICC_RESPONSE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_uicc_response) structure that describes the UICC's response. 

## Remarks

For more information about usage of this OID, see [MB UICC application and file system access](mb-uicc-application-and-file-system-access.md).

## Requirements

**Version**: Windows 10, version 1903
**Header**: Ntddndis.h (include Ndis.h)

## See also

[MB UICC application and file system access](mb-uicc-application-and-file-system-access.md)

[NDIS_STATUS_WWAN_UICC_BINARY_RESPONSE](ndis-status-wwan-uicc-binary-response.md)

[**NDIS_WWAN_UICC_ACCESS_BINARY**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_uicc_access_binary) 

[**NDIS_WWAN_UICC_RESPONSE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_uicc_response)
