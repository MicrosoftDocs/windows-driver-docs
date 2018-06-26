---
title: OID_WWAN_MPDP
author: windows-driver-content
description: OID_WWAN_MPDP 
ms.assetid: 2A8E496A-212A-4999-A82C-9B97CEEC2C7E
keywords:
- OID_WWAN_MPDP, MPDP OID
ms.author: windowsdriverdev
ms.date: 06/25/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OID_WWAN_MPDP

OID_WWAN_MPDP sets or queries information about multiple Packet Data Protocol (MPDP) interfaces, or NetAdapter objects, for a Mobile Broadband WDF Class Extension (MBBCx) client driver. 

> [!IMPORTANT]
> This OID is handled by MBBCx on behalf of MBBCx client drivers.

For query requests, MBBCx responds to NDIS asynchronously by initially returning NDIS_STATUS_INDICATION_REQUIRED. After the query request is complete, MBBCx sends an [NDIS_STATUS_WWAN_MPDP_LIST](ndis-status-wwan-mpdp-list.md) notification that contains a list of child interfaces for the primary NetAdapter, formatted in an [**NDIS_WWAN_MPDP_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_mpdp_list) structure. Each child interface corresponds to a NetAdapter object that the MBBCx client driver has created.

For set requests, MBBCx responds to NDIS asynchronously by returning NDIS_STATUS_INDICATION_REQUIRED. The set request contains an [**NDIS_WWAN_SET_MPDP_STATE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_set_mpdp_state) structure, which in turn contains an [**NDIS_WWAN_MPDP_INFO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_mpdp_info) structure with information for the operation that MBBCx should take. 

If the **Operation** member of the **NDIS_WWAN_MPDP_INFO** structure is set to **WwanMPDPOperationCreateChildInterface**, MBBCx invokes the client driver's [*EvtMbbDeviceCreateAdapter*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/mbbcx/nc-mbbcx-evt_mbb_device_create_adapter) callback. The status result of this callback, along with the GUID of the newly created child interface if the operation was successful, are returned to NDIS in an [**NDIS_WWAN_MPDP_STATE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_mpdp_state) structure contained in an [NDIS_STATUS_WWAN_MPDP_STATE](ndis-status-wwan-mpdp-state.md) notification.

If the **Operation** member of the **NDIS_WWAN_MPDP_INFO** structure is set to **WwanMPDPOperationDeleteChildInterface**, MBBCx deletes the corresponding NetAdapter object previously created by the client driver and returns information about the deletion operation to NDIS in an [**NDIS_WWAN_MPDP_STATE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_mpdp_state) structure contained in an [NDIS_STATUS_WWAN_MPDP_STATE](ndis-status-wwan-mpdp-state.md) notification. Because MBBCx manages the lifetime of the MPDP interfaces/NetAdapter objects this way, MBBCx client drivers must not delete the NetAdapter objects they create.

## Requirements

|   |   |
| --- | --- |
| Version | Windows 10, version 1809 |
| Header | Ntddndis.h (include Ndis.h) |

## See also

[Mobile Broadband (MBB) WDF class extension (MBBCx)](../netcx/mobile-broadband-mbb-wdf-class-extension-mbbcx.md)

[Writing an MBBCx client driver](../netcx/writing-an-mbbcx-client-driver.md)

[NDIS_STATUS_WWAN_MPDP_LIST](ndis-status-wwan-mpdp-list.md)

[**NDIS_WWAN_MPDP_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_mpdp_list)

[**NDIS_WWAN_SET_MPDP_STATE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_set_mpdp_state)

[**NDIS_WWAN_MPDP_INFO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_mpdp_info)

[NDIS_STATUS_WWAN_MPDP_STATE](ndis-status-wwan-mpdp-state.md)

[**NDIS_WWAN_MPDP_STATE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_mpdp_state)

[*EvtMbbDeviceCreateAdapter*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/mbbcx/nc-mbbcx-evt_mbb_device_create_adapter)