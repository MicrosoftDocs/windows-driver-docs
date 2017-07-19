---
title: NET\_BUFFER\_LIST\_RECEIVE\_QUEUE\_ID macro
author: windows-driver-content
description: The NET\_BUFFER\_LIST\_RECEIVE\_QUEUE\_ID macro sets or gets the identifier of a virtual machine queue (VMQ) or single root I/O virtualization (SR-IOV) receive queue identifier within the out-of-band (OOB) data of a NET\_BUFFER\_LIST structure.
ms.assetid: d205bb23-2e25-4643-baa9-19856de37eb1
ms.author: windowsdriverdev 
ms.date: 0718/2017 
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_BUFFER_LIST_RECEIVE_QUEUE_ID%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


