---
title: GetBestRoute2 function (Windows Drivers)
description: Learn more about the GetBestRoute2 function.
keywords:
- GetBestRoute2
- netioapi/GetBestRoute2
ms.date: 10/25/2022
---

# GetBestRoute2 function

The **GetBestRoute2** function retrieves the IP route entry on a local computer for the best route to the specified destination IP address.

## Syntax

``` c++
NETIOAPI_API GetBestRoute2(
  _In_opt_       NET_LUID            *InterfaceLuid,
  _In_           NET_IFINDEX         InterfaceIndex,
  _In_opt_ const SOCKADDR_INET       *SourceAddress,
  _In_     const SOCKADDR_INET       *DestinationAddress,
  _In_           ULONG               AddressSortOptions,
  _Out_          PMIB_IPFORWARD_ROW2 BestRoute,
  _Out_          SOCKADDR_INET       *BestSourceAddress
);
```

## Parameters

- *InterfaceLuid* \[in, optional\]  
   The locally unique identifier (LUID) to specify the network interface that is associated with an IP route entry.

- *InterfaceIndex* \[in\]  
   The local index value to specify the network interface that is associated with an IP route entry. This index value might change when a network adapter is disabled and then enabled, or under other circumstances, so this value does not persistent.

- *SourceAddress* \[in, optional\]  
   The source IP address. Your driver can omit this parameter and pass a **NULL** pointer.

- *DestinationAddress* \[in\]  
   The destination IP address.

- *AddressSortOptions* \[in\]  
   A set of options that affect how IP addresses are sorted. This parameter is currently not used.

- *BestRoute* \[out\]  
   A pointer to the [**MIB\_IPFORWARD\_ROW2**](mib-ipforward-row2.md) structure for the best route from the source IP address to the destination IP address.

- *BestSourceAddress* \[out\]  
   A pointer to the best source IP address.

## Return value

**GetBestRoute2** returns STATUS\_SUCCESS if the function succeeds.

If the function fails, **GetBestRoute2** returns one of the following error codes:

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
<td><p>An invalid parameter was passed to the function. This error is returned if a <strong>NULL</strong> pointer is passed in the <em>DestinationAddress</em>, <em>BestSourceAddress</em>, or <em>BestRoute</em> parameters. This error is also returned if both <em>InterfaceLuid</em> and <em>InterfaceIndex</em> parameters were unspecified. This error is also returned if the <em>DestinationAddress</em> parameter does not specify an IPv4 or IPv6 address and family</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_NOT_FOUND</strong></td>
<td><p>The specified interface could not be found. This error is returned if the network interface that the <em>InterfaceLuid</em> or <em>InterfaceIndex</em> parameter specifies could not be found.</p></td>
</tr>
<tr class="odd">
<td><strong>STATUS_NOT_SUPPORTED</strong></td>
<td><p>The request is not supported. This error is returned if no IPv4 stack is located on the local computer and an IPv4 address and family was specified in the <em>DestinationAddress</em> parameter, or if no IPv6 stack is located on the local computer and an IPv4 address and family was specified in the <em>DestinationAddress</em> parameter.</p></td>
</tr>
<tr class="even">
<td><strong>Other</strong></td>
<td><p>Use the <a href="/windows/win32/api/winbase/nf-winbase-formatmessage">FormatMessage</a> function to obtain the message string for the returned error.</p></td>
</tr>
</tbody>
</table>

## Remarks

The **GetBestRoute2** function is used to retrieve a [**MIB\_IPFORWARD\_ROW2**](mib-ipforward-row2.md) structure entry for the best route from a source IP address to a destination IP address.

On input, your driver must initialize the following parameters.

- *DestinationAddress*  
   Set to a valid IPv4 or IPv6 address and family.

- *InterfaceLuid* or *InterfaceIndex*  
   These parameters are used in the order that is listed earlier. So if *InterfaceLuid* is specified, this parameter is used to determine the interface. If no value was set for the *InterfaceLuid* member (the value of this parameter was set to zero), the *InterfaceIndex* parameter is next used to determine the interface.

In addition, on input, your driver can initialize the *SourceAddress* parameter to the preferred IPv4 or IPv6 address and family.

On output, when the call is successful, **GetBestRoute2** retrieves an MIB\_IPFORWARD\_ROW2 structure for the best route from the source IP address the destination IP address.

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

[**CreateIpForwardEntry2**](createipforwardentry2.md)

[**DeleteIpForwardEntry2**](deleteipforwardentry2.md)

[**GetIpForwardEntry2**](getipforwardentry2.md)

[**GetIpForwardTable2**](getipforwardtable2.md)

[**InitializeIpForwardEntry**](initializeipforwardentry.md)

[**MIB\_IPFORWARD\_ROW2**](mib-ipforward-row2.md)

[**MIB\_IPFORWARD\_TABLE2**](mib-ipforward-table2.md)

[**NotifyRouteChange2**](notifyroutechange2.md)

[**SetIpForwardEntry2**](setipforwardentry2.md)
