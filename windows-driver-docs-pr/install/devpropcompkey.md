---
title: DEVPROPCOMPKEY Structure (Windows Drivers)
description: Learn more about the DEVPROPCOMPKEY structure.
keywords:
- DEVPROP_STORE_SYSTEM
- DEVPROP_STORE_USER
- DEVPROPCOMPKEY
- PDEVPROPCOMPKEY
- devpropdef/DEVPROPCOMPKEY
- devpropdef/PDEVPROPCOMPKEY
ms.date: 09/09/2024
ms.topic: reference
---

# DEVPROPCOMPKEY structure

Describes a compound key for a device property.

## Syntax

``` c++
typedef struct _DEVPROPCOMPKEY {
  DEVPROPKEY   Key;
  DEVPROPSTORE Store;
  PCWSTR       LocaleName;
} DEVPROPCOMPKEY, *PDEVPROPCOMPKEY;
```

## Members

`Key`

A [**DEVPROPKEY**](devpropkey.md) structure that represents a key for a property.

`Store`

A **DEVPROPSTORE**-typed value that indicates the property store. Here are possible values:

| Value | Meaning |
| -- | -- |
| DEVPROP\_STORE\_SYSTEM | This value indicates to use the system wide property store. |
| DEVPROP\_STORE\_USER | This value indicates to use a property store specific to the current user. |

`LocaleName`

A string for the property's locale name.

## Requirements

<table>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Devpropdef.h</td>
</tr>
</tbody>
</table>

## See also

[**DEVPROPERTY**](devproperty.md)
