---
title: DEVPROPERTY structure (Windows Drivers)
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
ms.date: 11/01/2022
---

# DEVPROPERTY structure

Describes a property for a software device.

## Syntax

``` c++
typedef struct _DEVPROPERTY {
  DEVPROPCOMPKEY CompKey;
  DEVPROPTYPE    Type;
  ULONG          BufferSize;
  PVOID          Buffer;
} DEVPROPERTY, *PDEVPROPERTY;
```

## Members

- **CompKey**  
  A [**DEVPROPCOMPKEY**](devpropcompkey.md) structure that represents a compound key for a property.

- **Type**  
  A **DEVPROPTYPE** value that indicates the property type. Valid **DEVPROPTYPE** values are constructed from base DEVPROP\_TYPE\_ values, which may be modified by a logical OR with DEVPROP\_TYPEMOD\_ values, as appropriate.

  Here are possible DEVPROP\_TYPE\_ values:

    <table>
    <thead>
    <tr class="header">
    <th>Value</th>
    <th>Meaning</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><span id="DEVPROP_TYPE_EMPTY"></span><span id="devprop_type_empty"></span>
    <strong>DEVPROP_TYPE_EMPTY</strong>
    0x00000000</td>
    <td><p>Nothing, no property data</p></td>
    </tr>
    <tr class="even">
    <td><span id="DEVPROP_TYPE_NULL"></span><span id="devprop_type_null"></span>
    <strong>DEVPROP_TYPE_NULL</strong>
    0x00000001</td>
    <td><p>Null property data</p></td>
    </tr>
    <tr class="odd">
    <td><span id="DEVPROP_TYPE_SBYTE"></span><span id="devprop_type_sbyte"></span>
    <strong>DEVPROP_TYPE_SBYTE</strong>
    0x00000002</td>
    <td><p>8-bit signed int (SBYTE)</p></td>
    </tr>
    <tr class="even">
    <td><span id="DEVPROP_TYPE_BYTE"></span><span id="devprop_type_byte"></span>
    <strong>DEVPROP_TYPE_BYTE</strong>
    0x00000003</td>
    <td><p>8-bit unsigned int (BYTE)</p></td>
    </tr>
    <tr class="odd">
    <td><span id="DEVPROP_TYPE_INT16"></span><span id="devprop_type_int16"></span>
    <strong>DEVPROP_TYPE_INT16</strong>
    0x00000004</td>
    <td><p>16-bit signed int (SHORT)</p></td>
    </tr>
    <tr class="even">
    <td><span id="DEVPROP_TYPE_UINT16"></span><span id="devprop_type_uint16"></span>
    <strong>DEVPROP_TYPE_UINT16</strong>
    0x00000005</td>
    <td><p>16-bit unsigned int (USHORT)</p></td>
    </tr>
    <tr class="odd">
    <td><span id="DEVPROP_TYPE_INT32"></span><span id="devprop_type_int32"></span>
    <strong>DEVPROP_TYPE_INT32</strong>
    0x00000006</td>
    <td><p>32-bit signed int (LONG)</p></td>
    </tr>
    <tr class="even">
    <td><span id="DEVPROP_TYPE_UINT32"></span><span id="devprop_type_uint32"></span>
    <strong>DEVPROP_TYPE_UINT32</strong>
    0x00000007</td>
    <td><p>32-bit unsigned int (ULONG)</p></td>
    </tr>
    <tr class="odd">
    <td><span id="DEVPROP_TYPE_INT64"></span><span id="devprop_type_int64"></span>
    <strong>DEVPROP_TYPE_INT64</strong>
    0x00000008</td>
    <td><p>64-bit signed int (LONG64)</p></td>
    </tr>
    <tr class="even">
    <td><span id="DEVPROP_TYPE_UINT64"></span><span id="devprop_type_uint64"></span>
    <strong>DEVPROP_TYPE_UINT64</strong>
    0x00000009</td>
    <td><p>64-bit unsigned int (ULONG64)</p></td>
    </tr>
    <tr class="odd">
    <td><span id="DEVPROP_TYPE_FLOAT"></span><span id="devprop_type_float"></span>
    <strong>DEVPROP_TYPE_FLOAT</strong>
    0x0000000A</td>
    <td><p>32-bit floating-point (FLOAT)</p></td>
    </tr>
    <tr class="even">
    <td><span id="DEVPROP_TYPE_DOUBLE"></span><span id="devprop_type_double"></span>
    <strong>DEVPROP_TYPE_DOUBLE</strong>
    0x0000000B</td>
    <td><p>64-bit floating-point (DOUBLE)</p></td>
    </tr>
    <tr class="odd">
    <td><span id="DEVPROP_TYPE_DECIMAL"></span><span id="devprop_type_decimal"></span>
    <strong>DEVPROP_TYPE_DECIMAL</strong>
    0x0000000C</td>
    <td><p>128-bit data (DECIMAL)</p></td>
    </tr>
    <tr class="even">
    <td><span id="DEVPROP_TYPE_GUID"></span><span id="devprop_type_guid"></span>
    <strong>DEVPROP_TYPE_GUID</strong>
    0x0000000D</td>
    <td><p>128-bit unique identifier (GUID)</p></td>
    </tr>
    <tr class="odd">
    <td><span id="DEVPROP_TYPE_CURRENCY"></span><span id="devprop_type_currency"></span>
    <strong>DEVPROP_TYPE_CURRENCY</strong>
    0x0000000E</td>
    <td><p>64 bit signed int currency value (CURRENCY)</p></td>
    </tr>
    <tr class="even">
    <td><span id="DEVPROP_TYPE_DATE"></span><span id="devprop_type_date"></span>
    <strong>DEVPROP_TYPE_DATE</strong>
    0x0000000F</td>
    <td><p>date (DATE)</p></td>
    </tr>
    <tr class="odd">
    <td><span id="DEVPROP_TYPE_FILETIME"></span><span id="devprop_type_filetime"></span>
    <strong>DEVPROP_TYPE_FILETIME</strong>
    0x00000010</td>
    <td><p>file time (FILETIME)</p></td>
    </tr>
    <tr class="even">
    <td><span id="DEVPROP_TYPE_BOOLEAN"></span><span id="devprop_type_boolean"></span>
    <strong>DEVPROP_TYPE_BOOLEAN</strong>
    0x00000011</td>
    <td><p>8-bit boolean (DEVPROP_BOOLEAN)</p></td>
    </tr>
    <tr class="odd">
    <td><span id="DEVPROP_TYPE_STRING"></span><span id="devprop_type_string"></span>
    <strong>DEVPROP_TYPE_STRING</strong>
    0x00000012</td>
    <td><p>Null-terminated string</p></td>
    </tr>
    <tr class="even">
    <td><span id="DEVPROP_TYPE_STRING_LIST"></span><span id="devprop_type_string_list"></span>
    <strong>DEVPROP_TYPE_STRING_LIST</strong>
    DEVPROP_TYPE_STRING|DEVPROP_TYPEMOD_LIST</td>
    <td><p>Multi-sz string list</p></td>
    </tr>
    <tr class="odd">
    <td><span id="DEVPROP_TYPE_SECURITY_DESCRIPTOR"></span><span id="devprop_type_security_descriptor"></span>
    <strong>DEVPROP_TYPE_SECURITY_DESCRIPTOR</strong>
    0x00000013</td>
    <td><p>Self-relative binary SECURITY_DESCRIPTOR</p></td>
    </tr>
    <tr class="even">
    <td><span id="DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING"></span><span id="devprop_type_security_descriptor_string"></span>
    <strong>DEVPROP_TYPE_SECURITY_DESCRIPTOR_STRING</strong>
    0x00000014</td>
    <td><p>Security descriptor string (SDDL format)</p></td>
    </tr>
    <tr class="odd">
    <td><span id="DEVPROP_TYPE_DEVPROPKEY"></span><span id="devprop_type_devpropkey"></span>
    <strong>DEVPROP_TYPE_DEVPROPKEY</strong>
    0x00000015</td>
    <td><p>Device property key (DEVPROPKEY)</p></td>
    </tr>
    <tr class="even">
    <td><span id="DEVPROP_TYPE_DEVPROPTYPE"></span><span id="devprop_type_devproptype"></span>
    <strong>DEVPROP_TYPE_DEVPROPTYPE</strong>
    0x00000016</td>
    <td><p>Device property type (DEVPROPTYPE)</p></td>
    </tr>
    <tr class="odd">
    <td><span id="DEVPROP_TYPE_BINARY"></span><span id="devprop_type_binary"></span>
    <strong>DEVPROP_TYPE_BINARY</strong>
    DEVPROP_TYPE_BYTE|DEVPROP_TYPEMOD_ARRAY</td>
    <td><p>Custom binary data</p></td>
    </tr>
    <tr class="even">
    <td><span id="DEVPROP_TYPE_ERROR"></span><span id="devprop_type_error"></span>
    <strong>DEVPROP_TYPE_ERROR</strong>
    0x00000017</td>
    <td><p>32-bit Win32 system error code</p></td>
    </tr>
    <tr class="odd">
    <td><span id="DEVPROP_TYPE_NTSTATUS"></span><span id="devprop_type_ntstatus"></span>
    <strong>DEVPROP_TYPE_NTSTATUS</strong>
    0x00000018</td>
    <td><p>32-bit NTSTATUS code</p></td>
    </tr>
    <tr class="even">
    <td><span id="DEVPROP_TYPE_STRING_INDIRECT"></span><span id="devprop_type_string_indirect"></span>
    <strong>DEVPROP_TYPE_STRING_INDIRECT</strong>
    0x00000019</td>
    <td><p>String resource (@[path\]&lt;dllname&gt;,-&lt;strId&gt;)</p></td>
    </tr>
    </tbody>
    </table>

  Here are possible DEVPROP\_TYPEMOD\_ values:

    <table>
    <thead>
    <tr class="header">
    <th>Value</th>
    <th>Meaning</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><span id="DEVPROP_TYPEMOD_ARRAY"></span><span id="devprop_typemod_array"></span>
    <strong>DEVPROP_TYPEMOD_ARRAY</strong>
    0x00001000</td>
    <td><p>Array of fixed-sized data elements</p></td>
    </tr>
    <tr class="even">
    <td><span id="DEVPROP_TYPEMOD_LIST"></span><span id="devprop_typemod_list"></span>
    <strong>DEVPROP_TYPEMOD_LIST</strong>
    0x00002000</td>
    <td><p>List of variable-sized data elements</p></td>
    </tr>
    </tbody>
    </table>

- **BufferSize**  
  The size in bytes of the property in **Buffer**.

- **Buffer**  
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
<td>Devpropdef.h (include Swdevice.h)</td>
</tr>
</tbody>
</table>

## See also

[**SW\_DEVICE\_CREATE\_INFO**](/windows/win32/api/swdevicedef/ns-swdevicedef-sw_device_create_info)
