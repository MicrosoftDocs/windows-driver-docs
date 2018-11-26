---
title: NdisQueryMdl macro
description: The NdisQueryMdl macro retrieves the buffer length, and optionally the base virtual address, from an MDL.
ms.assetid: 0eccd784-c815-4094-87e5-a3e283abed73
ms.date: 07/18/2017
keywords:
 - NdisQueryMdl macro Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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
<td><a href="https://msdn.microsoft.com/library/windows/hardware/ff547985" data-raw-source="[&lt;strong&gt;Irql_NetBuffer_Function&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547985)"><strong>Irql_NetBuffer_Function</strong></a></td>
</tr>
</tbody>
</table>

## See also


[**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559)

[**NdisQueryBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff554407)

 

 




