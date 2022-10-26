---
title: GetIfStackTable function (Windows Drivers)
description: Learn more about the GetIfStackTable function.
keywords:
- GetIfStackTable
- netioapi/GetIfStackTable
ms.date: 10/25/2022
---

# GetIfStackTable function

The **GetIfStackTable** function retrieves a table of network interface stack row entries that specify the relationship of the network interfaces on an interface stack.

## Syntax

``` c++
NETIOAPI_API GetIfStackTable(
  _Out_ PMIB_IFSTACK_TABLE *Table
);
```

## Parameters

- *Table* \[out\]  
   A pointer to a buffer that receives the table of interface stack row entries in a [**MIB\_IFSTACK\_TABLE**](mib-ifstack-table.md) structure.

## Return value

**GetIfStackTable** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **GetIfStackTable** returns one of the following error codes:

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
<td><p>An invalid parameter was passed to the function. This error is returned if a <strong>NULL</strong> pointer is passed in the <em>Table</em> parameter.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_NOT_ENOUGH_MEMORY</strong></td>
<td><p>Insufficient memory resources are available to complete the operation.</p></td>
</tr>
<tr class="odd">
<td><strong>STATUS_NOT_FOUND</strong></td>
<td><p>No interface stack entries were found.</p></td>
</tr>
<tr class="even">
<td><strong>Other</strong></td>
<td><p>Use the <a href="/windows/win32/api/winbase/nf-winbase-formatmessage">FormatMessage</a> function to obtain the message string for the returned error.</p></td>
</tr>
</tbody>
</table>

## Remarks

The **GetIfStackTable** function enumerates the physical and logical network interfaces on an interface stack on a local computer and returns this information in a [**MIB\_IFSTACK\_TABLE**](mib-ifstack-table.md) structure.

Interface stack entries are returned in a MIB\_IFSTACK\_TABLE structure in the buffer that the *Table* parameter points to. The MIB\_IFSTACK\_TABLE structure contains an interface stack entry count and an array of [**MIB\_IFSTACK\_ROW**](mib-ifstack-row.md) structures for each interface stack entry.

The relationship between the interfaces in the interface stack is that the interface with index in the **HigherLayerInterfaceIndex** member of the MIB\_IFSTACK\_ROW structure is immediately above the interface with index in the **LowerLayerInterfaceIndex** member of the MIB\_IFSTACK\_ROW structure.

Memory is allocated by the **GetIfStackTable** function for the MIB\_IFSTACK\_TABLE structure and the MIB\_IFSTACK\_ROW entries in this structure. When these returned structures are no longer required, your driver should free the memory by calling [**FreeMibTable**](freemibtable.md).

Note that the returned MIB\_IFSTACK\_TABLE structure that the *Table* parameter points to might contain padding for alignment between the **NumEntries** member and the first MIB\_IFSTACK\_ROW array entry in the **Table** member of the MIB\_IFSTACK\_TABLE structure. Padding for alignment might also be present between the MIB\_IFSTACK\_ROW array entries. Any access to a MIB\_IFSTACK\_ROW array entry should assume padding may exist.

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

[**GetIfEntry2**](getifentry2.md)

[**GetIfTable2**](getiftable2.md)

[**GetInvertedIfStackTable**](getinvertedifstacktable.md)

[**GetIpInterfaceEntry**](getipinterfaceentry.md)

[**InitializeIpInterfaceEntry**](initializeipinterfaceentry.md)

[**MIB\_IF\_ROW2**](mib-if-row2.md)

[**MIB\_IF\_TABLE2**](mib-if-table2.md)

[**MIB\_IFSTACK\_ROW**](mib-ifstack-row.md)

[**MIB\_IFSTACK\_TABLE**](mib-ifstack-table.md)

[**MIB\_INVERTEDIFSTACK\_ROW**](mib-invertedifstack-row.md)

[**MIB\_INVERTEDIFSTACK\_TABLE**](mib-invertedifstack-table.md)

[**MIB\_IPINTERFACE\_ROW**](mib-ipinterface-row.md)

[**NotifyIpInterfaceChange**](notifyipinterfacechange.md)

[**SetIpInterfaceEntry**](setipinterfaceentry.md)
