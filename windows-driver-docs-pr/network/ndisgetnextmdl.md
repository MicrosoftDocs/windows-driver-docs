---
title: NdisGetNextMdl macro
description: The NdisGetNextMdl macro retrieves the next MDL in an MDL chain, given a pointer to the current MDL.
MS-HAID:
- 'ndis\_mdl\_ref\_477ede6e-4b6e-4484-872f-3ee94e37d7be.xml'
- 'netvista.ndisgetnextmdl'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5b59ca7c-0998-4d53-9553-4946ef85327c
keywords: ["NdisGetNextMdl macro Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NdisGetNextMdl
api_location:
- Ndis.h
api_type:
- HeaderDef
---

# NdisGetNextMdl macro


The **NdisGetNextMdl** macro retrieves the next MDL in an MDL chain, given a pointer to the current MDL.

Syntax
------

```ManagedCPlusPlus
VOID NdisGetNextMdl(
    _CurrentMdl,
    _NextMdl
);
```

Parameters
----------

*\_CurrentMdl*   
A pointer to the specified current MDL.

*\_NextMdl*   
A pointer to a caller-supplied variable in which this macro returns a pointer to the next MDL in the MDL chain, if any, that follows the MDL at *\_CurrentMdl* .

Return value
------------

None

Remarks
-------

The **NdisGetNextMdl** macro provides an MDL-based version of the [**NdisGetNextBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff552070) function.

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
<td><p>Supported in NDIS 6.0 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
<tr class="even">
<td><p>IRQL</p></td>
<td><p>Any level</p></td>
</tr>
</tbody>
</table>

## See also


[**NdisGetNextBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff552070)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NdisGetNextMdl%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





