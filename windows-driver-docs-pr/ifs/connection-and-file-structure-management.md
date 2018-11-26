---
title: Connection and File Structure Management
description: Connection and File Structure Management
ms.assetid: 3695cab3-6751-48ee-8b11-e70c2bceab29
keywords:
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

# Connection and File Structure Management


## <span id="ddk_connection_and_file_structure_management_if"></span><span id="DDK_CONNECTION_AND_FILE_STRUCTURE_MANAGEMENT_IF"></span>


There are six fundamental data structures used by RDBSS for managing connections and file structures. These data structures are used internally by RDBSS and by the various network mini-redirectors. There are two versions of these data structures. The network mini-redirector version contains fields that can be manipulated by a network mini-redirector driver. The network mini-redirector version of these data structures starts with the MRX\_ prefix. The RDBSS version contains additional fields that can only be manipulated by RDBSS.

These six fundamental data structures are as follows:

-   SRV\_CALL--server call context. This structure provides the abstraction for a remote server.

-   NET\_ROOT--net root. This structure abstracts a connection to a share.

-   V\_NET\_ROOT--view of net roots (also referred to as virtual netroots).

-   FCB--file control block. This structure represents an open file on a share.

-   SRV\_OPEN--server-side open context. This structure encapsulates an open handle on the server.

-   FOBX--file object extension. This structure is an RDBSS extension to the [**FILE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff545834) structure.

These data structures are organized in the following hierarchy:

```cpp
                SRV_CALL 
     FCB   <------> NET_ROOT
        SRV_OPEN  <---> V_NET_ROOT
            FOBX
                FILE_OBJECT
```

In response to kernel file system calls, RDBSS normally creates and finalizes for a network mini-redirector driver all of the previously mentioned structures except the FOBX structure. So, a network mini-redirector driver will normally only call a few of the RDBSS routines used for connection and file structure management. Most of these routines are called internally by RDBSS.

All of these data structures are reference counted. The reference counts on a data structure are as follows:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Data Structure</th>
<th align="left">Description of Reference Count</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>SRV_CALL</p></td>
<td align="left"><p>The number of NET_ROOT entries that point to SRV_CALL, plus some dynamic value.</p></td>
</tr>
<tr class="even">
<td align="left"><p>NET_ROOT</p></td>
<td align="left"><p>The number of FCB entries and V_NET_ROOT entries that point to NET_ROOT, plus some dynamic value.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>V_NET_ROOT</p></td>
<td align="left"><p>The number of SRV_OPEN entries that point to V_NET_ROOT, plus some dynamic value.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FCB</p></td>
<td align="left"><p>The number of SRV_OPEN entries that point to FCB, plus some dynamic value.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SRV_OPEN</p></td>
<td align="left"><p>The number of FOBX entries that point to SRV_OPEN, plus some dynamic value.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FOBX</p></td>
<td align="left"><p>Some dynamic value.</p></td>
</tr>
</tbody>
</table>

 

In each case, the dynamic value refers to the number of callers that have referenced the structure without dereferencing it. The static part of the reference count is maintained by the routines themselves. For example, [**RxCreateNetRoot**](https://msdn.microsoft.com/library/windows/hardware/ff554366) increments the reference count for the associated SRV\_CALL structure.

Reference calls and successful lookups increment the reference counts; dereference calls decrements the count. Create routine calls allocate a structure and set the reference count to 1.

The reference count associated with any data structure is at least 1 plus the number of instances of the data structure at the next lower level associated with it. For example, the reference count associated with a SRV\_CALL, which has two NET\_ROOTs associated with it, is at least 3. In addition to the references held by the RDBSS internal **NameTable** structures and the data structure at the next lower level, there are additional references that may have been acquired.

These restrictions ensure that a data structure at any given level cannot be finalized (released and the associated memory block freed) until all of the data structures at the next level below have been finalized or have released their references. For example, if a reference to an FCB is held, then it is safe to access the V\_NET\_ROOT, NET\_ROOT, and SRV\_CALL structures associated with it.

The two important abstractions used in the interface between the network mini-redirectors and RDBSS are SRV\_CALL and NET\_ROOT structures. A SRV\_CALL structure corresponds to the context associated with a server with which a connection has been established, and the NET\_ROOT structure corresponds to a share on a server (this could also be viewed as a portion of the namespace, which has been claimed by a network mini-redirector).

The creation of SRV\_CALL and NET\_ROOT structures typically involves at least one network round trip. To provide for asynchronous operations to continue, these operations are modeled as a two-phase activity. Each call-down to a network mini-redirector for creating a SRV\_CALL and a NET\_ROOT structure is accompanied by a call-up from the network mini-redirector to the RDBSS to notify the completion status of the request. Currently these are synchronous.

The creation of a SRV\_CALL structure is further complicated by the fact that the RDBSS must choose from a number of network mini-redirectors to establish a connection with a server. To provide the RDBSS with maximum flexibility in choosing the network mini-redirector that it wishes to deploy, the creation of a SRV\_CALL structure involves a third phase in which the RDBSS notifies the network mini-redirector of a winner. All of the losing network mini-redirectors destroy the associated context.

This section contains the following topics:

[The SRV\_CALL Structure](the-srv-call-structure.md)

[The NET\_ROOT Structure](the-net-root-structure.md)

[The V\_NET\_ROOT Structure](the-v-net-root-structure.md)

[The FCB Structure](the-fcb-structure.md)

[The SRV\_OPEN Structure](the-srv-open-structure.md)

[The FOBX Structure](the-fobx-structure.md)

[Connections and File Structure Locking](connections-and-file-structure-locking.md)

[Connection and File Control Block Management Routines](connection-and-file-control-block-management-routines.md)

 

 




