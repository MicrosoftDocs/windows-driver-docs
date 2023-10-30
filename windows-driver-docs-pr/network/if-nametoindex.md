---
title: if_nametoindex function (Windows Drivers)
description: Learn more about the if_nametoindex function.
keywords:
- if_nametoindex
- netioapi/if_nametoindex
ms.date: 10/18/2022
ms.topic: reference
---

# if\_nametoindex function

The **if\_nametoindex** function converts the ANSI interface name for a network interface to the local index for the interface.

## Syntax

``` c++
NET_IFINDEX NETIOAPI_API_ if_nametoindex(
  _In_ PCSTR InterfaceName
);
```

## Parameters

- *InterfaceName* \[in\]  
   A pointer to a NULL-terminated ANSI string that contains the interface name.

## Return value

If the function succeeds, **if\_nametoindex** returns the local interface index. If the function fails, **if\_nametoindex** returns zero.

## Remarks

The **if\_nametoindex** function maps an interface name into its corresponding index. This function is designed as part of basic socket extensions for IPv6 as described by the IETF in [RFC 2553](https://www.ietf.org/rfc/rfc2553.txt).

The **if\_nametoindex** function is implemented for portability of drivers with Unix environments, but the **ConvertInterface*Xxx*** functions are the preferred method to convert network interface identifiers. You can replace the **if\_nametoindex** function by a call to the [**ConvertInterfaceNameToLuidA**](convertinterfacenametoluida.md) function to convert the ANSI interface name to a [**NET\_LUID**](net-luid-value.md) union, followed by a call to the [**ConvertInterfaceLuidToIndex**](convertinterfaceluidtoindex.md) function to convert NET\_LUID to the local interface index.

If the **if\_nametoindex** function fails and returns zero, you cannot determine an error code.

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

[**ConvertInterfaceLuidToIndex**](convertinterfaceluidtoindex.md)

[**ConvertInterfaceNameToLuidA**](convertinterfacenametoluida.md)

[**NET\_LUID**](net-luid-value.md)
