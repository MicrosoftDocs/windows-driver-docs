---
title: KMDF Functions that Return NSTATUS Codes
description: KMDF Functions that Return NSTATUS Codes
ms.assetid: 0edd35c0-2357-4502-8c59-36b16cf7f294
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20KMDF%20Functions%20that%20Return%20NSTATUS%20Codes%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




