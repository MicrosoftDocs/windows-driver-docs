---
title: NotifyTeredoPortChange function (Windows Drivers)
description: Learn more about the NotifyTeredoPortChange function.
keywords:
- NotifyTeredoPortChange
- netioapi/NotifyTeredoPortChange
- NETIOAPI_API
ms.date: 10/25/2022
ms.topic: reference
---

# NotifyTeredoPortChange function

The **NotifyTeredoPortChange** function registers the driver to be notified for changes to the UDP port number that the Teredo client uses for the Teredo service port on a local computer.

## Syntax

``` c++
NETIOAPI_API NotifyTeredoPortChange(
  _In_    PTEREDO_PORT_CHANGE_CALLBACK Callback,
  _In_    PVOID                        CallerContext,
  _In_    BOOLEAN                      InitialNotification,
  _Inout_ HANDLE *                     NotificationHandle
);
```

## Parameters

- *Callback* \[in\]  
   A pointer to the function to call when a Teredo client port change occurs. This function is called when a Teredo port change notification is received.

- *CallerContext* \[in\]  
   A user context that is passed to the callback function that is specified in the Callback parameter when a Teredo port change notification is received.

- *InitialNotification* \[in\]  
   A value that indicates whether the callback should be called immediately after registration for driver change notification completes. This initial notification does not indicate that a change occurred to the Teredo client port. This parameter provides confirmation that the callback is registered.

- *NotificationHandle* \[in, out\]  
   A pointer that is used to return a handle that your driver can later use to deregister the driver change notification. On success, a notification handle is returned in this parameter. If an error occurs, **NULL** is returned.

## Return value

**NotifyTeredoPortChange** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **NotifyTeredoPortChange** returns one of the following error codes:

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
<td><p>An invalid parameter was passed to the function. This error is returned if the <em>Callback</em> parameter is a <strong>NULL</strong> pointer.</p></td>
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
<td><p>The <em>CallerContext</em> parameter that is passed to the <strong>NotifyTeredoPortChange</strong> function when it is registering the driver for change notifications.</p></td>
</tr>
<tr class="even">
<td><p>IN USHORT <em>Port</em></p></td>
<td><p>The UDP port number that the Teredo client currently uses. This parameter is zero when the <a href="mib-notification-type.md"><strong>MIB_NOTIFICATION_TYPE</strong></a> value that is passed in the <em>NotificationType</em> parameter to the callback function is set to <strong>MibInitialNotification</strong>. This situation can occur only if the <em>InitialNotification</em> parameter that is passed to <strong>NotifyTeredoPortChange</strong> was set to <strong>TRUE</strong> when registering the driver for change notifications.</p></td>
</tr>
<tr class="odd">
<td><p>IN MIB_NOTIFICATION_TYPE <em>NotificationType</em></p></td>
<td><p>The notification type. This member can be one of the values from the <a href="mib-notification-type.md"><strong>MIB_NOTIFICATION_TYPE</strong></a> enumeration type.</p></td>
</tr>
</tbody>
</table>

Your driver can use the [**GetTeredoPort**](getteredoport.md) function to retrieve the initial UDP port number that the Teredo client used for the Teredo service port.

The Teredo port is dynamic and can change any time that the Teredo client is restarted on the local computer. A driver can register to be notified when the Teredo service port changes by calling the **NotifyTeredoPortChange** function.

The Teredo client also uses static UDP port 3544 for listening to multicast traffic that is sent on multicast IPv4 address 224.0.0.253 as defined in RFC 4380. For more information, see [Teredo: Tunneling IPv6 over UDPthrough Network Address Translations (NATs)](https://go.microsoft.com/fwlink/p/?linkid=84066).

The **NotifyTeredoPortChange** function is used primarily by firewall drivers to configure the appropriate exceptions to enable incoming and outgoing Teredo traffic.

To deregister the driver for change notifications, call the [**CancelMibChangeNotify2**](cancelmibchangenotify2.md) function, passing the *NotificationHandle* parameter that the **NotifyTeredoPortChange** function returns.

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

[**GetTeredoPort**](getteredoport.md)

[**NotifyStableUnicastIpAddressTable**](notifystableunicastipaddresstable.md)
