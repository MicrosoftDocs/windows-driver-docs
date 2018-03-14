---
title: OID_WWAN_BASE_STATIONS_INFO
description: OID_WWAN_BASE_STATIONS_INFO
ms.assetid: 041CFD25-7CEA-4041-B723-E42FB8189461
keywords:
- MB base stations info OID, Mobile Broadband base stations info OID, Mobile Broadband miniport driver base stations info OID
ms.author: windowsdriverdev
ms.date: 08/21/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OID_WWAN_BASE_STATIONS_INFO

OID_WWAN_BASE_STATIONS_INFO retrieves information about the serving and neighboring cells known to the modem. For more info about cellular base station information query, see [MB base stations information query support](mb-base-stations-information-query-support.md).

For query requests, OID_WWAN_BASE_STATIONS_INFO uses the [NDIS_WWAN_BASE_STATIONS_INFO_REQ](https://msdn.microsoft.com/library/windows/hardware/4327021B-93FB-4605-B7D1-A7A6D661C8DF) structure, which in turn contains a [WWAN_BASE_STATIONS_INFO](https://msdn.microsoft.com/library/windows/hardware/66460B28-C2B4-4F05-A133-31A753AF9489) structure that specifies aspects of the cell information, such as the maximum number of neighbor cell measurements, to send in response. Modem miniport drivers must process query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request before later sending an [NDIS_STATUS_WWAN_BASE_STATIONS_INFO](ndis-status-wwan-base-stations-info.md) notification containing an [NDIS_WWAN_BASE_STATIONS_INFO](https://msdn.microsoft.com/library/windows/hardware/7C0E0903-F564-4F2B-95F9-FA8512FEF61B) structure, which in turn contains a [WWAN_BASE_STATIONS_INFO](https://msdn.microsoft.com/library/windows/hardware/66460B28-C2B4-4F05-A133-31A753AF9489) structure that provides information about both serving and neighboring base stations.

Set requests are not applicable.

Unsolicited events are not applicable.

## Requirements

| | |
| --- | --- |
| Version | Windows 10, version 1709 |
| Header | Ntddndis.h (include Ndis.h) |

## See also

[NDIS_WWAN_BASE_STATIONS_INFO_REQ](https://msdn.microsoft.com/library/windows/hardware/4327021B-93FB-4605-B7D1-A7A6D661C8DF)

[NDIS_STATUS_WWAN_BASE_STATIONS_INFO](ndis-status-wwan-base-stations-info.md)

[NDIS_WWAN_BASE_STATIONS_INFO](https://msdn.microsoft.com/library/windows/hardware/7C0E0903-F564-4F2B-95F9-FA8512FEF61B)

[WWAN_BASE_STATIONS_INFO](https://msdn.microsoft.com/library/windows/hardware/66460B28-C2B4-4F05-A133-31A753AF9489)

[MB base stations information query support](mb-base-stations-information-query-support.md)

