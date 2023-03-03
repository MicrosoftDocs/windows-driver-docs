---
title: GetIfEntry2 function (Windows Drivers)
description: Learn more about the GetIfEntry2 function.
keywords:
- GetIfEntry2
- netioapi/GetIfEntry2
ms.date: 10/25/2022
ms.topic: reference
---

# GetIfEntry2 function

The **GetIfEntry2** function retrieves information for the specified interface on a local computer.

## Syntax

``` c++
NETIOAPI_API GetIfEntry2(
  _Inout_ PMIB_IF_ROW2 Row
);
```

## Parameters

- *Row* \[in, out\]  
   A pointer to a [**MIB\_IF\_ROW2**](mib-if-row2.md) structure that, on successful return, receives information for an interface on the local computer. On input, your driver must set the **InterfaceLuid** member or the **InterfaceIndex** member of the MIB\_IF\_ROW2 structure to the interface to retrieve information for.

## Return value

**GetIfEntry2** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **GetIfEntry2** returns one of the following error codes:

<table>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>STATUS_INVALID_PARAMETER</strong></td>
<td><p>An invalid parameter was passed to the function. This error is returned if a <strong>NULL</strong> pointer is passed in the <em>Row</em> parameter.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_NOT_FOUND</strong></td>
<td><p>The specified interface could not be found. This error is returned if the function cannot find the network interface that is specified by the <strong>InterfaceLuid</strong> or <strong>InterfaceIndex</strong> member of the <a href="mib-if-row2.md"><strong>MIB_IF_ROW2</strong></a> structure that the <em>Row</em> parameter points to.</p></td>
</tr>
<tr class="odd">
<td><strong>Other</strong></td>
<td><p>Use the <a href="/windows/win32/api/winbase/nf-winbase-formatmessage">FormatMessage</a> function to obtain the message string for the returned error.</p></td>
</tr>
</tbody>
</table>

## Remarks

On input, your driver must initialize at least the **InterfaceLuid** or **InterfaceIndex** member in the [**MIB\_IF\_ROW2**](mib-if-row2.md) structure that is passed in the *Row* parameter. The members are used in the order that is listed earlier. So if **InterfaceLuid** is specified, this member is used to determine the interface. If no value was set for the **InterfaceLuid** member (the value of this member was set to zero), the **InterfaceIndex** member is next used to determine the interface.

On output, the remaining fields of the MIB\_IF\_ROW2 structure that the *Row* parameter points to are filled in.

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

[**GetIfTable2**](getiftable2.md)

[**GetIfTable2Ex**](getiftable2ex.md)

[**MIB\_IF\_ROW2**](mib-if-row2.md)

[**MIB\_IF\_TABLE2**](mib-if-table2.md)
