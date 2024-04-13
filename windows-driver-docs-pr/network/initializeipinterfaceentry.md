---
title: InitializeIpInterfaceEntry function (Windows Drivers)
description: Learn more about the InitializeIpInterfaceEntry function.
keywords:
- InitializeIpInterfaceEntry
- netioapi/InitializeIpInterfaceEntry
ms.date: 10/25/2022
ms.topic: reference
---

# InitializeIpInterfaceEntry function

The **InitializeIpInterfaceEntry** function initializes the members of an [**MIB\_IPINTERFACE\_ROW**](mib-ipinterface-row.md) structure entry with default values.

## Syntax

``` c++
VOID NETIOAPI_API_ InitializeIpInterfaceEntry(
  _Inout_ PMIB_IPINTERFACE_ROW Row
);
```

## Parameters

- *Row* \[in, out\]  
   A pointer to a [**MIB\_IPINTERFACE\_ROW**](mib-ipinterface-row.md) structure to initialize. On successful return, the fields in this parameter are initialized with default information for an interface on the local computer.

## Return value

**InitializeIpInterfaceEntry** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **InitializeIpInterfaceEntry** returns one of the following error codes:

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
<td><p>An invalid parameter was passed to the function. This error is returned if a <strong>NULL</strong> pointer is passed in the <em>Row</em> parameter</p></td>
</tr>
<tr class="even">
<td><strong>Other</strong></td>
<td><p>Use the <a href="/windows/win32/api/winbase/nf-winbase-formatmessage">FormatMessage</a> function to obtain the message string for the returned error.</p></td>
</tr>
</tbody>
</table>

## Remarks

On output, the members of the [**MIB\_IPINTERFACE\_ROW**](mib-ipinterface-row.md) structure that the *Row* parameter points to are initialized as follows.

- **Family**  
   Set to AF\_UNSPEC.

- **InterfaceLuid**  
   Set to an unspecified value.

- All other members  
   Set to zero.

Your driver must use the **InitializeIpInterfaceEntry** function to initialize the fields of a MIB\_IPINTERFACE\_ROW structure entry with default values. A driver can then change the fields in the MIB\_IPINTERFACE\_ROW entry that it wants to modify, and then call the [**SetIpInterfaceEntry**](setipinterfaceentry.md) function.

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

[**GetIpInterfaceEntry**](getipinterfaceentry.md)

[**GetIpInterfaceTable**](getipinterfacetable.md)

[**MIB\_IPINTERFACE\_ROW**](mib-ipinterface-row.md)

[**MIB\_IPINTERFACE\_TABLE**](mib-ipinterface-table.md)

[**SetIpInterfaceEntry**](setipinterfaceentry.md)
