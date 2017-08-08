---
title: OID\_PD\_OPEN\_PROVIDER
author: windows-driver-content
description: An NDIS protocol or filter driver sends an object identifier (OID) method request of OID\_PD\_OPEN\_PROVIDER to a PD-capable miniport driver to gain access to the PD capability in the miniport driver's PDPI provider object.
ms.assetid: B13E0FAC-A179-4785-9B39-CB498064947B
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_PD_OPEN_PROVIDER Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_PD_OPEN_PROVIDER%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


