---
title: DEVPROPERTY Structure (Windows Drivers)
description: Learn more about the DEVPROPERTY structure.
keywords:
- DEVPROP_TYPE_GUID
- DEVPROP_TYPE_INT16
- DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING
- DEVPROP_TYPE_SECURITY_DESCRIPTOR
- DEVPROP_TYPE_EMPTY
- DEVPROP_TYPE_UINT16
- DEVPROP_TYPE_DEVPROPTYPE
- DEVPROP_TYPE_FLOAT
- DEVPROP_TYPE_SBYTE
- DEVPROP_TYPE_ERROR
- DEVPROP_TYPE_STRING
- DEVPROP_TYPE_DEVPROPKEY
- DEVPROP_TYPE_UINT64
- DEVPROP_TYPE_INT32
- DEVPROP_TYPE_DOUBLE
- DEVPROP_TYPE_FILETIME
- DEVPROP_TYPE_DECIMAL
- DEVPROP_TYPE_UINT32
- DEVPROP_TYPE_NULL
- DEVPROP_TYPE_DATE
- DEVPROP_TYPE_INT64
- DEVPROP_TYPE_NTSTATUS
- DEVPROP_TYPEMOD_LIST
- DEVPROP_TYPE_CURRENCY
- DEVPROP_TYPE_BOOLEAN
- DEVPROP_TYPEMOD_ARRAY
- DEVPROP_TYPE_STRING_INDIRECT
- DEVPROP_TYPE_BYTE
- DEVPROP_TYPE_BINARY
- DEVPROP_TYPE_STRING_LIST
- DEVPROPERTY
- PDEVPROPERTY
- devpropdef/DEVPROPERTY
- devpropdef/PDEVPROPERTY
ms.date: 09/09/2024
ms.topic: reference
---

# DEVPROPERTY structure

Describes a property for a software device.

## Syntax

``` c++
typedef struct _DEVPROPERTY {
  DEVPROPCOMPKEY CompKey;
  DEVPROPTYPE    Type;
  ULONG          BufferSize;
  PVOID          Buffer;
} DEVPROPERTY, *PDEVPROPERTY;
```

## Members

`CompKey`

A [**DEVPROPCOMPKEY**](devpropcompkey.md) structure that represents a compound key for a property.

`Type`

A **DEVPROPTYPE** value that indicates the property type. Valid **DEVPROPTYPE** values are constructed from base DEVPROP\_TYPE\_ values, which may be modified by a logical OR with DEVPROP\_TYPEMOD\_ values, as appropriate.

Here are possible DEVPROP\_TYPE\_ values:

| Value | Meaning |
| -- | -- |
| [DEVPROP_TYPE_EMPTY](devprop-type-empty.md) 0x00000000 | Nothing, no property data |
| [DEVPROP_TYPE_NULL](devprop-type-null.md) 0x00000001 | Null property data |
| [DEVPROP_TYPE_SBYTE](devprop-type-sbyte.md) 0x00000002 | 8-bit signed int (SBYTE) |
| [DEVPROP_TYPE_BYTE](devprop-type-byte.md) 0x00000003 | 8-bit unsigned int (BYTE) |
| [DEVPROP_TYPE_INT16](devprop-type-int16.md) 0x00000004 | 16-bit signed int (SHORT) |
| [DEVPROP_TYPE_UINT16](devprop-type-uint16.md) 0x00000005 | 16-bit unsigned int (USHORT) |
| [DEVPROP_TYPE_INT32](devprop-type-int32.md) 0x00000006 | 32-bit signed int (LONG) |
| [DEVPROP_TYPE_UINT32](devprop-type-uint32.md) 0x00000007 | 32-bit unsigned int (ULONG) |
| [DEVPROP_TYPE_INT64](devprop-type-int64.md) 0x00000008 | 64-bit signed int (LONG64) |
| [DEVPROP_TYPE_UINT64](devprop-type-uint64.md) 0x00000009 | 64-bit unsigned int (ULONG64) |
| [DEVPROP_TYPE_FLOAT](devprop-type-float.md) 0x0000000A | 32-bit floating-point (FLOAT) |
| [DEVPROP_TYPE_DOUBLE](devprop-type-double.md) 0x0000000B | 64-bit floating-point (DOUBLE) |
| [DEVPROP_TYPE_DECIMAL](devprop-type-decimal.md) 0x0000000C | 128-bit data (DECIMAL) |
| [DEVPROP_TYPE_GUID](devprop-type-guid.md) 0x0000000D | 128-bit unique identifier (GUID) |
| [DEVPROP_TYPE_CURRENCY](devprop-type-currency.md) 0x0000000E | 64 bit signed int currency value (CURRENCY) |
| [DEVPROP_TYPE_DATE](devprop-type-date.md) 0x0000000F | date (DATE) |
| [DEVPROP_TYPE_FILETIME](devprop-type-filetime.md) 0x00000010 | file time (FILETIME) |
| [DEVPROP_TYPE_BOOLEAN](devprop-type-boolean.md) 0x00000011 | 8-bit boolean (DEVPROP_BOOLEAN) |
| [DEVPROP_TYPE_STRING](devprop-type-string.md) 0x00000012 | Null-terminated string |
| [DEVPROP_TYPE_STRING_LIST](devprop-type-string-list.md) (DEVPROP_TYPE_STRING \| DEVPROP_TYPEMOD_LIST) | Multi-sz string list |
| [DEVPROP_TYPE_SECURITY_DESCRIPTOR](devprop-type-security-descriptor.md) 0x00000013 | Self-relative binary SECURITY_DESCRIPTOR |
| [DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING](devprop-type-security-descriptor-string.md) 0x00000014 | Security descriptor string (SDDL format) |
| [DEVPROP_TYPE_DEVPROPKEY](devprop-type-devpropkey.md) 0x00000015 | Device property key (DEVPROPKEY) |
| [DEVPROP_TYPE_DEVPROPTYPE](devprop-type-devproptype.md) 0x00000016 | Device property type (DEVPROPTYPE) |
| [DEVPROP_TYPE_BINARY](devprop-type-binary.md) (DEVPROP_TYPE_BYTE \| DEVPROP_TYPEMOD_ARRAY) | Custom binary data |
| [DEVPROP_TYPE_ERROR](devprop-type-error.md) 0x00000017 | 32-bit Win32 system error code |
| [DEVPROP_TYPE_NTSTATUS](devprop-type-ntstatus.md) 0x00000018 | 32-bit NTSTATUS code |
| [DEVPROP_TYPE_STRING_INDIRECT](devprop-type-string-indirect.md) 0x00000019 | String resource (@[path\]&lt;dllname&gt;,-&lt;strId&gt;) |

Here are possible DEVPROP\_TYPEMOD\_ values:

| Value | Meaning |
| -- | -- |
| [DEVPROP_TYPEMOD_ARRAY](devprop-typemod-array.md) 0x00001000 | Array of fixed-sized data elements |
| [DEVPROP_TYPEMOD_LIST](devprop-typemod-list.md) 0x00002000 | List of variable-sized data elements |

`BufferSize`

The size in bytes of the property in `Buffer`.

`Buffer`

The buffer that contains the property info.

This member can be a **PBYTE** type if **MIDL\_PASS** is defined:

```cpp
  #ifdef MIDL_PASS
        [size_is(BufferSize)] PBYTE Buffer;
    #else
        __field_bcount_opt(BufferSize) PVOID Buffer;
    #endif
```
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

[**SW\_DEVICE\_CREATE\_INFO**](/windows/win32/api/swdevicedef/ns-swdevicedef-sw_device_create_info)
