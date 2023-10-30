---
title: DeleteUnicastIpAddressEntry function (Windows Drivers)
description: Learn more about the DeleteUnicastIpAddressEntry function.
keywords:
- DeleteUnicastIpAddressEntry
- netioapi/DeleteUnicastIpAddressEntry
ms.date: 10/25/2022
ms.topic: reference
---

# DeleteUnicastIpAddressEntry function

The **DeleteUnicastIpAddressEntry** function deletes an existing unicast IP address entry on a local computer.

## Syntax

``` c++
NETIOAPI_API DeleteUnicastIpAddressEntry(
  _In_ const MIB_UNICASTIPADDRESS_ROW *Row
);
```

## Parameters

- *Row* \[in\]  
   A pointer to a [**MIB\_UNICASTIPADDRESS\_ROW**](mib-unicastipaddress-row.md) structure entry for an existing unicast IP address entry to delete from the local computer.

## Return value

**DeleteUnicastIpAddressEntry** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **DeleteUnicastIpAddressEntry** returns one of the following error codes:

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
<td><p>An invalid parameter was passed to the function. This error is returned if a <strong>NULL</strong> pointer is passed in the <em>Row</em> parameter, the <strong>Address</strong> member of the <a href="mib-unicastipaddress-row.md"><strong>MIB_UNICASTIPADDRESS_ROW</strong></a> structure that the <em>Row</em> parameter points to was not set to a valid unicast IPv4 or IPv6 address, or both <strong>InterfaceLuid</strong> and <strong>InterfaceIndex</strong> members of the MIB_UNICASTIPADDRESS_ROW structure were unspecified.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_NOT_FOUND</strong></td>
<td><p>The specified interface could not be found. This error is returned if the function cannot find the network interface that is specified by the <strong>InterfaceLuid</strong> or <strong>InterfaceIndex</strong> member of the MIB_UNICASTIPADDRESS_ROW structure that the <em>Row</em> parameter points to.</p></td>
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

The **DeleteUnicastIpAddressEntry** function is used to delete an existing [**MIB\_UNICASTIPADDRESS\_ROW**](mib-unicastipaddress-row.md) structure entry on the local computer.

On input, your driver must initialize the following members of the MIB\_UNICASTIPADDRESS\_ROW structure that the *Row* parameter points to.

- **Address**  
   Set to a valid IPv4 or IPv6 unicast address and family.

- **InterfaceLuid** or **InterfaceIndex**  
   These members are used in the order that is listed earlier. So if **InterfaceLuid** is specified, this member is used to determine the interface. If no value was set for the **InterfaceLuid** member (the value of this member was set to zero), the **InterfaceIndex** member is next used to determine the interface.

If the function is successful, the existing IP address that the *Row* parameter represents is deleted.

Your driver can call the [**GetUnicastIpAddressTable**](getunicastipaddresstable.md) function to enumerate the unicast IP address entries on a local computer. Your driver can call the [**GetUnicastIpAddressEntry**](getunicastipaddressentry.md) function to retrieve a specific existing unicast IP address entry.

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

[**CreateUnicastIpAddressEntry**](createunicastipaddressentry.md)

[**GetUnicastIpAddressEntry**](getunicastipaddressentry.md)

[**GetUnicastIpAddressTable**](getunicastipaddresstable.md)

[**InitializeUnicastIpAddressEntry**](initializeunicastipaddressentry.md)

[**MIB\_UNICASTIPADDRESS\_ROW**](mib-unicastipaddress-row.md)

[**MIB\_UNICASTIPADDRESS\_TABLE**](mib-unicastipaddress-table.md)

[**NotifyUnicastIpAddressChange**](notifyunicastipaddresschange.md)

[**SetUnicastIpAddressEntry**](setunicastipaddressentry.md)
