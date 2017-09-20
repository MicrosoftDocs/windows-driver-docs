---
title: NET_BUFFER_LIST_GET_HASH_VALUE macro
author: windows-driver-content
description: The NET_BUFFER_LIST_GET_HASH_VALUE macro gets the hash value information from a NET_BUFFER_LIST structure. Version Information Windows VistaSupported. NDIS 6.0 driversSupported.
ms.assetid: 7e3794e4-1afe-416f-b8f8-689f6397fc6a
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_LIST_GET_HASH_VALUE macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_LIST\_GET\_HASH\_VALUE macro


The NET\_BUFFER\_LIST\_GET\_HASH\_VALUE macro gets the hash value information from a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

**Version Information**

<a href="" id="windows-vista"></a>Windows Vista  
Supported.

<a href="" id="ndis-6-0-drivers"></a>NDIS 6.0 drivers  
Supported.

Syntax
------

```ManagedCPlusPlus
ULONG NET_BUFFER_LIST_GET_HASH_VALUE(
   PNET_BUFFER_LIST NetBufferList
);
```

Parameters
----------

*NetBufferList*   
A pointer to a NET\_BUFFER\_LIST structure.

Return value
------------

NET\_BUFFER\_LIST\_GET\_HASH\_VALUE returns the hash value formatted as a ULONG.

## <a href="" id="ddk-net-buffer-list-get-hash-value-nr"></a>


Remarks
-------

For more information about the hash value, see [RSS Hashing Functions](https://msdn.microsoft.com/library/windows/hardware/ff570725).

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
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_BUFFER_LIST_GET_HASH_VALUE%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


