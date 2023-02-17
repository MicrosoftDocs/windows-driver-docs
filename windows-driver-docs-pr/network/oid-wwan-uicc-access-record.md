---
title: OID_WWAN_UICC_ACCESS_RECORD
ms.topic: reference
description: OID_WWAN_UICC_ACCESS_RECORD accesses a UICC linear fixed or cyclic file, the structure type of which is WwanUiccFileStructureCyclic or WwanUiccFileStructureLinear.
ms.date: 04/10/2019
keywords: 
 -OID_WWAN_UICC_ACCESS_RECORD Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# OID_WWAN_UICC_ACCESS_RECORD

OID_WWAN_UICC_ACCESS_RECORD accesses a UICC linear fixed or cyclic file, the structure type of which is **WwanUiccFileStructureCyclic** or **WwanUiccFileStructureLinear**.

Query requests read the contents of a record. Query payloads contain an [**NDIS_WWAN_UICC_ACCESS_RECORD**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_uicc_access_record) structure specifying information about the file to read. Miniport drivers must process Query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request before later sending an [NDIS_STATUS_WWAN_UICC_RECORD_RESPONSE](ndis-status-wwan-uicc-record-response.md) status notification containing an [**NDIS_WWAN_UICC_RESPONSE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_uicc_response) structure that describes the UICC's response. 

## Remarks

For more information about usage of this OID, see [MB UICC application and file system access](mb-uicc-application-and-file-system-access.md).

## Requirements

**Version**: Windows 10, version 1903
**Header**: Ntddndis.h (include Ndis.h)

## See also

[MB UICC application and file system access](mb-uicc-application-and-file-system-access.md)

[NDIS_STATUS_WWAN_UICC_RECORD_RESPONSE](ndis-status-wwan-uicc-record-response.md)

[**NDIS_WWAN_UICC_ACCESS_RECORD**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_uicc_access_record)

[**NDIS_WWAN_UICC_RESPONSE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_uicc_response)
