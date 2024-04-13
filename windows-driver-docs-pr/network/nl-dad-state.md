---
title: NL_DAD_STATE enumeration (Windows Drivers)
description: Learn more about the NL_DAD_STATE enumeration.
keywords:
- IpDadStateDeprecated
- IpDadStateDuplicate
- IpDadStateInvalid
- IpDadStatePreferred
- IpDadStateTentative
- NL_DAD_STATE
- nldef/NL_DAD_STATE
- NldsDeprecated
- NldsInvalid
- NldsDuplicate
- NldsTentative
- NldsPreferred
- nldef/IpDadStateDeprecated
- nldef/IpDadStateDuplicate
- nldef/IpDadStateInvalid
- nldef/IpDadStatePreferred
- nldef/NldsDeprecated
- nldef/IpDadStateTentative
- nldef/NldsPreferred
- nldef/NldsTentative
- nldef/NldsDuplicate
- nldef/NldsInvalid
ms.date: 10/25/2022
ms.topic: reference
---

# NL\_DAD\_STATE enumeration

The NL\_DAD\_STATE enumeration type defines the duplicate address detection (DAD) state.

## Syntax

``` c++
typedef enum  { 
  NldsInvalid,
  NldsTentative,
  NldsDuplicate,
  NldsDeprecated,
  NldsPreferred,
  IpDadStateInvalid     = 0,
  IpDadStateTentative,
  IpDadStateDuplicate,
  IpDadStateDeprecated,
  IpDadStatePreferred
} NL_DAD_STATE;
```

## Constants

- **NldsInvalid**  
   Reserved for system use. Do not use this value in your driver.

- **NldsTentative**  
   Reserved for system use. Do not use this value in your driver.

- **NldsDuplicate**  
   Reserved for system use. Do not use this value in your driver.

- **NldsDeprecated**  
   Reserved for system use. Do not use this value in your driver.

- **NldsPreferred**  
   Reserved for system use. Do not use this value in your driver.

- **IpDadStateInvalid**  
   The DAD state is invalid.

- **IpDadStateTentative**  
   The DAD state is tentative.

- **IpDadStateDuplicate**  
   A duplicate IP address has been detected.

- **IpDadStateDeprecated**  
   The IP address has been deprecated.

- **IpDadStatePreferred**  
   The IP address is the preferred address.

## Remarks

The DAD state applies to both IPv4 and IPv6 addresses.

## Requirements

<table>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Nldef.h (include Netioapi.h)</td>
</tr>
</tbody>
</table>
