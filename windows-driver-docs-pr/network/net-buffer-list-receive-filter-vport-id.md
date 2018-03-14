---
title: NET_BUFFER_LIST_RECEIVE_FILTER_VPORT_ID macro
author: windows-driver-content
description: The NET_BUFFER_LIST_RECEIVE_FILTER_VPORT_ID macro sets or gets the identifier of a virtual port (VPort) within the out-of-band (OOB) data in a NET_BUFFER_LIST structure.
ms.assetid: 809FE51C-8679-49D5-9E4A-5820747DBE97
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_LIST_RECEIVE_FILTER_VPORT_ID macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_LIST\_RECEIVE\_FILTER\_VPORT\_ID macro


The **NET\_BUFFER\_LIST\_RECEIVE\_FILTER\_VPORT\_ID** macro sets or gets the identifier of a virtual port (VPort) within the out-of-band (OOB) data in a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Syntax
------

```ManagedCPlusPlus
USHORT NET_BUFFER_LIST_RECEIVE_FILTER_VPORT_ID(
   PNET_BUFFER_LIST _NBL
);
```

Parameters
----------

*\_NBL*   
A pointer to a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Return value
------------

**NET\_BUFFER\_LIST\_RECEIVE\_FILTER\_VPORT\_ID** returns a USHORT value for a VPort identifier.

Remarks
-------

Miniport drivers that support the single root I/O virtualization (SR-IOV) interface can use the **NET\_BUFFER\_LIST\_RECEIVE\_FILTER\_VPORT\_ID** macro to set or get the VPort identifier in a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure. The **NET\_BUFFER\_LIST\_RECEIVE\_FILTER\_VPORT\_ID** macro accesses the VPort identifier from the **VPortId** member of the [**NDIS\_NET\_BUFFER\_LIST\_FILTERING\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566567) structure.

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
<td><p>Supported in NDIS 6.30 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


****
[**NDIS\_NET\_BUFFER\_LIST\_FILTERING\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566567)

[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

 

 




