---
title: KMDF Functions that Return NSTATUS Codes
description: KMDF Functions that Return NSTATUS Codes
ms.assetid: 0edd35c0-2357-4502-8c59-36b16cf7f294
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# KMDF Functions that Return NSTATUS Codes


Following is a list of KMDF DDIs that return NTSTATUS codes. Any of these DDIs could be failed except the following two: **WdfRequestReuse** and **WdfWaitLockAcquire**.

**WdfChildListAddOrUpdateChildDescriptionAsPresent**

**WdfChildListCreate**

**WdfChildListRetrieveAddressDescription**

**WdfChildListRetrieveNextDevice**

**WdfChildListUpdateChildDescriptionAsMissing**

**WdfCmResourceListAppendDescriptor**

**WdfCmResourceListInsertDescriptor**

**WdfCollectionAdd**

**WdfCollectionCreate**

**WdfCommonBufferCreate**

**WdfCommonBufferCreateWithConfig**

**WdfDeviceAddDependentUsageDeviceObject**

**WdfDeviceAddQueryInterface**

**WdfDeviceAddRemovalRelationsPhysicalDevice**

**WdfDeviceAllocAndQueryProperty**

**WdfDeviceAssignMofResourceName**

**WdfDeviceAssignS0IdleSettings**

**WdfDeviceAssignSxWakeSettings**

**WdfDeviceConfigureRequestDispatching**

**WdfDeviceCreate**

**WdfDeviceCreateDeviceInterface**

**WdfDeviceCreateSymbolicLink**

**WdfDeviceEnqueueRequest**

**WdfDeviceIndicateWakeStatus**

**WdfDeviceInitAssignName**

**WdfDeviceInitAssignSDDLString**

**WdfDeviceInitAssignWdmIrpPreprocessCallback**

**WdfDeviceInitRegisterPnpStateChangeCallback**

**WdfDeviceInitRegisterPowerPolicyStateChangeCallback**

**WdfDeviceInitRegisterPowerStateChangeCallback**

**WdfDeviceMiniportCreate**

**WdfDeviceOpenRegistryKey**

**WdfDeviceQueryProperty**

**WdfDeviceRetrieveDeviceInterfaceString**

**WdfDeviceRetrieveDeviceName**

**WdfDeviceStopIdle**

**WdfDeviceWdmDispatchPreprocessedIrp**

**WdfDmaEnablerCreate**

**WdfDmaTransactionCreate**

**WdfDmaTransactionExecute**

**WdfDmaTransactionInitialize**

**WdfDmaTransactionInitializeUsingRequest**

**WdfDmaTransactionRelease**

**WdfDpcCreate**

**WdfDriverCreate**

**WdfDriverOpenParametersRegistryKey**

**WdfDriverRegisterTraceInfo**

**WdfDriverRetrieveVersionString**

**WdfFdoAddStaticChild**

**WdfFdoInitAllocAndQueryProperty**

**WdfFdoInitOpenRegistryKey**

**WdfFdoInitQueryProperty**

**WdfFdoQueryForInterface**

**WdfInterruptCreate**

**WdfIoQueueCreate**

**WdfIoQueueFindRequest**

**WdfIoQueueReadyNotify**

**WdfIoQueueRetrieveFoundRequest**

**WdfIoQueueRetrieveNextRequest**

**WdfIoQueueRetrieveRequestByFileObject**

**WdfIoResourceListAppendDescriptor**

**WdfIoResourceListCreate**

**WdfIoResourceListInsertDescriptor**

**WdfIoResourceRequirementsListAppendIoResList**

**WdfIoResourceRequirementsListInsertIoResList**

**WdfIoTargetAllocAndQueryTargetProperty**

**WdfIoTargetCreate**

**WdfIoTargetFormatRequestForInternalIoctl**

**WdfIoTargetFormatRequestForInternalIoctlOthers**

**WdfIoTargetFormatRequestForIoctl**

**WdfIoTargetFormatRequestForRead**

**WdfIoTargetFormatRequestForWrite**

**WdfIoTargetOpen**

**WdfIoTargetQueryForInterface**

**WdfIoTargetQueryTargetProperty**

**WdfIoTargetSendInternalIoctlOthersSynchronously**

**WdfIoTargetSendInternalIoctlSynchronously**

**WdfIoTargetSendIoctlSynchronously**

**WdfIoTargetSendReadSynchronously**

**WdfIoTargetSendWriteSynchronously**

**WdfIoTargetStart**

**WdfLookasideListCreate**

**WdfMemoryAssignBuffer**

