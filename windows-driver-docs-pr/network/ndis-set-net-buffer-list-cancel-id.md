---
title: NDIS_SET_NET_BUFFER_LIST_CANCEL_ID macro
author: windows-driver-content
description: The NDIS_SET_NET_BUFFER_LIST_CANCEL_ID macro marks a NET_BUFFER_LIST structure with a cancellation identifier that a driver can later use to cancel the pending transmission of the associated data.
ms.assetid: bf68accb-5062-42e7-97e4-c2a3210f60b2
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_SET_NET_BUFFER_LIST_CANCEL_ID macro Network Drivers Starting with Windows Vista
---

# NDIS\_SET\_NET\_BUFFER\_LIST\_CANCEL\_ID macro


The NDIS\_SET\_NET\_BUFFER\_LIST\_CANCEL\_ID macro marks a NET\_BUFFER\_LIST structure with a cancellation identifier that a driver can later use to cancel the pending transmission of the associated data.

Syntax
------

```ManagedCPlusPlus
VOID NDIS_SET_NET_BUFFER_LIST_CANCEL_ID(
   PNET_BUFFER_LIST _NBL,
   ULONG            _CancelId
);
```

Parameters
----------

*\_NBL*   
A pointer to a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

*\_CancelId*   
A ULONG value that is a cancellation identifier for the NET\_BUFFER\_LIST structure.

Return value
------------

None

Remarks
-------

An NDIS driver can call the NDIS\_SET\_NET\_BUFFER\_LIST\_CANCEL\_ID macro for each NET\_BUFFER\_LIST structure that it passes to lower-level drivers for transmission. The NDIS\_SET\_NET\_BUFFER\_LIST\_CANCEL\_ID macro marks the specified NET\_BUFFER\_LIST structure with a cancellation identifier. Drivers must call the [**NdisGeneratePartialCancelId**](https://msdn.microsoft.com/library/windows/hardware/ff562623) function to obtain a value that the driver must use as the high-order byte of a cancellation identifier.

To cancel send requests, filter drivers call the [**NdisFCancelSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff561794) function. Other drivers call the [**NdisCancelSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff561623) function.

Drivers can call the [**NDIS\_GET\_NET\_BUFFER\_LIST\_CANCEL\_ID**](ndis-get-net-buffer-list-cancel-id.md) macro to retrieve a cancellation identifier from a NET\_BUFFER\_LIST structure.

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

[**NdisGeneratePartialCancelId**](https://msdn.microsoft.com/library/windows/hardware/ff562623)

[**NDIS\_GET\_NET\_BUFFER\_LIST\_CANCEL\_ID**](ndis-get-net-buffer-list-cancel-id.md)

[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

 

 




