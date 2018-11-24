---
title: OID_WWAN_MPDP
description: OID_WWAN_MPDP sets or queries information about Multiple Packet Data Protocol (MPDP) interfaces for the MB device representing the primary PDP context/EPS bearer.
ms.assetid: 2A8E496A-212A-4999-A82C-9B97CEEC2C7E
keywords:
- OID_WWAN_MPDP, MPDP OID
ms.date: 06/25/2018
---

# OID_WWAN_MPDP

OID_WWAN_MPDP sets or queries information about Multiple Packet Data Protocol (MPDP) interfaces for the MB device representing the primary PDP context/EPS bearer.

For query requests, the miniport driver responds to the MB service asynchronously by initially returning NDIS_STATUS_INDICATION_REQUIRED. After the query request is complete, the driver sends an [NDIS_STATUS_WWAN_MPDP_LIST](ndis-status-wwan-mpdp-list.md) notification that contains a list of child interfaces for the primary PDP context, formatted in an [**NDIS_WWAN_MPDP_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_mpdp_list) structure.

For set requests, like with query requests the miniport driver responds to the MB service asynchronously by initially returning NDIS_STATUS_INDICATION_REQUIRED. The set request contains an [**NDIS_WWAN_SET_MPDP_STATE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_set_mpdp_state) structure, which in turn contains an [**NDIS_WWAN_MPDP_INFO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_mpdp_info) structure with information for the operation. 

If the **Operation** member of the **NDIS_WWAN_MPDP_INFO** structure is set to **WwanMPDPOperationCreateChildInterface**, the client driver creates a new child interface for the primary PDP context. The status result of this operation, along with the GUID of the newly created child interface if the operation was successful, are returned to the MB service in an [**NDIS_WWAN_MPDP_STATE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_mpdp_state) structure contained in an [NDIS_STATUS_WWAN_MPDP_STATE](ndis-status-wwan-mpdp-state.md) notification.

If the **Operation** member of the **NDIS_WWAN_MPDP_INFO** structure is set to **WwanMPDPOperationDeleteChildInterface**, the miniport driver deletes the corresponding child interface it previously created and returns information about the deletion operation to the MB service in an [**NDIS_WWAN_MPDP_STATE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_mpdp_state) structure contained in an [NDIS_STATUS_WWAN_MPDP_STATE](ndis-status-wwan-mpdp-state.md) notification.

## Requirements

|   |   |
| --- | --- |
| Version | Windows 10, version 1809 |
| Header | Ntddndis.h (include Ndis.h) |

## See also

[NDIS_STATUS_WWAN_MPDP_LIST](ndis-status-wwan-mpdp-list.md)

[**NDIS_WWAN_MPDP_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_mpdp_list)

[**NDIS_WWAN_SET_MPDP_STATE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_set_mpdp_state)

[**NDIS_WWAN_MPDP_INFO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_mpdp_info)

[NDIS_STATUS_WWAN_MPDP_STATE](ndis-status-wwan-mpdp-state.md)

[**NDIS_WWAN_MPDP_STATE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_mpdp_state)

[*EvtMbbDeviceCreateAdapter*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/mbbcx/nc-mbbcx-evt_mbb_device_create_adapter)
