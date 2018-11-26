---
title: OID_GEN_MINIPORT_RESTART_ATTRIBUTES
description: The OID_GEN_MINIPORT_RESTART_ATTRIBUTES OID identifies general attributes for the propagation of miniport adapter restart attributes in an NDIS driver stack.
ms.assetid: 239993f6-2176-4925-aadc-44e0df66f56b
ms.date: 08/08/2017
keywords: 
 -OID_GEN_MINIPORT_RESTART_ATTRIBUTES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_MINIPORT\_RESTART\_ATTRIBUTES


The OID\_GEN\_MINIPORT\_RESTART\_ATTRIBUTES OID identifies general attributes for the propagation of miniport adapter restart attributes in an NDIS driver stack.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested.

Remarks
-------

The OID\_GEN\_MINIPORT\_RESTART\_ATTRIBUTES OID is not used to issue OID query or set requests.

If the **Oid** member in the [**NDIS\_RESTART\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff567255) structure is OID\_GEN\_MINIPORT\_RESTART\_ATTRIBUTES, the **Data** member of the structure contains an [**NDIS\_RESTART\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff567260) structure.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_RESTART\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff567255)

[**NDIS\_RESTART\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff567260)

 

 




