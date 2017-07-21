---
title: NET_BUFFER_LIST_RECEIVE_FILTER_VPORT_ID macro
author: windows-driver-content
description: The NET_BUFFER_LIST_RECEIVE_FILTER_VPORT_ID macro sets or gets the identifier of a virtual port (VPort) within the out-of-band (OOB) data in a NET_BUFFER_LIST structure.
ms.assetid: 809FE51C-8679-49D5-9E4A-5820747DBE97
ms.author: windowsdriverdev 
ms.date: 0718/2017 
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_BUFFER_LIST_RECEIVE_FILTER_VPORT_ID%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


