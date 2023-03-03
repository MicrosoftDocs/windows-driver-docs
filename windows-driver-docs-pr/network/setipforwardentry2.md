---
title: SetIpForwardEntry2 function (Windows Drivers)
description: Learn more about the SetIpForwardEntry2 function.
keywords:
- SetIpForwardEntry2
- netioapi/SetIpForwardEntry2
ms.date: 10/25/2022
ms.topic: reference
---

# SetIpForwardEntry2 function

The **SetIpForwardEntry2** function sets the properties of an IP route entry on a local computer.

## Syntax

``` c++
NETIOAPI_API SetIpForwardEntry2(
  _In_ const MIB_IPFORWARD_ROW2 *Route
);
```

## Parameters

- *Route* \[in\]  
   A pointer to a [**MIB\_IPFORWARD\_ROW2**](mib-ipforward-row2.md) structure entry for an IP route entry. Your driver must set the **DestinationPrefix** member of the MIB\_IPFORWARD\_ROW2 structure to a valid IP destination prefix and family, set the **NextHop** member of MIB\_IPFORWARD\_ROW2 to a valid IP address and family, and specify the **InterfaceLuid** member or the **InterfaceIndex** member of MIB\_IPFORWARD\_ROW2.

## Return value

**SetIpForwardEntry2** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **SetIpForwardEntry2** returns one of the following error codes:

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
<td><p>An invalid parameter was passed to the function. This error is returned if a <strong>NULL</strong> pointer is passed in the <em>Route</em> parameter, the <strong>DestinationPrefix</strong> member of the <a href="mib-ipforward-row2.md"><strong>MIB_IPFORWARD_ROW2</strong></a> structure that the <em>Route</em> parameter points to was not specified, the <strong>NextHop</strong> member of the MIB_IPFORWARD_ROW2 structure was not specified, or both <strong>InterfaceLuid</strong> and <strong>InterfaceIndex</strong> members of the MIB_IPFORWARD_ROW2 structure were unspecified.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_NOT_FOUND</strong></td>
<td><p>The specified interface could not be found. This error is returned if the function cannot find the network interface that is specified by the <strong>InterfaceLuid</strong> or <strong>InterfaceIndex</strong> member of the MIB_IPFORWARD_ROW2 structure that the <em>Route</em> parameter points to.</p></td>
</tr>
<tr class="odd">
<td><strong>Other</strong></td>
<td><p>Use the <a href="/windows/win32/api/winbase/nf-winbase-formatmessage">FormatMessage</a> function to obtain the message string for the returned error.</p></td>
</tr>
</tbody>
</table>

## Remarks

The **SetIpForwardEntry2** function is used to set the properties for an existing IP route entry on a local computer.

Your driver must initialize the following members of the [**MIB\_IPFORWARD\_ROW2**](mib-ipforward-row2.md) structure that the *Row* parameter points to.

- **DestinationPrefix**  
   Set to a valid IPv4 or IPv6 address prefix and family.

- **NextHop**  
   Set to a valid IPv4 or IPv6 address and family.

- **InterfaceLuid** or **InterfaceIndex**  
   These members are used in the order that is listed earlier. So if **InterfaceLuid** is specified, this member is used to determine the interface. If no value was set for the **InterfaceLuid** member (the value of this member was set to zero), the **InterfaceIndex** member is next used to determine the interface.

The route metric offset that is specified in the **Metric** member of the MIB\_IPFORWARD\_ROW2 structure that *Route* parameter points to represents only part of the complete route metric. The complete metric is a combination of this route metric offset added to the interface metric that is specified in the **Metric** member of the [**MIB\_IPINTERFACE\_ROW**](mib-ipinterface-row.md) structure of the associated interface. A driver can retrieve the interface metric by calling the [**GetIpInterfaceEntry**](getipinterfaceentry.md) function.

**SetIpForwardEntry2** ignores the **Age** and **Origin** members of the MIB\_IPFORWARD\_ROW2 structure that the *Row* parameter points to. These members are set by the network stack and cannot be changed by using the **SetIpForwardEntry2** function.

The **SetIpForwardEntry2** function fails if the **DestinationPrefix** and **NextHop** members of the MIB\_IPFORWARD\_ROW2 structure that the *Route* parameter points to do not match an an IP route entry on the specified interface.

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
