---
title: NDIS\_STATUS\_WAN\_CO\_FRAGMENT
author: windows-driver-content
description: The NDIS\_STATUS\_WAN\_CO\_FRAGMENT status indicates that a CoNDIS WAN miniport driver has received a partial packet from the endpoint of a VC.
ms.assetid: 5a534364-d528-45f8-a2e0-3c745b3b5ad0
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_WAN_CO_FRAGMENT Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WAN\_CO\_FRAGMENT


The NDIS\_STATUS\_WAN\_CO\_FRAGMENT status indicates that a CoNDIS WAN miniport driver has received a partial packet from the endpoint of a VC.

Remarks
-------

The **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure contains a pointer to an [**NDIS\_WAN\_CO\_FRAGMENT**](https://msdn.microsoft.com/library/windows/hardware/ff559030) structure. The NDIS\_WAN\_CO\_FRAGMENT structure describes the reason that the partial packet was received.

For more information about NDIS\_STATUS\_WAN\_CO\_FRAGMENT, see [Indicating CoNDIS WAN Miniport Driver Status](https://msdn.microsoft.com/library/windows/hardware/ff554825). For more information about the CoNDIS WAN interface, see [Implementing CoNDIS WAN Miniport Drivers](https://msdn.microsoft.com/library/windows/hardware/ff553805).

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

[**NDIS\_WAN\_CO\_FRAGMENT**](https://msdn.microsoft.com/library/windows/hardware/ff559030)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_WAN_CO_FRAGMENT%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


