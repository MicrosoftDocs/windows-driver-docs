---
title: SetIpNetEntry2 function (Windows Drivers)
description: Learn more about the SetIpNetEntry2 function.
keywords:
- SetIpNetEntry2
- netioapi/SetIpNetEntry2
ms.date: 10/25/2022
---

# SetIpNetEntry2 function

The **SetIpNetEntry2** function sets the physical address of an existing neighbor IP address entry on a local computer.

## Syntax

``` c++
NETIOAPI_API SetIpNetEntry2(
  _In_ PMIB_IPNET_ROW2 Row
);
```

## Parameters

- *Row* \[in\]  
   A pointer to a [**MIB\_IPNET\_ROW2**](mib-ipnet-row2.md) structure entry for a neighbor IP address entry.

## Return value

**SetIpNetEntry2** return STATUS\_SUCCESS if the function succeeds.

If the function fails, **SetIpNetEntry2** returns one of the following error codes:

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
<td><p>An invalid parameter was passed to the function. This error is returned in the following situations.</p>
<ul>
<li><p>A <strong>NULL</strong> pointer was passed in the <em>Row</em> parameter.</p></li>
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
<td><p>The request is not supported. This error is returned if no IPv4 stack is located on the local computer and an IPv4 address was specified in the <strong>Address</strong> member of the MIB_IPNET_ROW2 structure that the <em>Row</em> parameter points to, or if no IPv6 stack is located on the local computer and an IPv6 address was specified in the <strong>Address</strong> member.</p></td>
</tr>
<tr class="even">
<td><strong>Other</strong></td>
<td><p>Use the <a href="/windows/win32/api/winbase/nf-winbase-formatmessage">FormatMessage</a> function to obtain the message string for the returned error.</p></td>
</tr>
</tbody>
</table>

## Remarks

Your driver must initialize the following members of the [**MIB\_IPNET\_ROW2**](mib-ipnet-row2.md) structure that the *Row* parameter points to.

- **Address**  
   Set to a valid unicast, anycast, or multicast IPv4 or IPv6 address and family.

- **PhysicalAddress** and **PhysicalAddressLength**  
   Set to a valid physical address.

- **InterfaceLuid** or **InterfaceIndex**  
   These members are used in the order that is listed earlier. So if **InterfaceLuid** is specified, this member is used to determine the interface. If no value was set for the **InterfaceLuid** member (the value of this member was set to zero), the **InterfaceIndex** member is next used to determine the interface.

The **SetIpNetEntry2** function fails if the IP address that is passed in the **Address** member of the MIB\_IPNET\_ROW2 structure that the *Row* parameter points to is not an existing neighbor IP address on the interface that is specified.

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

[**ResolveIpNetEntry2**](resolveipnetentry2.md)
