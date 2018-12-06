---
title: OID_PD_OPEN_PROVIDER
description: An NDIS protocol or filter driver sends an object identifier (OID) method request of OID_PD_OPEN_PROVIDER to a PD-capable miniport driver to gain access to the PD capability in the miniport driver's PDPI provider object.
ms.assetid: B13E0FAC-A179-4785-9B39-CB498064947B
ms.date: 08/08/2017
keywords: 
 -OID_PD_OPEN_PROVIDER Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_PD\_OPEN\_PROVIDER


An NDIS protocol or filter driver sends an object identifier (OID) method request of OID\_PD\_OPEN\_PROVIDER to a PD-capable miniport driver to gain access to the PD capability in the miniport driver's PDPI provider object. All PD-capable miniport drivers must handle this OID request.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a buffer. This buffer contains the following data:

-   An [**NDIS\_PD\_OPEN\_PROVIDER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn931842) structure

Remarks
-------

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416)

[**NDIS\_PD\_OPEN\_PROVIDER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn931842)

[NDIS\_STATUS\_PD\_CURRENT\_CONFIG](https://msdn.microsoft.com/library/windows/hardware/dn931850)

[OID\_PD\_CLOSE\_PROVIDER](oid-pd-close-provider.md)

 

 




