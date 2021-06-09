---
title: DriverEntry of Display Miniport Driver function
description: The DriverEntry function provides the Microsoft DirectX graphics kernel subsystem with a set of pointers to functions implemented by the display miniport driver.
keywords: ["DriverEntry function Display Devices"]
topic_type:
- apiref
api_name:
- DriverEntry
api_location:
- NtosKrnl.exe
api_type:
- DllExport
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# DriverEntry of Display Miniport Driver function


The **DriverEntry** function provides the Microsoft DirectX graphics kernel subsystem with a set of pointers to functions implemented by the display miniport driver.

## Syntax

```ManagedCPlusPlus
NTSTATUS DriverEntry(
  _In_ PDRIVER_OBJECT  DriverObject,
  _In_ PUNICODE_STRING RegistryPath
);
```

## Parameters

*DriverObject* \[in\]
A pointer to a [**DRIVER\_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_driver_object) structure that represents the driver formed by the (display miniport, display port) driver pair.

*RegistryPath* \[in\]
A pointer to a [**UNICODE\_STRING**](/windows-hardware/drivers/ddi/wudfwdm/ns-wudfwdm-_unicode_string) structure that supplies the path to the driver's registry key.

## Return value

**DriverEntry** calls [**DxgkInitialize**](/windows-hardware/drivers/ddi/dispmprt/nf-dispmprt-dxgkinitialize) and must return the value returned by **DxgkInitialize**.

## Remarks

**DriverEntry** must perform the following steps:

1.  Allocate a [**DRIVER\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_driver_initialization_data) structure, and set its **Version** member to DXGKDDI\_INTERFACE\_VERSION, which is defined in Dispmprt.h.

2.  Fill in the remaining members of the [**DRIVER\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_driver_initialization_data) structure with pointers to the following functions, which are implemented by the display miniport driver.

    -   [*DxgkDdiAcquireSwizzlingRange*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_acquireswizzlingrange)
    -   [*DxgkDdiAddDevice*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_add_device)
    -   [*DxgkDdiBuildPagingBuffer*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_buildpagingbuffer)
    -   [*DxgkDdiCalibrateGpuClock*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_calibrategpuclock) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WDDM1\_3)
    -   [*DxgkDdiCancelCommand*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_cancelcommand) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiCheckMultiPlaneOverlaySupport*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_checkmultiplaneoverlaysupport) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiCloseAllocation*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_closeallocation)
    -   [*DxgkDdiCollectDbgInfo*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_collectdbginfo)
    -   [*DxgkDdiCommitVidPn*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_commitvidpn)
    -   [*DxgkDdiControlEtwLogging*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_control_etw_logging)
    -   [*DxgkDdiControlInterrupt*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_controlinterrupt)
    -   [*DxgkDdiCreateAllocation*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createallocation)
    -   [*DxgkDdiCreateContext*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createcontext)
    -   [*DxgkDdiCreateDevice*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createdevice)
    -   [*DxgkDdiCreateOverlay*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createoverlay)
    -   [*DxgkDdiDescribeAllocation*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_describeallocation)
    -   [*DxgkDdiDestroyAllocation*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_destroyallocation)
    -   [*DxgkDdiDestroyContext*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_destroycontext)
    -   [*DxgkDdiDestroyDevice*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_destroydevice)
    -   [*DxgkDdiDestroyOverlay*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_destroyoverlay)
    -   [*DxgkDdiDispatchIoRequest*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_dispatch_io_request)
    -   [*DxgkDdiDpcRoutine*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_dpc_routine)
    -   [*DxgkDdiEnumVidPnCofuncModality*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_enumvidpncofuncmodality)
    -   [*DxgkDdiEscape*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_escape)
    -   [*DxgkDdiFlipOverlay*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_flipoverlay)
    -   [*DxgkDdiFormatHistoryBuffer*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_formathistorybuffer) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiGetChildContainerId*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_get_child_container_id) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiGetNodeMetadata*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_getnodemetadata) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiGetScanLine*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_getscanline)
    -   [*DxgkDdiGetStandardAllocationDriverData*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_getstandardallocationdriverdata)
    -   [*DxgkDdiInterruptRoutine*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_interrupt_routine)
    -   [*DxgkDdiIsSupportedVidPn*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_issupportedvidpn)
    -   [*DxgkDdiLinkDevice*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_link_device)
    -   [*DxgkDdiNotifyAcpiEvent*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_notify_acpi_event) (optional)
    -   [*DxgkDdiNotifySurpriseRemoval*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_notify_surprise_removal) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiOpenAllocation*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_openallocationinfo)
    -   [*DxgkDdiPatch*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_patch)
    -   [*DxgkDdiPowerRuntimeControlRequest*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddipowerruntimecontrolrequest) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiPreemptCommand*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_preemptcommand)
    -   [*DxgkDdiPresent*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_present)
    -   [*DxgkDdiQueryAdapterInfo*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo)
    -   [*DxgkDdiQueryChildRelations*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_child_relations)
    -   [*DxgkDdiQueryChildStatus*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_child_status)
    -   [*DxgkDdiQueryCurrentFence*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_querycurrentfence)
    -   [*DxgkDdiQueryDependentEngineGroup*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_querydependentenginegroup) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiQueryDeviceDescriptor*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_device_descriptor)
    -   [*DxgkDdiQueryEngineStatus*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryenginestatus) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiQueryInterface*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_interface)
    -   [*DxgkDdiQueryVidPnHWCapability*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryvidpnhwcapability) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN7)
    -   [*DxgkDdiRecommendFunctionalVidPn*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_recommendfunctionalvidpn)
    -   [*DxgkDdiRecommendMonitorModes*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_recommendmonitormodes)
    -   [*DxgkDdiRecommendVidPnTopology*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_recommendvidpntopology)
    -   [*DxgkDdiReleaseSwizzlingRange*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_releaseswizzlingrange)
    -   [*DxgkDdiRemoveDevice*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_remove_device)
    -   [*DxgkDdiRender*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_render)
    -   [*DxgkDdiRenderKm*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_renderkm) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN7)
    -   [*DxgkDdiResetDevice*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_reset_device)
    -   [*DxgkDdiResetEngine*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_resetengine) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiResetFromTimeout*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_resetfromtimeout)
    -   [*DxgkDdiRestartFromTimeout*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_restartfromtimeout)
    -   [*DxgkDdiSetDisplayPrivateDriverFormat*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_setdisplayprivatedriverformat)
    -   [*DxgkDdiSetPalette*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_setpalette)
    -   [*DxgkDdiSetPointerPosition*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_setpointerposition)
    -   [*DxgkDdiSetPointerShape*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_setpointershape)
    -   [*DxgkDdiSetPowerComponentFState*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddisetpowercomponentfstate) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiSetPowerState*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_set_power_state)
    -   [*DxgkDdiSetVidPnSourceAddress*](/previous-versions/windows/hardware/drivers/ff560767(v=vs.85))
    -   [*DxgkDdiSetVidPnSourceVisibility*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_setvidpnsourcevisibility)
    -   [*DxgkDdiStartDevice*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_start_device)
    -   [*DxgkDdiStopCapture*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_stopcapture)
    -   [*DxgkDdiStopDevice*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_stop_device)
    -   [*DxgkDdiStopDeviceAndReleasePostDisplayOwnership*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_stop_device_and_release_post_display_ownership) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiSubmitCommand*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_submitcommand)
    -   [*DxgkDdiSystemDisplayEnable*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_system_display_enable) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiSystemDisplayWrite*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_system_display_write) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiUnload*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_unload)
    -   [*DxgkDdiUpdateActiveVidPnPresentPath*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_updateactivevidpnpresentpath)
    -   [*DxgkDdiUpdateOverlay*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_updateoverlay)


