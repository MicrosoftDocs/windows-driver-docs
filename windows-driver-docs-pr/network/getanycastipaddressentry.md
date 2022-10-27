---
title: GetAnycastIpAddressEntry function (Windows Drivers)
description: Learn more about the GetAnycastIpAddressEntry function.
keywords:
- GetAnycastIpAddressEntry
- netioapi/GetAnycastIpAddressEntry
ms.date: 10/25/2022
---

# GetAnycastIpAddressEntry function

The **GetAnycastIpAddressEntry** function retrieves information for an existing anycast IP address entry on a local computer.

## Syntax

``` c++
NETIOAPI_API GetAnycastIpAddressEntry(
  _Inout_ PMIB_ANYCASTIPADDRESS_ROW Row
);
```

## Parameters

- *Row* \[in, out\]  
   A pointer to a [**MIB\_ANYCASTIPADDRESS\_ROW**](mib-anycastipaddress-row.md) structure entry for an anycast IP address entry. On successful return, this structure is updated with the properties for an existing anycast IP address.

## Return value

**GetAnycastIpAddressEntry** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **GetAnycastIpAddressEntry** returns one of the following error codes:

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
<td><p>An invalid parameter was passed to the function. This error is returned if a <strong>NULL</strong> pointer is passed in the <em>Row</em> parameter, the <strong>Address</strong> member of the <a href="mib-anycastipaddress-row.md"><strong>MIB_ANYCASTIPADDRESS_ROW</strong></a> structure that the <em>Row</em> parameter points to was not set to a valid anycast IPv4 or IPv6 address, or both <strong>InterfaceLuid</strong> and <strong>InterfaceIndex</strong> members of the MIB_ANYCASTIPADDRESS_ROW structure were unspecified.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_NOT_FOUND</strong></td>
<td><p>The specified interface could not be found. This error is returned if the function cannot find the network interface that specified by the <strong>InterfaceLuid</strong> or <strong>InterfaceIndex</strong> member of the MIB_ANYCASTIPADDRESS_ROW structure that the <em>Row</em> parameter points to.</p></td>
</tr>
<tr class="odd">
<td><strong>STATUS_NOT_SUPPORTED</strong></td>
<td><p>The request is not supported. This error is returned if no IPv4 stack is located on the local computer and an IPv4 address was specified in the <strong>Address</strong> member of the MIB_UNICASTIPADDRESS_ROW structure that the <em>Row</em> parameter points to, or if no IPv6 stack is located on the local computer and an IPv6 address was specified in the <strong>Address</strong> member.</p></td>
</tr>
<tr class="even">
<td><strong>Other</strong></td>
<td><p>Use the <a href="/windows/win32/api/winbase/nf-winbase-formatmessage">FormatMessage</a> function to obtain the message string for the returned error.</p></td>
</tr>
</tbody>
</table>

## Remarks

The **GetAnycastIpAddressEntry** function is used to retrieve an existing [**MIB\_ANYCASTIPADDRESS\_ROW**](mib-anycastipaddress-row.md) structure entry.

On input, your driver must initialize the following members of the MIB\_ANYCASTIPADDRESS\_ROW structure that the *Row* parameter points to.

- **Address**  
   Set to a valid IPv4 or IPv6 anycast address and family.

- **InterfaceLuid** or **InterfaceIndex**  
   These members are used in the order that is listed earlier. So if **InterfaceLuid** is specified, this member is used to determine the interface. If no value was set for the **InterfaceLuid** member (the value of this member was set to zero), the **InterfaceIndex** member is next used to determine the interface.

On output, when the call is successful, **GetAnycastIpAddressEntry** retrieves the other properties for the anycast IP address and fills out the MIB\_ANYCASTIPADDRESS\_ROW structure that the *Row* parameter points to.

Your driver can call the [**GetAnycastIpAddressTable**](getanycastipaddresstable.md) function to enumerate the anycast IP address entries on a local computer.

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

[**CreateAnycastIpAddressEntry**](createanycastipaddressentry.md)

[**DeleteAnycastIpAddressEntry**](deleteanycastipaddressentry.md)

[**GetAnycastIpAddressTable**](getanycastipaddresstable.md)

[**MIB\_ANYCASTIPADDRESS\_ROW**](mib-anycastipaddress-row.md)

[**MIB\_ANYCASTIPADDRESS\_TABLE**](mib-anycastipaddress-table.md)
