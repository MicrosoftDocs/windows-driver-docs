---
title: Target Information
description: Target Information
keywords: ["Debugger Engine API, targets, info"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Target Information


The method [**GetDebuggeeType**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getdebuggeetype) returns the nature of the current target (for example, whether it is a kernel-mode or user-mode target), and how the [debugger engine](introduction.md#debugger-engine) is connected to it.

If the target is a crash dump file file, the method [**GetDumpFormatFlags**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getdumpformatflags) will indicate what information is contained in the dump.

### <span id="target_s_computer"></span><span id="TARGET_S_COMPUTER"></span>Target's Computer

The page size of the target's computer is returned by [**GetPageSize**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getpagesize). [**IsPointer64Bit**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-ispointer64bit) will indicate if the computer uses 32-bit or 64-bit addresses.

**Note**  Internally, the debugger engine always uses 64-bit addresses for the target. If the target only uses 32-bit addresses, the engine automatically converts them when communicating with the target.

 

The number of processors in the target's computer is returned by [**GetNumberProcessors**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getnumberprocessors).

There are three different processor types associated with the target's computer:

-   The *actual processor type* is the type of the physical processor in the target's computer. This is returned by [**GetActualProcessorType**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getactualprocessortype).

-   The *executing processor type* is the type of the processor used in the currently executing processor context. This is returned by [**GetExecutingProcessorType**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getexecutingprocessortype).

-   The *effective processor type* is the processor type the debugger uses when interpreting information from the target -- for example, setting breakpoints, accessing registers, and getting stack traces. The effective processor type is returned by [**GetEffectiveProcessorType**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-geteffectiveprocessortype) and can be changed using [**SetEffectiveProcessorType**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-seteffectiveprocessortype).

The effective processor type and executing processor type may differ from the actual processor type -- for example, when the physical processor is an x64 processor and it is running in x86 mode.

The different executing processor types that are supported by the physical processor on the target's computer are returned by [**GetPossibleExecutingProcessorTypes**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getpossibleexecutingprocessortypes). The number of these is returned by [**GetNumberPossibleExecutingProcessorTypes**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getnumberpossibleexecutingprocessortypes).

The list of processor types that is supported by the debugger engine is returned by [**GetSupportedProcessorTypes**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getsupportedprocessortypes). The number of supported processor types is returned by [**GetNumberSupportedProcessorTypes**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getnumbersupportedprocessortypes).

The names (full and abbreviated) of a processor type are returned by [**GetProcessorTypeNames**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getprocessortypenames).

The current time on the target's computer is returned by [**GetCurrentTimeDate**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getcurrenttimedate). The length of time the target's computer has been running since the last boot is returned by [**GetCurrentSystemUpTime**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getcurrentsystemuptime). Time information may not be available for all targets.

### <span id="target_versions"></span><span id="TARGET_VERSIONS"></span>Target Versions

The Windows version running on the target's computer is returned by [**GetSystemVersionValues**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol4-getsystemversionvalues) and the [**Request**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugadvanced3-request) operation [**DEBUG\_REQUEST\_GET\_WIN32\_MAJOR\_MINOR\_VERSIONS**](debug-request-get-win32-major-minor-versions.md), and a description of the Windows version is returned by [**GetSystemVersionString**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol4-getsystemversionstring). Some of this information is also returned by [**GetSystemVersion**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getsystemversion).

 

