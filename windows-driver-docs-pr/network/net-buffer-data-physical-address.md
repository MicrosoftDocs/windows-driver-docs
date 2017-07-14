---
title: NET\_BUFFER\_DATA\_PHYSICAL\_ADDRESS macro
description: The NET\_BUFFER\_DATA\_PHYSICAL\_ADDRESS macro retrieves the DataPhysicalAddress member of a NET\_BUFFER structure.
MS-HAID:
- 'header\_data\_split\_ref\_31410714-e5e0-458f-9cc8-5a7372b18d44.xml'
- 'netvista.net\_buffer\_data\_physical\_address'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: da9971ec-38ce-4489-a11a-886aab9c6e6c
keywords: ["NET_BUFFER_DATA_PHYSICAL_ADDRESS macro Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_BUFFER_DATA_PHYSICAL_ADDRESS
api_location:
- Ndis.h
api_type:
- HeaderDef
---

# NET\_BUFFER\_DATA\_PHYSICAL\_ADDRESS macro


The NET\_BUFFER\_DATA\_PHYSICAL\_ADDRESS macro retrieves the **DataPhysicalAddress** member of a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

Syntax
------

```ManagedCPlusPlus
NDIS_PHYSICAL_ADDRESS NET_BUFFER_DATA_PHYSICAL_ADDRESS(
   PNET_BUFFER _NB
);
```

Parameters
----------

*\_NB*   
A pointer to a NET\_BUFFER structure.

Return value
------------

NET\_BUFFER\_DATA\_PHYSICAL\_ADDRESS returns the **DataPhysicalAddress** member of a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

Remarks
-------

NDIS network drivers should use the NET\_BUFFER\_DATA\_PHYSICAL\_ADDRESS macro to get the **DataPhysicalAddress** member of a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

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


[**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_BUFFER_DATA_PHYSICAL_ADDRESS%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





