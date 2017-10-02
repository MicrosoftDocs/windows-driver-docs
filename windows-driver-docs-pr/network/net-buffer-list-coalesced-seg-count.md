---
title: NET_BUFFER_LIST_COALESCED_SEG_COUNT macro
author: windows-driver-content
description: The NET\_BUFFER\_LIST\_COALESCED\_SEG\_COUNT is a macro that NDIS drivers use to get and set the number of coalesced segments in a NET\_BUFFER\_LIST structure.
ms.assetid: CAF2D3C1-A91D-4FAF-8358-46064398C813
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NET_BUFFER_LIST_COALESCED_SEG_COUNT macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_LIST\_COALESCED\_SEG\_COUNT macro


The **NET\_BUFFER\_LIST\_COALESCED\_SEG\_COUNT** is a macro that NDIS drivers use to get and set the number of coalesced segments in a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Syntax
------

```ManagedCPlusPlus
PVOID NET_BUFFER_LIST_COALESCED_SEG_COUNT(
   PNET_BUFFER_LIST _NBL
);
```

Parameters
----------

*\_NBL*   
A pointer to a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Return value
------------

**NET\_BUFFER\_LIST\_COALESCED\_SEG\_COUNT** returns the **CoalescedSegCount** member of the [**NDIS\_RSC\_NBL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451655) union that is associated with the **TcpRecvSegCoalesceInfo** identifier. The information is retrieved from the **NetBufferListInfo** member of the indicated NET\_BUFFER\_LIST structure.

Remarks
-------

This macro uses the [**NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff568401) macro to access the **TcpRecvSegCoalesceInfo** information.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.30 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_RSC\_NBL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451655)

[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

[**NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff568401)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_BUFFER_LIST_COALESCED_SEG_COUNT%20macro%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


