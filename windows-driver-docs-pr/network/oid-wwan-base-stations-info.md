---
title: OID_WWAN_BASE_STATIONS_INFO
description: OID_WWAN_BASE_STATIONS_INFO
keywords:
- MB base stations info OID, Mobile Broadband base stations info OID, Mobile Broadband miniport driver base stations info OID
ms.date: 08/21/2017
ms.localizationpriority: medium
---

# OID_WWAN_BASE_STATIONS_INFO

OID_WWAN_BASE_STATIONS_INFO retrieves information about the serving and neighboring cells known to the modem. For more info about cellular base station information query, see [MB base stations information query support](mb-base-stations-information-query-support.md).

For query requests, OID_WWAN_BASE_STATIONS_INFO uses the [NDIS_WWAN_BASE_STATIONS_INFO_REQ](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_base_stations_info_req) structure, which in turn contains a [WWAN_BASE_STATIONS_INFO](/windows-hardware/drivers/ddi/wwan/ns-wwan-_wwan_base_stations_info) structure that specifies aspects of the cell information, such as the maximum number of neighbor cell measurements, to send in response. Modem miniport drivers must process query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request before later sending an [NDIS_STATUS_WWAN_BASE_STATIONS_INFO](ndis-status-wwan-base-stations-info.md) notification containing an [NDIS_WWAN_BASE_STATIONS_INFO](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_base_stations_info) structure, which in turn contains a [WWAN_BASE_STATIONS_INFO](/windows-hardware/drivers/ddi/wwan/ns-wwan-_wwan_base_stations_info) structure that provides information about both serving and neighboring base stations.

Set requests are not applicable.

Unsolicited events are not applicable.

## Requirements

**Version**: Windows 10, version 1709
**Header**: Ntddndis.h (include Ndis.h)

## See also

[NDIS_WWAN_BASE_STATIONS_INFO_REQ](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_base_stations_info_req)

[NDIS_STATUS_WWAN_BASE_STATIONS_INFO](ndis-status-wwan-base-stations-info.md)

[NDIS_WWAN_BASE_STATIONS_INFO](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_base_stations_info)

[WWAN_BASE_STATIONS_INFO](/windows-hardware/drivers/ddi/wwan/ns-wwan-_wwan_base_stations_info)

[MB base stations information query support](mb-base-stations-information-query-support.md)
