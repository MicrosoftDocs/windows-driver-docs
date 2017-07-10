---
title: NdisQueryMdl macro
description: The NdisQueryMdl macro retrieves the buffer length, and optionally the base virtual address, from an MDL.
MS-HAID:
- 'ndis\_mdl\_ref\_e6dae6d9-92ba-4e84-b14f-66bfda9e7508.xml'
- 'netvista.ndisquerymdl'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 0eccd784-c815-4094-87e5-a3e283abed73
keywords: ["NdisQueryMdl macro Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NdisQueryMdl
api_location:
- Ndis.h
api_type:
- HeaderDef
---

# NdisQueryMdl macro


The **NdisQueryMdl** macro retrieves the buffer length, and optionally the base virtual address, from an MDL.

Syntax
------

```ManagedCPlusPlus
VOID NdisQueryMdl(
    _Mdl,
    _VirtualAddress,
    _Length,
    _Priority
);
```

Parameters
----------

*\_Mdl*   
A pointer to an MDL.

*\_VirtualAddress*   
A pointer to a caller-supplied variable in which this macro returns the base virtual address of the virtual address range that is described by the MDL. The base virtual address can be **NULL** for either of the following reasons:

-   System resources are low or exhausted and the *\_Priority* parameter is set to **LowPagePriority** or **NormalPagePriority**.

-   System resources are exhausted and the *\_Priority* parameter is set to **HighPagePriority**.

*\_Length*   
A pointer to a caller-supplied variable in which this macro returns the length, in bytes, of the virtual address range that is described by the MDL.

*\_Priority*   
A page priority value. For a list of the possible values for this parameter, see the *Priority* parameter of the [**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559) macro.

Return value
------------

None

Remarks
-------

The **NdisQueryMdl** macro provides an MDL-based version of the [**NdisQueryBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff554407) function.

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
<td><p>&lt;= DISPATCH_LEVEL</p></td>
</tr>
<tr class="odd">
<td><p>DDI compliance rules</p></td>
<td>[<strong>Irql_NetBuffer_Function</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547985)</td>
</tr>
</tbody>
</table>

## See also


[**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559)

[**NdisQueryBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff554407)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NdisQueryMdl%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





