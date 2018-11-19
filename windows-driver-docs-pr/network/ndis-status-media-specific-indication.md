---
title: NDIS_STATUS_MEDIA_SPECIFIC_INDICATION
description: The NDIS_STATUS_MEDIA_SPECIFIC_INDICATION status indicates a media-specific status.
ms.assetid: 983ffff1-5157-46ae-b4ce-31ee1aa55955
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_MEDIA_SPECIFIC_INDICATION Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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

 

 




