---
title: Prefix Table Management
description: Prefix Table Management
ms.assetid: a48ed460-fab9-4a6d-bd2f-454b4932ea61
keywords:
- RDBSS WDK file systems , prefix tables
- Redirected Drive Buffering Subsystem WDK file systems , prefix tables
- prefix tables WDK network redirectors
- names WDK RDBSS
- version stamps WDK RDBSS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Prefix Table Management


## <span id="ddk_prefix_table_management_if"></span><span id="DDK_PREFIX_TABLE_MANAGEMENT_IF"></span>


RDBSS defines data structures that enable use of prefix tables to catalog SRV\_CALL, NET\_ROOT, and V\_NET\_ROOT names.

The current implementation of name management in RDBSS uses a table that has the following components:

-   A queue of inserted names

-   A version stamp

-   A table lock resource that controls table access

-   A value that indicates whether name matches are case insensitive

-   A bucket of hash value entries for this prefix table

The table lock resource is used in the normal way: shared for lookup operations, exclusive for change operations.

The version stamp changes with each change. The reason for the queue is that the prefix table package allows multiple callers to be enumerating at a time. The queue of inserted names and version stamp allow multiple callers to be enumerating simultaneously. The queue could be used as a faster lookup for file names, but the prefix table is definitely the correct approach for NET\_ROOT structures.

These prefix table management routines are used internally by RDBSS in response to a call from MUP to claim a name or to form the create path for a NET\_ROOT structure. These RDBSS prefix table management routines can also be used by network mini-redirectors, as long as the appropriate lock is acquired before accessing the table and the lock is released when work is completed. The normal use by a driver would be as follows:

-   Acquire a shared lock by calling **RxAcquirePrefixTableLockShared**.

-   Look up a name by calling [**RxPrefixTableLookupName**](https://msdn.microsoft.com/library/windows/hardware/ff554632).

-   Release the shared lock by calling **RxReleasePrefixTableLock**.

Note that certain routines are implemented only on Windows XP and previous versions of Windows. [**RxPrefixTableLookupName**](https://msdn.microsoft.com/library/windows/hardware/ff554632) is the only prefix table management routine implemented on all versions of Windows

The RDBSS prefix table management routines include the following:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Routine</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554595" data-raw-source="[&lt;strong&gt;RxpAcquirePrefixTableLockExclusive&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554595)"><strong>RxpAcquirePrefixTableLockExclusive</strong></a></p></td>
<td align="left"><p>This routine acquires an exclusive lock on a prefix table used to catalog SRV_CALL and NET_ROOT names.</p>
<p>This routine is only available on Windows XP and Windows 2000. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554598" data-raw-source="[&lt;strong&gt;RxpAcquirePrefixTableLockShared&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554598)"><strong>RxpAcquirePrefixTableLockShared</strong></a></p></td>
<td align="left"><p>This routine acquires a shared lock on a prefix table used to catalog SRV_CALL and NET_ROOT names.</p>
<p>This routine is only available on Windows XP and Windows 2000. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554632" data-raw-source="[&lt;strong&gt;RxPrefixTableLookupName&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554632)"><strong>RxPrefixTableLookupName</strong></a></p></td>
<td align="left"><p>The routine looks up a name in a prefix table used to catalog SRV_CALL and NET_ROOT names and converts from the underlying pointer to the containing structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554637" data-raw-source="[&lt;strong&gt;RxpReleasePrefixTableLock&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554637)"><strong>RxpReleasePrefixTableLock</strong></a></p></td>
<td align="left"><p>This routine releases a lock on a prefix table used to catalog SRV_CALL and NET_ROOT names.</p>
<p>This routine is only available on Windows XP and Windows 2000. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
</tbody>
</table>

 

Starting with Windows Server 2003, the routines mentioned in the previous table, except [**RxPrefixTableLookupName**](https://msdn.microsoft.com/library/windows/hardware/ff554632), are replaced by macros.The following macros are defined that call the prefix table routines with fewer parameters.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Macro</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>RxAcquirePrefixTableLockExclusive</strong> (<em>TABLE</em>, <em>WAIT</em>)</p></td>
<td align="left"><p>This macro acquires the prefix table lock in exclusive mode for change operations.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RxAcquirePrefixTableLockShared</strong> (<em>TABLE</em>, <em>WAIT</em>)</p></td>
<td align="left"><p>This macro acquires the prefix table lock in shared mode for lookup operations.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>RxIsPrefixTableLockAcquired</strong> (<em>TABLE</em>)</p></td>
<td align="left"><p>This macro indicates if the prefix table lock was acquired in either exclusive or shared mode.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RxIsPrefixTableLockExclusive</strong> (<em>TABLE</em>)</p></td>
<td align="left"><p>This macro indicates if the prefix table lock was acquired in exclusive mode.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>RxReleasePrefixTableLock</strong> (<em>TABLE</em>)</p></td>
<td align="left"><p>This macro frees the prefix table lock.</p></td>
</tr>
</tbody>
</table>

 

 

 




