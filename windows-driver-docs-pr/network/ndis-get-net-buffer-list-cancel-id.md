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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_GET_NET_BUFFER_LIST_CANCEL_ID%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


