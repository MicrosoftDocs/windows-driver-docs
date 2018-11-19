---
title: NtXxx Routines
description: NtXxx Routines
ms.assetid: 71db6fa6-d1f8-4aed-9de1-bba1f6cee1ce
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# NtXxx Routines


This section describes the **Nt*Xxx*** versions of the Windows Native System Services routines. Most native system services routines have two versions, one of which has a name begins with the prefix **Nt**; the other version has a name that begins with the prefix **Zw**. For example, calls to [**NtCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff556465) and [**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424) perform similar operations and are, in fact, serviced by the same kernel-mode system routine.

For calls from kernel-mode drivers, the **Nt*Xxx*** and **Zw*Xxx*** versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the **Nt*Xxx*** and **Zw*Xxx*** versions of a routine, see [Using Nt and Zw Versions of the Native System Services Routines](using-nt-and-zw-versions-of-the-native-system-services-routines.md).

The following table summarizes the **Nt*Xxx*** and **Zw*Xxx*** versions of the routines:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>NtXxx</th>
<th>ZwXxx</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>NtAllocateLocallyUniqueId</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566415" data-raw-source="[&lt;strong&gt;ZwAllocateLocallyUniqueId&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566415)"><strong>ZwAllocateLocallyUniqueId</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtAllocateVirtualMemory</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566416" data-raw-source="[&lt;strong&gt;ZwAllocateVirtualMemory&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566416)"><strong>ZwAllocateVirtualMemory</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtClose</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566417" data-raw-source="[&lt;strong&gt;ZwClose&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566417)"><strong>ZwClose</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtCommitComplete</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566418" data-raw-source="[&lt;strong&gt;ZwCommitComplete&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566418)"><strong>ZwCommitComplete</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtCommitEnlistment</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566419" data-raw-source="[&lt;strong&gt;ZwCommitEnlistment&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566419)"><strong>ZwCommitEnlistment</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtCommitTransaction</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566420" data-raw-source="[&lt;strong&gt;ZwCommitTransaction&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566420)"><strong>ZwCommitTransaction</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtCreateDirectoryObject</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566421" data-raw-source="[&lt;strong&gt;ZwCreateDirectoryObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566421)"><strong>ZwCreateDirectoryObject</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtCreateEnlistment</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566422" data-raw-source="[&lt;strong&gt;ZwCreateEnlistment&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566422)"><strong>ZwCreateEnlistment</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtCreateEvent</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566423" data-raw-source="[&lt;strong&gt;ZwCreateEvent&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566423)"><strong>ZwCreateEvent</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtCreateFile</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566424" data-raw-source="[&lt;strong&gt;ZwCreateFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566424)"><strong>ZwCreateFile</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtCreateKey</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566425" data-raw-source="[&lt;strong&gt;ZwCreateKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566425)"><strong>ZwCreateKey</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtCreateResourceManager</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566427" data-raw-source="[&lt;strong&gt;ZwCreateResourceManager&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566427)"><strong>ZwCreateResourceManager</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtCreateSection</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566428" data-raw-source="[&lt;strong&gt;ZwCreateSection&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566428)"><strong>ZwCreateSection</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtCreateTransaction</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566429" data-raw-source="[&lt;strong&gt;ZwCreateTransaction&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566429)"><strong>ZwCreateTransaction</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtCreateTransactionManager</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566430" data-raw-source="[&lt;strong&gt;ZwCreateTransactionManager&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566430)"><strong>ZwCreateTransactionManager</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtCurrentProcess</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566431" data-raw-source="[&lt;strong&gt;ZwCurrentProcess&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566431)"><strong>ZwCurrentProcess</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtCurrentThread</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566434" data-raw-source="[&lt;strong&gt;ZwCurrentThread&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566434)"><strong>ZwCurrentThread</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtDeleteFile</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566435" data-raw-source="[&lt;strong&gt;ZwDeleteFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566435)"><strong>ZwDeleteFile</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtDeleteKey</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566437" data-raw-source="[&lt;strong&gt;ZwDeleteKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566437)"><strong>ZwDeleteKey</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtDeleteValueKey</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566439" data-raw-source="[&lt;strong&gt;ZwDeleteValueKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566439)"><strong>ZwDeleteValueKey</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtDeviceIoControlFile</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566441" data-raw-source="[&lt;strong&gt;ZwDeviceIoControlFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566441)"><strong>ZwDeviceIoControlFile</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtDuplicateObject</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566445" data-raw-source="[&lt;strong&gt;ZwDuplicateObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566445)"><strong>ZwDuplicateObject</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtDuplicateToken</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566446" data-raw-source="[&lt;strong&gt;ZwDuplicateToken&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566446)"><strong>ZwDuplicateToken</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtEnumerateKey</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566447" data-raw-source="[&lt;strong&gt;ZwEnumerateKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566447)"><strong>ZwEnumerateKey</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtEnumerateTransactionObject</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566450" data-raw-source="[&lt;strong&gt;ZwEnumerateTransactionObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566450)"><strong>ZwEnumerateTransactionObject</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtEnumerateValueKey</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566453" data-raw-source="[&lt;strong&gt;ZwEnumerateValueKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566453)"><strong>ZwEnumerateValueKey</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtFlushBuffersFile</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566454" data-raw-source="[&lt;strong&gt;ZwFlushBuffersFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566454)"><strong>ZwFlushBuffersFile</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtFlushBuffersFileEx</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh967720" data-raw-source="[&lt;strong&gt;ZwFlushBuffersFileEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh967720)"><strong>ZwFlushBuffersFileEx</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtFlushKey</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566457" data-raw-source="[&lt;strong&gt;ZwFlushKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566457)"><strong>ZwFlushKey</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtFlushVirtualMemory</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566458" data-raw-source="[&lt;strong&gt;ZwFlushVirtualMemory&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566458)"><strong>ZwFlushVirtualMemory</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtFreeVirtualMemory</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566460" data-raw-source="[&lt;strong&gt;ZwFreeVirtualMemory&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566460)"><strong>ZwFreeVirtualMemory</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtFsControlFile</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566462" data-raw-source="[&lt;strong&gt;ZwFsControlFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566462)"><strong>ZwFsControlFile</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtGetNotificationResourceManager</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566467" data-raw-source="[&lt;strong&gt;ZwGetNotificationResourceManager&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566467)"><strong>ZwGetNotificationResourceManager</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtLoadDriver</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566470" data-raw-source="[&lt;strong&gt;ZwLoadDriver&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566470)"><strong>ZwLoadDriver</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtLockFile</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566474" data-raw-source="[&lt;strong&gt;ZwLockFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566474)"><strong>ZwLockFile</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtMakeTemporaryObject</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566477" data-raw-source="[&lt;strong&gt;ZwMakeTemporaryObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566477)"><strong>ZwMakeTemporaryObject</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtMapViewOfSection</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566481" data-raw-source="[&lt;strong&gt;ZwMapViewOfSection&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566481)"><strong>ZwMapViewOfSection</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtNotifyChangeKey</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566488" data-raw-source="[&lt;strong&gt;ZwNotifyChangeKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566488)"><strong>ZwNotifyChangeKey</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtOpenDirectoryObject</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566492" data-raw-source="[&lt;strong&gt;ZwOpenDirectoryObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566492)"><strong>ZwOpenDirectoryObject</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtOpenEnlistment</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567008" data-raw-source="[&lt;strong&gt;ZwOpenEnlistment&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567008)"><strong>ZwOpenEnlistment</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtOpenEvent</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567009" data-raw-source="[&lt;strong&gt;ZwOpenEvent&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567009)"><strong>ZwOpenEvent</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtOpenFile</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567011" data-raw-source="[&lt;strong&gt;ZwOpenFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567011)"><strong>ZwOpenFile</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtOpenKey</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567014" data-raw-source="[&lt;strong&gt;ZwOpenKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567014)"><strong>ZwOpenKey</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtOpenProcess</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567022" data-raw-source="[&lt;strong&gt;ZwOpenProcess&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567022)"><strong>ZwOpenProcess</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtOpenProcessTokenEx</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567024" data-raw-source="[&lt;strong&gt;ZwOpenProcessTokenEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567024)"><strong>ZwOpenProcessTokenEx</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtOpenResourceManager</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567026" data-raw-source="[&lt;strong&gt;ZwOpenResourceManager&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567026)"><strong>ZwOpenResourceManager</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtOpenSection</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567029" data-raw-source="[&lt;strong&gt;ZwOpenSection&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567029)"><strong>ZwOpenSection</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtOpenSymbolicLinkObject</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567030" data-raw-source="[&lt;strong&gt;ZwOpenSymbolicLinkObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567030)"><strong>ZwOpenSymbolicLinkObject</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtOpenThreadTokenEx</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567032" data-raw-source="[&lt;strong&gt;ZwOpenThreadTokenEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567032)"><strong>ZwOpenThreadTokenEx</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtOpenTransaction</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567033" data-raw-source="[&lt;strong&gt;ZwOpenTransaction&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567033)"><strong>ZwOpenTransaction</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtOpenTransactionManager</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567035" data-raw-source="[&lt;strong&gt;ZwOpenTransactionManager&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567035)"><strong>ZwOpenTransactionManager</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtPowerInformation</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/dn957454" data-raw-source="[&lt;strong&gt;ZwPowerInformation&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn957454)"><strong>ZwPowerInformation</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtPrepareComplete</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567037" data-raw-source="[&lt;strong&gt;ZwPrepareComplete&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567037)"><strong>ZwPrepareComplete</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtPrepareEnlistment</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567039" data-raw-source="[&lt;strong&gt;ZwPrepareEnlistment&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567039)"><strong>ZwPrepareEnlistment</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtPrePrepareComplete</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567040" data-raw-source="[&lt;strong&gt;ZwPrePrepareComplete&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567040)"><strong>ZwPrePrepareComplete</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtPrePrepareEnlistment</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567044" data-raw-source="[&lt;strong&gt;ZwPrePrepareEnlistment&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567044)"><strong>ZwPrePrepareEnlistment</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtQueryDirectoryFile</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567047" data-raw-source="[&lt;strong&gt;ZwQueryDirectoryFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567047)"><strong>ZwQueryDirectoryFile</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtQueryFullAttributesFile</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567049" data-raw-source="[&lt;strong&gt;ZwQueryFullAttributesFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567049)"><strong>ZwQueryFullAttributesFile</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtQueryInformationEnlistment</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567051" data-raw-source="[&lt;strong&gt;ZwQueryInformationEnlistment&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567051)"><strong>ZwQueryInformationEnlistment</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtQueryInformationFile</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567052" data-raw-source="[&lt;strong&gt;ZwQueryInformationFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567052)"><strong>ZwQueryInformationFile</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtQueryInformationResourceManager</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567054" data-raw-source="[&lt;strong&gt;ZwQueryInformationResourceManager&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567054)"><strong>ZwQueryInformationResourceManager</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtQueryInformationToken</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567055" data-raw-source="[&lt;strong&gt;ZwQueryInformationToken&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567055)"><strong>ZwQueryInformationToken</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtQueryInformationTransaction</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567057" data-raw-source="[&lt;strong&gt;ZwQueryInformationTransaction&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567057)"><strong>ZwQueryInformationTransaction</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtQueryInformationTransactionManager</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567058" data-raw-source="[&lt;strong&gt;ZwQueryInformationTransactionManager&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567058)"><strong>ZwQueryInformationTransactionManager</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtQueryKey</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567060" data-raw-source="[&lt;strong&gt;ZwQueryKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567060)"><strong>ZwQueryKey</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtQueryObject</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567062" data-raw-source="[&lt;strong&gt;ZwQueryObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567062)"><strong>ZwQueryObject</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtQueryQuotaInformationFile</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567064" data-raw-source="[&lt;strong&gt;ZwQueryQuotaInformationFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567064)"><strong>ZwQueryQuotaInformationFile</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtQuerySecurityObject</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567066" data-raw-source="[&lt;strong&gt;ZwQuerySecurityObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567066)"><strong>ZwQuerySecurityObject</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtQuerySecurityObject</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567068" data-raw-source="[&lt;strong&gt;ZwQuerySymbolicLinkObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567068)"><strong>ZwQuerySymbolicLinkObject</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtQueryValueKey</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567069" data-raw-source="[&lt;strong&gt;ZwQueryValueKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567069)"><strong>ZwQueryValueKey</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtQueryVirtualMemory</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/dn957455" data-raw-source="[&lt;strong&gt;ZwQueryVirtualMemory&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn957455)"><strong>ZwQueryVirtualMemory</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtQueryVolumeInformationFile</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567070" data-raw-source="[&lt;strong&gt;ZwQueryVolumeInformationFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567070)"><strong>ZwQueryVolumeInformationFile</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtReadFile</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567072" data-raw-source="[&lt;strong&gt;ZwReadFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567072)"><strong>ZwReadFile</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtReadOnlyEnlistment</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567074" data-raw-source="[&lt;strong&gt;ZwReadOnlyEnlistment&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567074)"><strong>ZwReadOnlyEnlistment</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtReadOnlyEnlistment</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567075" data-raw-source="[&lt;strong&gt;ZwRecoverEnlistment&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567075)"><strong>ZwRecoverEnlistment</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtRecoverResourceManager</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567078" data-raw-source="[&lt;strong&gt;ZwRecoverResourceManager&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567078)"><strong>ZwRecoverResourceManager</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtRecoverTransactionManager</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567079" data-raw-source="[&lt;strong&gt;ZwRecoverTransactionManager&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567079)"><strong>ZwRecoverTransactionManager</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtRollbackComplete</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567081" data-raw-source="[&lt;strong&gt;ZwRollbackComplete&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567081)"><strong>ZwRollbackComplete</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtRollbackEnlistment</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567083" data-raw-source="[&lt;strong&gt;ZwRollbackEnlistment&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567083)"><strong>ZwRollbackEnlistment</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtRollbackTransaction</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567086" data-raw-source="[&lt;strong&gt;ZwRollbackTransaction&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567086)"><strong>ZwRollbackTransaction</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtRollforwardTransactionManager</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567089" data-raw-source="[&lt;strong&gt;ZwRollforwardTransactionManager&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567089)"><strong>ZwRollforwardTransactionManager</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtSetEvent</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567092" data-raw-source="[&lt;strong&gt;ZwSetEvent&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567092)"><strong>ZwSetEvent</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtSetInformationEnlistment</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567094" data-raw-source="[&lt;strong&gt;ZwSetInformationEnlistment&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567094)"><strong>ZwSetInformationEnlistment</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtSetInformationFile</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567096" data-raw-source="[&lt;strong&gt;ZwSetInformationFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567096)"><strong>ZwSetInformationFile</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtSetInformationResourceManager</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567098" data-raw-source="[&lt;strong&gt;ZwSetInformationResourceManager&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567098)"><strong>ZwSetInformationResourceManager</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtSetInformationThread</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567101" data-raw-source="[&lt;strong&gt;ZwSetInformationThread&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567101)"><strong>ZwSetInformationThread</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtSetInformationToken</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567102" data-raw-source="[&lt;strong&gt;ZwSetInformationToken&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567102)"><strong>ZwSetInformationToken</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtSetInformationTransaction</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567104" data-raw-source="[&lt;strong&gt;ZwSetInformationTransaction&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567104)"><strong>ZwSetInformationTransaction</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtSetQuotaInformationFile</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567105" data-raw-source="[&lt;strong&gt;ZwSetQuotaInformationFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567105)"><strong>ZwSetQuotaInformationFile</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtSetSecurityObject</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567106" data-raw-source="[&lt;strong&gt;ZwSetSecurityObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567106)"><strong>ZwSetSecurityObject</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtSetValueKey</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567109" data-raw-source="[&lt;strong&gt;ZwSetValueKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567109)"><strong>ZwSetValueKey</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtSetVolumeInformationFile</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567112" data-raw-source="[&lt;strong&gt;ZwSetVolumeInformationFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567112)"><strong>ZwSetVolumeInformationFile</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtSinglePhaseReject</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567113" data-raw-source="[&lt;strong&gt;ZwSinglePhaseReject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567113)"><strong>ZwSinglePhaseReject</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtTerminateProcess</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567115" data-raw-source="[&lt;strong&gt;ZwTerminateProcess&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567115)"><strong>ZwTerminateProcess</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtUnloadDriver</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567117" data-raw-source="[&lt;strong&gt;ZwUnloadDriver&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567117)"><strong>ZwUnloadDriver</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtUnlockFile</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567118" data-raw-source="[&lt;strong&gt;ZwUnlockFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567118)"><strong>ZwUnlockFile</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtUnmapViewOfSection</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567119" data-raw-source="[&lt;strong&gt;ZwUnmapViewOfSection&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567119)"><strong>ZwUnmapViewOfSection</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtWaitForSingleObject</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567120" data-raw-source="[&lt;strong&gt;ZwWaitForSingleObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567120)"><strong>ZwWaitForSingleObject</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtWriteFile</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567121" data-raw-source="[&lt;strong&gt;ZwWriteFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567121)"><strong>ZwWriteFile</strong></a></p></td>
</tr>
</tbody>
</table>

 

 

 




