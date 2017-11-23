---
title: GUID_NDIS_STATUS_MEDIA_SPECIFIC_INDICATION_EX
author: windows-driver-content
description: This topic describes the GUID_NDIS_STATUS_MEDIA_SPECIFIC_INDICATION_EX GUID for the NDIS WMI interface.
ms.assetid: 34839471-5b3b-4a95-a610-bc35e7774c14
keywords:
- GUID_NDIS_STATUS_MEDIA_SPECIFIC_INDICATION_EX, WDK GUID_NDIS_STATUS_MEDIA_SPECIFIC_INDICATION_EX network drivers
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GUID_NDIS_STATUS_MEDIA_SPECIFIC_INDICATION_EX

The GUID_NDIS_STATUS_MEDIA_SPECIFIC_INDICATION_EX event GUID indicates a media-specific status. This WMI GUID is supported in NDIS 6.0 and later versions.

When a miniport driver indicates media-specific status, NDIS translates the status indication to a WMI GUID_NDIS_STATUS_MEDIA_SPECIFIC_INDICATION_EX indication for WMI clients.

Miniport drivers make media-specific status indications by calling the [NdisMIndicateStatusEx](https://msdn.microsoft.com/library/windows/hardware/ff563600) function with the **StatusCode** member of the [NDIS_STATUS_INDICATION](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure that the *StatusIndication* parameter points to set to NDIS_STATUS_MEDIA_SPECIFIC_INDICATION_EX. The **StatusBuffer** member of this structure points to a driver-allocated buffer that contains data in a format that is specific to the status indication that is identified in **StatusCode**.

Depending on the type of media-specific indication, the GUID header could be followed by data that is specific to the media-specific indication. The data buffer that NDIS provides with this GUID contains an [NDIS_WMI_EVENT_HEADER](https://msdn.microsoft.com/library/windows/hardware/ff567900) structure that is followed by the media-specific data, if any.

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")