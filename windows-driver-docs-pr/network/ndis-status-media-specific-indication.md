---
title: NDIS\_STATUS\_MEDIA\_SPECIFIC\_INDICATION
description: The NDIS\_STATUS\_MEDIA\_SPECIFIC\_INDICATION status indicates a media-specific status.
MS-HAID:
- 'ndis\_status\_indications\_ref\_5d9b0330-480b-4137-8a55-42cf7ec0bbaa.xml'
- 'netvista.ndis\_status\_media\_specific\_indication'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 983ffff1-5157-46ae-b4ce-31ee1aa55955
keywords: ["NDIS_STATUS_MEDIA_SPECIFIC_INDICATION Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NDIS_STATUS_MEDIA_SPECIFIC_INDICATION
api_location:
- Ndis.h
api_type:
- HeaderDef
---

# NDIS\_STATUS\_MEDIA\_SPECIFIC\_INDICATION


The NDIS\_STATUS\_MEDIA\_SPECIFIC\_INDICATION status indicates a media-specific status.

Remarks
-------

Miniport drivers make media-specific status indications by calling the [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) function with the **StatusCode** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure set to NDIS\_STATUS\_MEDIA\_SPECIFIC\_INDICATION. The **StatusBuffer** member of this structure points to a driver-allocated buffer. The buffer contains data in a format that is specific to the status indication that is identified in the **StatusCode** member.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported for NDIS 6.0 and NDIS 5.1 drivers in Windows Vista. Supported for NDIS 5.1 drivers in Windows XP.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_MEDIA_SPECIFIC_INDICATION%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





