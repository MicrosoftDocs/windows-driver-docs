---
title: NotifyStableUnicastIpAddressTable function (Windows Drivers)
description: Learn more about the NotifyStableUnicastIpAddressTable function.
keywords:
- NotifyStableUnicastIpAddressTable
- netioapi/NotifyStableUnicastIpAddressTable
ms.date: 10/25/2022
ms.topic: reference
---

# NotifyStableUnicastIpAddressTable function

The **NotifyStableUnicastIpAddressTable** function retrieves the stable unicast IP address table on a local computer.

## Syntax

``` c++
NETIOAPI_API NotifyStableUnicastIpAddressTable(
  _In_    ADDRESS_FAMILY                           Family,
  _Out_   PMIB_UNICASTIPADDRESS_TABLE              *Table,
  _In_    PSTABLE_UNICAST_IPADDRESS_TABLE_CALLBACK CallerCallback,
  _In_    PVOID                                    CallerContext,
  _Inout_ HANDLE                                   *NotificationHandle
);
```

## Parameters

- *Family* \[in\]  
   The address family to retrieve.

   Possible values for the address family are listed in the Winsock2.h header file. Note that the values for the AF\_ address family and PF\_ protocol family constants are identical (for example, AF\_INET and PF\_INET), so you can use either constant.

   On Windows Vista and later versions of the Windows operating systems, possible values for the *Family* parameter are defined in the Ws2def.h header file. Note that the Ws2def.h header file is automatically included in Netioapi.h and you should never use Ws2def.h directly.

   The following values are currently supported for the address family:

    - AF\_INET  
       The IPv4 address family. When this value is specified, the function retrieves the stable unicast IP address table that contains only IPv4 entries.

    - AF\_INET6  
       The IPv6 address family. When this value is specified, the function retrieves the stable unicast IP address table that contains only IPv6 entries.

    - AF\_UNSPEC  
       The address family is unspecified. When this value is specified, the function retrieves the stable unicast IP address table that contains both IPv4 and IPv6 entries.

- *Table* \[out\]  
   A pointer to a [**MIB\_UNICASTIPADDRESS\_TABLE**](mib-unicastipaddress-table.md) structure. When **NotifyStableUnicastIpAddressTable** is successful, this parameter returns the stable unicast IP address table on the local computer.

   When **NotifyStableUnicastIpAddressTable** returns ERROR\_IO\_PENDING, which indicates that the I/O request is pending, the stable unicast IP address table is returned to the function in the *CallerCallback* parameter.

- *CallerCallback* \[in\]  
   A pointer to the function to call with the stable unicast IP address table. This function is called if **NotifyStableUnicastIpAddressTable** returns ERROR\_IO\_PENDING, which indicates that the I/O request is pending.

- *CallerContext* \[in\]  
   A user context that is passed to the callback function that is specified in the *CallerCallback* parameter when the stable unicast IP address table is available.

- *NotificationHandle* \[in, out\]  
   A pointer that is used to return a handle that your driver can use to cancel the request to retrieve the stable unicast IP address table. This parameter is returned if the return value from **NotifyStableUnicastIpAddressTable** is ERROR\_IO\_PENDING, which indicates that the I/O request is pending.

## Return value

**NotifyStableUnicastIpAddressTable** returns STATUS\_SUCCESS and the stable unicast IP table is returned in the *Table* parameter if the function succeeds immediately.

If the I/O request is pending, the function returns ERROR\_IO\_PENDING and the function that the *CallerCallback* parameter points to is called when the I/O request has completed with the stable unicast IP address table.

If the function fails, **NotifyStableUnicastIpAddressTable** returns one of the following error codes:

<table>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>ERROR_INVALID_HANDLE</strong></td>
<td><p>An internal error occurred where an invalid handle was encountered.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_INVALID_PARAMETER</strong></td>
<td><p>An invalid parameter was passed to the function. This error is returned if the <em>Table</em> parameter was a <strong>NULL</strong> pointer, the <em>NotificationHandle</em> parameter was a <strong>NULL</strong> pointer, or the <em>Family</em> parameter was not either AF_INET, AF_INET6, or AF_UNSPEC.</p></td>
</tr>
<tr class="odd">
<td><strong>STATUS_NOT_ENOUGH_MEMORY</strong></td>
<td><p>There was insufficient memory.</p></td>
</tr>
<tr class="even">
<td><strong>Other</strong></td>
<td><p>Use the <a href="/windows/win32/api/winbase/nf-winbase-formatmessage">FormatMessage</a> function to obtain the message string for the returned error.</p></td>
</tr>
</tbody>
</table>

