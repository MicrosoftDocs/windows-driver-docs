---
title: CreateIpNetEntry2 function (Windows Drivers)
description: Learn more about the CreateIpNetEntry2 function.
keywords:
- CreateIpNetEntry2
- netioapi/CreateIpNetEntry2
ms.date: 10/25/2022
---

# CreateIpNetEntry2 function

The **CreateIpNetEntry2** function creates a new neighbor IP address entry on the local computer.

## Syntax

``` c++
NETIOAPI_API CreateIpNetEntry2(
  _In_ const MIB_IPNET_ROW2 *Row
);
```

## Parameters

- *Row* \[in\]  
   A pointer to a [**MIB\_IPNET\_ROW2**](mib-ipnet-row2.md) structure entry for an IP route entry.

## Return value

**CreateIpNetEntry2** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **CreateIpNetEntry2** returns one of the following error codes:

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
<td><p>An invalid parameter was passed to the function. This error is returned if one of the following items occurs:</p>
<ul>
<li><p>A <strong>NULL</strong> pointer is passed in the <em>Row</em> parameter.</p></li>
<li><p>The <strong>Address</strong> member of the <a href="mib-ipnet-row2.md"><strong>MIB_IPNET_ROW2</strong></a> structure that the <em>Row</em> parameter points to was not set to a valid unicast, anycast, or multicast IPv4 or IPv6 address.</p></li>
<li><p>The <strong>PhysicalAddress</strong> and <strong>PhysicalAddressLength</strong> members of the MIB_IPNET_ROW2 structure were not set to a valid physical address.</p></li>
<li><p>Both <strong>InterfaceLuid</strong> and <strong>InterfaceIndex</strong> members of the MIB_IPNET_ROW2 structure were unspecified.</p></li>
<li><p>A loopback address was passed in the <strong>Address</strong> member.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>STATUS_NOT_FOUND</strong></td>
<td><p>The specified interface could not be found. This error is returned if the function cannot find the network interface that is specified by the <strong>InterfaceLuid</strong> or <strong>InterfaceIndex</strong> member of the MIB_IPNET_ROW2 structure that the <em>Row</em> parameter points to.</p></td>
</tr>
<tr class="odd">
<td><strong>STATUS_NOT_SUPPORTED</strong></td>
<td><p>The request is not supported. This error is returned if no IPv4 stack is located on the local computer and an IPv4 address was specified in the <strong>Address</strong> member of the MIB_IPNET_ROW2 structure that the <em>Row</em> parameter points, or if no IPv6 stack is located on the local computer and an IPv6 address was specified in the <strong>Address</strong> member.</p></td>
</tr>
<tr class="even">
<td><strong>ERROR_OBJECT_ALREADY_EXISTS</strong></td>
<td><p>The object already exists. This error is returned if the <strong>Address</strong> member of the MIB_IPNET_ROW2 structure that the <em>Row</em> parameter points to is a duplicate of an existing neighbor IP address on the interface that is specified by the <strong>InterfaceLuid</strong> or <strong>InterfaceIndex</strong> member of the MIB_IPNET_ROW2 structure.</p></td>
</tr>
<tr class="odd">
<td><strong>Other</strong></td>
<td><p>Use the <a href="/windows/win32/api/winbase/nf-winbase-formatmessage">FormatMessage</a> function to obtain the message string for the returned error.</p></td>
</tr>
</tbody>
</table>

## Remarks

Your driver must initialize the following members of the [**MIB\_IPNET\_ROW2**](mib-ipnet-row2.md) structure that the *Row* parameter points to:

- Set the **Address** member to a valid unicast, anycast, or multicast IPv4 or IPv6 address and family.

- Set the **PhysicalAddress** and **PhysicalAddressLength** members in the MIB\_IPNET\_ROW2 structure to a valid physical address.

- Set **InterfaceLuid** or **InterfaceIndex** to the LUID or index value of the interface.

The **InterfaceLuid** and **InterfaceIndex** members are used in the order that is listed earlier. So if the **InterfaceLuid** is specified, this member is used to determine the interface to add the unicast IP address on. If no value was set for the **InterfaceLuid** member (the value of this member was set to zero), the **InterfaceIndex** member is next used to determine the interface.

The **CreateIpNetEntry2** function fails if the IP address that is passed in the **Address** member of the MIB\_IPNET\_ROW2 structure that the *Row* parameter points to is a duplicate of an existing neighbor IP address on the interface.

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

[**DeleteIpNetEntry2**](deleteipnetentry2.md)

[**FlushIpNetTable2**](flushipnettable2.md)

[**GetIpNetEntry2**](getipnetentry2.md)

[**GetIpNetTable2**](getipnettable2.md)

[**MIB\_IPNET\_ROW2**](mib-ipnet-row2.md)

[**MIB\_IPNET\_TABLE2**](mib-ipnet-table2.md)

[**ResolveIpNetEntry2**](resolveipnetentry2.md)

[**SetIpNetEntry2**](setipnetentry2.md)
