---
title: Prefix Table Management
description: Prefix Table Management
ms.assetid: a48ed460-fab9-4a6d-bd2f-454b4932ea61
keywords: ["RDBSS WDK file systems , prefix tables", "Redirected Drive Buffering Subsystem WDK file systems , prefix tables", "prefix tables WDK network redirectors", "names WDK RDBSS", "version stamps WDK RDBSS"]
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
<td align="left"><p>[<strong>RxpAcquirePrefixTableLockExclusive</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554595)</p></td>
<td align="left"><p>This routine acquires an exclusive lock on a prefix table used to catalog SRV_CALL and NET_ROOT names.</p>
<p>This routine is only available on Windows XP and Windows 2000. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxpAcquirePrefixTableLockShared</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554598)</p></td>
<td align="left"><p>This routine acquires a shared lock on a prefix table used to catalog SRV_CALL and NET_ROOT names.</p>
<p>This routine is only available on Windows XP and Windows 2000. This routine is used internally by RDBSS and should not be used by network mini-redirectors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxPrefixTableLookupName</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554632)</p></td>
<td align="left"><p>The routine looks up a name in a prefix table used to catalog SRV_CALL and NET_ROOT names and converts from the underlying pointer to the containing structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxpReleasePrefixTableLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554637)</p></td>
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Prefix%20Table%20Management%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




