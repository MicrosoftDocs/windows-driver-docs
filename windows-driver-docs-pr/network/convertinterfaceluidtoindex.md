---
title: ConvertInterfaceLuidToIndex function (Windows Drivers)
description: Learn more about the ConvertInterfaceLuidToIndex function.
keywords:
- ConvertInterfaceLuidToIndex
- netioapi/ConvertInterfaceLuidToIndex
ms.date: 10/18/2022
---

# ConvertInterfaceLuidToIndex function

The **ConvertInterfaceLuidToIndex** function converts a locally unique identifier (LUID) for a network interface to the local index for the interface.

> [!NOTE]
> The ConvertInterface*Xxx* API family enumerates identifiers over all interfaces bound to TCP/IP, which may include virtual miniports, lightweight filters, tunnel adapters, and physical interfaces.

## Syntax

``` c++
NETIOAPI_API ConvertInterfaceLuidToIndex(
  _In_  const NET_LUID     *InterfaceLuid,
  _Out_       PNET_IFINDEX InterfaceIndex
);
```

## Parameters

- *InterfaceLuid* \[in\]  
   A pointer to a [**NET\_LUID**](net-luid-value.md) union for the network interface.

- *InterfaceIndex* \[out\]  
   The local index value for the network interface.

## Return value

**ConvertInterfaceLuidToIndex** returns STATUS\_SUCCESS if the function succeeds. If the function fails, the *InterfaceIndex* parameter is set to NET\_IFINDEX\_UNSPECIFIED, and **ConvertInterfaceLuidToIndex** returns the following error code:

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
<td><p>One of the parameters is invalid. <strong>ConvertInterfaceLuidToIndex</strong> returns this error if either <em>InterfaceLuid</em> or <em>InterfaceIndex</em> is <strong>NULL</strong>, or if <em>InterfaceLuid</em> is invalid.</p></td>
</tr>
</tbody>
</table>

## Remarks

The **ConvertInterfaceLuidToIndex** function is protocol-independent and works with network interfaces for both the IPv6 and IPv4 protocols.

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

[**ConvertInterfaceAliasToLuid**](convertinterfacealiastoluid.md)

[**ConvertInterfaceGuidToLuid**](convertinterfaceguidtoluid.md)

[**ConvertInterfaceIndexToLuid**](convertinterfaceindextoluid.md)

[**ConvertInterfaceLuidToAlias**](convertinterfaceluidtoalias.md)

[**ConvertInterfaceLuidToGuid**](convertinterfaceluidtoguid.md)

[**ConvertInterfaceLuidToNameA**](convertinterfaceluidtonamea.md)

[**ConvertInterfaceLuidToNameW**](convertinterfaceluidtonamew.md)

[**ConvertInterfaceNameToLuidA**](convertinterfacenametoluida.md)

[**ConvertInterfaceNameToLuidW**](convertinterfacenametoluidw.md)

[**NET\_LUID**](net-luid-value.md)
