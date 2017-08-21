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

For query requests, OID_WWAN_BASE_STATIONS_INFO uses the [NDIS_WWAN_BASE_STATIONS_INFO_REQ](TBD) structure, which in turn contains a [WWAN_BASE_STATIONS_INFO](TBD) structure that specifies aspects of the cell information, such as the maximum number of neighbor cell measurements, to send in response. Modem miniport drivers must process query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request before later sending an [NDIS_STATUS_WWAN_BASE_STATIONS_INFO](ndis-status-wwan-base-stations-info.md) notification containing an [NDIS_WWAN_BASE_STATIONS_INFO](TBD) structure, which in turn contains a [WWAN_BASE_STATIONS_INFO](TBD) structure that provides information about both serving and neighboring base stations.

Set requests are not applicable.

Unsolicited events are not applicable.

## Requirements

| | |
| --- | --- |
| Version | Windows 10, version 1709 |
| Header | Ntddndis.h (include Ndis.h) |

## See also

[NDIS_WWAN_BASE_STATIONS_INFO_REQ](TBD)

[NDIS_STATUS_WWAN_BASE_STATIONS_INFO](ndis-status-wwan-base-stations-info.md)

[NDIS_WWAN_BASE_STATIONS_INFO](TBD)

[WWAN_BASE_STATIONS_INFO](TBD)

[MB base stations information query support](mb-base-stations-information-query-support.md)

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")