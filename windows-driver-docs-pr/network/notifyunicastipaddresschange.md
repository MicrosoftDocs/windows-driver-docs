---
title: NotifyUnicastIpAddressChange function (Windows Drivers)
description: Learn more about the NotifyUnicastIpAddressChange function.
keywords:
- NotifyUnicastIpAddressChange
- netioapi/NotifyUnicastIpAddressChange
ms.date: 10/25/2022
---

# NotifyUnicastIpAddressChange function

The **NotifyUnicastIpAddressChange** function registers the driver to be notified for changes to all unicast IP interfaces, unicast IPv4 addresses, or unicast IPv6 addresses on a local computer.

## Syntax

``` c++
NETIOAPI_API NotifyUnicastIpAddressChange(
  _In_    ADDRESS_FAMILY                     Family,
  _In_    PUNICAST_IPADDRESS_CHANGE_CALLBACK Callback,
  _In_    PVOID                              CallerContext,
  _In_    BOOLEAN                            InitialNotification,
  _Inout_ HANDLE                             *NotificationHandle
);
```

## Parameters

- *Family* \[in\]  
   The address family to register the driver for change notifications on.

   Possible values for the address family are listed in the Winsock2.h header file. Note that the values for the AF\_ address family and PF\_ protocol family constants are identical (for example, AF\_INET and PF\_INET), so you can use either constant.

   On Windows Vista and later versions of the Windows operating systems, possible values for the *Family* parameter are defined in the Ws2def.h header file. Note that the Ws2def.h header file is automatically included in Netioapi.h and you should never use Ws2def.h directly.

   The following values are currently supported for the address family:

    - AF\_INET  
       The IPv4 address family. When this value is specified, the function registers the driver only for unicast IPv4 address change notifications.

    - AF\_INET6  
       The IPv6 address family. When this value is specified, the function registers the driver only for unicast IPv6 address change notifications.

    - AF\_UNSPEC  
       The address family is unspecified. When this value is specified, the function registers the driver for both unicast IPv4 and IPv6 address change notifications.

- *Callback* \[in\]  
   A pointer to the function to call when a change occurs. This function is called when a unicast IP address notification is received.

- *CallerContext* \[in\]  
   A user context that is passed to the callback function that is specified in the *Callback* parameter when an interface notification is received.

- *InitialNotification* \[in\]  
   A value that indicates whether the callback should be called immediately after registration for change notification completes. This initial notification does not indicate that a change occurred to a unicast IP address. This parameter provides confirmation that the callback is registered.

- *NotificationHandle* \[in, out\]  
   A pointer that is used to return a handle that your driver can later use to deregister the driver change notification. On success, a notification handle is returned in this parameter. If an error occurs, **NULL** is returned.

## Return value

**NotifyUnicastIpAddressChange** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **NotifyUnicastIpAddressChange** returns one of the following error codes:

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
<td><p>An invalid parameter was passed to the function. This error is returned if the <em>Family</em> parameter was not either AF_INET, AF_INET6, or AF_UNSPEC.</p></td>
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

Your driver must set the *Family* parameter to either AF\_INET, AF\_INET6, or AF\_UNSPEC.

The invocation of the callback function that is specified in the *Callback* parameter is serialized. The callback function should be defined as a function of type **VOID**. The parameters that are passed to the callback function include the following.

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
<td><p>The <em>CallerContext</em> parameter that is passed to the <strong>NotifyUnicastIpAddressChange</strong> function when it is registering the driver for change notifications.</p></td>
</tr>
<tr class="even">
<td><p>IN PMIB_UNICASTIPADDRESS_ROW <em>Row</em> OPTIONAL</p></td>
<td><p>A pointer to the <a href="mib-unicastipaddress-row.md"><strong>MIB_UNICASTIPADDRESS_ROW</strong></a> entry for the unicast IP address that was changed. This parameter is a <strong>NULL</strong> pointer when the <a href="mib-notification-type.md"><strong>MIB_NOTIFICATION_TYPE</strong></a> value that is passed in the <em>NotificationType</em> parameter to the callback function is set to <strong>MibInitialNotification</strong>. This situation can occur only if the <em>InitialNotification</em> parameter that is passed to <strong>NotifyUnicastIpAddressChange</strong> was set to <strong>TRUE</strong> when registering the driver for change notifications.</p></td>
</tr>
<tr class="odd">
<td><p>IN MIB_NOTIFICATION_TYPE <em>NotificationType</em></p></td>
<td><p>The notification type. This member can be one of the values from the <a href="mib-notification-type.md"><strong>MIB_NOTIFICATION_TYPE</strong></a> enumeration type.</p></td>
</tr>
</tbody>
</table>

To deregister the driver for change notifications, call the [**CancelMibChangeNotify2**](cancelmibchangenotify2.md) function, passing the *NotificationHandle* parameter that **NotifyUnicastIpAddressChange** returns.

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

[**GetUnicastIpAddressEntry**](getunicastipaddressentry.md)

[**GetUnicastIpAddressTable**](getunicastipaddresstable.md)

[**InitializeUnicastIpAddressEntry**](initializeunicastipaddressentry.md)

[**MIB\_NOTIFICATION\_TYPE**](mib-notification-type.md)

[**MIB\_UNICASTIPADDRESS\_ROW**](mib-unicastipaddress-row.md)

[**MIB\_UNICASTIPADDRESS\_TABLE**](mib-unicastipaddress-table.md)

[**NotifyStableUnicastIpAddressTable**](notifystableunicastipaddresstable.md)

[**SetUnicastIpAddressEntry**](setunicastipaddressentry.md)
