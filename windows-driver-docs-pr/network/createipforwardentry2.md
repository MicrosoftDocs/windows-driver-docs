---
title: CreateIpForwardEntry2 function (Windows Drivers)
description: Learn more about the CreateIpForwardEntry2 function.
keywords:
- CreateIpForwardEntry2
- netioapi/CreateIpForwardEntry2
ms.date: 10/25/2022
ms.topic: reference
---

# CreateIpForwardEntry2 function

The **CreateIpForwardEntry2** function creates a new IP route entry on a local computer.

## Syntax

``` c++
NETIOAPI_API CreateIpForwardEntry2(
  _In_ const MIB_IPFORWARD_ROW2 *Row
);
```

## Parameters

- *Row* \[in\]  
   A pointer to a [**MIB\_IPFORWARD\_ROW2**](mib-ipforward-row2.md) structure entry for an IP route entry.

## Return value

**CreateIpForwardEntry2** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **CreateIpForwardEntry2** returns one of the following error codes:

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
<td><p>An invalid parameter was passed to the function. This error is returned if one of the following situations occurs:</p>
<ul>
<li><p>A <strong>NULL</strong> pointer is passed in the <em>Row</em> parameter.</p></li>
<li><p>The <strong>DestinationPrefix</strong> member of the <a href="mib-ipforward-row2.md"><strong>MIB_IPFORWARD_ROW2</strong></a> structure that the <em>Row</em> parameter points to was not specified.</p></li>
<li><p>The <strong>NextHop</strong> member of the MIB_IPFORWARD_ROW2 structure was not specified.</p></li>
<li><p>Both <strong>InterfaceLuid</strong> and <strong>InterfaceIndex</strong> members of the MIB_IPFORWARD_ROW2 structure were unspecified.</p></li>
<li><p>The <strong>PreferredLifetime</strong> member of the MIB_IPFORWARD_ROW2 structure is greater than the <strong>ValidLifetime</strong> member.</p></li>
<li><p>The <strong>SitePrefixLength</strong> member of the MIB_IPFORWARD_ROW2 structure is greater than the prefix length that is specified by the <strong>DestinationPrefix</strong> member.</p></li>
</ul>
<p>This error is returned if a <strong>NULL</strong> pointer is passed in the <em>Row</em> parameter, the <strong>DestinationPrefix</strong> member of the <a href="mib-ipforward-row2.md"><strong>MIB_IPFORWARD_ROW2</strong></a> structure that is pointed to by the <em>Row</em> parameter was not specified, the <strong>NextHop</strong> member of the MIB_IPFORWARD_ROW2 structure was not specified, or both <strong>InterfaceLuid</strong> and <strong>InterfaceIndex</strong> members of the MIB_IPFORWARD_ROW2 structure were unspecified. This error is also returned if the <strong>PreferredLifetime</strong> member that is specified in the MIB_IPFORWARD_ROW2 structure is greater than the <strong>ValidLifetime</strong> member, or if the <strong>SitePrefixLength</strong> in the MIB_IPFORWARD_ROW2 structure is greater than the prefix length that is specified in the <strong>DestinationPrefix</strong> member.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_NOT_FOUND</strong></td>
<td><p>The specified interface could not be found. This error is returned if the function cannot find the network interface that is specified by the <strong>InterfaceLuid</strong> or <strong>InterfaceIndex</strong> member of the MIB_IPNET_ROW2 structure that the <em>Row</em> parameter points to.</p></td>
</tr>
<tr class="odd">
<td><strong>STATUS_NOT_SUPPORTED</strong></td>
<td><p>The request is not supported. This error is returned if the interface that is specified does not support routes. This error is returned if no IPv4 stack is located on the local computer and AF_INET was specified in the address family in the <strong>DestinationPrefix</strong> member of the MIB_IPFORWARD_ROW2 structure that the <em>Row</em> parameter points to, or if no IPv6 stack is located on the local computer and AF_INET6 was specified for the address family in the <strong>DestinationPrefix</strong> member.</p></td>
</tr>
<tr class="even">
<td><strong>ERROR_OBJECT_ALREADY_EXISTS</strong></td>
<td><p>The object already exists. This error is returned if the <strong>DestinationPrefix</strong> member of the MIB_IPFORWARD_ROW2 structure that the <em>Row</em> parameter points to is a duplicate of an existing IP route entry on the interface that is specified by the <strong>InterfaceLuid</strong> or <strong>InterfaceIndex</strong> member of the MIB_IPFORWARD_ROW2 structure.</p></td>
</tr>
<tr class="odd">
<td><strong>Other</strong></td>
<td><p>Use the <a href="/windows/win32/api/winbase/nf-winbase-formatmessage">FormatMessage</a> function to obtain the message string for the returned error.</p></td>
</tr>
</tbody>
</table>

