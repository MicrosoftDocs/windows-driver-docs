---
title: FlushIpNetTable2 function (Windows Drivers)
description: Learn more about the .
keywords:
- FlushIpNetTable2
- netioapi/FlushIpNetTable2
ms.date: 10/25/2022
---

# FlushIpNetTable2 function

The **FlushIpNetTable2** function flushes the IP neighbor table on a local computer.

## Syntax

``` c++
NETIOAPI_API FlushIpNetTable2(
  _In_ ADDRESS_FAMILY Family,
  _In_ NET_IFINDEX    InterfaceIndex
);
```

## Parameters

- *Family* \[in\]  
   The address family to flush.

   Possible values for the address family are listed in the Winsock2.h header file. Note that the values for the AF\_ address family and PF\_ protocol family constants are identical (for example, AF\_INET and PF\_INET), so you can use either constant.

   On Windows Vista and later versions of the Windows operating systems, possible values for the *Family* parameter are defined in the Ws2def.h header file. Note that the Ws2def.h header file is automatically included in Netioapi.h and you should never use Ws2def.h directly.

   The following values are currently supported for the address family:

   - AF\_INET  
     The IPv4 address family. When this value is specified, this function flushes the neighbor IP address table that contains only IPv4 entries.

   - AF\_INET6  
     The IPv6 address family. When this value is specified, this function flushes the neighbor IP address table that contains only IPv6 entries.

   - AF\_UNSPEC  
     The address family is unspecified. When this value is specified, this function flushes the neighbor IP address table that contains both IPv4 and IPv6 entries.

- *InterfaceIndex* \[in\]  
   The interface index. If the index is specified, the function flushes the neighbor IP address entries on a specific interface.Ootherwise, the function flushes the neighbor IP address entries on all the interfaces. To ignore the interface, set this parameter to zero.

## Return value

**FlushIpNetTable2** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **FlushIpNetTable2** returns one of the following error codes:

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
<td><p>An invalid parameter was passed to the function. This error is returned if the <em>Family</em> parameter was not specified as AF_INET, AF_INET6, or AF_UNSPEC.</p></td>
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

The **FlushIpNetTable2** function flushes or deletes the neighbor IP addresses on a local computer. Your driver can use the *Family* parameter to limit neighbor IP addresses to delete to a particular IP address family. If neighbor IP addresses for both IPv4 and IPv6 should be deleted, your driver should set the *Family* parameter to AF\_UNSPEC. Your driver can use the *InterfaceIndex* parameter to limit neighbor IP addresses to delete to a particular interface. If neighbor IP addresses for all interfaces should be deleted, your driver should set the *InterfaceIndex* parameter to zero.

Your driver must initialize the *Family* parameter to either AF\_INET, AF\_INET6, or AF\_UNSPEC.

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

[**CreateIpNetEntry2**](createipnetentry2.md)

[**DeleteIpNetEntry2**](deleteipnetentry2.md)

[**GetIpNetEntry2**](getipnetentry2.md)

[**GetIpNetTable2**](getipnettable2.md)

[**MIB\_IPNET\_ROW2**](mib-ipnet-row2.md)

[**MIB\_IPNET\_TABLE2**](mib-ipnet-table2.md)

[**ResolveIpNetEntry2**](resolveipnetentry2.md)

[**SetIpNetEntry2**](setipnetentry2.md)
