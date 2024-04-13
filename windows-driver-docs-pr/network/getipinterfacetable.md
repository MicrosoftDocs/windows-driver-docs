---
title: GetIpInterfaceTable function (Windows Drivers)
description: Learn more about the GetIpInterfaceTable function.
keywords:
- GetIpInterfaceTable
- netioapi/GetIpInterfaceTable
ms.date: 10/25/2022
ms.topic: reference
---

# GetIpInterfaceTable function

The **GetIpInterfaceTable** function retrieves the IP interface entries on a local computer.

## Syntax

``` c++
NETIOAPI_API GetIpInterfaceTable(
  _In_  ADDRESS_FAMILY         Family,
  _Out_ PMIB_IPINTERFACE_TABLE *Table
);
```

## Parameters

- *Family* \[in\]  
   The address family of IP interfaces to retrieve.

   Possible values for the address family are listed in the Winsock2.h header file. Note that the values for the AF\_ address family and PF\_ protocol family constants are identical (for example, AF\_INET and PF\_INET), so you can use either constant.

   On Windows Vista and later versions of the Windows operating systems, possible values for the *Family* parameter are defined in the Ws2def.h header file. Note that the Ws2def.h header file is automatically included in Netioapi.h and you should never use Ws2def.h directly.

   The following values are currently supported for the address family:

   - AF\_INET  
     The IPv4 address family.

   - AF\_INET6  
     The IPv6 address family.

   - AF\_UNSPEC  
     The address family is unspecified. When this value is specified, the **GetIpInterfaceTable** function returns the IP interface table that contains both IPv4 and IPv6 entries.

- *Table* \[out\]  
   A pointer to a buffer that receives the table of IP interface entries in a [**MIB\_IPINTERFACE\_TABLE**](mib-ipinterface-table.md) structure.

## Return value

**GetIpInterfaceTable** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **GetIpInterfaceTable** returns one of the following error codes:

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
<td><p>No IP interface entries, as specified in the <em>Family</em> parameter, were found.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_NOT_SUPPORTED</strong></td>
<td><p>The function is not supported. This error is returned when the IP transport that is specified in the <em>Address</em> parameter is not configured on the local computer. This error is also returned on versions of Windows where this function is not supported.</p></td>
</tr>
<tr class="odd">
<td><strong>Other</strong></td>
<td><p>Use the <a href="/windows/win32/api/winbase/nf-winbase-formatmessage">FormatMessage</a> function to obtain the message string for the returned error.</p></td>
</tr>
</tbody>
</table>

## Remarks

The **GetIpInterfaceTable** function enumerates the IP interfaces on a local computer and returns this information in an [**MIB\_IPINTERFACE\_TABLE**](mib-ipinterface-table.md) structure.

**GetIpInterfaceTable** returns IP interface entries in a MIB\_IPINTERFACE\_TABLE structure in the buffer that the *Table* parameter points to. The MIB\_IPINTERFACE\_TABLE structure contains an IP interface entry count and an array of [**MIB\_IPINTERFACE\_ROW**](mib-ipinterface-row.md) structures for each IP interface entry. When these returned structures are no longer required, your driver should free the memory by calling the [**FreeMibTable**](freemibtable.md) function.

Your driver must initialize the *Family* parameter to either AF\_INET or AF\_INET6.

Note that the returned MIB\_IPINTERFACE\_TABLE structure that the *Table* parameter points to might contain padding for alignment between the **NumEntries** member and the first [**MIB\_IPINTERFACE\_ROW**](mib-ipinterface-row.md) array entry in the **Table** member of the MIB\_IPINTERFACE\_TABLE structure. Padding for alignment might also be present between the MIB\_IPINTERFACE\_ROW array entries. Any access to a MIB\_IPINTERFACE\_ROW array entry should assume padding might exist.

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

[**MIB\_IPINTERFACE\_ROW**](mib-ipinterface-row.md)

[**MIB\_IPINTERFACE\_TABLE**](mib-ipinterface-table.md)

[**MIB\_IPNET\_ROW2**](mib-ipnet-row2.md)

[**MIB\_IPNET\_TABLE2**](mib-ipnet-table2.md)
