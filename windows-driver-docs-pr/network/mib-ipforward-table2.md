---
title: MIB_IPFORWARD_TABLE2 structure (Windows Drivers)
description: Learn more about the MIB_IPFORWARD_TABLE2 structure.
keywords:
- MIB_IPFORWARD_TABLE2
- PMIB_IPFORWARD_TABLE2
- netioapi/MIB_IPFORWARD_TABLE2
- netioapi/PMIB_IPFORWARD_TABLE2
ms.date: 10/25/2022
ms.topic: reference
---

# MIB\_IPFORWARD\_TABLE2 structure

The MIB\_IPFORWARD\_TABLE2 structure contains a table of IP route entries.

## Syntax

``` c++
typedef struct _MIB_IPFORWARD_TABLE2 {
  ULONG              NumEntries;
  MIB_IPFORWARD_ROW2 Table[ANY_SIZE];
} MIB_IPFORWARD_TABLE2, *PMIB_IPFORWARD_TABLE2;
```

## Members

- **NumEntries**  
   A value that specifies the number of IP route entries in the array.

- **Table**  
   An array of [**MIB\_IPFORWARD\_ROW2**](mib-ipforward-row2.md) structures that contain IP route entries.

## Remarks

The [**GetIpForwardEntry2**](getipforwardentry2.md) function enumerates the IP route entries on a local computer and returns this information in a MIB\_IPFORWARD\_TABLE2 structure.

The **GetIpForwardEntry2** function retrieves a single IP route entry and returns this information in a [**MIB\_IPFORWARD\_ROW2**](mib-ipforward-row2.md) structure.

The MIB\_IPFORWARD\_TABLE2 structure might contain padding for alignment between the **NumEntries** member and the first MIB\_IPFORWARD\_ROW2 array entry in the **Table** member. Padding for alignment might also be present between the MIB\_IPFORWARD\_ROW2 array entries in the **Table** member. Any access to a MIB\_IPFORWARD\_ROW2 array entry should assume padding might exist.

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

[**GetIpForwardEntry2**](getipforwardentry2.md)

[**GetIpForwardTable2**](getipforwardtable2.md)

[**MIB\_IPFORWARD\_ROW2**](mib-ipforward-row2.md)
