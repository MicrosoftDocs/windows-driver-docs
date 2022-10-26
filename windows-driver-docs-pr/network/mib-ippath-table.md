---
title: MIB_IPPATH_TABLE structure (Windows Drivers)
description: Learn more about the MIB_IPPATH_TABLE structure.
keywords:
- MIB_IPPATH_TABLE
- PMIB_IPPATH_TABLE
- netioapi/MIB_IPPATH_TABLE
- netioapi/PMIB_IPPATH_TABLE
ms.date: 10/25/2022
---

# MIB\_IPPATH\_TABLE structure

The MIB\_IPPATH\_TABLE structure contains a table of IP path entries.

## Syntax

``` c++
typedef struct _MIB_IPPATH_TABLE {
  ULONG          NumEntries;
  MIB_IPPATH_ROW Table[ANY_SIZE];
} MIB_IPPATH_TABLE, *PMIB_IPPATH_TABLE;
```

## Members

- **NumEntries**  
   A value that specifies the number of IP path entries in the array.

- **Table**  
   An array of [**MIB\_IPPATH\_ROW**](mib-ippath-row.md) structures that contain IP path entries.

## Remarks

The [**GetIpPathTable**](getippathtable.md) function enumerates the IP path entries on a local computer and returns this information in a MIB\_IPPATH\_TABLE structure. The [**FlushIpPathTable**](flushippathtable.md) function flushes the IP path table entries on a local computer.

The [**GetIpPathEntry**](getippathentry.md) function retrieves a single IP path entry and returns this information in a [**MIB\_IPPATH\_ROW**](mib-ippath-row.md) structure.

The MIB\_IPPATH\_TABLE structure might contain padding for alignment between the **NumEntries** member and the first MIB\_IPPATH\_ROW array entry in the **Table** member. Padding for alignment might also be present between the MIB\_IPPATH\_ROW array entries in the **Table** member. Any access to a MIB\_IPPATH\_ROW array entry should assume padding might exist.

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

[**FlushIpPathTable**](flushippathtable.md)

[**GetIpPathEntry**](getippathentry.md)

[**GetIpPathTable**](getippathtable.md)

[**MIB\_IPPATH\_ROW**](mib-ippath-row.md)
