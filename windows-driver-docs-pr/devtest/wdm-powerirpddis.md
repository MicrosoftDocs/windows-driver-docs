---
title: PowerIrpDDIs rule (wdm)
description: The PowerIrpDDIs rule specifies that when a driver is processing a system or a device IRP\_MJ\_POWER with IRP\_MN\_SET\_POWER, it should not call DDIs that can only be call at PASSIVE\_LEVEL.
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

**Driver model: WDM**

## How to test

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>PowerIrpDDIs</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](./using-static-driver-verifier-to-find-defects-in-drivers.md#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](./using-static-driver-verifier-to-find-defects-in-drivers.md#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](./using-static-driver-verifier-to-find-defects-in-drivers.md#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

## Applies to

[**ExIsProcessorFeaturePresent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exisprocessorfeaturepresent)  
[**ExRaiseAccessViolation**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exraiseaccessviolation)  
[**ExRaiseDatatypeMisalignment**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exraisedatatypemisalignment)  
[**ExUuidCreate**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exuuidcreate)  
[**HalExamineMBR**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-halexaminembr)  
[**HalGetInterruptVector**](/previous-versions/windows/hardware/drivers/ff546644(v=vs.85))  
[**IoBuildDeviceIoControlRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest)  
[**IoBuildSynchronousFsdRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuildsynchronousfsdrequest)  
[**IoCheckShareAccess**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocheckshareaccess)  
[**IoConnectInterrupt**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioconnectinterrupt)  
[**IoCreateController**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatecontroller)  
[**IoCreateFile**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatefile)  
[**IoCreateSymbolicLink**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatesymboliclink)  
[**IoCreateSynchronizationEvent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatesynchronizationevent)  
[**IoCreateUnprotectedSymbolicLink**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreateunprotectedsymboliclink)  
[**IoDeleteController**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iodeletecontroller)  
[**IoDeleteSymbolicLink**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iodeletesymboliclink)  
[**IoDetachDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iodetachdevice)  
[**IoDisconnectInterrupt**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iodisconnectinterrupt)  
[**IoGetConfigurationInformation**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iogetconfigurationinformation)  
[**IoGetDeviceInterfaceAlias**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceinterfacealias)  
[**IoGetDeviceInterfaces**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceinterfaces)  
[**IoGetDeviceNumaNode**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdevicenumanode)  
[**IoGetDeviceObjectPointer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceobjectpointer)  
[**IoGetDeviceProperty**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceproperty)  
[**IoGetDevicePropertyData**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdevicepropertydata)  
[**IoGetDmaAdapter**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdmaadapter)  
[**IoGetFileObjectGenericMapping**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iogetfileobjectgenericmapping)  
[**IoInitializeTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioinitializetimer)  
[**IoIsWdmVersionAvailable**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioiswdmversionavailable)  
[**IoOpenDeviceInterfaceRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceinterfaceregistrykey)  
[**IoOpenDeviceRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceregistrykey)  
[**IoRegisterBootDriverReinitialization**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioregisterbootdriverreinitialization)  
[**IoRegisterDeviceInterface**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterdeviceinterface)  
[**IoRegisterDriverReinitialization**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioregisterdriverreinitialization)  
[**IoRegisterLastChanceShutdownNotification**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterlastchanceshutdownnotification)  
[**IoRegisterPlugPlayNotification**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterplugplaynotification)  
[**IoRegisterShutdownNotification**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregistershutdownnotification)  
[**IoRemoveShareAccess**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioremoveshareaccess)  
[**IoReportDetectedDevice**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioreportdetecteddevice)  
[**IoReportTargetDeviceChange**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioreporttargetdevicechange)  
[**IoSetDeviceInterfaceState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetdeviceinterfacestate)  
[**IoSetDevicePropertyData**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetdevicepropertydata)  
[**IoUnregisterPlugPlayNotification**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iounregisterplugplaynotification)  
[**IoUnregisterPlugPlayNotificationEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iounregisterplugplaynotificationex)  
[**IoUnregisterShutdownNotification**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iounregistershutdownnotification)  
[**IoUpdateShareAccess**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioupdateshareaccess)  
[**IoWMIAllocateInstanceIds**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iowmiallocateinstanceids)  
[**IoWMIRegistrationControl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iowmiregistrationcontrol)  
[**KeDelayExecutionThread**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kedelayexecutionthread)  
[**KeInitializeSemaphore**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializesemaphore)  
[**KeQueryPriorityThread**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kequeryprioritythread)  
[**KeQueryRuntimeThread**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kequeryruntimethread)  
[**KeRevertToUserAffinityThreadEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereverttouseraffinitythreadex)  
[**KeSetSystemAffinityThread**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesetsystemaffinitythread)  
[**KeSetSystemGroupAffinityThread**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesetsystemgroupaffinitythread)  
[**MmGetSystemRoutineAddress**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetsystemroutineaddress)  
[**PsGetVersion**](/windows-hardware/drivers/ddi/wdm/nf-wdm-psgetversion)  
[**PsRemoveLoadImageNotifyRoutine**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-psremoveloadimagenotifyroutine)  
[**PsSetCreateProcessNotifyRoutine**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-pssetcreateprocessnotifyroutine)  
[**PsSetCreateProcessNotifyRoutineEx**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-pssetcreateprocessnotifyroutineex)  
[**PsSetCreateThreadNotifyRoutine**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-pssetcreatethreadnotifyroutine)  
[**PsSetLoadImageNotifyRoutine**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-pssetloadimagenotifyroutine)  
[**PsTerminateSystemThread**](/windows-hardware/drivers/ddi/wdm/nf-wdm-psterminatesystemthread)  
[**SeAccessCheck**](/windows-hardware/drivers/ddi/wdm/nf-wdm-seaccesscheck)  
[**SeAssignSecurity**](/windows-hardware/drivers/ddi/wdm/nf-wdm-seassignsecurity)  
[**SeDeassignSecurity**](/windows-hardware/drivers/ddi/wdm/nf-wdm-sedeassignsecurity)  
[**SeSinglePrivilegeCheck**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-sesingleprivilegecheck)  
[**SeValidSecurityDescriptor**](/windows-hardware/drivers/ddi/wdm/nf-wdm-sevalidsecuritydescriptor)  
[**ZwAllocateLocallyUniqueId**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-zwallocatelocallyuniqueid)  
[**ZwAllocateVirtualMemory**](/previous-versions/ff566416(v=vs.85))  
[**ZwClose**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose)  
[**ZwCommitComplete**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcommitcomplete)  
[**ZwCommitEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcommitenlistment)  
[**ZwCommitTransaction**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcommittransaction)  
[**ZwCreateDirectoryObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatedirectoryobject)  
[**ZwCreateEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreateenlistment)  
[**ZwCreateEvent**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwcreateevent)  
[**ZwCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile)  
[**ZwCreateKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatekey)  
[**ZwCreateKeyTransacted**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatekeytransacted)  
[**ZwCreateResourceManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreateresourcemanager)  
[**ZwCreateTransaction**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreatetransaction)  
[**ZwCreateTransactionManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntcreatetransactionmanager)  
[**ZwDeleteFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwdeletefile)  
[**ZwDeleteKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwdeletekey)  
[**ZwDeleteValueKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwdeletevaluekey)  
[**ZwDeviceIoControlFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwdeviceiocontrolfile)  
[**ZwDuplicateToken**](/previous-versions/ff566446(v=vs.85))  
[**ZwEnumerateKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwenumeratekey)  
[**ZwEnumerateTransactionObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntenumeratetransactionobject)  
[**ZwEnumerateValueKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwenumeratevaluekey)  
[**ZwFlushBuffersFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwflushbuffersfile)  
[**ZwFreeVirtualMemory**](/previous-versions/ff566460(v=vs.85))  
[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85))  
[**ZwGetNotificationResourceManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntgetnotificationresourcemanager)  
[**ZwLoadDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwloaddriver)  
[**ZwLockFile**](/previous-versions/ff566474(v=vs.85))  
[**ZwMakeTemporaryObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwmaketemporaryobject)  
[**ZwMapViewOfSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwmapviewofsection)  
[**ZwNotifyChangeKey**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwnotifychangekey)  
[**ZwOpenDirectoryObject**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwopendirectoryobject)  
[**ZwOpenEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntopenenlistment)  
[**ZwOpenEvent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopenevent)  
[**ZwOpenFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntopenfile)  
[**ZwOpenKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopenkey)  
[**ZwOpenKeyEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopenkeyex)  
[**ZwOpenKeyTransacted**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopenkeytransacted)  
[**ZwOpenKeyTransactedEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopenkeytransactedex)  
[**ZwOpenProcess**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ntopenprocess)  
[**ZwOpenProcessTokenEx**](/previous-versions/ff567024(v=vs.85))  
[**ZwOpenResourceManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntopenresourcemanager)  
[**ZwOpenSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopensection)  
[**ZwOpenSymbolicLinkObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopensymboliclinkobject)  
[**ZwOpenThreadTokenEx**](/previous-versions/ff567032(v=vs.85))  
[**ZwOpenTransaction**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntopentransaction)  
[**ZwOpenTransactionManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntopentransactionmanager)  
[**ZwPowerInformation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntpowerinformation)  
[**ZwPrepareComplete**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntpreparecomplete)  
[**ZwPrepareEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntprepareenlistment)  
[**ZwPrePrepareComplete**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntprepreparecomplete)  
[**ZwPrePrepareEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntpreprepareenlistment)  
[**ZwQueryDirectoryFile**](/previous-versions/ff567047(v=vs.85))  
[**ZwQueryEaFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwqueryeafile)  
[**ZwQueryFullAttributesFile**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwqueryfullattributesfile)  
[**ZwQueryInformationEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntqueryinformationenlistment)  
[**ZwQueryInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationfile)  
[**ZwQueryInformationResourceManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntqueryinformationresourcemanager)  
[**ZwQueryInformationToken**](/previous-versions/ff567055(v=vs.85))  
[**ZwQueryInformationTransaction**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntqueryinformationtransaction)  
[**ZwQueryInformationTransactionManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntqueryinformationtransactionmanager)  
[**ZwQueryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwquerykey)  
[**ZwQueryObject**](/previous-versions/ff567062(v=vs.85))  
[**ZwQueryQuotaInformationFile**](/previous-versions/ff567064(v=vs.85))  
[**ZwQuerySecurityObject**](/previous-versions/ff567066(v=vs.85))  
[**ZwQuerySymbolicLinkObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwquerysymboliclinkobject)  
[**ZwQueryValueKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwqueryvaluekey)  
[**ZwQueryVolumeInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwqueryvolumeinformationfile)  
[**ZwReadFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntreadfile)  
[**ZwReadOnlyEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntreadonlyenlistment)  
[**ZwRecoverEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrecoverenlistment)  
[**ZwRecoverTransactionManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrecovertransactionmanager)  
[**ZwRollbackComplete**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrollbackcomplete)  
[**ZwRollbackEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrollbackenlistment)  
[**ZwRollbackTransaction**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrollbacktransaction)  
[**ZwRollforwardTransactionManager**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntrollforwardtransactionmanager)  
[**ZwSetEaFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwseteafile)  
[**ZwSetInformationEnlistment**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntsetinformationenlistment)  
[**ZwSetInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntsetinformationfile)  
[**ZwSetInformationThread**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-zwsetinformationthread)  
[**ZwSetInformationToken**](/previous-versions/ff567102(v=vs.85))  
[**ZwSetInformationTransaction**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntsetinformationtransaction)  
[**ZwSetQuotaInformationFile**](/previous-versions/ff567105(v=vs.85))  
[**ZwSetSecurityObject**](/previous-versions/ff567106(v=vs.85))  
[**ZwSetValueKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwsetvaluekey)  
[**ZwSetVolumeInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwsetvolumeinformationfile)  
[**ZwSinglePhaseReject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ntsinglephasereject)  
[**ZwTerminateProcess**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-zwterminateprocess)  
[**ZwUnloadDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwunloaddriver)  
[**ZwUnlockFile**](/previous-versions/ff567118(v=vs.85))  
[**ZwUnmapViewOfSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwunmapviewofsection)  
[**ZwWriteFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntwritefile)  
