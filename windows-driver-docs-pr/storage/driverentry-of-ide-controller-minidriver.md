---
title: DriverEntry of IDE Controller Minidriver Function
description: DriverEntry initializes the minidriver.
keywords: ["DriverEntry function Storage Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- DriverEntry
api_location:
- NtosKrnl.exe
api_type:
- DllExport
ms.date: 03/13/2024
---

# DriverEntry of IDE Controller Minidriver function

An IDE controller minidriver's **DriverEntry** initializes driver-wide data structures and resources.

## Syntax

```ManagedCPlusPlus
NTSTATUS DriverEntry(
  _In_ PDRIVER_OBJECT  DriverObject,
  _In_ PUNICODE_STRING RegistryPath
);
```

## Parameters

**DriverObject** contains a pointer to the IDE controller minidriver's driver object.

**RegistryPath** specifies a string indicating the path to the driver's configuration information in the registry.

## Return value

**DriverEntry** returns STATUS_SUCCESS if successful; otherwise it returns the NTSTATUS code received from the [**PciIdeXInitialize**](/previous-versions/windows/hardware/drivers/ff563788(v=vs.85)) library routine.

## Remarks

Each controller minidriver must have a routine named **DriverEntry** in order to load.

An IDE controller minidriver's **DriverEntry** routine must call the [**PciIdeXInitialize**](/previous-versions/windows/hardware/drivers/ff563788(v=vs.85)) library routine. **PciIdeXInitialize** initializes the controller minidriver's dispatch tables, allocates an extension for the *DriverObject*, and stores various values in the driver object's extension. Values that must be stored in the driver object's extension include the size of the driver extension and a pointer to a controller minidriver [**HwIdeXGetControllerProperties**](/previous-versions/windows/hardware/drivers/ff557254(v=vs.85)) routine that retrieves information about the IDE controller.

## Requirements

| Category | Requirement |
| -------- | ----------- |
| Target platform | Desktop |
| Header          | *Ide.h* (include *Ide.h*) |
| Library         | *NtosKrnl.lib* |
| DLL             | *NtosKrnl.exe* |

## See also

[**HwIdeXGetControllerProperties**](/previous-versions/windows/hardware/drivers/ff557254(v=vs.85))

[**IDE_CONTROLLER_PROPERTIES**](/previous-versions/windows/hardware/drivers/ff559076(v=vs.85))

[**PciIdeXInitialize**](/previous-versions/windows/hardware/drivers/ff563788(v=vs.85))
