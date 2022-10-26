---
title: NotifyIpInterfaceChange function (Windows Drivers)
description: Learn more about the NotifyIpInterfaceChange function.
keywords:
- NotifyIpInterfaceChange
- netioapi/NotifyIpInterfaceChange
ms.date: 10/25/2022
---

# NotifyIpInterfaceChange function

The **NotifyIpInterfaceChange** function registers the driver to be notified for changes to all IP interfaces, IPv4 interfaces, or IPv6 interfaces on a local computer.

## Syntax

``` c++
NETIOAPI_API NotifyIpInterfaceChange(
  _In_    ADDRESS_FAMILY               Family,
  _In_    PIPINTERFACE_CHANGE_CALLBACK Callback,
  _In_    PVOID                        CallerContext,
  _In_    BOOLEAN                      InitialNotification,
  _Inout_ HANDLE                       *NotificationHandle
);
```

## Parameters

- *Family* \[in\]  
   The address family to register the driver for change notifications on.

   Possible values for the address family are listed in the Winsock2.h header file. Note that the values for the AF\_ address family and PF\_ protocol family constants are identical (for example, AF\_INET and PF\_INET), so you can use either constant.

   On Windows Vista and later versions of the Windows operating systems, possible values for the *Family* parameter are defined in the Ws2def.h header file. Note that the Ws2def.h header file is automatically included in Netioapi.h and you should never use Ws2def.h directly.

   The following values are currently supported for the address family:

    - AF\_INET  
       The IPv4 address family. When this value is specified, this function registers the driver to be notified only for IPv4 change notifications.

    - AF\_INET6  
       The IPv6 address family. When this value is specified, this function registers the driver for only IPv6 change notifications.

    - AF\_UNSPEC  
       The address family is unspecified. When this value is specified, this function registers the driver to be notified for both IPv4 and IPv6 changes.

- *Callback* \[in\]  
   A pointer to the function to call when a change occurs. This function is called when an interface notification is received.

- *CallerContext* \[in\]  
   A user context that is passed to the callback function that is specified in the *Callback* parameter when an interface notification is received.

- *InitialNotification* \[in\]  
   A value that indicates whether the callback should be invoked immediately after registration for change notification completes. This initial notification does not indicate a change occurred to an IP interface. The purpose of this parameter to provide confirmation that the callback is registered.

- *NotificationHandle* \[in, out\]  
   A pointer used to return a handle that can be later used to deregister the change notification. On success, a notification handle is returned in this parameter. If an error occurs, **NULL** is returned.

## Return value

**NotifyIpInterfaceChange** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **NotifyIpInterfaceChange** returns one of the following error codes:

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
<td><p>The <em>CallerContext</em> parameter that is passed to the <strong>NotifyIpInterfaceChange</strong> function when it is registering the driver for change notifications.</p></td>
</tr>
<tr class="even">
<td><p>IN PMIB_IPINTERFACE_ROW <em>Row</em> OPTIONAL</p></td>
<td><p>A pointer to the <a href="mib-ipinterface-row.md"><strong>MIB_IPINTERFACE_ROW</strong></a> entry for the interface that was changed. This parameter is a <strong>NULL</strong> pointer when the <a href="mib-notification-type.md"><strong>MIB_NOTIFICATION_TYPE</strong></a> value that is passed in the <em>NotificationType</em> parameter to the callback function is set to <strong>MibInitialNotification</strong>. This situation can occur only if the <em>InitialNotification</em> parameter that is passed to <strong>NotifyIpInterfaceChange</strong> was set to <strong>TRUE</strong> when registering the driver for change notifications.</p></td>
</tr>
<tr class="odd">
<td><p>IN MIB_NOTIFICATION_TYPE <em>NotificationType</em></p></td>
<td><p>The notification type. This member can be one of the values from the <a href="mib-notification-type.md"><strong>MIB_NOTIFICATION_TYPE</strong></a> enumeration type.</p></td>
</tr>
</tbody>
</table>

To deregister the driver for change notifications, call the [**CancelMibChangeNotify2**](cancelmibchangenotify2.md) function, passing the *NotificationHandle* parameter that **NotifyIpInterfaceChange** returns.

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

[**GetIfEntry2**](getifentry2.md)

[**GetIfStackTable**](getifstacktable.md)

[**GetIfTable2**](getiftable2.md)

[**GetInvertedIfStackTable**](getinvertedifstacktable.md)

[**GetIpInterfaceEntry**](getipinterfaceentry.md)

[**InitializeIpInterfaceEntry**](initializeipinterfaceentry.md)

[**MIB\_IF\_ROW2**](mib-if-row2.md)

[**MIB\_IF\_TABLE2**](mib-if-table2.md)

[**MIB\_IPINTERFACE\_ROW**](mib-ipinterface-row.md)

[**MIB\_NOTIFICATION\_TYPE**](mib-notification-type.md)

[**SetIpInterfaceEntry**](setipinterfaceentry.md)
