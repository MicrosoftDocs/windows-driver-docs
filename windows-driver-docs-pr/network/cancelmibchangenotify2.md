---
title: CancelMibChangeNotify2 function (Windows Drivers)
description: Learn more about the CancelMibChangeNotify2 function.
keywords:
- CancelMibChangeNotify2
- netioapi/CancelMibChangeNotify2
ms.date: 10/25/2022
---

# CancelMibChangeNotify2 function

The **CancelMibChangeNotify2** function deregisters a driver change notification for IP interface changes, IP address changes, IP route changes, and requests to retrieve the stable Unicast IP address table.

## Syntax

``` c++
NETIOAPI_API CancelMibChangeNotify2(
  _In_ HANDLE NotificationHandle
);
```

## Parameters

- *NotificationHandle* \[in\]  
   The handle that is returned from a notification registration or retrieval function to indicate which notification to cancel.

## Return value

**CancelMibChangeNotify2** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **CancelMibChangeNotify2** returns one of the following error codes:

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
<td><p>An invalid parameter was passed to the function. <strong>CancelMibChangeNotify2</strong> returns this error if the <em>NotificationHandle</em> parameter was a <strong>NULL</strong> pointer.</p></td>
</tr>
<tr class="even">
<td><strong>Other</strong></td>
<td><p>Use the <a href="/windows/win32/api/winbase/nf-winbase-formatmessage">FormatMessage</a> function to obtain the message string for the returned error.</p></td>
</tr>
</tbody>
</table>

## Remarks

The **CancelMibChangeNotify2** function deregisters a driver change notification previously requested for IP interface changes, IP address changes, or IP route changes on a local computer. These requests are made by calling [**NotifyIpInterfaceChange**](notifyipinterfacechange.md), [**NotifyRouteChange2**](notifyroutechange2.md), or [**NotifyUnicastIpAddressChange**](notifyunicastipaddresschange.md). The **CancelMibChangeNotify2** function also cancels a previous request to retrieve the stable unicast IP address table on a local computer. This request is made by calling the [**NotifyStableUnicastIpAddressTable**](notifystableunicastipaddresstable.md) function.

The *NotificationHandle* parameter that is returned to these notification functions is passed to **CancelMibChangeNotify2** to deregister driver change notifications or to cancel a pending request to retrieve the stable unicast IP address table.

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
<td><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also

[**NotifyIpInterfaceChange**](notifyipinterfacechange.md)

[**NotifyRouteChange2**](notifyroutechange2.md)

[**NotifyStableUnicastIpAddressTable**](notifystableunicastipaddresstable.md)

[**NotifyUnicastIpAddressChange**](notifyunicastipaddresschange.md)