3.  Pass *DriverObject*, *RegistryPath*, and the filled in [**DRIVER\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_driver_initialization_data) structure to [**DxgkInitialize**](/windows-hardware/drivers/ddi/dispmprt/nf-dispmprt-dxgkinitialize).

4.  Return the value returned by [**DxgkInitialize**](/windows-hardware/drivers/ddi/dispmprt/nf-dispmprt-dxgkinitialize).

The [**DRIVER\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_driver_initialization_data) structure does not need to remain in memory after **DriverEntry** returns.

**DriverEntry** should be made pageable.

For kernel mode display-only driver (KMDOD) interface, the [KMDDOD_INITIALIZATION_DATA](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_kmddod_initialization_data) structure lists all functions that can be implemented by a KMDOD. All of these functions, except for the [DxgkDdiPresentDisplayOnly](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_presentdisplayonly) function, can also be implemented by a full display miniport driver.  The DriverEntry function of the kernel mode display-only driver (KMDOD) supplies function pointers to the display port driver by filling in all members of a KMDDOD_INITIALIZATION_DATA structure and then passing that structure to the [DxgkInitializeDisplayOnlyDriver](/windows-hardware/drivers/ddi/dispmprt/nf-dispmprt-dxgkinitializedisplayonlydriver) function.

Note that if a KMDOD does not support the VSync control feature, it should not implement certain functions—see Saving Energy with VSync Control.

The following structures and enumeration are also used with kernel mode display-only drivers:

* [D3DKMT_MOVE_RECT](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmt_move_rect)
* [D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_d3dkmt_present_display_only_flags)
* [DXGK_PRESENT_DISPLAY_ONLY_PROGRESS_ID](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_present_display_only_progress_id)
* [DXGKARG_PRESENT_DISPLAYONLY](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_present_displayonly)
* [DXGKARGCB_PRESENT_DISPLAYONLY_PROGRESS](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkargcb_present_displayonly_progress)


## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Library</p></td>
<td align="left">NtosKrnl.lib</td>
</tr>
<tr class="even">
<td align="left"><p>DLL</p></td>
<td align="left">NtosKrnl.exe</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**DxgkInitialize**](/windows-hardware/drivers/ddi/dispmprt/nf-dispmprt-dxgkinitialize)

[*DxgkDdiUnload*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_unload)

