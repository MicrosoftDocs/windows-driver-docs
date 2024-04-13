---
title: InitializeIpForwardEntry function (Windows Drivers)
description: Learn more about the InitializeIpForwardEntry function.
keywords:
- InitializeIpForwardEntry
- netioapi/InitializeIpForwardEntry
ms.date: 10/25/2022
ms.topic: reference
---

# InitializeIpForwardEntry function

The **InitializeIpForwardEntry** function initializes a [**MIB\_IPFORWARD\_ROW2**](mib-ipforward-row2.md) structure with default values for an IP route entry on a local computer.

## Syntax

``` c++
VOID NETIOAPI_API_ InitializeIpForwardEntry(
  _Out_ PMIB_IPFORWARD_ROW2 Row
);
```

## Parameters

- *Row* \[out\]  
   On entry, a pointer to a [**MIB\_IPFORWARD\_ROW2**](mib-ipforward-row2.md) structure entry for an IP route entry.

   On return, the MIB\_IPFORWARD\_ROW2 structure that this parameter points to is initialized with default values for an IP route entry.

## Return value

None

## Remarks

Your driver must use the **InitializeIpForwardEntry** function to initialize the members of a [**MIB\_IPFORWARD\_ROW2**](mib-ipforward-row2.md) structure entry with default values for an IP route entry for later use with the [**CreateIpForwardEntry2**](createipforwardentry2.md) function.

On input, your driver must pass **InitializeIpForwardEntry** a new MIB\_IPFORWARD\_ROW2 structure to initialize.

On output, the members of the MIB\_IPFORWARD\_ROW2 structure that the *Row* parameter points to are initialized as follows.

- **ValidLifetime** and **PreferredLifetime**  
   Set to an infinite value,

- **Loopback**, **AutoconfigureAddress**, **Publish**, and **Immortal**  
   Set to **TRUE**.

- **SitePrefixLength**, **Metric**, and **Protocol**  
   Set to illegal values.

- All other members  
   Set to zero.

After a driver calls **InitializeIpForwardEntry**, the driver can then change the members in the MIB\_IPFORWARD\_ROW2 entry that it wants to modify, and then call the **CreateIpForwardEntry2** to add the new IP route entry to the local computer.

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
<td><p>&lt; DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also

[**CreateIpForwardEntry2**](createipforwardentry2.md)

[**DeleteIpForwardEntry2**](deleteipforwardentry2.md)

[**GetBestRoute2**](getbestroute2.md)

[**GetIpForwardEntry2**](getipforwardentry2.md)

[**GetIpForwardTable2**](getipforwardtable2.md)

[**MIB\_IPFORWARD\_ROW2**](mib-ipforward-row2.md)

[**MIB\_IPFORWARD\_TABLE2**](mib-ipforward-table2.md)

[**NotifyRouteChange2**](notifyroutechange2.md)

[**SetIpForwardEntry2**](setipforwardentry2.md)
