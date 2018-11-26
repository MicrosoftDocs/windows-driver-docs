---
title: NDIS_STATUS_OFFLOAD_ENCASPULATION_CHANGE
description: Miniport drivers use the NDIS_STATUS_OFFLOAD_ENCASPULATION_CHANGE status indication to notify NDIS and overlying drivers that there has been change in the encapsulation settings.
ms.assetid: 2db2a42e-85a2-41a6-b6ab-13b493057648
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_OFFLOAD_ENCASPULATION_CHANGE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_OFFLOAD\_ENCASPULATION\_CHANGE


Miniport drivers use the NDIS\_STATUS\_OFFLOAD\_ENCASPULATION\_CHANGE status indication to notify NDIS and overlying drivers that there has been change in the encapsulation settings.

Remarks
-------

The **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure contains an [**NDIS\_OFFLOAD\_ENCAPSULATION**](https://msdn.microsoft.com/library/windows/hardware/ff566702) structure. NDIS\_OFFLOAD\_ENCAPSULATION specifies the encapsulation settings.

For more information about encapsulation settings, see [OID\_OFFLOAD\_ENCAPSULATION](https://msdn.microsoft.com/library/windows/hardware/ff569762).

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
<td><p>Supported in NDIS 6.0 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_OFFLOAD\_ENCAPSULATION**](https://msdn.microsoft.com/library/windows/hardware/ff566702)

[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[OID\_OFFLOAD\_ENCAPSULATION](https://msdn.microsoft.com/library/windows/hardware/ff569762)

 

 




