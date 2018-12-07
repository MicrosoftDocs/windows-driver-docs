---
title: Connections and File Structure Locking
description: Connections and File Structure Locking
ms.assetid: 7286a34f-db8f-4b0a-ab7f-674b9dc641a8
keywords:
- locking WDK RDBSS
- per-device object tables WDK RDBSS
- exclusive locks WDK RDBSS
- reference counts WDK RDBSS
- table-per-NET_ROOT structure WDK RDBSS
- data structures WDK file systems
- RDBSS WDK file systems , connection and file structures
- Redirected Drive Buffering Subsystem WDK file systems , connection and file structures
- connection structures WDK RDBSS
- file structures WDK RDBSS
- structures WDK RDBSS
- connection information WDK RDBSS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Connections and File Structure Locking


## <span id="ddk_connections_and_file_structure_locking_if"></span><span id="DDK_CONNECTIONS_AND_FILE_STRUCTURE_LOCKING_IF"></span>


For locking purposes, there are two levels of lookup tables used:

-   A per-device object table for SRV\_CALL and NET\_ROOT structures (prefix table)

-   A table-per-NET\_ROOT structure for FCB structures (FCB table)

These separate tables allow directory operations on different NET\_ROOT structures to be almost completely non-interfering once the connections are established. Directory operations on the same NET\_ROOT structure do interfere slightly, however. The following table describes what locks are needed for specific operations:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Operation</th>
<th align="left">Data types</th>
<th align="left">Lock required</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Create or Finalize</p></td>
<td align="left"><p></p>
SRV_CALL
NET_ROOT
V_NET_ROOT</td>
<td align="left"><p>An exclusive lock on the NetName table (the TableLock field of RxContext-&gt;RxDeviceObject-&gt;pRxNetNameTable).</p></td>
</tr>
<tr class="even">
<td align="left"><p>Reference, Dereference, or Lookup</p></td>
<td align="left"><p></p>
SRV_CALL
NET_ROOT
V_NET_ROOT</td>
<td align="left"><p>A shared or exclusive lock on the NetName table (the TableLock field of RxContext-&gt;RxDeviceObject-&gt;pRxNetNameTable).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Create or Finalize</p></td>
<td align="left"><p></p>
FCB
SRV_OPEN
FOBX</td>
<td align="left"><p>An exclusive lock on the FCB table (the TableLock field of NET_ROOT-&gt;FcbTable).</p></td>
</tr>
<tr class="even">
<td align="left"><p>Reference, Dereference, or Lookup</p></td>
<td align="left"><p></p>
FCB
SRV_OPEN
FOBX</td>
<td align="left"><p>A shared or exclusive lock on the FCB table (the TableLock field of NET_ROOT-&gt;FcbTable).</p></td>
</tr>
</tbody>
</table>

 

Note that manipulations of SRV\_OPEN and FOBX data structures currently require the same lock as needed for manipulations of FCB data structures. This is simply a memory saving idea. Future versions of Windows may add another resource at the FCB level to remove this restriction so that a set of shared resources could be used to decrease the probability of a collision to an acceptably low level.

If you require both locks (FinalizeNetFcb, for example), you must take the lock on NetName table first and then the lock on the FCB table. You must release the locks in the opposite order.

The SRV\_CALL, NET\_ROOT, and V\_NET\_ROOT creation and finalization process is governed by the acquisition and release of the RDBSS lock on the NetName table.

The FCB creation and finalization process is governed by the acquisition and release of the lock on the NetName table associated with the NET\_ROOT structure.

The FOBX and SRVOPEN creation and finalization process is governed by the acquisition and release of the lock on the FCB table.

The following table summarizes the locks and the modes in which the locks need to be acquired for creation and finalization of the various data structures:

<table>
<colgroup>
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Type of Operation</th>
<th align="left">SRV_CALL</th>
<th align="left">NET_ROOT</th>
<th align="left">FCB</th>
<th align="left">SRV_OPEN</th>
<th align="left">FOBX</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Create</p></td>
<td align="left"><p>Exclusive lock on NetName table</p></td>
<td align="left"><p>Exclusive lock on NetName table</p></td>
<td align="left"><p>Exclusive lock on FCB table</p></td>
<td align="left"><p>Exclusive lock on FCB table</p></td>
<td align="left"><p>Exclusive lock on FCB table</p></td>
</tr>
<tr class="even">
<td align="left"><p>Finalize</p></td>
<td align="left"><p>Exclusive lock on NetName table</p></td>
<td align="left"><p>Exclusive lock on NetName table</p></td>
<td align="left"><p>Exclusive lock on FCB table</p></td>
<td align="left"><p>Exclusive lock on FCB table</p></td>
<td align="left"><p>Exclusive lock on FCB table</p></td>
</tr>
</tbody>
</table>

 

Referencing and dereferencing these data structures must adhere to certain conventions as well.

When the reference count associated with any of the data structures drops to 1 (the sole reference being held by the name table in most cases), the data structure is a potential candidate for finalization. The data structure can be either finalized immediately or it can be marked for scavenging. Both of these methods are implemented in RDBSS. When the locking requirements are met during dereferencing, the data structures are finalized immediately. The one exception to this is when delayed operation optimization is implemented (dereferencing the FCB structure, for example). Otherwise, the data structure is marked for scavenging.

A network mini-redirector should have an exclusive lock on the NetName table in order to call a finalization routine.

To execute a Create on one of these data structures, a network mini-redirector driver should do something similar to the following:

```cpp
    getshared();lookup();
    if (failed) {
        release(); getexclusive(); lookup();
            if ((failed) { create(); }
        }
    deref();
    release();
```

When you have successfully acquired the lock, insert the node into the table, release the lock, and then see if the server is available. If the server is available, set up the rest of the information and unblock anyone who is waiting on the same server (the SRV\_CALL or NET\_ROOT structures).

 

 