## Remarks

All unicast IP addresses, except dial-on-demand addresses, are considered stable only if they are in the preferred state. For a normal unicast IP address entry, this state would correspond to a **DadState** member of the [**MIB\_UNICASTIPADDRESS\_ROW**](mib-unicastipaddress-row.md) for the IP address that is set to **IpDadStatePreferred**. Every dial-on-demand address defines its own stability metric. Currently the only dial-on-demand address that the **NotifyStableUnicastIpAddressTable** function considers is the unicast IP address that the Teredo client uses on the local computer.

Your driver must set the *Family* parameter to either AF\_INET, AF\_INET6, or AF\_UNSPEC.

When **NotifyStableUnicastIpAddressTable** is successful and returns STATUS\_SUCCESS, the *Table* parameter returns the stable unicast IP address table on the local computer.

When **NotifyStableUnicastIpAddressTable** returns ERROR\_IO\_PENDING, which indicates that the I/O request is pending, the stable unicast IP address table is returned to the function in the *CallerCallback* parameter.

If the unicast IP address that Teredo uses is available on the local computer but not in the stable (qualified) state, **NotifyStableUnicastIpAddressTable** returns ERROR\_IO\_PENDING and the stable unicast IP address table is eventually returned by calling the function in the *CallerCallback* parameter. If the Teredo address is not available or is in the stable state and the other unicast IP addresses are in a stable state, the function in the *CallerCallback* parameter is never called.

The callback function that is specified in the *CallerCallback* parameter should be defined as a function of type **VOID**. The parameters that are passed to the callback function include the following.

<table>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>IN PVOID <em>CallerContext</em></p></td>
<td><p>The <em>CallerContext</em> parameter that is passed to the <strong>NotifyStableUnicastIpAddressTable</strong> function when it is registering the driver for notifications.</p></td>
</tr>
<tr class="even">
<td><p>IN PMIB_UNICASTIPADDRESS_TABLE <em>AddressTable</em></p></td>
<td><p>A pointer to a <a href="mib-unicastipaddress-table.md"><strong>MIB_UNICASTIPADDRESS_TABLE</strong></a> structure that contains the stable unicast IP address table on the local computer.</p></td>
</tr>
</tbody>
</table>

The **NotifyStableUnicastIpAddressTable** function is used primarily by drivers that use the Teredo client.

To cancel the notification after the callback is complete, call the [**CancelMibChangeNotify2**](cancelmibchangenotify2.md) function, passing the *NotificationHandle* parameter that **NotifyStableUnicastIpAddressTable** returns.

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

[**CancelMibChangeNotify2**](cancelmibchangenotify2.md)

[**CreateUnicastIpAddressEntry**](createunicastipaddressentry.md)

[**DeleteUnicastIpAddressEntry**](deleteunicastipaddressentry.md)

[**GetTeredoPort**](getteredoport.md)

[**GetUnicastIpAddressEntry**](getunicastipaddressentry.md)

[**GetUnicastIpAddressTable**](getunicastipaddresstable.md)

[**InitializeUnicastIpAddressEntry**](initializeunicastipaddressentry.md)

[**MIB\_NOTIFICATION\_TYPE**](mib-notification-type.md)

[**MIB\_UNICASTIPADDRESS\_ROW**](mib-unicastipaddress-row.md)

[**MIB\_UNICASTIPADDRESS\_TABLE**](mib-unicastipaddress-table.md)

[**NotifyTeredoPortChange**](notifyteredoportchange.md)

[**NotifyUnicastIpAddressChange**](notifyunicastipaddresschange.md)

[**SetUnicastIpAddressEntry**](setunicastipaddressentry.md)
