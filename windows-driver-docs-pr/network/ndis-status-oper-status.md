---
title: NDIS_STATUS_OPER_STATUS
description: The NDIS_STATUS_OPER_STATUS status indicates the current operational state of an NDIS network interface to overlying drivers.
ms.assetid: dbe7ce19-290d-4a48-a6c2-1b95e956c26c
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_OPER_STATUS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_OPER\_STATUS


The NDIS\_STATUS\_OPER\_STATUS status indicates the current operational state of an NDIS network interface to overlying drivers.

Remarks
-------

NDIS generates this status indication; NDIS miniport drivers should not generate this status indication.

NDIS supplies an [**NDIS\_OPER\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff566737) structure in the **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure.

The **StatusBufferSize** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure is set to sizeof(NDIS\_OPER\_STATE).

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


[**NDIS\_OPER\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff566737)

[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

 

 




