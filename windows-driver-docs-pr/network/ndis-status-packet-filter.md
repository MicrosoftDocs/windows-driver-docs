---
title: NDIS_STATUS_PACKET_FILTER
author: windows-driver-content
description: The NDIS_STATUS_PACKET_FILTER status indicates a packet filter change to overlying drivers.
ms.assetid: 7633772a-cd3d-4030-b97a-9d503341fdeb
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_PACKET_FILTER Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_PACKET\_FILTER


The NDIS\_STATUS\_PACKET\_FILTER status indicates a packet filter change to overlying drivers. NDIS generates this status indications for a miniport adapter to notify overlying drivers that there might be a change in the miniport adapter's packet filter setting.

Remarks
-------

NDIS does not guarantee that the packet filter has changed when NDIS generates the NDIS\_STATUS\_PACKET\_FILTER status indication.

NDIS filter drivers can also generate the NDIS\_STATUS\_PACKET\_FILTER status indication.

NDIS supplies a bitwise OR of the filter type flags in the **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure. For a list of the filter type flags, see the [OID\_GEN\_CURRENT\_PACKET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569575) OID. For additional information about packet filters, see [OID\_GEN\_SUPPORTED\_PACKET\_FILTERS](https://msdn.microsoft.com/library/windows/hardware/ff569643).

The **StatusBufferSize** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure is set to sizeof(ULONG).

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


[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[OID\_GEN\_CURRENT\_PACKET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569575)

[OID\_GEN\_SUPPORTED\_PACKET\_FILTERS](https://msdn.microsoft.com/library/windows/hardware/ff569643)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_PACKET_FILTER%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


