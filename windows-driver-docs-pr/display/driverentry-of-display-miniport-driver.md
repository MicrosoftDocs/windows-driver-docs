---
title: DriverEntry of Display Miniport Driver function
description: The DriverEntry function provides the Microsoft DirectX graphics kernel subsystem with a set of pointers to functions implemented by the display miniport driver.
ms.assetid: 64b4e9d5-eb6e-48ab-95bf-a237ec32a54b
keywords: ["DriverEntry function Display Devices"]
topic_type:
- apiref
api_name:
- DriverEntry
api_location:
- NtosKrnl.exe
api_type:
- DllExport
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DriverEntry of Display Miniport Driver function


The **DriverEntry** function provides the Microsoft DirectX graphics kernel subsystem with a set of pointers to functions implemented by the display miniport driver.

Syntax
------

```ManagedCPlusPlus
NTSTATUS DriverEntry(
  _In_ PDRIVER_OBJECT  DriverObject,
  _In_ PUNICODE_STRING RegistryPath
);
```

Parameters
----------

*DriverObject* \[in\]
A pointer to a [**DRIVER\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff544174) structure that represents the driver formed by the (display miniport, display port) driver pair.

*RegistryPath* \[in\]
A pointer to a [**UNICODE\_STRING**](https://msdn.microsoft.com/library/windows/hardware/ff564879) structure that supplies the path to the driver's registry key.

Return value
------------

**DriverEntry** calls [**DxgkInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff560824) and must return the value returned by **DxgkInitialize**.

Remarks
-------

**DriverEntry** must perform the following steps:

1.  Allocate a [**DRIVER\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff556169) structure, and set its **Version** member to DXGKDDI\_INTERFACE\_VERSION, which is defined in Dispmprt.h.

2.  Fill in the remaining members of the [**DRIVER\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff556169) structure with pointers to the following functions, which are implemented by the display miniport driver:

    -   [*DxgkDdiAcquireSwizzlingRange*](https://msdn.microsoft.com/library/windows/hardware/ff559582)
    -   [*DxgkDdiAddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559586)
    -   [*DxgkDdiBuildPagingBuffer*](https://msdn.microsoft.com/library/windows/hardware/ff559587)
    -   [*DxgkDdiCalibrateGpuClock*](https://msdn.microsoft.com/library/windows/hardware/dn467321) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WDDM1\_3)
    -   [*DxgkDdiCancelCommand*](https://msdn.microsoft.com/library/windows/hardware/hh451344) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiCheckMultiPlaneOverlaySupport*](https://msdn.microsoft.com/library/windows/hardware/dn282642) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiCloseAllocation*](https://msdn.microsoft.com/library/windows/hardware/ff559592)
    -   [*DxgkDdiCollectDbgInfo*](https://msdn.microsoft.com/library/windows/hardware/ff559595)
    -   [*DxgkDdiCommitVidPn*](https://msdn.microsoft.com/library/windows/hardware/ff559597)
    -   [*DxgkDdiControlEtwLogging*](https://msdn.microsoft.com/library/windows/hardware/ff559599)
    -   [*DxgkDdiControlInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559602)
    -   [*DxgkDdiCreateAllocation*](https://msdn.microsoft.com/library/windows/hardware/ff559606)
    -   [*DxgkDdiCreateContext*](https://msdn.microsoft.com/library/windows/hardware/ff559612)
    -   [*DxgkDdiCreateDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559615)
    -   [*DxgkDdiCreateOverlay*](https://msdn.microsoft.com/library/windows/hardware/ff559616)
    -   [*DxgkDdiDescribeAllocation*](https://msdn.microsoft.com/library/windows/hardware/ff559620)
    -   [*DxgkDdiDestroyAllocation*](https://msdn.microsoft.com/library/windows/hardware/ff559630)
    -   [*DxgkDdiDestroyContext*](https://msdn.microsoft.com/library/windows/hardware/ff559636)
    -   [*DxgkDdiDestroyDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559639)
    -   [*DxgkDdiDestroyOverlay*](https://msdn.microsoft.com/library/windows/hardware/ff559642)
    -   [*DxgkDdiDispatchIoRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559643)
    -   [*DxgkDdiDpcRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff559645)
    -   [*DxgkDdiEnumVidPnCofuncModality*](https://msdn.microsoft.com/library/windows/hardware/ff559649)
    -   [*DxgkDdiEscape*](https://msdn.microsoft.com/library/windows/hardware/ff559653)
    -   [*DxgkDdiFlipOverlay*](https://msdn.microsoft.com/library/windows/hardware/ff559655)
    -   [*DxgkDdiFormatHistoryBuffer*](https://msdn.microsoft.com/library/windows/hardware/dn439360) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiGetChildContainerId*](https://msdn.microsoft.com/library/windows/hardware/hh451349) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiGetNodeMetadata*](https://msdn.microsoft.com/library/windows/hardware/dn265415) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiGetScanLine*](https://msdn.microsoft.com/library/windows/hardware/ff559668)
    -   [*DxgkDdiGetStandardAllocationDriverData*](https://msdn.microsoft.com/library/windows/hardware/ff559673)
    -   [*DxgkDdiInterruptRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff559680)
    -   [*DxgkDdiIsSupportedVidPn*](https://msdn.microsoft.com/library/windows/hardware/ff559684)
    -   [*DxgkDdiLinkDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559687)
    -   [*DxgkDdiNotifyAcpiEvent*](https://msdn.microsoft.com/library/windows/hardware/ff559695) (optional)
    -   [*DxgkDdiNotifySurpriseRemoval*](https://msdn.microsoft.com/library/windows/hardware/hh780297) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiOpenAllocation*](https://msdn.microsoft.com/library/windows/hardware/ff559699)
    -   [*DxgkDdiPatch*](https://msdn.microsoft.com/library/windows/hardware/ff559737)
    -   [*DxgkDdiPowerRuntimeControlRequest*](https://msdn.microsoft.com/library/windows/hardware/hh451396) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiPreemptCommand*](https://msdn.microsoft.com/library/windows/hardware/ff559741)
    -   [*DxgkDdiPresent*](https://msdn.microsoft.com/library/windows/hardware/ff559743)
    -   [*DxgkDdiQueryAdapterInfo*](https://msdn.microsoft.com/library/windows/hardware/ff559746)
    -   [*DxgkDdiQueryChildRelations*](https://msdn.microsoft.com/library/windows/hardware/ff559750)
    -   [*DxgkDdiQueryChildStatus*](https://msdn.microsoft.com/library/windows/hardware/ff559754)
    -   [*DxgkDdiQueryCurrentFence*](https://msdn.microsoft.com/library/windows/hardware/ff559758)
    -   [*DxgkDdiQueryDependentEngineGroup*](https://msdn.microsoft.com/library/windows/hardware/hh451407) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiQueryDeviceDescriptor*](https://msdn.microsoft.com/library/windows/hardware/ff559761)
    -   [*DxgkDdiQueryEngineStatus*](https://msdn.microsoft.com/library/windows/hardware/hh451411) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiQueryInterface*](https://msdn.microsoft.com/library/windows/hardware/ff559764)
    -   [*DxgkDdiQueryVidPnHWCapability*](https://msdn.microsoft.com/library/windows/hardware/ff559771) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN7)
    -   [*DxgkDdiRecommendFunctionalVidPn*](https://msdn.microsoft.com/library/windows/hardware/ff559775)
    -   [*DxgkDdiRecommendMonitorModes*](https://msdn.microsoft.com/library/windows/hardware/ff559780)
    -   [*DxgkDdiRecommendVidPnTopology*](https://msdn.microsoft.com/library/windows/hardware/ff559782)
    -   [*DxgkDdiReleaseSwizzlingRange*](https://msdn.microsoft.com/library/windows/hardware/ff559786)
    -   [*DxgkDdiRemoveDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559789)
    -   [*DxgkDdiRender*](https://msdn.microsoft.com/library/windows/hardware/ff559793)
    -   [*DxgkDdiRenderKm*](https://msdn.microsoft.com/library/windows/hardware/ff559800) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN7)
    -   [*DxgkDdiResetDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559808)
    -   [*DxgkDdiResetEngine*](https://msdn.microsoft.com/library/windows/hardware/hh451418) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiResetFromTimeout*](https://msdn.microsoft.com/library/windows/hardware/ff559815)
    -   [*DxgkDdiRestartFromTimeout*](https://msdn.microsoft.com/library/windows/hardware/ff559820)
    -   [*DxgkDdiSetDisplayPrivateDriverFormat*](https://msdn.microsoft.com/library/windows/hardware/ff560751)
    -   [*DxgkDdiSetPalette*](https://msdn.microsoft.com/library/windows/hardware/ff560754)
    -   [*DxgkDdiSetPointerPosition*](https://msdn.microsoft.com/library/windows/hardware/ff560757)
    -   [*DxgkDdiSetPointerShape*](https://msdn.microsoft.com/library/windows/hardware/ff560762)
    -   [*DxgkDdiSetPowerComponentFState*](https://msdn.microsoft.com/library/windows/hardware/hh451422) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiSetPowerState*](https://msdn.microsoft.com/library/windows/hardware/ff560764)
    -   [*DxgkDdiSetVidPnSourceAddress*](https://msdn.microsoft.com/library/windows/hardware/ff560767)
    -   [*DxgkDdiSetVidPnSourceVisibility*](https://msdn.microsoft.com/library/windows/hardware/ff560771)
    -   [*DxgkDdiStartDevice*](https://msdn.microsoft.com/library/windows/hardware/ff560775)
    -   [*DxgkDdiStopCapture*](https://msdn.microsoft.com/library/windows/hardware/ff560776)
    -   [*DxgkDdiStopDevice*](https://msdn.microsoft.com/library/windows/hardware/ff560781)
    -   [*DxgkDdiStopDeviceAndReleasePostDisplayOwnership*](https://msdn.microsoft.com/library/windows/hardware/hh451415) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiSubmitCommand*](https://msdn.microsoft.com/library/windows/hardware/ff560790)
    -   [*DxgkDdiSystemDisplayEnable*](https://msdn.microsoft.com/library/windows/hardware/hh451426) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiSystemDisplayWrite*](https://msdn.microsoft.com/library/windows/hardware/hh451429) (DXGKDDI\_INTERFACE\_VERSION &gt;= DXGKDDI\_INTERFACE\_VERSION\_WIN8)
    -   [*DxgkDdiUnload*](https://msdn.microsoft.com/library/windows/hardware/ff560801)
    -   [*DxgkDdiUpdateActiveVidPnPresentPath*](https://msdn.microsoft.com/library/windows/hardware/ff560803)
    -   [*DxgkDdiUpdateOverlay*](https://msdn.microsoft.com/library/windows/hardware/ff560804)

    Additional *DxgkDdiXxx* functions that can be implemented by display miniport drivers are described in the interfaces listed in [Kernel-Mode Interfaces Implemented By the Display Miniport Driver](https://msdn.microsoft.com/library/windows/hardware/hh451569).

3.  Pass *DriverObject*, *RegistryPath*, and the filled in [**DRIVER\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff556169) structure to [**DxgkInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff560824).

4.  Return the value returned by [**DxgkInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff560824).

The [**DRIVER\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff556169) structure does not need to remain in memory after **DriverEntry** returns.

**DriverEntry** should be made pageable.

Requirements
------------

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


[**DxgkInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff560824)

[*DxgkDdiUnload*](https://msdn.microsoft.com/library/windows/hardware/ff560801)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DriverEntry%20of%20Display%20Miniport%20Driver%20function%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





