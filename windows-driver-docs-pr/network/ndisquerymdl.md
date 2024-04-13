---
title: NdisQueryMdl macro
description: The NdisQueryMdl macro retrieves the buffer length, and optionally the base virtual address, from an MDL.
ms.date: 07/18/2017
keywords:
 - NdisQueryMdl macro Network Drivers Starting with Windows Vista
---

# NdisQueryMdl macro


The **NdisQueryMdl** macro retrieves the buffer length, and optionally the base virtual address, from an MDL.

## Syntax

```ManagedCPlusPlus
VOID NdisQueryMdl(
    _Mdl,
    _VirtualAddress,
    _Length,
    _Priority
);
```

## Parameters

*\_Mdl*   
A pointer to an MDL.

*\_VirtualAddress*   
A pointer to a caller-supplied variable in which this macro returns the base virtual address of the virtual address range that is described by the MDL. The base virtual address can be **NULL** for either of the following reasons:

-   System resources are low or exhausted and the *\_Priority* parameter is set to **LowPagePriority** or **NormalPagePriority**.

-   System resources are exhausted and the *\_Priority* parameter is set to **HighPagePriority**.

*\_Length*   
A pointer to a caller-supplied variable in which this macro returns the length, in bytes, of the virtual address range that is described by the MDL.

*\_Priority*   
A page priority value. For a list of the possible values for this parameter, see the *Priority* parameter of the [**MmGetSystemAddressForMdlSafe**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetsystemaddressformdlsafe) macro.

## Return value

None

## Remarks

The **NdisQueryMdl** macro provides an MDL-based version of the [**NdisQueryBuffer**](/previous-versions/windows/hardware/network/ff554407(v=vs.85)) function.

## Requirements

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
<td><a href="/windows-hardware/drivers/devtest/ndis-irql-netbuffer-function" data-raw-source="[&lt;strong&gt;Irql_NetBuffer_Function&lt;/strong&gt;](../devtest/ndis-irql-netbuffer-function.md)"><strong>Irql_NetBuffer_Function</strong></a></td>
</tr>
</tbody>
</table>

## See also


[**MmGetSystemAddressForMdlSafe**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetsystemaddressformdlsafe)

[**NdisQueryBuffer**](/previous-versions/windows/hardware/network/ff554407(v=vs.85))

