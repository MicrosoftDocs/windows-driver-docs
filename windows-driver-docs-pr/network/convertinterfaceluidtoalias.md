---
title: ConvertInterfaceLuidToAlias function (Windows Drivers)
description: Learn more about the ConvertInterfaceLuidToAlias function.
keywords:
- ConvertInterfaceLuidToAlias
- netioapi/ConvertInterfaceLuidToAlias
ms.date: 10/18/2022
---

# ConvertInterfaceLuidToAlias function

The **ConvertInterfaceLuidToAlias** function converts a locally unique identifier (LUID) for a network interface to an interface alias.

> [!NOTE]
> The ConvertInterface*Xxx* API family enumerates identifiers over all interfaces bound to TCP/IP, which may include virtual miniports, lightweight filters, tunnel adapters, and physical interfaces.

## Syntax

``` c++
NETIOAPI_API ConvertInterfaceLuidToAlias(
  _In_  const NET_LUID *InterfaceLuid,
  _Out_       PWSTR    InterfaceAlias,
  _In_        SIZE_T   Length
);
```

## Parameters

- *InterfaceLuid* \[in\]  
   A pointer to a [**NET\_LUID**](net-luid-value.md) union for the network interface.

- *InterfaceAlias* \[out\]  
   A pointer to a buffer to hold the NULL-terminated Unicode string. If **ConvertInterfaceLuidToAlias** returns successfully, *InterfaceAlias* contains the alias name of the network interface.

- *Length* \[in\]  
   The length, by character count, of the buffer that the *InterfaceAlias* parameter points to. This value must be large enough to hold the alias name of the network interface and the terminating NULL character. The maximum allowed length is NDIS\_IF\_MAX\_STRING\_SIZE + 1. For more information about NDIS\_IF\_MAX\_STRING\_SIZE, see the following Remarks section.

## Return value

**ConvertInterfaceLuidToAlias** returns STATUS\_SUCCESS if the function succeeds. If the function fails, **ConvertInterfaceLuidToAlias** returns one of the following error codes:

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
<td><p>One of the parameters is invalid. <strong>ConvertInterfaceLuidToAlias</strong> returns this error if either <em>InterfaceLuid</em> or <em>InterfaceAlias</em> is <strong>NULL</strong>, or if <em>InterfaceLuid</em> is invalid.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_NOT_ENOUGH_MEMORY</strong></td>
<td><p>Not enough storage is available. <strong>ConvertInterfaceLuidToAlias</strong> returns this error if the size of the buffer that the <em>InterfaceAlias</em> parameter points to was not as large as specified in the <em>Length</em> parameter and, therefore, the buffer could not hold the alias name.</p></td>
</tr>
</tbody>
</table>

## Remarks

The **ConvertInterfaceLuidToAlias** function is protocol-independent and works with network interfaces for both the IPv6 and IPv4 protocols.

The maximum length of the alias name for a network interface, NDIS\_IF\_MAX\_STRING\_SIZE, without the terminating NULL character, is declared in the *Ntddndis.h* header file. NDIS\_IF\_MAX\_STRING\_SIZE is defined to be the IF\_MAX\_STRING\_SIZE constant, which is defined in the *Ifdef.h* header file.

> [!NOTE]
> The *Ntddndis.h* and *Ifdef.h* header files are automatically included in the *Netioapi.h* header file. You should never use the *Ntddndis.h* and *Ifdef.h* header files directly.

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

[**ConvertInterfaceLuidToGuid**](convertinterfaceluidtoguid.md)

[**ConvertInterfaceLuidToIndex**](convertinterfaceluidtoindex.md)

[**ConvertInterfaceLuidToNameA**](convertinterfaceluidtonamea.md)

[**ConvertInterfaceLuidToNameW**](convertinterfaceluidtonamew.md)

[**ConvertInterfaceNameToLuidA**](convertinterfacenametoluida.md)

[**ConvertInterfaceNameToLuidW**](convertinterfacenametoluidw.md)

[**NET\_LUID**](net-luid-value.md)
