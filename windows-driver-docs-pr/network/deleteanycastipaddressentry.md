---
title: DeleteAnycastIpAddressEntry function (Windows Drivers)
description: Learn more about the DeleteAnycastIpAddressEntry function.
keywords:
- DeleteAnycastIpAddressEntry
- netioapi/DeleteAnycastIpAddressEntry
ms.date: 10/25/2022
ms.topic: reference
---

# DeleteAnycastIpAddressEntry function

The **DeleteAnycastIpAddressEntry** function deletes an existing anycast IP address entry on a local computer.

## Syntax

``` c++
NETIOAPI_API DeleteAnycastIpAddressEntry(
  _In_ const MIB_ANYCASTIPADDRESS_ROW *Row
);
```

## Parameters

- *Row* \[in\]  
   A pointer to a [**MIB\_ANYCASTIPADDRESS\_ROW**](mib-anycastipaddress-row.md) structure entry for an existing anycast IP address entry to delete from the local computer.

## Return value

**DeleteAnycastIpAddressEntry** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **DeleteAnycastIpAddressEntry** returns one of the following error codes:

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
<td><p>An invalid parameter was passed to the function. This error is returned if a <strong>NULL</strong> pointer is passed in the <em>Row</em> parameter, the <strong>Address</strong> member of the <a href="mib-anycastipaddress-row.md"><strong>MIB_ANYCASTIPADDRESS_ROW</strong></a> structure that the <em>Row</em> parameter points to was not set to a valid unicast IPv4 or IPv6 address, or both <strong>InterfaceLuid</strong> and <strong>InterfaceIndex</strong> members of the MIB_ANYCASTIPADDRESS_ROW structure were unspecified.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_NOT_FOUND</strong></td>
<td><p>The specified interface could not be found. This error is returned if the function cannot find the network interface that is specified by the <strong>InterfaceLuid</strong> or <strong>InterfaceIndex</strong> member of the MIB_ANYCASTIPADDRESS_ROW structure that the <em>Row</em> parameter points to.</p></td>
</tr>
<tr class="odd">
<td><strong>STATUS_NOT_SUPPORTED</strong></td>
<td><p>The request is not supported. This error is returned if no IPv4 stack is located on the local computer and an IPv4 address was specified in the <strong>Address</strong> member of the MIB_ANYCASTIPADDRESS_ROW structure that the <em>Row</em> parameter points to, or if no IPv6 stack is located on the local computer and an IPv6 address was specified in the <strong>Address</strong> member.</p></td>
</tr>
<tr class="even">
<td><strong>Other</strong></td>
<td><p>Use the <a href="/windows/win32/api/winbase/nf-winbase-formatmessage">FormatMessage</a> function to obtain the message string for the returned error.</p></td>
</tr>
</tbody>
</table>

## Remarks

The **DeleteAnycastIpAddressEntry** function is used to delete an existing [**MIB\_ANYCASTIPADDRESS\_ROW**](mib-anycastipaddress-row.md) structure entry on the local computer.

On input, your driver must initialize the following members of the MIB\_ANYCASTIPADDRESS\_ROW structure that the *Row* parameter points to.

- **Address**  
   Set to a valid unicast IPv4 or IPv6 address and family.

- **InterfaceLuid** or **InterfaceIndex**  
   These members are used in the order that is listed earlier. So if **InterfaceLuid** is specified, this member is used to determine the interface. If no value was set for the **InterfaceLuid** member (the value of this member was set to zero), the **InterfaceIndex** member is next used to determine the interface.

If the function is successful, the existing IP address that the *Row* parameter represents was deleted.

Your driver can call the [**GetAnycastIpAddressTable**](getanycastipaddresstable.md) function to enumerate the anycast IP address entries on a local computer. Your driver can call the [**GetAnycastIpAddressEntry**](getanycastipaddressentry.md) function to retrieve a specific existing anycast IP address entry.

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

[**GetAnycastIpAddressEntry**](getanycastipaddressentry.md)

[**GetAnycastIpAddressTable**](getanycastipaddresstable.md)

[**MIB\_ANYCASTIPADDRESS\_ROW**](mib-anycastipaddress-row.md)

[**MIB\_ANYCASTIPADDRESS\_TABLE**](mib-anycastipaddress-table.md)
