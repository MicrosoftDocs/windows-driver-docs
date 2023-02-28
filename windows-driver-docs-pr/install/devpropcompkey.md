---
title: DEVPROPCOMPKEY structure (Windows Drivers)
description: Learn more about the DEVPROPCOMPKEY structure.
keywords:
- DEVPROP_STORE_SYSTEM
- DEVPROP_STORE_USER
- DEVPROPCOMPKEY
- PDEVPROPCOMPKEY
- devpropdef/DEVPROPCOMPKEY
- devpropdef/PDEVPROPCOMPKEY
ms.date: 11/01/2022
ms.topic: reference
---

# DEVPROPCOMPKEY structure

Describes a compound key for a device property.

## Syntax

``` c++
typedef struct _DEVPROPCOMPKEY {
  DEVPROPKEY   Key;
  DEVPROPSTORE Store;
  PCWSTR       LocaleName;
} DEVPROPCOMPKEY, *PDEVPROPCOMPKEY;
```

## Members

**Key**

A [**DEVPROPKEY**](devpropkey.md) structure that represents a key for a property.

**Store**

A **DEVPROPSTORE**-typed value that indicates the property store. Here are possible values:

**DEVPROP\_STORE\_SYSTEM**

**DEVPROP\_STORE\_USER**

**LocaleName**

A string for the property's locale name.

## Requirements

<table>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Devpropdef.h (include Swdevice.h)</td>
</tr>
</tbody>
</table>

## See also

[**DEVPROPERTY**](devproperty.md)
