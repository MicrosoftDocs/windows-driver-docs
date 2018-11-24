---
title: '_Kernel_IoGetDmaAdapter_ Annotation for drivers'
description: Use the _Kernel_IoGetDmaAdapter_ annotation to direct the code analysis tools to look for misuse of DMA pointers.
ms.assetid: 51F71815-D899-48F5-8F81-92B139FC6B8E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# \_Kernel\_IoGetDmaAdapter\_ Annotation for drivers


Use the \_Kernel\_IoGetDmaAdapter\_ annotation to direct the code analysis tools to look for misuse of DMA pointers.

If a function calls an interface annotated with the \_Kernel\_IoGetDmaAdapter\_ annotation, it shall have retry logic such that retries occur until the function succeeds.

The IoGetDmaAdapter routine could return fewer than the requested number of registers, and the caller is required to proceed using the actual number, not the requested number.

```ManagedCPlusPlus
_Must_inspect_result_
_IRQL_requires_max_(PASSIVE_LEVEL)
NTKERNELAPI
struct _DMA_ADAPTER *
IoGetDmaAdapter(
    _In_opt_ PDEVICE_OBJECT PhysicalDeviceObject,           // required for PnP drivers
    _In_ struct _DEVICE_DESCRIPTION *DeviceDescription,
    _Out_ _When_(return!=0, _Kernel_IoGetDmaAdapter_ _At_(*NumberOfMapRegisters, _Must_inspect_result_))
    PULONG NumberOfMapRegisters
```

## <span id="related_topics"></span>Related topics


[SAL 2.0 Annotations for Windows Drivers](sal-2-annotations-for-windows-drivers.md)

 

 






