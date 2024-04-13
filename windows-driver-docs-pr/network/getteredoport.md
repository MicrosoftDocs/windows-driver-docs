---
title: GetTeredoPort function (Windows Drivers)
description: Learn more about the GetTeredoPort function.
keywords:
- GetTeredoPort
- netioapi/GetTeredoPort
ms.date: 10/25/2022
ms.topic: reference
---

# GetTeredoPort function

The **GetTeredoPort** function retrieves the dynamic UDP port number that the Teredo client uses on a local computer.

## Syntax

``` c++
NETIOAPI_API GetTeredoPort(
  _Out_ USHORT *Port
);
```

## Parameters

- *Port* \[out\]  
   A pointer to the UDP port number. On successful return, this parameter is filled with the port number that the Teredo client uses.

## Return value

**GetTeredoPort** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **GetTeredoPort** returns one of the following error codes:

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
<td><p>An invalid parameter was passed to the function. This error is returned if a <strong>NULL</strong> pointer is passed in the <em>Port</em> parameter.</p></td>
</tr>
<tr class="even">
<td><strong>ERROR_NOT_READY</strong></td>
<td><p>The device is not ready. This error is returned if the Teredo client is not started on the local computer.</p></td>
</tr>
<tr class="odd">
<td><strong>STATUS_NOT_SUPPORTED</strong></td>
<td><p>The request is not supported. This error is returned if no IPv6 stack is located on the local computer.</p></td>
</tr>
<tr class="even">
<td><strong>Other</strong></td>
<td><p>Use the <a href="/windows/win32/api/winbase/nf-winbase-formatmessage">FormatMessage</a> function to obtain the message string for the returned error.</p></td>
</tr>
</tbody>
</table>

## Remarks

The **GetTeredoPort** function retrieves the current UDP port number that the Teredo client usesfor the Teredo service port. The Teredo port is dynamic and can change any time that the Teredo client is restarted on the local computer. A driver can register to be notified when the Teredo service port changes by calling the [**NotifyTeredoPortChange**](notifyteredoportchange.md) function.

The Teredo client also uses static UDP port 3544 for listening to multicast traffic that is sent on multicast IPv4 address 224.0.0.253 as defined in RFC 4380. For more information, see [Teredo: Tunneling IPv6 over UDPthrough Network Address Translations (NATs)](https://go.microsoft.com/fwlink/p/?linkid=84066).

The **GetTeredoPort** function is used primarily by firewall drivers in order to configure the appropriate exceptions to enable incoming and outgoing Teredo traffic.

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

[**NotifyTeredoPortChange**](notifyteredoportchange.md)

[**NotifyStableUnicastIpAddressTable**](notifystableunicastipaddresstable.md)
