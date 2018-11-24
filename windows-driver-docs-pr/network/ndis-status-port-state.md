---
title: NDIS_STATUS_PORT_STATE
description: Miniport drivers that support NDIS ports use the NDIS_STATUS_PORT_STATE status indication to indicate changes in the state of an NDIS port.
ms.assetid: 28e76963-af06-4a00-83ef-14e009cf35ec
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_PORT_STATE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_PORT\_STATE


Miniport drivers that support NDIS ports use the NDIS\_STATUS\_PORT\_STATE status indication to indicate changes in the state of an NDIS port.

Remarks
-------

Miniport drivers must set the port number in the **PortNumber** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure. The **StatusBuffer** member of this structure contains a pointer to an [**NDIS\_PORT\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff566800) structure.

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


[**NDIS\_PORT\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff566800)

[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

 

 




