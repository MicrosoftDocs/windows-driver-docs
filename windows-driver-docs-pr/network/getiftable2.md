---
title: GetIfTable2 function (Windows Drivers)
description: Learn more about the GetIfTable2 function.
keywords:
- GetIfTable2
- netioapi/GetIfTable2
ms.date: 10/25/2022
---

# GetIfTable2 function

The **GetIfTable2** function retrieves the MIB-II interface table.

## Syntax

``` c++
NETIOAPI_API GetIfTable2(
  _Out_ PMIB_IF_TABLE2 *Table
);
```

## Parameters

- *Table* \[out\]  
   A pointer to a buffer that receives the table of interfaces in a [**MIB\_IF\_TABLE2**](mib-if-table2.md) structure.

## Return value

**GetIfTable2** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **GetIfTable2** returns one of the following error codes:

<table>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>STATUS_NOT_ENOUGH_MEMORY</strong></td>
<td><p>Insufficient memory resources are available to complete the operation.</p></td>
</tr>
<tr class="even">
<td><strong>Other</strong></td>
<td><p>Use the <a href="/windows/win32/api/winbase/nf-winbase-formatmessage">FormatMessage</a> function to obtain the message string for the returned error.</p></td>
</tr>
</tbody>
</table>

## Remarks

The **GetIfTable2** function enumerates the logical and physical interfaces on a local computer and returns this information in a [**MIB\_IF\_TABLE2**](mib-if-table2.md) structure.

Your driver can use a similar function, [**GetIfTable2Ex**](getiftable2ex.md), to specify the level of interfaces to return. A call to the **GetIfTable2Ex** function with the *Level* parameter set to **MibIfTableNormal** retrieves the same results as calling the **GetIfTable2** function.

**GetIfTable2** returns interfaces in a MIB\_IF\_TABLE2 structure in the buffer that the *Table* parameter points to. The MIB\_IF\_TABLE2 structure contains an interface count and an array of [**MIB\_IF\_ROW2**](mib-if-row2.md) structures for each interface. **GetIfTable2** allocates memory for the MIB\_IF\_TABLE2 structure and the MIB\_IF\_ROW2 entries in this structure. When these returned structures are no longer required, your driver should free the memory by calling [**FreeMibTable**](freemibtable.md).

Note that the returned MIB\_IF\_TABLE2 structure that the *Table* parameter points to might contain padding for alignment between the **NumEntries** member and the first MIB\_IF\_ROW2 array entry in the **Table** member of the MIB\_IF\_TABLE2 structure. Padding for alignment might also be present between the MIB\_IF\_ROW2 array entries. Any access to a MIB\_IF\_ROW2 array entry should assume padding may exist.

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

[**FreeMibTable**](freemibtable.md)

[**GetIfTable2Ex**](getiftable2ex.md)

[**MIB\_IF\_TABLE2**](mib-if-table2.md)

[**MIB\_IF\_ROW2**](mib-if-row2.md)