**WdfMemoryCopyFromBuffer**

**WdfMemoryCopyToBuffer**

**WdfMemoryCreate**

**WdfMemoryCreateFromLookaside**

**WdfMemoryCreatePreallocated**

**WdfObjectAllocateContext**

**WdfObjectCreate**

**WdfObjectQuery**

**WdfPdoAddEjectionRelationsPhysicalDevice**

**WdfPdoInitAddCompatibleID**

**WdfPdoInitAddDeviceText**

**WdfPdoInitAddHardwareID**

**WdfPdoInitAssignDeviceID**

**WdfPdoInitAssignInstanceID**

**WdfPdoInitAssignRawDevice**

**WdfPdoMarkMissing**

**WdfPdoRetrieveAddressDescription**

**WdfPdoRetrieveIdentificationDescription**

**WdfPdoUpdateAddressDescription**

**WdfRegistryAssignMemory**

**WdfRegistryAssignMultiString**

**WdfRegistryAssignString**

**WdfRegistryAssignULong**

**WdfRegistryAssignUnicodeString**

**WdfRegistryAssignValue**

**WdfRegistryCreateKey**

**WdfRegistryOpenKey**

**WdfRegistryQueryMemory**

**WdfRegistryQueryMultiString**

**WdfRegistryQueryString**

**WdfRegistryQueryULong**

**WdfRegistryQueryUnicodeString**

**WdfRegistryQueryValue**

**WdfRegistryRemoveKey**

**WdfRegistryRemoveValue**

**WdfRequestAllocateTimer**

**WdfRequestChangeTarget**

**WdfRequestCreate**

**WdfRequestCreateFromIrp**

**WdfRequestForwardToIoQueue**

**WdfRequestGetStatus**

**WdfRequestProbeAndLockUserBufferForRead**

**WdfRequestProbeAndLockUserBufferForWrite**

**WdfRequestRequeue**

**WdfRequestRetrieveInputBuffer**

**WdfRequestRetrieveInputMemory**

**WdfRequestRetrieveInputWdmMdl**

**WdfRequestRetrieveOutputBuffer**

**WdfRequestRetrieveOutputMemory**

**WdfRequestRetrieveOutputWdmMdl**

**WdfRequestRetrieveUnsafeUserInputBuffer**

**WdfRequestRetrieveUnsafeUserOutputBuffer**

**WdfRequestReuse**

**WdfRequestUnmarkCancelable**

**WdfSpinLockCreate**

**WdfStringCreate**

**WdfTimerCreate**

**WdfUsbInterfaceSelectSetting**

**WdfUsbTargetDeviceAllocAndQueryString**

**WdfUsbTargetDeviceCreate**

**WdfUsbTargetDeviceCyclePortSynchronously**

**WdfUsbTargetDeviceFormatRequestForControlTransfer**

**WdfUsbTargetDeviceFormatRequestForCyclePort**

**WdfUsbTargetDeviceFormatRequestForString**

**WdfUsbTargetDeviceFormatRequestForUrb**

**WdfUsbTargetDeviceIsConnectedSynchronous**

**WdfUsbTargetDeviceQueryString**

**WdfUsbTargetDeviceResetPortSynchronously**

**WdfUsbTargetDeviceRetrieveConfigDescriptor**

**WdfUsbTargetDeviceRetrieveCurrentFrameNumber**

**WdfUsbTargetDeviceRetrieveInformation**

**WdfUsbTargetDeviceSelectConfig**

**WdfUsbTargetDeviceSendControlTransferSynchronously**

**WdfUsbTargetDeviceSendUrbSynchronously**

**WdfUsbTargetPipeAbortSynchronously**

**WdfUsbTargetPipeConfigContinuousReader**

**WdfUsbTargetPipeFormatRequestForAbort**

**WdfUsbTargetPipeFormatRequestForRead**

**WdfUsbTargetPipeFormatRequestForReset**

**WdfUsbTargetPipeFormatRequestForUrb**

**WdfUsbTargetPipeFormatRequestForWrite**

**WdfUsbTargetPipeReadSynchronously**

**WdfUsbTargetPipeResetSynchronously**

**WdfUsbTargetPipeSendUrbSynchronously**

**WdfUsbTargetPipeWriteSynchronously**

**WdfWaitLockAcquire**

**WdfWaitLockCreate**

**WdfWmiInstanceCreate**

**WdfWmiInstanceFireEvent**

**WdfWmiInstanceRegister**

**WdfWmiProviderCreate**

**WdfWorkItemCreate**

 

 





