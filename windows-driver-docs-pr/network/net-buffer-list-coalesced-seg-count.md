---
title: NET_BUFFER_LIST_COALESCED_SEG_COUNT macro
author: windows-driver-content
description: The NET_BUFFER_LIST_COALESCED_SEG_COUNT is a macro that NDIS drivers use to get and set the number of coalesced segments in a NET_BUFFER_LIST structure.
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

 

 




