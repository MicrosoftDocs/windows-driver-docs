---
title: IP_ADDRESS_PREFIX structure (Windows Drivers)
description: Learn more about the IP_ADDRESS_PREFIX structure.
keywords:
- IP_ADDRESS_PREFIX
- PIP_ADDRESS_PREFIX
- netioapi/IP_ADDRESS_PREFIX
- netioapi/PIP_ADDRESS_PREFIX
ms.date: 10/25/2022
ms.topic: reference
---

# IP\_ADDRESS\_PREFIX structure

The IP\_ADDRESS\_PREFIX structure stores an IP address prefix.

## Syntax

``` c++
typedef struct _IP_ADDRESS_PREFIX {
  SOCKADDR_INET Prefix;
  UINT8         PrefixLength;
} IP_ADDRESS_PREFIX, *PIP_ADDRESS_PREFIX;
```

## Members

- **Prefix**  
   The prefix or network part of the address represented as an IP address.

- **PrefixLength**  
   The length, in bits, of the prefix or network part of the IP address. For a unicast IPv4 address, any value that is greater than 32 is an illegal value. For a unicast IPv6 address, any value that is greater than 128 is an illegal value. A value of 255 is typically used to represent an illegal value.

## Requirements

<table>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Netioapi.h (include Netioapi.h)</td>
</tr>
</tbody>
</table>
