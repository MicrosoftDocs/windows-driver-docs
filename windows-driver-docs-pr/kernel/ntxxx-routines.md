---
title: NtXxx Routines
author: windows-driver-content
description: NtXxx Routines
ms.assetid: 71db6fa6-d1f8-4aed-9de1-bba1f6cee1ce
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
<td><p>[<strong>ZwAllocateLocallyUniqueId</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566415)</p></td>
</tr>
<tr class="even">
<td><p>NtAllocateVirtualMemory</p></td>
<td><p>[<strong>ZwAllocateVirtualMemory</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566416)</p></td>
</tr>
<tr class="odd">
<td><p>NtClose</p></td>
<td><p>[<strong>ZwClose</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566417)</p></td>
</tr>
<tr class="even">
<td><p>NtCommitComplete</p></td>
<td><p>[<strong>ZwCommitComplete</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566418)</p></td>
</tr>
<tr class="odd">
<td><p>NtCommitEnlistment</p></td>
<td><p>[<strong>ZwCommitEnlistment</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566419)</p></td>
</tr>
<tr class="even">
<td><p>NtCommitTransaction</p></td>
<td><p>[<strong>ZwCommitTransaction</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566420)</p></td>
</tr>
<tr class="odd">
<td><p>NtCreateDirectoryObject</p></td>
<td><p>[<strong>ZwCreateDirectoryObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566421)</p></td>
</tr>
<tr class="even">
<td><p>NtCreateEnlistment</p></td>
<td><p>[<strong>ZwCreateEnlistment</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566422)</p></td>
</tr>
<tr class="odd">
<td><p>NtCreateEvent</p></td>
<td><p>[<strong>ZwCreateEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566423)</p></td>
</tr>
<tr class="even">
<td><p>NtCreateFile</p></td>
<td><p>[<strong>ZwCreateFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566424)</p></td>
</tr>
<tr class="odd">
<td><p>NtCreateKey</p></td>
<td><p>[<strong>ZwCreateKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566425)</p></td>
</tr>
<tr class="even">
<td><p>NtCreateResourceManager</p></td>
<td><p>[<strong>ZwCreateResourceManager</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566427)</p></td>
</tr>
<tr class="odd">
<td><p>NtCreateSection</p></td>
<td><p>[<strong>ZwCreateSection</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566428)</p></td>
</tr>
<tr class="even">
<td><p>NtCreateTransaction</p></td>
<td><p>[<strong>ZwCreateTransaction</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566429)</p></td>
</tr>
<tr class="odd">
<td><p>NtCreateTransactionManager</p></td>
<td><p>[<strong>ZwCreateTransactionManager</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566430)</p></td>
</tr>
<tr class="even">
<td><p>NtCurrentProcess</p></td>
<td><p>[<strong>ZwCurrentProcess</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566431)</p></td>
</tr>
<tr class="odd">
<td><p>NtCurrentThread</p></td>
<td><p>[<strong>ZwCurrentThread</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566434)</p></td>
</tr>
<tr class="even">
<td><p>NtDeleteFile</p></td>
<td><p>[<strong>ZwDeleteFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566435)</p></td>
</tr>
<tr class="odd">
<td><p>NtDeleteKey</p></td>
<td><p>[<strong>ZwDeleteKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566437)</p></td>
</tr>
<tr class="even">
<td><p>NtDeleteValueKey</p></td>
<td><p>[<strong>ZwDeleteValueKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566439)</p></td>
</tr>
<tr class="odd">
<td><p>NtDeviceIoControlFile</p></td>
<td><p>[<strong>ZwDeviceIoControlFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566441)</p></td>
</tr>
<tr class="even">
<td><p>NtDuplicateObject</p></td>
<td><p>[<strong>ZwDuplicateObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566445)</p></td>
</tr>
<tr class="odd">
<td><p>NtDuplicateToken</p></td>
<td><p>[<strong>ZwDuplicateToken</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566446)</p></td>
</tr>
<tr class="even">
<td><p>NtEnumerateKey</p></td>
<td><p>[<strong>ZwEnumerateKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566447)</p></td>
</tr>
<tr class="odd">
<td><p>NtEnumerateTransactionObject</p></td>
<td><p>[<strong>ZwEnumerateTransactionObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566450)</p></td>
</tr>
<tr class="even">
<td><p>NtEnumerateValueKey</p></td>
<td><p>[<strong>ZwEnumerateValueKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566453)</p></td>
</tr>
<tr class="odd">
<td><p>NtFlushBuffersFile</p></td>
<td><p>[<strong>ZwFlushBuffersFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566454)</p></td>
</tr>
<tr class="even">
<td><p>NtFlushBuffersFileEx</p></td>
<td><p>[<strong>ZwFlushBuffersFileEx</strong>](https://msdn.microsoft.com/library/windows/hardware/hh967720)</p></td>
</tr>
<tr class="odd">
<td><p>NtFlushKey</p></td>
<td><p>[<strong>ZwFlushKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566457)</p></td>
</tr>
<tr class="even">
<td><p>NtFlushVirtualMemory</p></td>
<td><p>[<strong>ZwFlushVirtualMemory</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566458)</p></td>
</tr>
<tr class="odd">
<td><p>NtFreeVirtualMemory</p></td>
<td><p>[<strong>ZwFreeVirtualMemory</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566460)</p></td>
</tr>
<tr class="even">
<td><p>NtFsControlFile</p></td>
<td><p>[<strong>ZwFsControlFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566462)</p></td>
</tr>
<tr class="odd">
<td><p>NtGetNotificationResourceManager</p></td>
<td><p>[<strong>ZwGetNotificationResourceManager</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566467)</p></td>
</tr>
<tr class="even">
<td><p>NtLoadDriver</p></td>
<td><p>[<strong>ZwLoadDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566470)</p></td>
</tr>
<tr class="odd">
<td><p>NtLockFile</p></td>
<td><p>[<strong>ZwLockFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566474)</p></td>
</tr>
<tr class="even">
<td><p>NtMakeTemporaryObject</p></td>
<td><p>[<strong>ZwMakeTemporaryObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566477)</p></td>
</tr>
<tr class="odd">
<td><p>NtMapViewOfSection</p></td>
<td><p>[<strong>ZwMapViewOfSection</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566481)</p></td>
</tr>
<tr class="even">
<td><p>NtNotifyChangeKey</p></td>
<td><p>[<strong>ZwNotifyChangeKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566488)</p></td>
</tr>
<tr class="odd">
<td><p>NtOpenDirectoryObject</p></td>
<td><p>[<strong>ZwOpenDirectoryObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566492)</p></td>
</tr>
<tr class="even">
<td><p>NtOpenEnlistment</p></td>
<td><p>[<strong>ZwOpenEnlistment</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567008)</p></td>
</tr>
<tr class="odd">
<td><p>NtOpenEvent</p></td>
<td><p>[<strong>ZwOpenEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567009)</p></td>
</tr>
<tr class="even">
<td><p>NtOpenFile</p></td>
<td><p>[<strong>ZwOpenFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567011)</p></td>
</tr>
<tr class="odd">
<td><p>NtOpenKey</p></td>
<td><p>[<strong>ZwOpenKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567014)</p></td>
</tr>
<tr class="even">
<td><p>NtOpenProcess</p></td>
<td><p>[<strong>ZwOpenProcess</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567022)</p></td>
</tr>
<tr class="odd">
<td><p>NtOpenProcessTokenEx</p></td>
<td><p>[<strong>ZwOpenProcessTokenEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567024)</p></td>
</tr>
<tr class="even">
<td><p>NtOpenResourceManager</p></td>
<td><p>[<strong>ZwOpenResourceManager</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567026)</p></td>
</tr>
<tr class="odd">
<td><p>NtOpenSection</p></td>
<td><p>[<strong>ZwOpenSection</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567029)</p></td>
</tr>
<tr class="even">
<td><p>NtOpenSymbolicLinkObject</p></td>
<td><p>[<strong>ZwOpenSymbolicLinkObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567030)</p></td>
</tr>
<tr class="odd">
<td><p>NtOpenThreadTokenEx</p></td>
<td><p>[<strong>ZwOpenThreadTokenEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567032)</p></td>
</tr>
<tr class="even">
<td><p>NtOpenTransaction</p></td>
<td><p>[<strong>ZwOpenTransaction</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567033)</p></td>
</tr>
<tr class="odd">
<td><p>NtOpenTransactionManager</p></td>
<td><p>[<strong>ZwOpenTransactionManager</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567035)</p></td>
</tr>
<tr class="even">
<td><p>NtPowerInformation</p></td>
<td><p>[<strong>ZwPowerInformation</strong>](https://msdn.microsoft.com/library/windows/hardware/dn957454)</p></td>
</tr>
<tr class="odd">
<td><p>NtPrepareComplete</p></td>
<td><p>[<strong>ZwPrepareComplete</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567037)</p></td>
</tr>
<tr class="even">
<td><p>NtPrepareEnlistment</p></td>
<td><p>[<strong>ZwPrepareEnlistment</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567039)</p></td>
</tr>
<tr class="odd">
<td><p>NtPrePrepareComplete</p></td>
<td><p>[<strong>ZwPrePrepareComplete</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567040)</p></td>
</tr>
<tr class="even">
<td><p>NtPrePrepareEnlistment</p></td>
<td><p>[<strong>ZwPrePrepareEnlistment</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567044)</p></td>
</tr>
<tr class="odd">
<td><p>NtQueryDirectoryFile</p></td>
<td><p>[<strong>ZwQueryDirectoryFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567047)</p></td>
</tr>
<tr class="even">
<td><p>NtQueryFullAttributesFile</p></td>
<td><p>[<strong>ZwQueryFullAttributesFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567049)</p></td>
</tr>
<tr class="odd">
<td><p>NtQueryInformationEnlistment</p></td>
<td><p>[<strong>ZwQueryInformationEnlistment</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567051)</p></td>
</tr>
<tr class="even">
<td><p>NtQueryInformationFile</p></td>
<td><p>[<strong>ZwQueryInformationFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567052)</p></td>
</tr>
<tr class="odd">
<td><p>NtQueryInformationResourceManager</p></td>
<td><p>[<strong>ZwQueryInformationResourceManager</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567054)</p></td>
</tr>
<tr class="even">
<td><p>NtQueryInformationToken</p></td>
<td><p>[<strong>ZwQueryInformationToken</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567055)</p></td>
</tr>
<tr class="odd">
<td><p>NtQueryInformationTransaction</p></td>
<td><p>[<strong>ZwQueryInformationTransaction</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567057)</p></td>
</tr>
<tr class="even">
<td><p>NtQueryInformationTransactionManager</p></td>
<td><p>[<strong>ZwQueryInformationTransactionManager</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567058)</p></td>
</tr>
<tr class="odd">
<td><p>NtQueryKey</p></td>
<td><p>[<strong>ZwQueryKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567060)</p></td>
</tr>
<tr class="even">
<td><p>NtQueryObject</p></td>
<td><p>[<strong>ZwQueryObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567062)</p></td>
</tr>
<tr class="odd">
<td><p>NtQueryQuotaInformationFile</p></td>
<td><p>[<strong>ZwQueryQuotaInformationFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567064)</p></td>
</tr>
<tr class="even">
<td><p>NtQuerySecurityObject</p></td>
<td><p>[<strong>ZwQuerySecurityObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567066)</p></td>
</tr>
<tr class="odd">
<td><p>NtQuerySecurityObject</p></td>
<td><p>[<strong>ZwQuerySymbolicLinkObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567068)</p></td>
</tr>
<tr class="even">
<td><p>NtQueryValueKey</p></td>
<td><p>[<strong>ZwQueryValueKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567069)</p></td>
</tr>
<tr class="odd">
<td><p>NtQueryVirtualMemory</p></td>
<td><p>[<strong>ZwQueryVirtualMemory</strong>](https://msdn.microsoft.com/library/windows/hardware/dn957455)</p></td>
</tr>
<tr class="even">
<td><p>NtQueryVolumeInformationFile</p></td>
<td><p>[<strong>ZwQueryVolumeInformationFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567070)</p></td>
</tr>
<tr class="odd">
<td><p>NtReadFile</p></td>
<td><p>[<strong>ZwReadFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567072)</p></td>
</tr>
<tr class="even">
<td><p>NtReadOnlyEnlistment</p></td>
<td><p>[<strong>ZwReadOnlyEnlistment</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567074)</p></td>
</tr>
<tr class="odd">
<td><p>NtReadOnlyEnlistment</p></td>
<td><p>[<strong>ZwRecoverEnlistment</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567075)</p></td>
</tr>
<tr class="even">
<td><p>NtRecoverResourceManager</p></td>
<td><p>[<strong>ZwRecoverResourceManager</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567078)</p></td>
</tr>
<tr class="odd">
<td><p>NtRecoverTransactionManager</p></td>
<td><p>[<strong>ZwRecoverTransactionManager</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567079)</p></td>
</tr>
<tr class="even">
<td><p>NtRollbackComplete</p></td>
<td><p>[<strong>ZwRollbackComplete</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567081)</p></td>
</tr>
<tr class="odd">
<td><p>NtRollbackEnlistment</p></td>
<td><p>[<strong>ZwRollbackEnlistment</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567083)</p></td>
</tr>
<tr class="even">
<td><p>NtRollbackTransaction</p></td>
<td><p>[<strong>ZwRollbackTransaction</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567086)</p></td>
</tr>
<tr class="odd">
<td><p>NtRollforwardTransactionManager</p></td>
<td><p>[<strong>ZwRollforwardTransactionManager</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567089)</p></td>
</tr>
<tr class="even">
<td><p>NtSetEvent</p></td>
<td><p>[<strong>ZwSetEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567092)</p></td>
</tr>
<tr class="odd">
<td><p>NtSetInformationEnlistment</p></td>
<td><p>[<strong>ZwSetInformationEnlistment</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567094)</p></td>
</tr>
<tr class="even">
<td><p>NtSetInformationFile</p></td>
<td><p>[<strong>ZwSetInformationFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567096)</p></td>
</tr>
<tr class="odd">
<td><p>NtSetInformationResourceManager</p></td>
<td><p>[<strong>ZwSetInformationResourceManager</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567098)</p></td>
</tr>
<tr class="even">
<td><p>NtSetInformationThread</p></td>
<td><p>[<strong>ZwSetInformationThread</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567101)</p></td>
</tr>
<tr class="odd">
<td><p>NtSetInformationToken</p></td>
<td><p>[<strong>ZwSetInformationToken</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567102)</p></td>
</tr>
<tr class="even">
<td><p>NtSetInformationTransaction</p></td>
<td><p>[<strong>ZwSetInformationTransaction</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567104)</p></td>
</tr>
<tr class="odd">
<td><p>NtSetQuotaInformationFile</p></td>
<td><p>[<strong>ZwSetQuotaInformationFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567105)</p></td>
</tr>
<tr class="even">
<td><p>NtSetSecurityObject</p></td>
<td><p>[<strong>ZwSetSecurityObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567106)</p></td>
</tr>
<tr class="odd">
<td><p>NtSetValueKey</p></td>
<td><p>[<strong>ZwSetValueKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567109)</p></td>
</tr>
<tr class="even">
<td><p>NtSetVolumeInformationFile</p></td>
<td><p>[<strong>ZwSetVolumeInformationFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567112)</p></td>
</tr>
<tr class="odd">
<td><p>NtSinglePhaseReject</p></td>
<td><p>[<strong>ZwSinglePhaseReject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567113)</p></td>
</tr>
<tr class="even">
<td><p>NtTerminateProcess</p></td>
<td><p>[<strong>ZwTerminateProcess</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567115)</p></td>
</tr>
<tr class="odd">
<td><p>NtUnloadDriver</p></td>
<td><p>[<strong>ZwUnloadDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567117)</p></td>
</tr>
<tr class="even">
<td><p>NtUnlockFile</p></td>
<td><p>[<strong>ZwUnlockFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567118)</p></td>
</tr>
<tr class="odd">
<td><p>NtUnmapViewOfSection</p></td>
<td><p>[<strong>ZwUnmapViewOfSection</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567119)</p></td>
</tr>
<tr class="even">
<td><p>NtWaitForSingleObject</p></td>
<td><p>[<strong>ZwWaitForSingleObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567120)</p></td>
</tr>
<tr class="odd">
<td><p>NtWriteFile</p></td>
<td><p>[<strong>ZwWriteFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567121)</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20NtXxx%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


