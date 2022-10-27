---
title: MIB_IPINTERFACE_TABLE structure (Windows Drivers)
description: Learn more about the MIB_IPINTERFACE_TABLE structure.
keywords:
- MIB_IPINTERFACE_TABLE
- PMIB_IPINTERFACE_TABLE
- netioapi/MIB_IPINTERFACE_TABLE
- netioapi/PMIB_IPINTERFACE_TABLE
ms.date: 10/25/2022
---

# MIB\_IPINTERFACE\_TABLE structure

The MIB\_IPINTERFACE\_TABLE structure contains a table of IP interface entries.

## Syntax

``` c++
typedef struct _MIB_IPINTERFACE_TABLE {
  ULONG               NumEntries;
  MIB_IPINTERFACE_ROW Table[ANY_SIZE];
} MIB_IPINTERFACE_TABLE, *PMIB_IPINTERFACE_TABLE;
```

## Members

- **NumEntries**  
   The number of IP interface entries in the array.

- **Table**  
   An array of [**MIB\_IPINTERFACE\_ROW**](mib-ipinterface-row.md) structures that contain IP interface entries.

## Remarks

The [**GetIpInterfaceTable**](getipinterfacetable.md) function enumerates the IP interface entries on a local computer and returns this information in a MIB\_IPINTERFACE\_TABLE structure.

The MIB\_IPINTERFACE\_TABLE structure might contain padding for alignment between the **NumEntries** member and the first [**MIB\_IPINTERFACE\_ROW**](mib-ipinterface-row.md) array entry in the **Table** member. Padding for alignment might also be present between the MIB\_IPINTERFACE\_ROW array entries in the **Table** member. Any access to a MIB\_IPINTERFACE\_ROW array entry should assume padding might exist.

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

## See also

[**GetIpInterfaceTable**](getipinterfacetable.md)

[**MIB\_IPINTERFACE\_ROW**](mib-ipinterface-row.md)
