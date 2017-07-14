---
title: NET\_BUFFER\_LIST\_NBL\_FLAGS macro
description: The NET\_BUFFER\_LIST\_NBL\_FLAGS macro retrieves the NblFlags member of a NET\_BUFFER\_LIST structure.
MS-HAID:
- 'header\_data\_split\_ref\_74da1fee-e613-48da-b951-ac37861e162c.xml'
- 'netvista.net\_buffer\_list\_nbl\_flags'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3ae4336d-4b62-476e-9b20-bf41fc308dc4
keywords: ["NET_BUFFER_LIST_NBL_FLAGS macro Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_BUFFER_LIST_NBL_FLAGS
api_location:
- Ndis.h
api_type:
- HeaderDef
---

# NET\_BUFFER\_LIST\_NBL\_FLAGS macro


The NET\_BUFFER\_LIST\_NBL\_FLAGS macro retrieves the **NblFlags** member of a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Syntax
------

```ManagedCPlusPlus
VOID NET_BUFFER_LIST_NBL_FLAGS(
   PNET_BUFFER_LIST _NBL
);
```

Parameters
----------

*\_NBL*   
A pointer to a NET\_BUFFER\_LIST structure.

Return value
------------

None

Remarks
-------

NDIS network drivers should use the NET\_BUFFER\_LIST\_NBL\_FLAGS macro to get the **NblFlags** member of a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

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
<td><p>Supported in NDIS 6.1 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_BUFFER_LIST_NBL_FLAGS%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





