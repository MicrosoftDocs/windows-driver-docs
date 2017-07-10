---
title: NET\_BUFFER\_LIST\_PROTOCOL\_RESERVED macro
description: NET\_BUFFER\_LIST\_PROTOCOL\_RESERVED is a macro that NDIS drivers use to access the ProtocolReserved member of a NET\_BUFFER\_LIST structure.
MS-HAID:
- 'ndis\_netbuf\_macros\_ref\_efa353ca-7059-4e14-968e-d8b1be50d4ea.xml'
- 'netvista.net\_buffer\_list\_protocol\_reserved'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f14d2948-59f8-4249-aca1-dc207a5ba596
keywords: ["NET_BUFFER_LIST_PROTOCOL_RESERVED macro Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_BUFFER_LIST_PROTOCOL_RESERVED
api_location:
- Ndis.h
api_type:
- HeaderDef
---

# NET\_BUFFER\_LIST\_PROTOCOL\_RESERVED macro


NET\_BUFFER\_LIST\_PROTOCOL\_RESERVED is a macro that NDIS drivers use to access the **ProtocolReserved** member of a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Syntax
------

```ManagedCPlusPlus
PVOID NET_BUFFER_LIST_PROTOCOL_RESERVED(
   PNET_BUFFER_LIST _NBL
);
```

Parameters
----------

*\_NBL*   
A pointer to a NET\_BUFFER\_LIST structure.

Return value
------------

NET\_BUFFER\_LIST\_PROTOCOL\_RESERVED returns a pointer to the start of the **ProtocolReserved** member of the indicated NET\_BUFFER\_LIST structure.

Remarks
-------

Protocol drivers and NDIS intermediate drivers can use **ProtocolReserved** for their own purposes.

**Note**  Only one driver can use **ProtocolReserved** . Therefore, if another driver has used **ProtocolReserved**, an intermediate driver cannot use it.

 

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


[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_BUFFER_LIST_PROTOCOL_RESERVED%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





