---
title: GetIpPathEntry function (Windows Drivers)
description: Learn more about the GetIpPathEntry function.
keywords:
- GetIpPathEntry
- netioapi/GetIpPathEntry
ms.date: 10/25/2022
ms.topic: reference
---

# GetIpPathEntry function

The **GetIpPathEntry** function retrieves information for an IP path entry on a local computer.

## Syntax

``` c++
NETIOAPI_API GetIpPathEntry(
  _Inout_ PMIB_IPPATH_ROW Row
);
```

## Parameters

- *Row* \[in, out\]  
   A pointer to a [**MIB\_IPPATH\_ROW**](mib-ippath-row.md) structure entry for an IP path entry. On successful return, this structure is updated with the properties for IP path entry.

## Return value

**GetIpPathEntry** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **GetIpPathEntry** returns one of the following error codes:

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
<td><p>An invalid parameter was passed to the function. This error is returned if a <strong>NULL</strong> pointer is passed in the <em>Row</em> parameter, the <strong>si_family</strong> member in the <strong>Destination</strong> member of the <a href="mib-ippath-row.md"><strong>MIB_IPPATH_ROW</strong></a> structure that the <em>Row</em> parameter points to was not set to AF_INET or AF_INET6, or both <strong>InterfaceLuid</strong> and <strong>InterfaceIndex</strong> members of the MIB_IPPATH_ROW structure were unspecified. This error is also returned if the <strong>si_family</strong> member in the <strong>Source</strong> member of the MIB_IPPATH_ROW structure did not match the destination IP address family and the <strong>si_family</strong> for the source IP address was not specified as AF_UNSPEC.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_NOT_FOUND</strong></td>
<td><p>The specified interface could not be found. This error is returned if the function cannot find the network interface that is specified by the <strong>InterfaceLuid</strong> or <strong>InterfaceIndex</strong> member of the MIB_IPPATH_ROW structure that the <em>Row</em> parameter points to.</p></td>
</tr>
<tr class="odd">
<td><strong>STATUS_NOT_SUPPORTED</strong></td>
<td><p>The request is not supported. This error is returned if no IPv4 stack is located on the local computer and an IPv4 address was specified in the <strong>Source</strong> and <strong>Destination</strong> members of the MIB_IPPATH_ROW structure that the <em>Row</em> parameter points to, or if no IPv6 stack is located on the local computer and an IPv6 address was specified in the <strong>Source</strong> and <strong>Destination</strong> members.</p></td>
</tr>
<tr class="even">
<td><strong>Other</strong></td>
<td><p>Use the <a href="/windows/win32/api/winbase/nf-winbase-formatmessage">FormatMessage</a> function to obtain the message string for the returned error.</p></td>
</tr>
</tbody>
</table>

## Remarks

The **GetIpPathEntry** function is used to retrieve a [**MIB\_IPPATH\_ROW**](mib-ippath-row.md) structure entry.

On input, your driver must initialize the following members of the MIB\_IPPATH\_ROW structure that the *Row* parameter points to.

- **Destination**  
   Set to a valid IPv4 or IPv6 address and family.

- **Source**  
   Set the address family that is specified in the **Source** member to the destination IP address family that is specified in the **Destination** member, or to AF\_UNSPEC.

- **InterfaceLuid** or **InterfaceIndex**  
   These members are used in the order that is listed earlier. So if **InterfaceLuid** is specified, this member is used to determine the interface. If no value was set for the **InterfaceLuid** member (the value of this member was set to zero), the **InterfaceIndex** member is next used to determine the interface.

On output, when the call is successful, **GetIpPathEntry** retrieves the other properties for the IP path entry and fills in the MIB\_IPPATH\_ROW structure that the *Row* parameter points to.

Your driver can call the [**GetIpPathTable**](getippathtable.md) function to enumerate the IP path entries on a local computer.

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

[**FlushIpPathTable**](flushippathtable.md)

[**GetIpPathTable**](getippathtable.md)

[**MIB\_IPPATH\_ROW**](mib-ippath-row.md)

[**MIB\_IPPATH\_TABLE**](mib-ippath-table.md)
