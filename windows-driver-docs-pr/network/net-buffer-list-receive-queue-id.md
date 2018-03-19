---
title: NET_BUFFER_LIST_RECEIVE_QUEUE_ID macro
author: windows-driver-content
description: The NET_BUFFER_LIST_RECEIVE_QUEUE_ID macro sets or gets the identifier of a virtual machine queue (VMQ) or single root I/O virtualization (SR-IOV) receive queue identifier within the out-of-band (OOB) data of a NET_BUFFER_LIST structure.
ms.assetid: d205bb23-2e25-4643-baa9-19856de37eb1
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_LIST_RECEIVE_QUEUE_ID macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_LIST\_RECEIVE\_QUEUE\_ID macro


The **NET\_BUFFER\_LIST\_RECEIVE\_QUEUE\_ID** macro sets or gets the identifier of a virtual machine queue (VMQ) or single root I/O virtualization (SR-IOV) receive queue identifier within the out-of-band (OOB) data of a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

For the SR-IOV interface, the receive queue is created on a default or nondefault virtual port (VPort). Starting with Windows Server 2012, only the default receive queue of a VPort is supported.

Syntax
------

```ManagedCPlusPlus
USHORT NET_BUFFER_LIST_RECEIVE_QUEUE_ID(
   PNET_BUFFER_LIST _NBL
);
```

Parameters
----------

*\_NBL*   
A pointer to a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Return value
------------

**NET\_BUFFER\_LIST\_RECEIVE\_QUEUE\_ID** returns a **USHORT** value for a receive queue identifier.

Remarks
-------

Any NDIS 6.20 or later driver can use **NET\_BUFFER\_LIST\_RECEIVE\_QUEUE\_ID** to set or get the receive queue identifier from a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure. **NET\_BUFFER\_LIST\_RECEIVE\_QUEUE\_ID** accesses the receive queue identifier from the **QueueId** member of the [**NDIS\_NET\_BUFFER\_LIST\_FILTERING\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566567) structure.

**Note**  When a VMQ is deleted (for example, during VM live migration), it is possible for the miniport driver to receive an NBL that contains an invalid **QueueId** value. If this happens, the miniport should ignore the invalid queue ID and use 0 (the default queue) instead. The **QueueId** is found in the **NetBufferListFilteringInfo** portion of the NBL's OOB data, and is retrieved by using the **NET\_BUFFER\_LIST\_RECEIVE\_QUEUE\_ID** macro.

 

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
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.20 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_NET\_BUFFER\_LIST\_FILTERING\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566567)

[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

 

 




