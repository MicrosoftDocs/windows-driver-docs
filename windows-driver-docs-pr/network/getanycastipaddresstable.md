---
title: GetAnycastIpAddressTable function (Windows Drivers)
description: Learn more about the GetAnycastIpAddressTable function.
keywords:
- GetAnycastIpAddressTable
- netioapi/GetAnycastIpAddressTable
ms.date: 10/25/2022
ms.topic: reference
---

# GetAnycastIpAddressTable function

The **GetAnycastIpAddressTable** function retrieves the anycast IP address table on a local computer.

## Syntax

``` c++
NETIOAPI_API GetAnycastIpAddressTable(
  _In_  ADDRESS_FAMILY              Family,
  _Out_ PMIB_ANYCASTIPADDRESS_TABLE *Table
);
```

## Parameters

- *Family* \[in\]  
   The address family to retrieve.

   Possible values for the address family are listed in the Winsock2.h header file. Note that the values for the AF\_ address family and PF\_ protocol family constants are identical (for example, AF\_INET and PF\_INET), so you can use either constant.

   On Windows Vista and later versions of the Windows operating systems, possible values for the *Family* parameterare defined in the Ws2def.h header file. Note that the Ws2def.h header file is automatically included in Netioapi.h and you should never use Ws2def.h directly.

   The following values are currently supported for the address family:

   - AF\_INET  
     The IPv4 address family. When this value is specified, this function returns the anycast IP address table that contains only IPv4 entries.

   - AF\_INET6  
     The IPv6 address family. When this value is specified, this function returns the anycast IP address table that contains only IPv6 entries.

   - AF\_UNSPEC  
     The address family is unspecified. When this value is specified, this function returns the anycast IP address table that contains both IPv4 and IPv6 entries.

- *Table* \[out\]  
   A pointer to a [**MIB\_ANYCASTIPADDRESS\_TABLE**](mib-anycastipaddress-table.md) structure that contains a table of anycast IP address entries on the local computer.

## Return value

**GetAnycastIpAddressTable** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **GetAnycastIpAddressTable** returns one of the following error codes:

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
<td><p>An invalid parameter was passed to the function. This error is returned if a <strong>NULL</strong> pointer is passed in the <em>Table</em> parameter or the <em>Family</em> parameter was not specified as AF_INET, AF_INET6, or AF_UNSPEC.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_NOT_ENOUGH_MEMORY</strong></td>
<td><p>Insufficient memory resources are available to complete the operation.</p></td>
</tr>
<tr class="odd">
<td><strong>STATUS_NOT_FOUND</strong></td>
<td><p>No anycast IP address entries, as specified in the <em>Family</em> parameter, were found.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_NOT_SUPPORTED</strong></td>
<td><p>The request is not supported. This error is returned if no IPv4 stack is located on the local computer and AF_INET was specified in the <em>Family</em> parameter, or if no IPv6 stack is located on the local computer and AF_INET6 was specified in the <em>Family</em> parameter. This error is also returned on versions of Windows where this function is not supported.</p></td>
</tr>
<tr class="odd">
<td><strong>Other</strong></td>
<td><p>Use the <a href="/windows/win32/api/winbase/nf-winbase-formatmessage">FormatMessage</a> function to obtain the message string for the returned error.</p></td>
</tr>
</tbody>
</table>

## Remarks

The **GetAnycastIpAddressTable** function enumerates the anycast IP addresses on a local computer and returns this information in a [**MIB\_ANYCASTIPADDRESS\_TABLE**](mib-anycastipaddress-table.md) structure.

The anycast IP address entries are returned in a MIB\_ANYCASTIPADDRESS\_TABLE structure in the buffer that the *Table* parameter points to. The MIB\_ANYCASTIPADDRESS\_TABLE structure contains an anycast IP address entry count and an array of [**MIB\_ANYCASTIPADDRESS\_ROW**](mib-anycastipaddress-row.md) structures for each anycast IP address entry. When these returned structures are no longer required, your driver should free the memory by calling [**FreeMibTable**](freemibtable.md).

Your driver must initialize the *Family* parameter to either AF\_INET, AF\_INET6, or AF\_UNSPEC.

Note that the returned MIB\_ANYCASTIPADDRESS\_TABLE structure that the *Table* parameter points to might contain padding for alignment between the **NumEntries** member and the first MIB\_ANYCASTIPADDRESS\_ROW array entry in the **Table** member of the MIB\_ANYCASTIPADDRESS\_TABLE structure. Padding for alignment might also be present between the MIB\_ANYCASTIPADDRESS\_ROW array entries. Any access to a MIB\_ANYCASTIPADDRESS\_ROW array entry should assume padding may exist.

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

[**MIB\_ANYCASTIPADDRESS\_ROW**](mib-anycastipaddress-row.md)

[**MIB\_ANYCASTIPADDRESS\_TABLE**](mib-anycastipaddress-table.md)
