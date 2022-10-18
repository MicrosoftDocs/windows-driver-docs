---
title: ConvertInterfaceLuidToGuid function (Windows Drivers)
description: Learn more about the ConvertInterfaceLuidToGuid function.
keywords:
- ConvertInterfaceLuidToGuid
- netioapi/ConvertInterfaceLuidToGuid
ms.date: 10/18/2022
---

# ConvertInterfaceLuidToGuid function

The **ConvertInterfaceLuidToGuid** function converts a locally unique identifier (LUID) for a network interface to a globally unique identifier (GUID) for the interface.

> [!NOTE]
> The ConvertInterface*Xxx* API family enumerates identifiers over all interfaces bound to TCP/IP, which may include virtual miniports, lightweight filters, tunnel adapters, and physical interfaces.

## Syntax

``` c++
NETIOAPI_API ConvertInterfaceLuidToGuid(
  _In_  const NET_LUID *InterfaceLuid,
  _Out_       GUID     *InterfaceGuid
);
```

## Parameters

- *InterfaceLuid* \[in\]  
   A pointer to a [**NET\_LUID**](net-luid-value.md) union for the network interface.

- *InterfaceGuid* \[out\]  
   A pointer to the GUID for the network interface.

## Return value

**ConvertInterfaceLuidToGuid** returns STATUS\_SUCCESS if the function succeeds. If the function fails, the *InterfaceGuid* parameter is set to **NULL**, and **ConvertInterfaceLuidToGuid** returns the following error code:

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
<td><p>One of the parameters is invalid. <strong>ConvertInterfaceLuidToGuid</strong> returns this error if either <em>InterfaceLuid</em> or <em>InterfaceGuid</em> is <strong>NULL</strong>, or if <em>InterfaceLuid</em> is invalid.</p></td>
</tr>
</tbody>
</table>

## Remarks

The **ConvertInterfaceLuidToGuid** function is protocol-independent and works with network interfaces for both the IPv6 and IPv4 protocols.

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

[**ConvertInterfaceLuidToIndex**](convertinterfaceluidtoindex.md)

[**ConvertInterfaceLuidToNameA**](convertinterfaceluidtonamea.md)

[**ConvertInterfaceLuidToNameW**](convertinterfaceluidtonamew.md)

[**ConvertInterfaceNameToLuidA**](convertinterfacenametoluida.md)

[**ConvertInterfaceNameToLuidW**](convertinterfacenametoluidw.md)

[**NET\_LUID**](net-luid-value.md)
