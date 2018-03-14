---
title: NET_BUFFER_LIST_SET_HASH_VALUE macro
author: windows-driver-content
description: The NET_BUFFER_LIST_SET_HASH_VALUE macro sets the hash value information in a NET_BUFFER_LIST structure. Version InformationWindows VistaSupported. NDIS 6.0 driversSupported.
ms.assetid: cca681ab-7867-40e3-beab-ad001fb0dd39
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_LIST_SET_HASH_VALUE macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_LIST\_SET\_HASH\_VALUE macro


The NET\_BUFFER\_LIST\_SET\_HASH\_VALUE macro sets the hash value information in a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

**Version Information**

<a href="" id="windows-vista"></a>Windows Vista  
Supported.

<a href="" id="ndis-6-0-drivers"></a>NDIS 6.0 drivers  
Supported.

Syntax
------

```ManagedCPlusPlus
VOID NET_BUFFER_LIST_SET_HASH_VALUE(
   PNET_BUFFER_LIST NetBufferList,
   ULONG            HashValue
);
```

Parameters
----------

*NetBufferList*   
A pointer to a NET\_BUFFER\_LIST structure.

*HashValue*   
The hash value, which is formatted as a ULONG.

Return value
------------

None

## <a href="" id="ddk-net-buffer-list-set-hash-value-nr"></a>


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

 

 




