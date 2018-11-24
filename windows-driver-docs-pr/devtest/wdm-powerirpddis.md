---
title: PowerIrpDDIs rule (wdm)
description: The PowerIrpDDIs rule specifies that when a driver is processing a system or a device IRP\_MJ\_POWER with IRP\_MN\_SET\_POWER, it should not call DDIs that can only be call at PASSIVE\_LEVEL.
ms.assetid: C56C73E5-75D6-427A-8582-24D6B1404A70
ms.date: 05/21/2018
keywords: ["PowerIrpDDIs rule (wdm)"]
topic_type:
- apiref
api_name:
- PowerIrpDDIs
api_type:
- NA
ms.localizationpriority: medium
---

# PowerIrpDDIs rule (wdm)


The **PowerIrpDDIs** rule specifies that when a driver is processing a system or a device IRP\_MJ\_POWER with IRP\_MN\_SET\_POWER, it should not call DDIs that can only be call at PASSIVE\_LEVEL.

|              |     |
|--------------|-----|
| Driver model | WDM |

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At compile time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>PowerIrpDDIs</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh454281" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**ExIsProcessorFeaturePresent**](https://msdn.microsoft.com/library/windows/hardware/ff545442)
[**ExRaiseAccessViolation**](https://msdn.microsoft.com/library/windows/hardware/ff545509)
[**ExRaiseDatatypeMisalignment**](https://msdn.microsoft.com/library/windows/hardware/ff545524)
[**ExUuidCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545658)
[**HalExamineMBR**](https://msdn.microsoft.com/library/windows/hardware/ff546584)
[**HalGetInterruptVector**](https://msdn.microsoft.com/library/windows/hardware/ff546612)
[**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318)
[**IoBuildSynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548330)
[**IoCheckShareAccess**](https://msdn.microsoft.com/library/windows/hardware/ff548341)
[**IoConnectInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff548371)
[**IoCreateController**](https://msdn.microsoft.com/library/windows/hardware/ff548395)
[**IoCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff548418)
[**IoCreateSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff549043)
[**IoCreateSynchronizationEvent**](https://msdn.microsoft.com/library/windows/hardware/ff549045)
[**IoCreateUnprotectedSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff549050)
[**IoDeleteController**](https://msdn.microsoft.com/library/windows/hardware/ff549078)
[**IoDeleteSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff549085)
[**IoDetachDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549087)
[**IoDisconnectInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff549089)
[**IoGetConfigurationInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549157)
[**IoGetDeviceInterfaceAlias**](https://msdn.microsoft.com/library/windows/hardware/ff549180)
[**IoGetDeviceInterfaces**](https://msdn.microsoft.com/library/windows/hardware/ff549186)
[**IoGetDeviceNumaNode**](https://msdn.microsoft.com/library/windows/hardware/ff549191)
[**IoGetDeviceObjectPointer**](https://msdn.microsoft.com/library/windows/hardware/ff549198)
[**IoGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff549203)
[**IoGetDevicePropertyData**](https://msdn.microsoft.com/library/windows/hardware/ff549206)
[**IoGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff549220)
[**IoGetFileObjectGenericMapping**](https://msdn.microsoft.com/library/windows/hardware/ff549231)
[**IoInitializeTimer**](https://msdn.microsoft.com/library/windows/hardware/ff549344)
[**IoIsWdmVersionAvailable**](https://msdn.microsoft.com/library/windows/hardware/ff549382)
[**IoOpenDeviceInterfaceRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff549433)
[**IoOpenDeviceRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff549443)
[**IoRegisterBootDriverReinitialization**](https://msdn.microsoft.com/library/windows/hardware/ff549494)
[**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506)
[**IoRegisterDriverReinitialization**](https://msdn.microsoft.com/library/windows/hardware/ff549511)
[**IoRegisterLastChanceShutdownNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549518)
[**IoRegisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549526)
[**IoRegisterShutdownNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549541)
[**IoRemoveShareAccess**](https://msdn.microsoft.com/library/windows/hardware/ff549587)
[**IoReportDetectedDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549597)
[**IoReportTargetDeviceChange**](https://msdn.microsoft.com/library/windows/hardware/ff549625)
[**IoSetDeviceInterfaceState**](https://msdn.microsoft.com/library/windows/hardware/ff549700)
[**IoSetDevicePropertyData**](https://msdn.microsoft.com/library/windows/hardware/ff549704)
[**IoUnregisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff550398)
[**IoUnregisterPlugPlayNotificationEx**](https://msdn.microsoft.com/library/windows/hardware/ff550404)
[**IoUnregisterShutdownNotification**](https://msdn.microsoft.com/library/windows/hardware/ff550409)
[**IoUpdateShareAccess**](https://msdn.microsoft.com/library/windows/hardware/ff550412)
[**IoWMIAllocateInstanceIds**](https://msdn.microsoft.com/library/windows/hardware/ff550429)
[**IoWMIRegistrationControl**](https://msdn.microsoft.com/library/windows/hardware/ff550480)
[**KeDelayExecutionThread**](https://msdn.microsoft.com/library/windows/hardware/ff551986)
[**KeInitializeSemaphore**](https://msdn.microsoft.com/library/windows/hardware/ff552150)
[**KeQueryPriorityThread**](https://msdn.microsoft.com/library/windows/hardware/ff553062)
[**KeQueryRuntimeThread**](https://msdn.microsoft.com/library/windows/hardware/ff553065)
[**KeRevertToUserAffinityThreadEx**](https://msdn.microsoft.com/library/windows/hardware/ff553190)
[**KeSetSystemAffinityThread**](https://msdn.microsoft.com/library/windows/hardware/ff553267)
[**KeSetSystemGroupAffinityThread**](https://msdn.microsoft.com/library/windows/hardware/ff553275)
[**MmGetSystemRoutineAddress**](https://msdn.microsoft.com/library/windows/hardware/ff554563)
[**PsGetVersion**](https://msdn.microsoft.com/library/windows/hardware/ff559941)
[**PsRemoveLoadImageNotifyRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559949)
[**PsSetCreateProcessNotifyRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559951)
[**PsSetCreateProcessNotifyRoutineEx**](https://msdn.microsoft.com/library/windows/hardware/ff559953)
[**PsSetCreateThreadNotifyRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559954)
[**PsSetLoadImageNotifyRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559957)
[**PsTerminateSystemThread**](https://msdn.microsoft.com/library/windows/hardware/ff559959)
[**SeAccessCheck**](https://msdn.microsoft.com/library/windows/hardware/ff563674)
[**SeAssignSecurity**](https://msdn.microsoft.com/library/windows/hardware/ff563676)
[**SeDeassignSecurity**](https://msdn.microsoft.com/library/windows/hardware/ff563716)
[**SeSinglePrivilegeCheck**](https://msdn.microsoft.com/library/windows/hardware/ff563740)
[**SeValidSecurityDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff563793)
[**ZwAllocateLocallyUniqueId**](https://msdn.microsoft.com/library/windows/hardware/ff566415)
[**ZwAllocateVirtualMemory**](https://msdn.microsoft.com/library/windows/hardware/ff566416)
[**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417)
[**ZwCommitComplete**](https://msdn.microsoft.com/library/windows/hardware/ff566418)
[**ZwCommitEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff566419)
[**ZwCommitTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff566420)
[**ZwCreateDirectoryObject**](https://msdn.microsoft.com/library/windows/hardware/ff566421)
[**ZwCreateEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff566422)
[**ZwCreateEvent**](https://msdn.microsoft.com/library/windows/hardware/ff566423)
[**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424)
[**ZwCreateKey**](https://msdn.microsoft.com/library/windows/hardware/ff566425)
[**ZwCreateKeyTransacted**](https://msdn.microsoft.com/library/windows/hardware/ff566426)
[**ZwCreateResourceManager**](https://msdn.microsoft.com/library/windows/hardware/ff566427)
[**ZwCreateTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff566429)
[**ZwCreateTransactionManager**](https://msdn.microsoft.com/library/windows/hardware/ff566430)
[**ZwDeleteFile**](https://msdn.microsoft.com/library/windows/hardware/ff566435)
[**ZwDeleteKey**](https://msdn.microsoft.com/library/windows/hardware/ff566437)
[**ZwDeleteValueKey**](https://msdn.microsoft.com/library/windows/hardware/ff566439)
[**ZwDeviceIoControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566441)
[**ZwDuplicateToken**](https://msdn.microsoft.com/library/windows/hardware/ff566446)
[**ZwEnumerateKey**](https://msdn.microsoft.com/library/windows/hardware/ff566447)
[**ZwEnumerateTransactionObject**](https://msdn.microsoft.com/library/windows/hardware/ff566450)
[**ZwEnumerateValueKey**](https://msdn.microsoft.com/library/windows/hardware/ff566453)
[**ZwFlushBuffersFile**](https://msdn.microsoft.com/library/windows/hardware/ff566454)
[**ZwFreeVirtualMemory**](https://msdn.microsoft.com/library/windows/hardware/ff566460)
[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462)
[**ZwGetNotificationResourceManager**](https://msdn.microsoft.com/library/windows/hardware/ff566467)
[**ZwLoadDriver**](https://msdn.microsoft.com/library/windows/hardware/ff566470)
[**ZwLockFile**](https://msdn.microsoft.com/library/windows/hardware/ff566474)
[**ZwMakeTemporaryObject**](https://msdn.microsoft.com/library/windows/hardware/ff566477)
[**ZwMapViewOfSection**](https://msdn.microsoft.com/library/windows/hardware/ff566481)
[**ZwNotifyChangeKey**](https://msdn.microsoft.com/library/windows/hardware/ff566488)
[**ZwOpenDirectoryObject**](https://msdn.microsoft.com/library/windows/hardware/ff566492)
[**ZwOpenEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567008)
[**ZwOpenEvent**](https://msdn.microsoft.com/library/windows/hardware/ff567009)
[**ZwOpenFile**](https://msdn.microsoft.com/library/windows/hardware/ff567011)
[**ZwOpenKey**](https://msdn.microsoft.com/library/windows/hardware/ff567014)
[**ZwOpenKeyEx**](https://msdn.microsoft.com/library/windows/hardware/ff567015)
[**ZwOpenKeyTransacted**](https://msdn.microsoft.com/library/windows/hardware/ff567018)
[**ZwOpenKeyTransactedEx**](https://msdn.microsoft.com/library/windows/hardware/ff567020)
[**ZwOpenProcess**](https://msdn.microsoft.com/library/windows/hardware/ff567022)
[**ZwOpenProcessTokenEx**](https://msdn.microsoft.com/library/windows/hardware/ff567024)
[**ZwOpenResourceManager**](https://msdn.microsoft.com/library/windows/hardware/ff567026)
[**ZwOpenSection**](https://msdn.microsoft.com/library/windows/hardware/ff567029)
[**ZwOpenSymbolicLinkObject**](https://msdn.microsoft.com/library/windows/hardware/ff567030)
[**ZwOpenThreadTokenEx**](https://msdn.microsoft.com/library/windows/hardware/ff567032)
[**ZwOpenTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff567033)
[**ZwOpenTransactionManager**](https://msdn.microsoft.com/library/windows/hardware/ff567035)
[**ZwPowerInformation**](https://msdn.microsoft.com/library/windows/hardware/dn957454)
[**ZwPrepareComplete**](https://msdn.microsoft.com/library/windows/hardware/ff567037)
[**ZwPrepareEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567039)
[**ZwPrePrepareComplete**](https://msdn.microsoft.com/library/windows/hardware/ff567040)
[**ZwPrePrepareEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567044)
[**ZwQueryDirectoryFile**](https://msdn.microsoft.com/library/windows/hardware/ff567047)
[**ZwQueryEaFile**](https://msdn.microsoft.com/library/windows/hardware/ff961907)
[**ZwQueryFullAttributesFile**](https://msdn.microsoft.com/library/windows/hardware/ff567049)
[**ZwQueryInformationEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567051)
[**ZwQueryInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567052)
[**ZwQueryInformationResourceManager**](https://msdn.microsoft.com/library/windows/hardware/ff567054)
[**ZwQueryInformationToken**](https://msdn.microsoft.com/library/windows/hardware/ff567055)
[**ZwQueryInformationTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff567057)
[**ZwQueryInformationTransactionManager**](https://msdn.microsoft.com/library/windows/hardware/ff567058)
[**ZwQueryKey**](https://msdn.microsoft.com/library/windows/hardware/ff567060)
[**ZwQueryObject**](https://msdn.microsoft.com/library/windows/hardware/ff567062)
[**ZwQueryQuotaInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567064)
[**ZwQuerySecurityObject**](https://msdn.microsoft.com/library/windows/hardware/ff567066)
[**ZwQuerySymbolicLinkObject**](https://msdn.microsoft.com/library/windows/hardware/ff567068)
[**ZwQueryValueKey**](https://msdn.microsoft.com/library/windows/hardware/ff567069)
[**ZwQueryVolumeInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567070)
[**ZwReadFile**](https://msdn.microsoft.com/library/windows/hardware/ff567072)
[**ZwReadOnlyEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567074)
[**ZwRecoverEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567075)
[**ZwRecoverTransactionManager**](https://msdn.microsoft.com/library/windows/hardware/ff567079)
[**ZwRollbackComplete**](https://msdn.microsoft.com/library/windows/hardware/ff567081)
[**ZwRollbackEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567083)
[**ZwRollbackTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff567086)
[**ZwRollforwardTransactionManager**](https://msdn.microsoft.com/library/windows/hardware/ff567089)
[**ZwSetEaFile**](https://msdn.microsoft.com/library/windows/hardware/ff961908)
[**ZwSetInformationEnlistment**](https://msdn.microsoft.com/library/windows/hardware/ff567094)
[**ZwSetInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567096)
[**ZwSetInformationThread**](https://msdn.microsoft.com/library/windows/hardware/ff567101)
[**ZwSetInformationToken**](https://msdn.microsoft.com/library/windows/hardware/ff567102)
[**ZwSetInformationTransaction**](https://msdn.microsoft.com/library/windows/hardware/ff567104)
[**ZwSetQuotaInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567105)
[**ZwSetSecurityObject**](https://msdn.microsoft.com/library/windows/hardware/ff567106)
[**ZwSetValueKey**](https://msdn.microsoft.com/library/windows/hardware/ff567109)
[**ZwSetVolumeInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff567112)
[**ZwSinglePhaseReject**](https://msdn.microsoft.com/library/windows/hardware/ff567113)
[**ZwTerminateProcess**](https://msdn.microsoft.com/library/windows/hardware/ff567115)
[**ZwUnloadDriver**](https://msdn.microsoft.com/library/windows/hardware/ff567117)
[**ZwUnlockFile**](https://msdn.microsoft.com/library/windows/hardware/ff567118)
[**ZwUnmapViewOfSection**](https://msdn.microsoft.com/library/windows/hardware/ff567119)
[**ZwWriteFile**](https://msdn.microsoft.com/library/windows/hardware/ff567121)
 

 