## Remarks

The **CreateIpForwardEntry2** function is used to add a new neighbor IP address entry on a local computer. Use the [**InitializeIpForwardEntry**](initializeipforwardentry.md) function to initialize the members of a [**MIB\_IPFORWARD\_ROW2**](mib-ipforward-row2.md) structure entry with default values. A driver can then change the members in the MIB\_IPFORWARD\_ROW2 entry that it wants to modify and then call **CreateIpForwardEntry2**.

Your driver must initialize the following members of the MIB\_IPFORWARD\_ROW2 structure that the *Row* parameter points to:

- Set **DestinationPrefix** to a valid IPv4 or IPv6 address prefix.

- Set **NextHop** to a valid IPv4 or IPv6 address and family.

- Set **InterfaceLuid** or **InterfaceIndex** to the LUID or index value of the interface.

The **InterfaceLuid** and **InterfaceIndex** members are used in the order that is listed earlier. So if the **InterfaceLuid** is specified, this member is used to determine the interface to add the IP route entry on. If no value was set for the **InterfaceLuid** member (the value of this member was set to zero), the **InterfaceIndex** member is next used to determine the interface.

The route metric offset that is specified in the **Metric** member of the MIB\_IPFORWARD\_ROW2 structure that the *Row* parameter points to represents only part of the complete route metric. The complete metric is a combination of this route metric offset added to the interface metric that is specified in the **Metric** member of the [**MIB\_IPINTERFACE\_ROW**](mib-ipinterface-row.md) structure of the associated interface. A driver can retrieve the interface metric by calling the [**GetIpInterfaceEntry**](getipinterfaceentry.md) function.

The **Age** and **Origin** members of the MIB\_IPFORWARD\_ROW2 structure that the *Row* parameter points to are ignored when the **CreateIpForwardEntry2** function is called. These members are set by the network stack and cannot be set by using the **CreateIpForwardEntry2** function.

The **CreateIpForwardEntry2** function fails if the **DestinationPrefix** and **NextHop** members of the MIB\_IPFORWARD\_ROW2 structure that the *Row* parameter points to are a duplicate of an existing IP route entry on the interface that is specified in the **InterfaceLuid** or **InterfaceIndex** members.

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

[**DeleteIpForwardEntry2**](deleteipforwardentry2.md)

[**GetBestRoute2**](getbestroute2.md)

[**GetIpForwardEntry2**](getipforwardentry2.md)

[**GetIpForwardTable2**](getipforwardtable2.md)

[**GetIpInterfaceEntry**](getipinterfaceentry.md)

[**InitializeIpForwardEntry**](initializeipforwardentry.md)

[**MIB\_IPFORWARD\_ROW2**](mib-ipforward-row2.md)

[**MIB\_IPFORWARD\_TABLE2**](mib-ipforward-table2.md)

[**MIB\_IPINTERFACE\_ROW**](mib-ipinterface-row.md)

[**NotifyRouteChange2**](notifyroutechange2.md)

[**SetIpForwardEntry2**](setipforwardentry2.md)
