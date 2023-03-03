---
title: GetIpInterfaceEntry function (Windows Drivers)
description: Learn more about the GetIpInterfaceEntry function.
keywords:
- GetIpInterfaceEntry
- netioapi/GetIpInterfaceEntry
ms.date: 10/25/2022
ms.topic: reference
---

# GetIpInterfaceEntry function

The **GetIpInterfaceEntry** function retrieves IP information for the specified interface on a local computer.

## Syntax

``` c++
NETIOAPI_API GetIpInterfaceEntry(
  _Inout_ PMIB_IPINTERFACE_ROW Row
);
```

## Parameters

- *Row* \[in, out\]  
   A pointer to a [**MIB\_IPINTERFACE\_ROW**](mib-ipinterface-row.md) structure that, on successful return, receives information for an interface on the local computer. On input, your driver must set the **InterfaceLuid** member or the **InterfaceIndex** member of the MIB\_IPINTERFACE\_ROW to the interface to retrieve information for.

## Return value

**GetIpInterfaceEntry** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **GetIpInterfaceEntry** returns one of the following error codes:

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
<td><p>An invalid parameter was passed to the function. This error is returned if a <strong>NULL</strong> pointer is passed in the <em>Row</em> parameter, the <strong>Family</strong> member of the MIB_IPINTERFACE_ROW structure that the <em>Row</em> parameter points to was not specified as AF_INET or AF_INET6, or the <strong>InterfaceLuid</strong> and <strong>InterfaceIndex</strong> members of the MIB_IPINTERFACE_ROW structure were unspecified.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_NOT_FOUND</strong></td>
<td><p>The specified interface could not be found. This error is returned if the function cannot find the network interface that is specified by the <strong>InterfaceLuid</strong> or <strong>InterfaceIndex</strong> member of the MIB_IPINTERFACE_ROW structure that the <em>Row</em> parameter points to.</p></td>
</tr>
<tr class="odd">
<td><strong>Other</strong></td>
<td><p>Use the <a href="/windows/win32/api/winbase/nf-winbase-formatmessage">FormatMessage</a> function to obtain the message string for the returned error.</p></td>
</tr>
</tbody>
</table>

## Remarks

On input, your driver must initialize the following members of the [**MIB\_IPINTERFACE\_ROW**](mib-ipinterface-row.md) structure that the *Row* parameter points to.

- **Family**  
   Set to either AF\_INET or AF\_INET6.

- **InterfaceLuid** or **InterfaceIndex**  
   These members are used in the order that is listed earlier. So if **InterfaceLuid** is specified, this member is used to determine the interface. If no value was set for the **InterfaceLuid** member (the value of this member was set to zero), the **InterfaceIndex** member is next used to determine the interface.

On output, **GetIpInterfaceEntry** fills in the remaining members of the MIB\_IPINTERFACE\_ROW structure that the *Row* parameter points to.

Your driver must use the [**InitializeIpInterfaceEntry**](initializeipinterfaceentry.md) function to initialize the fields of a MIB\_IPINTERFACE\_ROW structure entry with default values. A driver can then change the fields in the MIB\_IPINTERFACE\_ROW entry that it wants to modify, and then call the [**SetIpInterfaceEntry**](setipinterfaceentry.md) function.

Unprivileged simultaneous access to multiple networks of different security requirements creates a security hole and enables an unprivileged driver to accidentally relay data between the two networks. A typical example is simultaneous access to a virtual private network (VPN) and the Internet. The Windows Server 2003 and Windows XP operating systems use a weak host model, where Remote Access Service (RAS) prevents such simultaneous access by increasing the route metric of all default routes over other interfaces. Therefore, all traffic is routed through the VPN interface, disrupting other network connectivity.

On Windows Vista and later versions of the Windows operating systems, by default, a strong host model is used. If a source IP address is specified in the route lookup by using the [**GetBestRoute2**](getbestroute2.md) function, the route lookup is restricted to the interface of the source IP address. The route metric modification by RAS has no effect because the list of potential routes does not even have the route for the VPN interface, which enables traffic to the Internet. Your driver can use the **DisableDefaultRoutes** member of the MIB\_IPINTERFACE\_ROW to disable using the default route on an interface. VPN clients can use this member as a security measure to restrict split tunneling when split tunneling is not required by the VPN client. A VPN client can call the [**SetIpInterfaceEntry**](setipinterfaceentry.md) function to set the **DisableDefaultRoutes** member to **TRUE** when it is required. A VPN client can query the current state of the **DisableDefaultRoutes** member by calling the **GetIpInterfaceEntry** function.

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

[**GetBestRoute2**](getbestroute2.md)

[**GetIfEntry2**](getifentry2.md)

[**GetIfTable2**](getiftable2.md)

[**GetIfTable2Ex**](getiftable2ex.md)

[**GetIpInterfaceTable**](getipinterfacetable.md)

[**MIB\_IF\_ROW2**](mib-if-row2.md)

[**MIB\_IF\_TABLE2**](mib-if-table2.md)

[**MIB\_IPINTERFACE\_ROW**](mib-ipinterface-row.md)

[**MIB\_IPINTERFACE\_TABLE**](mib-ipinterface-table.md)

[**SetIpInterfaceEntry**](setipinterfaceentry.md)
