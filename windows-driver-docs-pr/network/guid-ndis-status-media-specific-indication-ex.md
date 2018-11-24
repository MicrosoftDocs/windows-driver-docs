---
title: GUID_NDIS_STATUS_MEDIA_SPECIFIC_INDICATION_EX
description: This topic describes the GUID_NDIS_STATUS_MEDIA_SPECIFIC_INDICATION_EX GUID for the NDIS WMI interface.
ms.assetid: 34839471-5b3b-4a95-a610-bc35e7774c14
keywords:
- GUID_NDIS_STATUS_MEDIA_SPECIFIC_INDICATION_EX, WDK GUID_NDIS_STATUS_MEDIA_SPECIFIC_INDICATION_EX network drivers
ms.date: 11/22/2017
ms.localizationpriority: medium
---

# GUID_NDIS_STATUS_MEDIA_SPECIFIC_INDICATION_EX

The GUID_NDIS_STATUS_MEDIA_SPECIFIC_INDICATION_EX event GUID indicates a media-specific status. This WMI GUID is supported in NDIS 6.0 and later versions.

When a miniport driver indicates media-specific status, NDIS translates the status indication to a WMI GUID_NDIS_STATUS_MEDIA_SPECIFIC_INDICATION_EX indication for WMI clients.

Miniport drivers make media-specific status indications by calling the [NdisMIndicateStatusEx](https://msdn.microsoft.com/library/windows/hardware/ff563600) function with the **StatusCode** member of the [NDIS_STATUS_INDICATION](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure that the *StatusIndication* parameter points to set to NDIS_STATUS_MEDIA_SPECIFIC_INDICATION_EX. The **StatusBuffer** member of this structure points to a driver-allocated buffer that contains data in a format that is specific to the status indication that is identified in **StatusCode**.

Depending on the type of media-specific indication, the GUID header could be followed by data that is specific to the media-specific indication. The data buffer that NDIS provides with this GUID contains an [NDIS_WMI_EVENT_HEADER](https://msdn.microsoft.com/library/windows/hardware/ff567900) structure that is followed by the media-specific data, if any.

