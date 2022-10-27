---
title: FreeMibTable function (Windows Drivers)
description: Learn more about the FreeMibTable function.
keywords:
- FreeMibTable
- netioapi/FreeMibTable
ms.date: 10/25/2022
---

# FreeMibTable function

The **FreeMibTable** function frees the buffer that is allocated by the functions that return tables of network interfaces, addresses, and routes (for example, [**GetIfTable2**](getiftable2.md) and [**GetAnycastIpAddressTable**](getanycastipaddresstable.md)).

## Syntax

``` c++
VOID NETIOAPI_API_ FreeMibTable(
  _In_ PVOID Memory
);
```

## Parameters

- *Memory* \[in\]  
   A pointer to the buffer to free.

## Return value

None

## Remarks

The **FreeMibTable** function is used to free the internal buffers that various functions use to retrieve tables of interfaces, addresses, and routes. When these tables are no longer needed, your driver should call **FreeMibTable** to release the memory that these tables use.

## Requirements

<table>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td><a href="/windows-hardware/drivers/develop/target-platforms">Universal</a></td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Netioapi.h (include Netioapi.h)</td>
</tr>
<tr class="even">
<td><p>Library</p></td>
<td>Netio.lib</td>
</tr>
<tr class="odd">
<td><p>IRQL</p></td>
<td><p>&lt; DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also

[**GetAnycastIpAddressTable**](getanycastipaddresstable.md)

[**GetIfStackTable**](getifstacktable.md)

[**GetIfTable2**](getiftable2.md)

[**GetIfTable2Ex**](getiftable2ex.md)

[**GetInvertedIfStackTable**](getinvertedifstacktable.md)

[**GetIpForwardTable2**](getipforwardtable2.md)

[**GetIpInterfaceTable**](getipinterfacetable.md)

[**GetIpNetTable2**](getipnettable2.md)

[**GetIpPathTable**](getippathtable.md)

[**GetMulticastIpAddressTable**](getmulticastipaddresstable.md)

[**GetUnicastIpAddressTable**](getunicastipaddresstable.md)
