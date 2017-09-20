---
title: Target Information
description: Target Information
ms.assetid: e818c0bb-ba91-4752-8baf-00fff759106f
keywords: ["Debugger Engine API, targets, info"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Target Information


The method [**GetDebuggeeType**](https://msdn.microsoft.com/library/windows/hardware/ff546559) returns the nature of the current target (for example, whether it is a kernel-mode or user-mode target), and how the [debugger engine](introduction.md#debugger-engine) is connected to it.

If the target is a crash dump file file, the method [**GetDumpFormatFlags**](https://msdn.microsoft.com/library/windows/hardware/ff546592) will indicate what information is contained in the dump.

### <span id="target_s_computer"></span><span id="TARGET_S_COMPUTER"></span>Target's Computer

The page size of the target's computer is returned by [**GetPageSize**](https://msdn.microsoft.com/library/windows/hardware/ff548086). [**IsPointer64Bit**](https://msdn.microsoft.com/library/windows/hardware/ff551092) will indicate if the computer uses 32-bit or 64-bit addresses.

**Note**  Internally, the debugger engine always uses 64-bit addresses for the target. If the target only uses 32-bit addresses, the engine automatically converts them when communicating with the target.

 

The number of processors in the target's computer is returned by [**GetNumberProcessors**](https://msdn.microsoft.com/library/windows/hardware/ff547950).

There are three different processor types associated with the target's computer:

-   The *actual processor type* is the type of the physical processor in the target's computer. This is returned by [**GetActualProcessorType**](https://msdn.microsoft.com/library/windows/hardware/ff545572).

-   The *executing processor type* is the type of the processor used in the currently executing processor context. This is returned by [**GetExecutingProcessorType**](https://msdn.microsoft.com/library/windows/hardware/ff546670).

-   The *effective processor type* is the processor type the debugger uses when interpreting information from the target -- for example, setting breakpoints, accessing registers, and getting stack traces. The effective processor type is returned by [**GetEffectiveProcessorType**](https://msdn.microsoft.com/library/windows/hardware/ff546595) and can be changed using [**SetEffectiveProcessorType**](https://msdn.microsoft.com/library/windows/hardware/ff556657).

The effective processor type and executing processor type may differ from the actual processor type -- for example, when the physical processor is an x64 processor and it is running in x86 mode.

The different executing processor types that are supported by the physical processor on the target's computer are returned by [**GetPossibleExecutingProcessorTypes**](https://msdn.microsoft.com/library/windows/hardware/ff548130). The number of these is returned by [**GetNumberPossibleExecutingProcessorTypes**](https://msdn.microsoft.com/library/windows/hardware/ff547939).

The list of processor types that is supported by the debugger engine is returned by [**GetSupportedProcessorTypes**](https://msdn.microsoft.com/library/windows/hardware/ff548438). The number of supported processor types is returned by [**GetNumberSupportedProcessorTypes**](https://msdn.microsoft.com/library/windows/hardware/ff547966).

The names (full and abbreviated) of a processor type are returned by [**GetProcessorTypeNames**](https://msdn.microsoft.com/library/windows/hardware/ff548169).

The current time on the target's computer is returned by [**GetCurrentTimeDate**](https://msdn.microsoft.com/library/windows/hardware/ff546553). The length of time the target's computer has been running since the last boot is returned by [**GetCurrentSystemUpTime**](https://msdn.microsoft.com/library/windows/hardware/ff545883). Time information may not be available for all targets.

### <span id="target_versions"></span><span id="TARGET_VERSIONS"></span>Target Versions

The Windows version running on the target's computer is returned by [**GetSystemVersionValues**](https://msdn.microsoft.com/library/windows/hardware/ff549258) and the [**Request**](https://msdn.microsoft.com/library/windows/hardware/ff554564) operation [**DEBUG\_REQUEST\_GET\_WIN32\_MAJOR\_MINOR\_VERSIONS**](https://msdn.microsoft.com/library/windows/hardware/ff541563), and a description of the Windows version is returned by [**GetSystemVersionString**](https://msdn.microsoft.com/library/windows/hardware/ff549245). Some of this information is also returned by [**GetSystemVersion**](https://msdn.microsoft.com/library/windows/hardware/ff549234).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Target%20Information%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




