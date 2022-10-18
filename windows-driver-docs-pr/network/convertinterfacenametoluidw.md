---
title: ConvertInterfaceNameToLuidW function (Windows Drivers)
description: Learn more about the ConvertInterfaceNameToLuidW function.
keywords:
- ConvertInterfaceNameToLuidW
- netioapi/ConvertInterfaceNameToLuidW
ms.date: 10/18/2022
---

# ConvertInterfaceNameToLuidW function

The **ConvertInterfaceNameToLuidW** function converts a Unicode network interface name to the locally unique identifier (LUID) for the interface.

> [!NOTE]
> The ConvertInterface*Xxx* API family enumerates identifiers over all interfaces bound to TCP/IP, which may include virtual miniports, lightweight filters, tunnel adapters, and physical interfaces.

## Syntax

``` c++
NETIOAPI_API ConvertInterfaceNameToLuidW(
  _In_  const WCHAR    *InterfaceName,
  _Out_       NET_LUID *InterfaceLuid
);
```

## Parameters

- *InterfaceName* \[in\]  
   A pointer to a NULL-terminated Unicode string that contains the network interface name.

- *InterfaceLuid* \[out\]  
   A pointer to the [**NET\_LUID**](net-luid-value.md) union for this interface.

## Return value

**ConvertInterfaceNameToLuidW** returns STATUS\_SUCCESS if the function succeeds. If the function fails, **ConvertInterfaceNameToLuidW** returns one of the following error codes:

<table>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>STATUS_INVALID_NAME</strong></td>
<td><p>The interface name is invalid. <strong>ConvertInterfaceNameToLuidW</strong> returns this error if the <em>InterfaceName</em> parameter contains an invalid name or the length of the <em>InterfaceName</em> parameter exceeds the maximum allowed string length for this parameter.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_INVALID_PARAMETER</strong></td>
<td><p>One of the parameters is invalid. <strong>ConvertInterfaceNameToLuidW</strong> returns this error if the <em>InterfaceLuid</em> parameter is <strong>NULL</strong>.</p></td>
</tr>
</tbody>
</table>

## Remarks

The **ConvertInterfaceNameToLuidW** function is protocol-independent and works with network interfaces for both the IPv6 and IPv4 protocols.

The maximum length of the network interface name, NDIS\_IF\_MAX\_STRING\_SIZE, without the terminating NULL character, is defined in the Ntddndis.h header file. NDIS\_IF\_MAX\_STRING\_SIZE is defined to be the IF\_MAX\_STRING\_SIZE constant, which is defined in the Ifdef.h header file.

> [!NOTE]
> The *Ntddndis.h* and *Ifdef.h* header files are automatically included in the *Netioapi.h* header file. You should never use the *Ntddndis.h* and *Ifdef.h* header files directly.

Use the [**ConvertInterfaceNameToLuidA**](convertinterfacenametoluida.md) function to convert an ANSI interface name to a LUID.

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

[**ConvertInterfaceLuidToNameW**](convertinterfaceluidtonamew.md)

[**ConvertInterfaceNameToLuidA**](convertinterfacenametoluida.md)

[**NET\_LUID**](net-luid-value.md)
