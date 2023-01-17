---
title: MCDM KM driver implementation guidelines
description: Implementation guidelines for MCDM kernel-mode driver
ms.date: 01/12/2023
---

# MCDM KM driver implementation guidelines

This article provides guidance on how to write the kernel-mode driver portion of a Microsoft Compute Only Driver (MCDM) driver, also referred to as a compute-only driver.

See also the following articles:

* [Microsoft Compute Driver Model overview](mcdm.md)
* [MCDM architecture](mcdm-architecture.md)

## Driver INF file

MCDM devices belong to the **ComputeAccelerator** class, which needs to be specified in the INF file:

``` INF
[Version]
...
Class=ComputeAccelerator
ClassGuid={F01A9D53-3FF6-48D2-9F97-C8A7004BE10C}
...
```

## Driver initialization

A compute-only driver must supply a [**DriverEntry**](driverentry-of-display-miniport-driver.md) function that performs the following steps:

* Allocate and initialize a [**DRIVER_INITIALIZATION_DATA**](/windows-hardware/drivers/ddi/content/dispmprt/ns-dispmprt-_driver_initialization_data) structure. See [Driver function support requirements](#driver-function-support-requirements) for details.
* Call [**DxgkInitialize**](/en-us/windows-hardware/drivers/ddi/content/dispmprt/nf-dispmprt-dxgkinitialize) with the initialized structure.

## Driver function support requirements

A compute-only driver exposes the functions that it implements in the [**DRIVER_INITIALIZATION_DATA**](/windows-hardware/drivers/ddi/content/dispmprt/ns-dispmprt-_driver_initialization_data) structure.

### Minimum required support

At a minimum, a compute-only driver must supply the following device driver interface (DDI) functions:

* [DxgkDdiAddDevice](/windows-hardware/drivers/ddi/content/dispmprt/nc-dispmprt-dxgkddi_add_device)
* [DxgkDdiBuildPagingBuffer](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_buildpagingbuffer)
* [DxgkDdiCalibrateGpuClock](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_calibrategpuclock)
* [DxgkDdiCloseAllocation](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_closeallocation)
* [DxgkDdiCollectDbgInfo](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_collectdbginfo)
* [DxgkDdiCreateAllocation](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_createallocation)
* [DxgkDdiCreateContext](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_createcontext)
* [DxgkDdiCreateDevice](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_createdevice)
* [DxgkDdiDescribeAllocation](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_describeallocation)
* [DxgkDdiDestroyAllocation](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_destroyallocation)
* [DxgkDdiDestroyContext](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_destroycontext)
* [DxgkDdiDestroyDevice](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_destroydevice)
* [DxgkDdiDpcRoutine](/windows-hardware/drivers/ddi/content/dispmprt/nc-dispmprt-dxgkddi_dpc_routine)
* [DxgkDdiFormatHistoryBuffer](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_formathistorybuffer)
* [DxgkDdiGetNodeMetadata](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_getnodemetadata)
* [DxgkDdiGetStandardAllocationDriverData](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_getstandardallocationdriverdata)
* [DxgkDdiInterruptRoutine](/windows-hardware/drivers/ddi/content/dispmprt/nc-dispmprt-dxgkddi_interrupt_routine)
* [DxgkDdiOpenAllocation](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_openallocationinfo)
* [DxgkDdiPreemptCommand](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_preemptcommand)
* [DxgkDdiQueryAdapterInfo](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo) (fore more information, see [DxgkDdiQueryAdapterInfo requirements](#query-adapter-info-requirements))
* [DxgkDdiQueryDependentEngineGroup](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_querydependentenginegroup)
* [DxgkDdiQueryDeviceDescriptor](/windows-hardware/drivers/ddi/content/dispmprt/nc-dispmprt-dxgkddi_query_device_descriptor)
* [DxgkDdiQueryEngineStatus](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_queryenginestatus)
* [DxgkDdiRemoveDevice](/windows-hardware/drivers/ddi/content/dispmprt/nc-dispmprt-dxgkddi_remove_device)
* [DxgkDdiResetDevice](/windows-hardware/drivers/ddi/content/dispmprt/nc-dispmprt-dxgkddi_reset_device)
* [DxgkDdiResetEngine](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_resetengine)
* [DxgkDdiResetFromTimeout](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_resetfromtimeout)
* [DxgkDdiRestartFromTimeout](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_restartfromtimeout)
* [DxgkDdiSetPowerState](./dxgkddisetpowerpstate.md)
* DxgkDdiSetStablePowerState
* DxgkDdiSetVirtualMachineData
* [DxgkDdiStartDevice](/windows-hardware/drivers/ddi/content/dispmprt/nc-dispmprt-dxgkddi_start_device)
* [DxgkDdiStopDevice](/windows-hardware/drivers/ddi/content/dispmprt/nc-dispmprt-dxgkddi_stop_device)
* [DxgkDdiUnload](/windows-hardware/drivers/ddi/content/dispmprt/nc-dispmprt-dxgkddi_unload)
* DxgkDdiQueryChildStatus
* [DxgkDdiQueryChildRelations](/windows-hardware/drivers/ddi/content/dispmprt/nc-dispmprt-dxgkddi_query_child_relations)
* DxgkDdiQueryConnectionChange
* DxgkDdiQueryDeviceDescriptor

### CPU host aperture support

If CPU host aperture is supported, pointers to the following functions must also be provided:

* [DxgkDdiMapCpuHostAperture](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_mapcpuhostaperture)
* [DxgkDdiUnmapCpuHostAperture](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_unmapcpuhostaperture)

For more information, see [CPU host aperture](cpu-host-aperature.md).

### Physical addressing support

If physical addressing is used, pointers to the following functions must also be provided:

* [DxgkDdiPatch](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_patch)
* [DxgkDdiRender](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_render)
* [DxgkDdiSubmitCommand](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_submitcommand)

### GPU virtual addressing support

If GPU virtual addressing is used, pointers to the following functions must also be provided:

* [DxgkDdiCreateProcess](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_createprocess)
* [DxgkDdiDestroyProcess](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_destroyprocess)
* [DxgkDdiGetRootPageTableSize](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_getrootpagetablesize)
* [DxgkDdiSetRootPageTable](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_setrootpagetable)
* [DxgkDdiSubmitCommandVirtual](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_submitcommandvirtual)

### IoMmu isolation support

If IoMmu isolation is supported, pointers to the following functions must also be provided:

* [DxgkDdiBeginExclusiveAccess](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_beginexclusiveaccess)
* [DxgkDdiEndExclusiveAccess](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_endexclusiveaccess)

### Link adapter support

For optional link adapter support, a pointer to the following function must also be provided:

* [DxgkDdiLinkDevice](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_link_device)

### Power management support

For optional power management support, pointers to the following functions must also be provided:

* [DxgkDdiSetPowerComponentFState](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddisetpowercomponentfstate); required if reported components support F-states.
* [DxgkDdiPowerRuntimeControlRequest](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddipowerruntimecontrolrequest)
* DxgkDdiPowerRuntimeSetDeviceHandle

NOTE: power management support is required on Modern Standby or Connected Standby systems.

For more information, see [GPU power management of idle states and active power](gpu-power-management-of-idle-and-active-power.md).

### Surprise removal support

For optional surprise removal support, pointers to the following functions must also be provided:

* [DxgkDdiNotifySurpriseRemoval](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_notify_surprise_removal)

### Cancel support

For optional cancel support, pointers to the following functions must also be provided:

* [DxgkDdiCancelCommand](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_cancelcommand)

### Interface support

For optional interface support, pointers to the following functions must also be provided:

* [DxgkDdiQueryInterface](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_interface)

### Hardware scheduling support

For optional hardware scheduling support, pointers to the following functions must also be provided:

* DxgkDdiCreateHwContext
* DxgkDdiCreateHwQueue
* DxgkDdiDestroyHwContext
* DxgkDdiDestroyHwQueue
* [DxgkDdiPresentToHwQueue](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_presenttohwqueue)
* [DxgkDdiResetHwEngine
* [DxgkDdiResumeContext](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_resumecontext)
* [DxgkDdiResumeHwEngine](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_resumehwengine)
* [DxgkDdiSetContextSchedulingProperties](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_setcontextschedulingproperties)
* [DxgkDdiSetSchedulingLogBuffer](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_setschedulinglogbuffer)
* [DxgkDdiSetupPriorityBands](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_setupprioritybands)
* [DxgkDdiSignalMonitoredFence](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_signalmonitoredfence)
* [DxgkDdiSubmitCommandToHwQueue](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_submitcommandtohwqueue)
* [DxgkDdiSuspendContext](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_suspendcontext)
* [DxgkDdiSwitchToHwContextList](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_switchtohwcontextlist)
* [DxgkDdiUpdateHwContextState](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_updatehwcontextstate)

### UpdateAllocationProperty support

For optional UpdateAllocationProperty support, pointers to the following functions must also be provided:

* DxgkDdiValidateUpdateAllocationProperty

### Escape support

For optional escape support, pointers to the following functions must also be provided:

* [DxgkDdiEscape](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_escape)

### Event Tracing for Windows support

For optional ETW support, pointers to the following functions must also be provided:

* [DxgkDdiControlEtwLogging](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_control_etw_logging)

### Child device support

For optional child device support, pointers to the following functions must also be provided:

* [DxgkDdiGetChildContainerId](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_get_child_container_id)

### Power consumption reporting support

For optional power consumption reporting support, pointers to the following functions must also be provided:

* [DxgkDdiSetTrackedWorkloadPowerLevel](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_settrackedworkloadpowerlevel)

### Command submission validation

For optional command submission validation, pointers to the following functions must also be provided:

* [DxgkDdiValidateSubmitCommand](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_validatesubmitcommand)

### IOCTL support

For optional IOCTL support, a pointer to the following function can be provided:

[DxgkDdiDispatchIoRequest](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_dispatch_io_request)

### Prohibited functions

The following DDIs must not be provided in an MCDM driver:

* DxgkDdiAcquireSwizzlingRange
* DxgkDdiCheckMultiPlaneOverlaySupport
* DxgkDdiCheckMultiPlaneOverlaySupport2
* DxgkDdiCheckMultiPlaneOverlaySupport3
* DxgkDdiCommitVidPn
* DxgkDdiControlDiagnosticReporting
* DxgkDdiControlInterrupt
* DxgkDdiControlInterrupt2
* DxgkDdiControlModeBehavior
* DxgkDdiCreateOverlay
* DxgkDdiCreatePeriodicFrameNotification
* DxgkDdiCreateProtectedSession
* DxgkDdiDestroyOverlay
* DxgkDdiDestroyPeriodicFrameNotification
* DxgkDdiDestroyProtectedSession
* DxgkDdiDisplayDetectControl
* DxgkDdiEnumVidPnCofuncModality
* DxgkDdiExchangePreStartInfo
* DxgkDdiFlipOverlay
* DxgkDdiGetMultiPlaneOverlayCaps
* DxgkDdiGetPostCompositionCaps
* DxgkDdiGetScanLine
* DxgkDdiIsSupportedVidPn
* DxgkDdiNotifyAcpiEvent
* DxgkDdiNotifyFocusPresent
* DxgkDdiPostMultiPlaneOverlayPresent
* DxgkDdiPresent
* DxgkDdiQueryConnectionChange
* DxgkDdiQueryCurrentFence

### WDDM 1.x functions

The following functions are used for WDDM 1.x drivers only:

* DxgkDdiQueryDiagnosticTypesSupport
* DxgkDdiQueryVidPnHWCapability
* DxgkDdiRecommendFunctionalVidPn
* DxgkDdiRecommendMonitorModes
* DxgkDdiRecommendVidPnTopology
* DxgkDdiReleaseSwizzlingRange
* DxgkDdiRenderGdi
* DxgkDdiRenderKm
* DxgkDdiSetDisplayPrivateDriverFormat
* DxgkDdiSetPalette
* DxgkDdiSetPointerPosition
* DxgkDdiSetPointerShape
* DxgkDdiSetPowerPState (the driver shouldn't report any P-state power components)
* DxgkDdiSetTargetAdjustedColorimetry
* DxgkDdiSetTargetAdjustedColorimetry2
* DxgkDdiSetTargetAnalogCopyProtection
* DxgkDdiSetTargetContentType
* DxgkDdiSetTargetGamma
* DxgkDdiSetTimingsFromVidPn
* DxgkDdiSetVideoProtectedRegion
* DxgkDdiSetVidPnSourceAddress
* DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay
* DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay2
* DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay3
* DxgkDdiSetVidPnSourceVisibility
* DxgkDdiStopCapture
* DxgkDdiStopDeviceAndReleasePostDisplayOwnership
* DxgkDdiSubmitRender
* DxgkDdiSystemDisplayEnable
* DxgkDdiSystemDisplayWrite
* DxgkDdiUpdateActiveVidPnPresentPath
* DxgkDdiUpdateMonitorLinkInfo
* DxgkDdiUpdateOverlay

## Query adapter info requirements

As previously stated, a compute-only driver must support [DxgkDdiQueryAdapterInfo](/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo).

The following [DXGK_QUERYADAPTERINFOTYPE](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_queryadapterinfotype) types must be supported:

* DXGKQAITYPE_DRIVERCAPS
* DXGKQAITYPE_NUMPOWERCOMPONENTS
* DXGKQAITYPE_HISTORYBUFFERPRECISION
* DXGKQAITYPE_QUERYSEGMENT4 (for more information, see [Using memory segments to describe the GPU address space](using-memory-segments-to-describe-the-gpu-address-space.md))

Support for the following DXGK_QUERYADAPTERINFOTYPE types is optional:

* DXGK_ADAPTER_PERFDATA
* DXGK_ADAPTER_PERFDATACAPS
* DXGKQAITYPE_UMDRIVERPRIVATE
* DXGKQAITYPE_PHYSICALADAPTERCAPS
* DXGK_NODE_PERFDATA
* DXGK_GPUVERSION

If one or more invalid memory blocks were reported, the following DXGK_QUERYADAPTERINFOTYPE must be supported:

* DXGKQAITYPE_SEGMENTMEMORYSTATE

If GPUVA is supported, the following DXGK_QUERYADAPTERINFOTYPE must be supported:

* DXGKQAITYPE_GPUMMUCAPS
* DXGKQAITYPE_PAGETABLELEVELDESC

If the number of power components reported is greater than zero, the following DXGK_QUERYADAPTERINFOTYPE must be supported:

* DXGKQAITYPE_POWERCOMPONENTINFO

If the [IoMmuSecureModeSupported](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-dxgk_iommu_caps) cap is set, the following DXGK_QUERYADAPTERINFOTYPE must be supported:

* DXGKQAITYPE_FRAMEBUFFERSAVESIZE
* DXGKQAITYPE_HARDWARERESERVEDRANGES

The following DXGK_QUERYADAPTERINFOTYPE must not be supported:

* DXGKQAITYPE_DEVICE_TYPE_CAPS
* DXGKQAITYPE_DISPLAY_DRIVERCAPS_EXTENSION
* DXGKQAITYPE_DISPLAYID_DESCRIPTOR
* DXGKQAITYPE_INTEGRATED_DISPLAY_DESCRIPTOR
* DXGKQAITYPE_INTEGRATED_DISPLAY_DESCRIPTOR2
* DXGKQAITYPE_POWERCOMPONENTPSTATEINFO
* DXGKQAITYPE_PREFERREDGPUNODE
* DXGKQAITYPE_QUERYCOLORIMETRYOVERRIDES
* DXGKQAITYPE_QUERYSEGMENT
* DXGKQAITYPE_QUERYSEGMENT2
* DXGKQAITYPE_QUERYSEGMENT3
* DXGKQAITYPE_UEFIFRAMEBUFFERRANGES

## Driver capability requirements

The following [DXGK_DRIVERCAPS](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_drivercaps) structure members must be set to appropriate values:

| Member | Notes |
| ------ | ----- |
| HighestAcceptableAddress  | If this address is less than the highest physical address of the system memory that is present during driver load, the load will fail. |
| InterruptMessageNumber    | Set as appropriate. |
| [SchedulingCaps](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidschcaps) | See [SchedulingCaps requirements](#schedulingcaps-requirements). |
| [MemoryManagementCaps](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidmmcaps) | See [MemoryManagementCaps requirements](#memorymanagementcaps-requirements). |
| [GpuEngineTopology](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_gpuenginetopology) | Set **NbAsymetricProcessingNodes** to the number supported GPU engines. |
| [WDDMVersion](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_wddmversion) | Must be set to DXGKDDI_WDDMv2_6 or later. |
| [PreemptionCaps](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_preemption_caps)  | Set **GraphicsPreemptionGranularity** appropriately to the level supported by the hardware. At a minimum you should attempt to support packet-level preemption; that is, a dequeue packet that has been scheduled but hasn't yet started executing. Set **ComputePreemptionGranularity** to anything other than D3DKMDT_COMPUTE_PREEMPTION_NONE. |
| SupportPerEngineTDR | Must be set to TRUE. See [TDR Changes in Windows 8 and later](tdr-changes-in-windows-8.md). |
| SupportRuntimePowerManagement | Set as appropriate. See [GPU power management of idle states and active power](gpu-power-management-of-idle-and-active-power.md). |
| SupportSurpriseRemovalInHibernation | Set to TRUE if the driver supports surprise removal when in hibernation; otherwise set as appropriate. See [DXGKDDI_NOTIFY_SURPRISE_REMOVAL](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_notify_surprise_removal). |
| HybridDiscrete   | Must be set to FALSE. |
| HybridIntegrated | Must be set to FALSE. |
| InternalGpuVirtualAddressRangeStart | Set as appropriate. If GpuVA isn't supported, set to zero. If GpuVA is supported, this value specifies the start of the VA range that the OS will use when allocating internal resources for OS internal use. |
| InternalGpuVirtualAddressRangeEnd | Set as appropriate. If GpuVA isn't supported, set to zero. If GpuVA is supported, this value specifies the end of the VA range that the OS will use when allocating internal resources for OS internal use. If both the start and end values are zero, the OS will use the entire available VA range. |
| SupportSurpriseRemoval | Set as appropriate. Set to TRUE if the driver supports surprise removal even outside of hibernation. See [DXGKDDI_NOTIFY_SURPRISE_REMOVAL](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_notify_surprise_removal). |
| ComputeOnly | Must be set to TRUE. This flag must be implemented. |

The following [DXGK_DRIVERCAPS](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_drivercaps) structure members must be set to zero or FALSE, accordingly:

* MaxAllocationListSlotId
* ApertureSegmentCommitLimit
* MaxPointerWidth
* MaxPointerHeight
* PointerCaps
* NumberOfSwizzlingRanges
* MaxOverlays
* GammaRampCaps
* ColorTransformCaps
* PresentationCaps
* MaxQueuedFlipOnVSync
* FlipCaps
* SupportNonVGA
* SupportSmoothRotation
* SupportDirectFlip
* SupportMultiPlaneOverlay
* MaxOverlayPlanes
* SupportMultiPlaneOverlayImmediateFlip
* CursorScaledWithMultiPlaneOverlayPlane0
* HybridAcpiChainingRequired
* MaxQueuedMultiPlaneOverlayFlipVSync
* SupportContextlessPresent
* Detachable

### SchedulingCaps requirements

The following [DXGK_DRIVERCAPS](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_drivercaps).[SchedulingCaps](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidschcaps) structure members must be set to appropriate values:

| Member                    | Notes |
| ------                    | ----- |
| MultiEngineAware          | Must be set to TRUE. See [GPU Preemption](gpu-preemption.md). |
| VSyncPowerSaveAware       | Must be set to FALSE. |
| PreemptionAware           | Must be set to TRUE. See [GPU Preemption](gpu-preemption.md). |
| NoDmaPatching             | Must be set to FALSE. |
| CancelCommandAware        | Set as appropriate. See [DXGKDDI_CANCELCOMMAND](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_cancelcommand). |
| No64BitAtomics            | Set as appropriate. See [Context Monitoring](context-monitoring.md). |
| LowIrqlPreemptCommand     | Set to TRUE. The OS will call the driver's [DxgkDdiPreemptCommand](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_preemptcommand) at low IRQL. |
| HwQueuePacketCap          | Reserved; set to zero. |

### MemoryManagementCaps requirements

The following [DXGK_DRIVERCAPS](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_drivercaps).[MemoryManagementCaps](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidmmcaps) structure members must be set to appropriate values:

| Member                      | Notes |
| ------                      | ----- |
| OutOfOrderLock              | Must be set to FALSE. |
| DedicatedPagingEngine       | Must be set to FALSE. |
| PagingEngineCanSwizzle      | Must be set to FALSE. |
| SectionBackedPrimary        | Must be set to FALSE. |
| CrossAdapterResource        | Set as appropriate. See [Using Cross Adapter Resources in a Hybrid System](using-cross-adapter-resources-in-a-hybrid-system.md). |
| VirtualAddressingSupported  | Set as appropriate. See [GPU Virtual Memory In WDDM 2.0](gpu-virtual-memory-in-wddm-2-0.md). If this member is set, the driver must also set GpuMmuSupported and/or IoMmuSupported. |
| GpuMmuSupported             | Set as appropriate. See [GpuMmu Model](gpummu-model.md). |
| IoMmuSupported              | Set as appropriate. This cap is set when the device shares page tables with the CPU (shared virtual memory (SVM)). See [IoMmu Model](iommu-model.md). |
| ReplicateGdiContent         | Must be set to FALSE. |
| NonCpuVisiblePrimary        | Must be set to FALSE. |
| ParavirtualizationSupported | MCDM host drivers that support the virtualization of the device through the GPU partitioning interface (GPU-P with SR-IOV) should set this field to FALSE. All other cases (drivers for physical machines without GPU-P support or guest drivers of vGPUs that have been exposed through GPU-P) should set this field to TRUE. |
| IoMmuSecureModeSupported    | Set as appropriate. If this cap is set TRUE, the driver supports IoMmu isolation (the device has a dedicated page table for the IoMmu unit). If this cap is set FALSE, the device can't be used in the "secure" virtual machines (Windows Sandbox or MDAG). |
| DisableSelfRefreshVRAMInS3  | Set as appropriate. |

## Memory Management

Virtual addressing is required. Physical addressing support might be enabled in the future.

Devices aren't required to support a memory aperture.

Only [linear memory-space segments](linear-memory-space-segments.md) and [linear aperture-space segments](linear-aperture-space-segments.md) are supported.