---
title: NtXxx Routines
description: NtXxx Routines
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# NtXxx Routines


This section describes the **Nt*Xxx*** versions of the Windows Native System Services routines. Most native system services routines have two versions, one of which has a name begins with the prefix **Nt**; the other version has a name that begins with the prefix **Zw**. For example, calls to [**NtCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile) and [**ZwCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile) perform similar operations and are, in fact, serviced by the same kernel-mode system routine.

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
<td><p><a href="/windows-hardware/drivers/ddi/ntddk/nf-ntddk-zwallocatelocallyuniqueid" data-raw-source="[&lt;strong&gt;ZwAllocateLocallyUniqueId&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-zwallocatelocallyuniqueid)"><strong>ZwAllocateLocallyUniqueId</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtAllocateVirtualMemory</p></td>
<td><p><a href="/previous-versions/ff566416(v=vs.85)" data-raw-source="[&lt;strong&gt;ZwAllocateVirtualMemory&lt;/strong&gt;](/previous-versions/ff566416(v=vs.85))"><strong>ZwAllocateVirtualMemory</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtClose</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose" data-raw-source="[&lt;strong&gt;ZwClose&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose)"><strong>ZwClose</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtCommitComplete</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcommitcomplete" data-raw-source="[&lt;strong&gt;ZwCommitComplete&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcommitcomplete)"><strong>ZwCommitComplete</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtCommitEnlistment</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcommitenlistment" data-raw-source="[&lt;strong&gt;ZwCommitEnlistment&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcommitenlistment)"><strong>ZwCommitEnlistment</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtCommitTransaction</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcommittransaction" data-raw-source="[&lt;strong&gt;ZwCommitTransaction&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcommittransaction)"><strong>ZwCommitTransaction</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtCreateDirectoryObject</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatedirectoryobject" data-raw-source="[&lt;strong&gt;ZwCreateDirectoryObject&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatedirectoryobject)"><strong>ZwCreateDirectoryObject</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtCreateEnlistment</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreateenlistment" data-raw-source="[&lt;strong&gt;ZwCreateEnlistment&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreateenlistment)"><strong>ZwCreateEnlistment</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtCreateEvent</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwcreateevent" data-raw-source="[&lt;strong&gt;ZwCreateEvent&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwcreateevent)"><strong>ZwCreateEvent</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtCreateFile</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile" data-raw-source="[&lt;strong&gt;ZwCreateFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile)"><strong>ZwCreateFile</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtCreateKey</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatekey" data-raw-source="[&lt;strong&gt;ZwCreateKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatekey)"><strong>ZwCreateKey</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtCreateResourceManager</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreateresourcemanager" data-raw-source="[&lt;strong&gt;ZwCreateResourceManager&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreateresourcemanager)"><strong>ZwCreateResourceManager</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtCreateSection</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatesection" data-raw-source="[&lt;strong&gt;ZwCreateSection&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatesection)"><strong>ZwCreateSection</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtCreateTransaction</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreatetransaction" data-raw-source="[&lt;strong&gt;ZwCreateTransaction&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreatetransaction)"><strong>ZwCreateTransaction</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtCreateTransactionManager</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreatetransactionmanager" data-raw-source="[&lt;strong&gt;ZwCreateTransactionManager&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreatetransactionmanager)"><strong>ZwCreateTransactionManager</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtCurrentProcess</p></td>
<td><p><a href="/windows-hardware/drivers/kernel/zwcurrentprocess"><strong>ZwCurrentProcess</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtCurrentThread</p></td>
<td><p><a href="/windows-hardware/drivers/kernel/zwcurrentthread"><strong>ZwCurrentThread</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtDeleteFile</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwdeletefile" data-raw-source="[&lt;strong&gt;ZwDeleteFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwdeletefile)"><strong>ZwDeleteFile</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtDeleteKey</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwdeletekey" data-raw-source="[&lt;strong&gt;ZwDeleteKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwdeletekey)"><strong>ZwDeleteKey</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtDeleteValueKey</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwdeletevaluekey" data-raw-source="[&lt;strong&gt;ZwDeleteValueKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwdeletevaluekey)"><strong>ZwDeleteValueKey</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtDeviceIoControlFile</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwdeviceiocontrolfile" data-raw-source="[&lt;strong&gt;ZwDeviceIoControlFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwdeviceiocontrolfile)"><strong>ZwDeviceIoControlFile</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtDuplicateObject</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwduplicateobject" data-raw-source="[&lt;strong&gt;ZwDuplicateObject&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwduplicateobject)"><strong>ZwDuplicateObject</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtDuplicateToken</p></td>
<td><p><a href="/previous-versions/ff566446(v=vs.85)" data-raw-source="[&lt;strong&gt;ZwDuplicateToken&lt;/strong&gt;](/previous-versions/ff566446(v=vs.85))"><strong>ZwDuplicateToken</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtEnumerateKey</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwenumeratekey" data-raw-source="[&lt;strong&gt;ZwEnumerateKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwenumeratekey)"><strong>ZwEnumerateKey</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtEnumerateTransactionObject</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntenumeratetransactionobject" data-raw-source="[&lt;strong&gt;ZwEnumerateTransactionObject&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntenumeratetransactionobject)"><strong>ZwEnumerateTransactionObject</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtEnumerateValueKey</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwenumeratevaluekey" data-raw-source="[&lt;strong&gt;ZwEnumerateValueKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwenumeratevaluekey)"><strong>ZwEnumerateValueKey</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtFlushBuffersFile</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwflushbuffersfile" data-raw-source="[&lt;strong&gt;ZwFlushBuffersFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwflushbuffersfile)"><strong>ZwFlushBuffersFile</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtFlushBuffersFileEx</p></td>
<td><p><a href="/previous-versions/hh967720(v=vs.85)" data-raw-source="[&lt;strong&gt;ZwFlushBuffersFileEx&lt;/strong&gt;](/previous-versions/hh967720(v=vs.85))"><strong>ZwFlushBuffersFileEx</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtFlushKey</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwflushkey" data-raw-source="[&lt;strong&gt;ZwFlushKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwflushkey)"><strong>ZwFlushKey</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtFlushVirtualMemory</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwflushvirtualmemory" data-raw-source="[&lt;strong&gt;ZwFlushVirtualMemory&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwflushvirtualmemory)"><strong>ZwFlushVirtualMemory</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtFreeVirtualMemory</p></td>
<td><p><a href="/previous-versions/ff566460(v=vs.85)" data-raw-source="[&lt;strong&gt;ZwFreeVirtualMemory&lt;/strong&gt;](/previous-versions/ff566460(v=vs.85))"><strong>ZwFreeVirtualMemory</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtFsControlFile</p></td>
<td><p><a href="/previous-versions/ff566462(v=vs.85)" data-raw-source="[&lt;strong&gt;ZwFsControlFile&lt;/strong&gt;](/previous-versions/ff566462(v=vs.85))"><strong>ZwFsControlFile</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtGetNotificationResourceManager</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntgetnotificationresourcemanager" data-raw-source="[&lt;strong&gt;ZwGetNotificationResourceManager&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntgetnotificationresourcemanager)"><strong>ZwGetNotificationResourceManager</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtLoadDriver</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwloaddriver" data-raw-source="[&lt;strong&gt;ZwLoadDriver&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwloaddriver)"><strong>ZwLoadDriver</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtLockFile</p></td>
<td><p><a href="/previous-versions/ff566474(v=vs.85)" data-raw-source="[&lt;strong&gt;ZwLockFile&lt;/strong&gt;](/previous-versions/ff566474(v=vs.85))"><strong>ZwLockFile</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtMakeTemporaryObject</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwmaketemporaryobject" data-raw-source="[&lt;strong&gt;ZwMakeTemporaryObject&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwmaketemporaryobject)"><strong>ZwMakeTemporaryObject</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtMapViewOfSection</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwmapviewofsection" data-raw-source="[&lt;strong&gt;ZwMapViewOfSection&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwmapviewofsection)"><strong>ZwMapViewOfSection</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtNotifyChangeKey</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwnotifychangekey" data-raw-source="[&lt;strong&gt;ZwNotifyChangeKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwnotifychangekey)"><strong>ZwNotifyChangeKey</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtOpenDirectoryObject</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwopendirectoryobject" data-raw-source="[&lt;strong&gt;ZwOpenDirectoryObject&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwopendirectoryobject)"><strong>ZwOpenDirectoryObject</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtOpenEnlistment</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntopenenlistment" data-raw-source="[&lt;strong&gt;ZwOpenEnlistment&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntopenenlistment)"><strong>ZwOpenEnlistment</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtOpenEvent</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopenevent" data-raw-source="[&lt;strong&gt;ZwOpenEvent&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopenevent)"><strong>ZwOpenEvent</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtOpenFile</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntopenfile" data-raw-source="[&lt;strong&gt;ZwOpenFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntopenfile)"><strong>ZwOpenFile</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtOpenKey</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopenkey" data-raw-source="[&lt;strong&gt;ZwOpenKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopenkey)"><strong>ZwOpenKey</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtOpenProcess</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ntopenprocess" data-raw-source="[&lt;strong&gt;ZwOpenProcess&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ntopenprocess)"><strong>ZwOpenProcess</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtOpenProcessTokenEx</p></td>
<td><p><a href="/previous-versions/ff567024(v=vs.85)" data-raw-source="[&lt;strong&gt;ZwOpenProcessTokenEx&lt;/strong&gt;](/previous-versions/ff567024(v=vs.85))"><strong>ZwOpenProcessTokenEx</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtOpenResourceManager</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntopenresourcemanager" data-raw-source="[&lt;strong&gt;ZwOpenResourceManager&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntopenresourcemanager)"><strong>ZwOpenResourceManager</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtOpenSection</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopensection" data-raw-source="[&lt;strong&gt;ZwOpenSection&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopensection)"><strong>ZwOpenSection</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtOpenSymbolicLinkObject</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopensymboliclinkobject" data-raw-source="[&lt;strong&gt;ZwOpenSymbolicLinkObject&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopensymboliclinkobject)"><strong>ZwOpenSymbolicLinkObject</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtOpenThreadTokenEx</p></td>
<td><p><a href="/previous-versions/ff567032(v=vs.85)" data-raw-source="[&lt;strong&gt;ZwOpenThreadTokenEx&lt;/strong&gt;](/previous-versions/ff567032(v=vs.85))"><strong>ZwOpenThreadTokenEx</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtOpenTransaction</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntopentransaction" data-raw-source="[&lt;strong&gt;ZwOpenTransaction&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntopentransaction)"><strong>ZwOpenTransaction</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtOpenTransactionManager</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntopentransactionmanager" data-raw-source="[&lt;strong&gt;ZwOpenTransactionManager&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntopentransactionmanager)"><strong>ZwOpenTransactionManager</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtPowerInformation</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntpowerinformation" data-raw-source="[&lt;strong&gt;ZwPowerInformation&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntpowerinformation)"><strong>ZwPowerInformation</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtPrepareComplete</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntpreparecomplete" data-raw-source="[&lt;strong&gt;ZwPrepareComplete&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntpreparecomplete)"><strong>ZwPrepareComplete</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtPrepareEnlistment</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntprepareenlistment" data-raw-source="[&lt;strong&gt;ZwPrepareEnlistment&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntprepareenlistment)"><strong>ZwPrepareEnlistment</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtPrePrepareComplete</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntprepreparecomplete" data-raw-source="[&lt;strong&gt;ZwPrePrepareComplete&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntprepreparecomplete)"><strong>ZwPrePrepareComplete</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtPrePrepareEnlistment</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntpreprepareenlistment" data-raw-source="[&lt;strong&gt;ZwPrePrepareEnlistment&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntpreprepareenlistment)"><strong>ZwPrePrepareEnlistment</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtQueryDirectoryFile</p></td>
<td><p><a href="/previous-versions/ff567047(v=vs.85)" data-raw-source="[&lt;strong&gt;ZwQueryDirectoryFile&lt;/strong&gt;](/previous-versions/ff567047(v=vs.85))"><strong>ZwQueryDirectoryFile</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtQueryFullAttributesFile</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwqueryfullattributesfile" data-raw-source="[&lt;strong&gt;ZwQueryFullAttributesFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwqueryfullattributesfile)"><strong>ZwQueryFullAttributesFile</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtQueryInformationEnlistment</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntqueryinformationenlistment" data-raw-source="[&lt;strong&gt;ZwQueryInformationEnlistment&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntqueryinformationenlistment)"><strong>ZwQueryInformationEnlistment</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtQueryInformationFile</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationfile" data-raw-source="[&lt;strong&gt;ZwQueryInformationFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationfile)"><strong>ZwQueryInformationFile</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtQueryInformationResourceManager</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntqueryinformationresourcemanager" data-raw-source="[&lt;strong&gt;ZwQueryInformationResourceManager&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntqueryinformationresourcemanager)"><strong>ZwQueryInformationResourceManager</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtQueryInformationToken</p></td>
<td><p><a href="/previous-versions/ff567055(v=vs.85)" data-raw-source="[&lt;strong&gt;ZwQueryInformationToken&lt;/strong&gt;](/previous-versions/ff567055(v=vs.85))"><strong>ZwQueryInformationToken</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtQueryInformationTransaction</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntqueryinformationtransaction" data-raw-source="[&lt;strong&gt;ZwQueryInformationTransaction&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntqueryinformationtransaction)"><strong>ZwQueryInformationTransaction</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtQueryInformationTransactionManager</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntqueryinformationtransactionmanager" data-raw-source="[&lt;strong&gt;ZwQueryInformationTransactionManager&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntqueryinformationtransactionmanager)"><strong>ZwQueryInformationTransactionManager</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtQueryKey</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwquerykey" data-raw-source="[&lt;strong&gt;ZwQueryKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwquerykey)"><strong>ZwQueryKey</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtQueryObject</p></td>
<td><p><a href="/previous-versions/ff567062(v=vs.85)" data-raw-source="[&lt;strong&gt;ZwQueryObject&lt;/strong&gt;](/previous-versions/ff567062(v=vs.85))"><strong>ZwQueryObject</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtQueryQuotaInformationFile</p></td>
<td><p><a href="/previous-versions/ff567064(v=vs.85)" data-raw-source="[&lt;strong&gt;ZwQueryQuotaInformationFile&lt;/strong&gt;](/previous-versions/ff567064(v=vs.85))"><strong>ZwQueryQuotaInformationFile</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtQuerySecurityObject</p></td>
<td><p><a href="/previous-versions/ff567066(v=vs.85)" data-raw-source="[&lt;strong&gt;ZwQuerySecurityObject&lt;/strong&gt;](/previous-versions/ff567066(v=vs.85))"><strong>ZwQuerySecurityObject</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtQuerySecurityObject</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwquerysymboliclinkobject" data-raw-source="[&lt;strong&gt;ZwQuerySymbolicLinkObject&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwquerysymboliclinkobject)"><strong>ZwQuerySymbolicLinkObject</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtQueryValueKey</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwqueryvaluekey" data-raw-source="[&lt;strong&gt;ZwQueryValueKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwqueryvaluekey)"><strong>ZwQueryValueKey</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtQueryVirtualMemory</p></td>
<td><p><a href="/previous-versions/dn957455(v=vs.85)" data-raw-source="[&lt;strong&gt;ZwQueryVirtualMemory&lt;/strong&gt;](/previous-versions/dn957455(v=vs.85))"><strong>ZwQueryVirtualMemory</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtQueryVolumeInformationFile</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwqueryvolumeinformationfile" data-raw-source="[&lt;strong&gt;ZwQueryVolumeInformationFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwqueryvolumeinformationfile)"><strong>ZwQueryVolumeInformationFile</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtReadFile</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntreadfile" data-raw-source="[&lt;strong&gt;ZwReadFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntreadfile)"><strong>ZwReadFile</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtReadOnlyEnlistment</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntreadonlyenlistment" data-raw-source="[&lt;strong&gt;ZwReadOnlyEnlistment&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntreadonlyenlistment)"><strong>ZwReadOnlyEnlistment</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtReadOnlyEnlistment</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrecoverenlistment" data-raw-source="[&lt;strong&gt;ZwRecoverEnlistment&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrecoverenlistment)"><strong>ZwRecoverEnlistment</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtRecoverResourceManager</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrecoverresourcemanager" data-raw-source="[&lt;strong&gt;ZwRecoverResourceManager&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrecoverresourcemanager)"><strong>ZwRecoverResourceManager</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtRecoverTransactionManager</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrecovertransactionmanager" data-raw-source="[&lt;strong&gt;ZwRecoverTransactionManager&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrecovertransactionmanager)"><strong>ZwRecoverTransactionManager</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtRollbackComplete</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrollbackcomplete" data-raw-source="[&lt;strong&gt;ZwRollbackComplete&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrollbackcomplete)"><strong>ZwRollbackComplete</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtRollbackEnlistment</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrollbackenlistment" data-raw-source="[&lt;strong&gt;ZwRollbackEnlistment&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrollbackenlistment)"><strong>ZwRollbackEnlistment</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtRollbackTransaction</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrollbacktransaction" data-raw-source="[&lt;strong&gt;ZwRollbackTransaction&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrollbacktransaction)"><strong>ZwRollbackTransaction</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtRollforwardTransactionManager</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrollforwardtransactionmanager" data-raw-source="[&lt;strong&gt;ZwRollforwardTransactionManager&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrollforwardtransactionmanager)"><strong>ZwRollforwardTransactionManager</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtSetEvent</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwsetevent" data-raw-source="[&lt;strong&gt;ZwSetEvent&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwsetevent)"><strong>ZwSetEvent</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtSetInformationEnlistment</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntsetinformationenlistment" data-raw-source="[&lt;strong&gt;ZwSetInformationEnlistment&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntsetinformationenlistment)"><strong>ZwSetInformationEnlistment</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtSetInformationFile</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntsetinformationfile" data-raw-source="[&lt;strong&gt;ZwSetInformationFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntsetinformationfile)"><strong>ZwSetInformationFile</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtSetInformationResourceManager</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntsetinformationresourcemanager" data-raw-source="[&lt;strong&gt;ZwSetInformationResourceManager&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntsetinformationresourcemanager)"><strong>ZwSetInformationResourceManager</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtSetInformationThread</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntddk/nf-ntddk-zwsetinformationthread" data-raw-source="[&lt;strong&gt;ZwSetInformationThread&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-zwsetinformationthread)"><strong>ZwSetInformationThread</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtSetInformationToken</p></td>
<td><p><a href="/previous-versions/ff567102(v=vs.85)" data-raw-source="[&lt;strong&gt;ZwSetInformationToken&lt;/strong&gt;](/previous-versions/ff567102(v=vs.85))"><strong>ZwSetInformationToken</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtSetInformationTransaction</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntsetinformationtransaction" data-raw-source="[&lt;strong&gt;ZwSetInformationTransaction&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntsetinformationtransaction)"><strong>ZwSetInformationTransaction</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtSetQuotaInformationFile</p></td>
<td><p><a href="/previous-versions/ff567105(v=vs.85)" data-raw-source="[&lt;strong&gt;ZwSetQuotaInformationFile&lt;/strong&gt;](/previous-versions/ff567105(v=vs.85))"><strong>ZwSetQuotaInformationFile</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtSetSecurityObject</p></td>
<td><p><a href="/previous-versions/ff567106(v=vs.85)" data-raw-source="[&lt;strong&gt;ZwSetSecurityObject&lt;/strong&gt;](/previous-versions/ff567106(v=vs.85))"><strong>ZwSetSecurityObject</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtSetValueKey</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwsetvaluekey" data-raw-source="[&lt;strong&gt;ZwSetValueKey&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwsetvaluekey)"><strong>ZwSetValueKey</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtSetVolumeInformationFile</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwsetvolumeinformationfile" data-raw-source="[&lt;strong&gt;ZwSetVolumeInformationFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwsetvolumeinformationfile)"><strong>ZwSetVolumeInformationFile</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtSinglePhaseReject</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ntsinglephasereject" data-raw-source="[&lt;strong&gt;ZwSinglePhaseReject&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntsinglephasereject)"><strong>ZwSinglePhaseReject</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtTerminateProcess</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntddk/nf-ntddk-zwterminateprocess" data-raw-source="[&lt;strong&gt;ZwTerminateProcess&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-zwterminateprocess)"><strong>ZwTerminateProcess</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtUnloadDriver</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwunloaddriver" data-raw-source="[&lt;strong&gt;ZwUnloadDriver&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwunloaddriver)"><strong>ZwUnloadDriver</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtUnlockFile</p></td>
<td><p><a href="/previous-versions/ff567118(v=vs.85)" data-raw-source="[&lt;strong&gt;ZwUnlockFile&lt;/strong&gt;](/previous-versions/ff567118(v=vs.85))"><strong>ZwUnlockFile</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtUnmapViewOfSection</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-zwunmapviewofsection" data-raw-source="[&lt;strong&gt;ZwUnmapViewOfSection&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwunmapviewofsection)"><strong>ZwUnmapViewOfSection</strong></a></p></td>
</tr>
<tr class="even">
<td><p>NtWaitForSingleObject</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwwaitforsingleobject" data-raw-source="[&lt;strong&gt;ZwWaitForSingleObject&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwwaitforsingleobject)"><strong>ZwWaitForSingleObject</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>NtWriteFile</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntwritefile" data-raw-source="[&lt;strong&gt;ZwWriteFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntwritefile)"><strong>ZwWriteFile</strong></a></p></td>
</tr>
</tbody>
</table>

 

