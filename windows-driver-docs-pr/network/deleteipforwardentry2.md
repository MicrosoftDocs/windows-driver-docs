---
title: DeleteIpForwardEntry2 function (Windows Drivers)
description: Learn more about the DeleteIpForwardEntry2 function.
keywords:
- DeleteIpForwardEntry2
- netioapi/DeleteIpForwardEntry2
ms.date: 10/25/2022
---

# DeleteIpForwardEntry2 function

The **DeleteIpForwardEntry2** function deletes an IP route entry on a local computer.

## Syntax

``` c++
NETIOAPI_API DeleteIpForwardEntry2(
  _In_ const MIB_IPFORWARD_ROW2 *Row
);
```

## Parameters

- *Row* \[in\]  
   A pointer to a [**MIB\_IPFORWARD\_ROW2**](mib-ipforward-row2.md) structure entry for an IP route entry. On successful return, this entry is deleted.

## Return value

**DeleteIpForwardEntry2** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **DeleteIpForwardEntry2** returns one of the following error codes:

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
<td><p>An invalid parameter was passed to the function. This error is returned if a <strong>NULL</strong> pointer is passed in the <em>Row</em> parameter, the <strong>DestinationPrefix</strong> member of the <a href="mib-ipforward-row2.md"><strong>MIB_IPFORWARD_ROW2</strong></a> structure that the <em>Row</em> parameter points to was not specified, the <strong>NextHop</strong> member of the MIB_IPFORWARD_ROW2 structure was not specified, or both <strong>InterfaceLuid</strong> and <strong>InterfaceIndex</strong> members of the MIB_IPFORWARD_ROW2 structure were unspecified.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_NOT_FOUND</strong></td>
<td><p>The specified interface could not be found. This error is returned if the function cannot find the network interface that is specified by the <strong>InterfaceLuid</strong> or <strong>InterfaceIndex</strong> member of the MIB_IPFORWARD_ROW2 structure that the <em>Row</em> parameter points to.</p></td>
</tr>
<tr class="odd">
<td><strong>STATUS_NOT_SUPPORTED</strong></td>
<td><p>The request is not supported. This error is returned if no IPv4 stack is located on the local computer and an IPv4 address was specified in the <strong>Address</strong> member of the MIB_IPFORWARD_ROW2 structure that the <em>Row</em> parameter points to, or if no IPv6 stack is located on the local computer and an IPv6 address was specified in the <strong>Address</strong> member.</p></td>
</tr>
<tr class="even">
<td><strong>Other</strong></td>
<td><p>Use the <a href="/windows/win32/api/winbase/nf-winbase-formatmessage">FormatMessage</a> function to obtain the message string for the returned error.</p></td>
</tr>
</tbody>
</table>

## Remarks

The **DeleteIpForwardEntry2** function is used to delete a [**MIB\_IPFORWARD\_ROW2**](mib-ipforward-row2.md) structure entry.

On input, your driver must initialize the following members of the MIB\_IPFORWARD\_ROW2 structure that the *Row* parameter points to.

- **DestinationPrefix**  
   Set to a valid IPv4 or IPv6 address prefix and family.

- **NextHop**  
   Set to a valid IPv4 or IPv6 address and family.

- **InterfaceLuid** or **InterfaceIndex**  
   These members are used in the order that is listed earlier. So if **InterfaceLuid** is specified, this member is used to determine the interface. If no value was set for the **InterfaceLuid** member (the value of this member was set to zero), the **InterfaceIndex** member is next used to determine the interface.

On output, when the call is successful, **DeleteIpForwardEntry2** deletes the IP route entry.

The **DeleteIpForwardEntry2** function fails if the **DestinationPrefix** and **NextHop** members of the MIB\_IPFORWARD\_ROW2 structure that the *Row* parameter points to do not match an existing IP route entry on the interface that is specified in the **InterfaceLuid** or **InterfaceIndex** members.

Your driver can call the [**GetIpForwardTable2**](getipforwardtable2.md) function to enumerate the IP route entries on a local computer.

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

[**CreateIpForwardEntry2**](createipforwardentry2.md)

[**GetBestRoute2**](getbestroute2.md)

[**GetIpForwardEntry2**](getipforwardentry2.md)

[**GetIpForwardTable2**](getipforwardtable2.md)

[**InitializeIpForwardEntry**](initializeipforwardentry.md)

[**MIB\_IPFORWARD\_ROW2**](mib-ipforward-row2.md)

[**MIB\_IPFORWARD\_TABLE2**](mib-ipforward-table2.md)

[**NotifyRouteChange2**](notifyroutechange2.md)

[**SetIpForwardEntry2**](setipforwardentry2.md)
