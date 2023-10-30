---
title: NDIS_STATUS_WWAN_BASE_STATIONS_INFO
ms.topic: reference
description: NDIS_STATUS_WWAN_BASE_STATIONS_INFO
keywords:
- NDIS_STATUS_WWAN_BASE_STATIONS_INFO, base stations information query status notification, Mobile Broadband base stations information query status notification, MB base stations information query status notification
ms.date: 03/02/2023
---

# NDIS_STATUS_WWAN_BASE_STATIONS_INFO

The NDIS_STATUS_WWAN_BASE_STATIONS_INFO notification is sent by modem miniport drivers in response to an [OID_WWAN_BASE_STATIONS_INFO](oid-wwan-base-stations-info.md) query request to provide the MB host with information about both serving and neighboring base stations.

This notification uses the [NDIS_WWAN_BASE_STATIONS_INFO](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_base_stations_info) structure.

## Requirements

**Version**: Windows 10, version 1709
**Header**: Ndis.h

## See also

[OID_WWAN_BASE_STATIONS_INFO](oid-wwan-base-stations-info.md)

[NDIS_WWAN_BASE_STATIONS_INFO](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_base_stations_info)

[MB base stations information query operations](mb-base-stations-information-query-support.md)
