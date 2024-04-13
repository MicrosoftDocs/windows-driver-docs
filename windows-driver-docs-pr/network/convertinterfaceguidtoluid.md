---
title: ConvertInterfaceGuidToLuid function (Windows Drivers)
description: Learn more about the ConvertInterfaceGuidToLuid function.
keywords:
- ConvertInterfaceGuidToLuid
- netioapi/ConvertInterfaceGuidToLuid
ms.date: 10/18/2022
ms.topic: reference
---

# ConvertInterfaceGuidToLuid function

The **ConvertInterfaceGuidToLuid** function converts a globally unique identifier (GUID) for a network interface to the locally unique identifier (LUID) for the interface.

> [!NOTE]
> The ConvertInterface*Xxx* API family enumerates identifiers over all interfaces bound to TCP/IP, which may include virtual miniports, lightweight filters, tunnel adapters, and physical interfaces.

## Syntax

``` c++
NETIOAPI_API ConvertInterfaceGuidToLuid(
  _In_  const GUID      *InterfaceGuid,
  _Out_       PNET_LUID InterfaceLuid
);
```

## Parameters

- *InterfaceGuid* \[in\]  
   A pointer to a GUID for the network interface.

- *InterfaceLuid* \[out\]  
   A pointer to the [**NET\_LUID**](net-luid-value.md) union for the network interface.

## Return value

**ConvertInterfaceGuidToLuid** returns STATUS\_SUCCESS if the function succeeds. If the function fails, the *InterfaceLuid* parameter is set to **NULL**, and **ConvertInterfaceGuidToLuid** returns the following error code:

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
<td><p>One of the parameters was invalid. <strong>ConvertInterfaceGuidToLuid</strong> returns this error if either <em>InterfaceAlias</em> or <em>InterfaceLuid</em> is <strong>NULL</strong>, or if <em>InterfaceGuid</em> is invalid.</p></td>
</tr>
</tbody>
</table>

## Remarks

The **ConvertInterfaceGuidToLuid** function is protocol-independent and works with network interfaces for both the IPv6 and IPv4 protocols.

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

[**ConvertInterfaceIndexToLuid**](convertinterfaceindextoluid.md)

[**ConvertInterfaceLuidToAlias**](convertinterfaceluidtoalias.md)

[**ConvertInterfaceLuidToGuid**](convertinterfaceluidtoguid.md)

[**ConvertInterfaceLuidToIndex**](convertinterfaceluidtoindex.md)

[**ConvertInterfaceLuidToNameA**](convertinterfaceluidtonamea.md)

[**ConvertInterfaceLuidToNameW**](convertinterfaceluidtonamew.md)

[**ConvertInterfaceNameToLuidA**](convertinterfacenametoluida.md)

[**ConvertInterfaceNameToLuidW**](convertinterfacenametoluidw.md)

[**NET\_LUID**](net-luid-value.md)
