---
title: DriverEntry of Display Miniport Driver Function
description: The DriverEntry function provides the DirectX graphics kernel subsystem with a set of pointers to functions implemented by the display miniport driver.
keywords: ["DriverEntry function Display Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- DriverEntry
api_location:
- NtosKrnl.exe
api_type:
- DllExport
ms.date: 04/05/2024
---

# DriverEntry function of a display miniport driver

The **DriverEntry** function provides the DirectX graphics kernel subsystem (*Dxgkrnl*) with a set of pointers to functions that the display miniport driver (KMD) implements.

## Syntax

```ManagedCPlusPlus
NTSTATUS DriverEntry(
  _In_ PDRIVER_OBJECT  DriverObject,
  _In_ PUNICODE_STRING RegistryPath
);
```

## Parameters

**DriverObject** is a pointer to a [**DRIVER_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_driver_object) structure that represents the driver formed by the (display miniport, display port) driver pair.

**RegistryPath** is a pointer to a [**UNICODE_STRING**](/windows-hardware/drivers/ddi/wudfwdm/ns-wudfwdm-_unicode_string) structure that supplies the path to the driver's registry key.

## Return value

**DriverEntry** must return the value returned by the call to [**DxgkInitialize**](/windows-hardware/drivers/ddi/dispmprt/nf-dispmprt-dxgkinitialize).

## Remarks

**DriverEntry** must perform the following steps:

1. Allocate a [**DRIVER_INITIALIZATION_DATA**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_driver_initialization_data) structure, and set its **Version** member to **DXGKDDI_INTERFACE_VERSION**, which is defined in *Dispmprt.h*.

2. Fill in the remaining members of [**DRIVER_INITIALIZATION_DATA**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_driver_initialization_data) with pointers to the functions that KMD implements.

3. Pass **DriverObject**, **RegistryPath**, and the filled in [**DRIVER_INITIALIZATION_DATA**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_driver_initialization_data) structure to [**DxgkInitialize**](/windows-hardware/drivers/ddi/dispmprt/nf-dispmprt-dxgkinitialize).

4. Return the value returned by [**DxgkInitialize**](/windows-hardware/drivers/ddi/dispmprt/nf-dispmprt-dxgkinitialize).

The [**DRIVER_INITIALIZATION_DATA**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_driver_initialization_data) structure doesn't need to remain in memory after **DriverEntry** returns.

**DriverEntry** should be made pageable.

### DriverEntry for a kernel-mode display-only driver

For the kernel-mode display-only driver (KMDOD) interface, the [**KMDDOD_INITIALIZATION_DATA**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_kmddod_initialization_data) structure lists all functions that can be implemented by a KMDOD. All of these functions, except for the [**DxgkDdiPresentDisplayOnly**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_presentdisplayonly) function, can also be implemented by a full display miniport driver (KMD). The KMDOD's **DriverEntry** function supplies function pointers to the display port driver by filling in all members of **KMDDOD_INITIALIZATION_DATA** and then passing that structure to the [**DxgkInitializeDisplayOnlyDriver**](/windows-hardware/drivers/ddi/dispmprt/nf-dispmprt-dxgkinitializedisplayonlydriver) function.

If a KMDOD doesn't support the VSync control feature, it shouldn't implement certain functions. See [Saving Energy with VSync Control](saving-energy-with-vsync-control.md).

The following structures and enumeration are also used with KMDODs:

* [D3DKMT_MOVE_RECT](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmt_move_rect)
* [D3DKMT_PRESENT_DISPLAY_ONLY_FLAGS](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_d3dkmt_present_display_only_flags)
* [DXGK_PRESENT_DISPLAY_ONLY_PROGRESS_ID](/windows-hardware/drivers/ddi/d3dkmddi/ne-d3dkmddi-_dxgk_present_display_only_progress_id)
* [DXGKARG_PRESENT_DISPLAYONLY](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_present_displayonly)
* [DXGKARGCB_PRESENT_DISPLAYONLY_PROGRESS](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkargcb_present_displayonly_progress)

## Requirements

| Requirement | Detail |
| ----------- | ------ |
| Target platform | Desktop |
| Minimum supported client | Windows Vista  |
| Library | *NtosKrnl.lib* |
| DLL | *NtosKrnl.exe* |

## See also

[**DxgkInitialize**](/windows-hardware/drivers/ddi/dispmprt/nf-dispmprt-dxgkinitialize)

[***DxgkDdiUnload***](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_unload)
