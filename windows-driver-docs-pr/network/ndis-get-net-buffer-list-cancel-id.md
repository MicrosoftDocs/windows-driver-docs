---
title: NDIS_GET_NET_BUFFER_LIST_CANCEL_ID macro
author: windows-driver-content
description: The NDIS_GET_NET_BUFFER_LIST_CANCEL_ID macro gets the cancellation identifier from a NET_BUFFER_LIST structure.
ms.assetid: ad302c12-24d9-4310-ac5a-dd295589fcbd
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_GET_NET_BUFFER_LIST_CANCEL_ID macro Network Drivers Starting with Windows Vista
---

# NDIS\_GET\_NET\_BUFFER\_LIST\_CANCEL\_ID macro


The NDIS\_GET\_NET\_BUFFER\_LIST\_CANCEL\_ID macro gets the cancellation identifier from a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Syntax
------

```ManagedCPlusPlus
ULONG NDIS_GET_NET_BUFFER_LIST_CANCEL_ID(
   PNET_BUFFER_LIST _NBL
);
```

Parameters
----------

*\_NBL*   
A pointer to a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Return value
------------

NDIS\_GET\_NET\_BUFFER\_LIST\_CANCEL\_ID returns a ULONG value that is a cancellation identifier for the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Remarks
-------

To cancel send requests, filter drivers call the [**NdisFCancelSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff561794) function. Other NDIS drivers call the [**NdisCancelSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff561623) function.

Drivers can call the **NDIS\_SET\_NET\_BUFFER\_LIST\_CANCEL\_ID** macro to set a cancellation identifier in a NET\_BUFFER\_LIST structure.

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
<td><p>Supported in NDIS 6.0 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NdisCancelSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff561623)

[**NdisFCancelSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff561794)

[**NDIS\_SET\_NET\_BUFFER\_LIST\_CANCEL\_ID**](ndis-set-net-buffer-list-cancel-id.md)

[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

 

 




