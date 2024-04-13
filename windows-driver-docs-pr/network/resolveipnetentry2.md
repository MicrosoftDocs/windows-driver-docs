---
title: ResolveIpNetEntry2 function (Windows Drivers)
description: Learn more about the ResolveIpNetEntry2 function.
keywords:
- ResolveIpNetEntry2
- netioapi/ResolveIpNetEntry2
ms.date: 10/25/2022
ms.topic: reference
---

# ResolveIpNetEntry2 function

The **ResolveIpNetEntry2** function resolves the physical address for a neighbor IP address entry on a local computer.

## Syntax

``` c++
NETIOAPI_API ResolveIpNetEntry2(
  _Inout_        PMIB_IPNET_ROW2 Row,
  _In_opt_ const SOCKADDR_INET   *SourceAddress
);
```

## Parameters

- *Row* \[in, out\]  
   A pointer to a [**MIB\_IPNET\_ROW2**](mib-ipnet-row2.md) structure entry for a neighbor IP address entry. On successful return, this structure is updated with the properties for neighbor IP address.

- *SourceAddress* \[in, optional\]  
   A pointer to an optional source IP address that is used to select the interface to send the requests on for the neighbor IP address entry.

## Return value

**ResolveIpNetEntry2** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **ResolveIpNetEntry2** returns one of the following error codes:

<table>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>STATUS_BAD_NETWORK_NAME</strong></td>
<td><p>The network name cannot be found. This error is returned if the network with the neighbor IP address is unreachable.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_INVALID_PARAMETER</strong></td>
<td><p>An invalid parameter was passed to the function. This error is returned if a <strong>NULL</strong> pointer is passed in the <em>Row</em> parameter, the <strong>Address</strong> member of the <a href="mib-ipnet-row2.md"><strong>MIB_IPNET_ROW2</strong></a> structure that the <em>Row</em> parameter points to was not set to a valid IPv4 or IPv6 address, or both <strong>InterfaceLuid</strong> and <strong>InterfaceIndex</strong> members of the MIB_IPNET_ROW2 structure were unspecified. This error is also returned if a loopback address was passed in the <strong>Address</strong> member.</p></td>
</tr>
<tr class="odd">
<td><strong>STATUS_NOT_FOUND</strong></td>
<td><p>The specified interface could not be found. This error is returned if the function cannot find the network interface that is specified by the <strong>InterfaceLuid</strong> or <strong>InterfaceIndex</strong> member of the MIB_IPNET_ROW2 structure that the <em>Row</em> parameter points to.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_NOT_SUPPORTED</strong></td>
<td><p>The request is not supported. This error is returned if no IPv4 stack is located on the local computer and an IPv4 address was specified in the <strong>Address</strong> member of the MIB_IPNET_ROW2 structure that the <em>Row</em> parameter points to, or if no IPv6 stack is located on the local computer and an IPv6 address was specified in the <strong>Address</strong> member.</p></td>
</tr>
<tr class="odd">
<td><strong>Other</strong></td>
<td><p>Use the <a href="/windows/win32/api/winbase/nf-winbase-formatmessage">FormatMessage</a> function to obtain the message string for the returned error.</p></td>
</tr>
</tbody>
</table>

## Remarks

The **ResolveIpNetEntry2** function is used to resolve the physical address for a neighbor IP address entry on a local computer. This function flushes any existing neighbor entry that matches the IP address on the interface and then resolves the physical address (MAC) address by sending ARP requests for an IPv4 address or Neighbor Solicitation (NS) requests for an IPv6 address. If the *SourceAddress* parameter is specified, **ResolveIpNetEntry2** selects the interface with this source IP address to send the requests on. If the *SourceAddress* parameter is not specified (**NULL** was passed in this parameter), **ResolveIpNetEntry2** automatically selects the best interface to send the requests on.

Your driver must initialize the following members of the [**MIB\_IPNET\_ROW2**](mib-ipnet-row2.md) structure that the *Row* parameter points to.

- **Address**  
   Set to a valid IPv4 or IPv6 address and family.

- **InterfaceLuid** or **InterfaceIndex**  
   These members are used in the order that is listed earlier. So if **InterfaceLuid** is specified, this member is used to determine the interface. If no value was set for the **InterfaceLuid** member (the value of this member was set to zero), the **InterfaceIndex** member is next used to determine the interface.

If the IP address that is passed in the **Address** member of the MIB\_IPNET\_ROW2 structure that the *Row* parameter points to is a duplicate of an existing neighbor IP address on the interface, the **ResolveIpNetEntry2** function flushes the existing entry before resolving the IP address.

On output, when the call is successful, **ResolveIpNetEntry2** retrieves the other properties for the neighbor IP address and fills in the MIB\_IPNET\_ROW2 structure that the *Row* parameter points to. The **PhysicalAddress** and **PhysicalAddressLength** members in the MIB\_IPNET\_ROW2 structure are initialized to a valid physical address.

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

[**FlushIpNetTable2**](flushipnettable2.md)

[**GetIpNetEntry2**](getipnetentry2.md)

[**GetIpNetTable2**](getipnettable2.md)

[**MIB\_IPNET\_ROW2**](mib-ipnet-row2.md)

[**MIB\_IPNET\_TABLE2**](mib-ipnet-table2.md)

[**SetIpNetEntry2**](setipnetentry2.md)
