---
title: ConvertInterfaceLuidToNameW function (Windows Drivers)
description: Learn more about the ConvertInterfaceLuidToNameW function.
keywords:
- ConvertInterfaceLuidToNameW
- netioapi/ConvertInterfaceLuidToNameW
ms.date: 10/18/2022
---

# ConvertInterfaceLuidToNameW function

The **ConvertInterfaceLuidToNameW** function converts a locally unique identifier (LUID) for a network interface to the Unicode interface name.

> [!NOTE]
> The ConvertInterface*Xxx* API family enumerates identifiers over all interfaces bound to TCP/IP, which may include virtual miniports, lightweight filters, tunnel adapters, and physical interfaces.

## Syntax

``` c++
NETIOAPI_API ConvertInterfaceLuidToNameW(
  _In_  const NET_LUID *InterfaceLuid,
  _Out_       PWSTR    InterfaceName,
  _In_        SIZE_T   Length
);
```

## Parameters

- *InterfaceLuid* \[in\]  
   A pointer to a [**NET\_LUID**](net-luid-value.md) union for the network interface.

- *InterfaceName* \[out\]  
   A pointer to a buffer to hold the NULL-terminated Unicode string. If **ConvertInterfaceLuidToNameW** returns successfully, *InterfaceName* contains the Unicode interface name.

- *Length* \[in\]  
   The length of the buffer, by character count, that the *InterfaceName* parameter points to. This value must be large enough to hold the interface name and the terminating NULL character. The maximum allowed length is NDIS\_IF\_MAX\_STRING\_SIZE + 1. For more information about NDIS\_IF\_MAX\_STRING\_SIZE, see the following Remarks section.

## Return value

**ConvertInterfaceLuidToNameW** returns STATUS\_SUCCESS if the function succeeds. If the function fails, **ConvertInterfaceLuidToNameW** returns one of the following error codes:

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
<td><p>One of the parameters is invalid. <strong>ConvertInterfaceLuidToNameW</strong> returns this error if either <em>InterfaceLuid</em> or <em>InterfaceName</em> is <strong>NULL</strong>, or if <em>InterfaceLuid</em> is invalid.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_NOT_ENOUGH_MEMORY</strong></td>
<td><p><strong>ConvertInterfaceLuidToNameW</strong> returns this error if the <em>InterfaceName</em> buffer was not as large as specified in the <em>Length</em> parameter and, therefore, the buffer could not hold the interface name.</p></td>
</tr>
</tbody>
</table>

## Remarks

The **ConvertInterfaceLuidToNameW** function is protocol-independent and works with network interfaces for both the IPv6 and IPv4 protocols.

The maximum length of the network interface name, NDIS\_IF\_MAX\_STRING\_SIZE, without the terminating NULL character, is defined in the Ntddndis.h header file. The NDIS\_IF\_MAX\_STRING\_SIZE is defined to be the IF\_MAX\_STRING\_SIZE constant, which is defined in the Ifdef.h header file.

> [!NOTE]
> The *Ntddndis.h* and *Ifdef.h* header files are automatically included in the *Netioapi.h* header file. You should never use the *Ntddndis.h* and *Ifdef.h* header files directly.

Use [**ConvertInterfaceLuidToNameA**](convertinterfaceluidtonamea.md) to convert a network interface LUID to an ANSI interface name.

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

[**ConvertInterfaceLuidToIndex**](convertinterfaceluidtoindex.md)

[**ConvertInterfaceLuidToNameA**](convertinterfaceluidtonamea.md)

[**ConvertInterfaceNameToLuidA**](convertinterfacenametoluida.md)

[**ConvertInterfaceNameToLuidW**](convertinterfacenametoluidw.md)

[**NET\_LUID**](net-luid-value.md)
