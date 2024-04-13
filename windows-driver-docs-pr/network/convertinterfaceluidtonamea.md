---
title: ConvertInterfaceLuidToNameA function (Windows Drivers)
description: Learn more about the ConvertInterfaceLuidToNameA function.
keywords:
- ConvertInterfaceLuidToNameA
- netioapi/ConvertInterfaceLuidToNameA
ms.date: 10/18/2022
ms.topic: reference
---

# ConvertInterfaceLuidToNameA function

The **ConvertInterfaceLuidToNameA** function converts a locally unique identifier (LUID) for a network interface to the ANSI interface name.

> [!NOTE]
> The ConvertInterface*Xxx* API family enumerates identifiers over all interfaces bound to TCP/IP, which may include virtual miniports, lightweight filters, tunnel adapters, and physical interfaces.

## Syntax

``` c++
NETIOAPI_API ConvertInterfaceLuidToNameA(
  _In_  const NET_LUID *InterfaceLuid,
  _Out_       PSTR     InterfaceName,
  _In_        SIZE_T   Length
);
```

## Parameters

- *InterfaceLuid* \[in\]  
   A pointer to a [**NET\_LUID**](net-luid-value.md) union for a network interface.

- *InterfaceName* \[out\]  
   A pointer to a buffer to hold the NULL-terminated ANSI string. If **ConvertInterfaceLuidToNameA** returns successfully, *InterfaceName* contains the ANSI interface name.

- *Length* \[in\]  
   The length, in bytes, of the buffer that the *InterfaceName* parameter points to. This value must be large enough to hold the interface name and the terminating NULL character. The maximum allowed length is NDIS\_IF\_MAX\_STRING\_SIZE + 1. For more information about NDIS\_IF\_MAX\_STRING\_SIZE, see the following Remarks section.

## Return value

**ConvertInterfaceLuidToNameA** returns STATUS\_SUCCESS if the function succeeds. If the function fails, **ConvertInterfaceLuidToNameA** returns one of the following error codes:

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
<td><p>One of the parameters is invalid. <strong>ConvertInterfaceLuidToNameA</strong> returns this error if either <em>InterfaceLuid</em> or <em>InterfaceName</em> is <strong>NULL</strong>, or if <em>InterfaceLuid</em> is invalid.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_NOT_ENOUGH_MEMORY</strong></td>
<td><p><strong>ConvertInterfaceLuidToNameA</strong> returns this error if the <em>InterfaceName</em> buffer was not as large as specified in the <em>Length</em> parameter and, therefore, the buffer could not hold the interface name.</p></td>
</tr>
</tbody>
</table>

## Remarks

The **ConvertInterfaceLuidToNameA** function is protocol-independent and works with network interfaces for both the IPv6 and IPv4 protocols.

The maximum length of the name for a network interface, NDIS\_IF\_MAX\_STRING\_SIZE, without the terminating NULL character, is defined in the Ntddndis.h header file. NDIS\_IF\_MAX\_STRING\_SIZE is defined to be the IF\_MAX\_STRING\_SIZE constant, which is defined in the Ifdef.h header file.

> [!NOTE]
> The *Ntddndis.h* and *Ifdef.h* header files are automatically included in the *Netioapi.h* header file. You should never use the *Ntddndis.h* and *Ifdef.h* header files directly.

Use the [**ConvertInterfaceLuidToNameW**](convertinterfaceluidtonamew.md) function to convert a network interface LUID to a Unicode interface name.

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

[**ConvertInterfaceLuidToNameW**](convertinterfaceluidtonamew.md)

[**ConvertInterfaceNameToLuidA**](convertinterfacenametoluida.md)

[**ConvertInterfaceNameToLuidW**](convertinterfacenametoluidw.md)

[**NET\_LUID**](net-luid-value.md)
