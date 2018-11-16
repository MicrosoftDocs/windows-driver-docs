---
title: Using Floating Point in a WDM Driver
description: Kernel-mode WDM drivers for Windows must follow certain guidelines when using floating-point operations. These differ between x86 and x64 systems. By default, Windows turns off arithmetic exceptions for both systems.
ms.assetid: 73414084-4054-466a-b64c-5c81b224be92
keywords: ["floating point WDK kernel", "floating-point unit WDK kernel", "FPU WDK kernel", "KeSaveFloatingPointState", "KeRestoreFloatingPointState", "WDM drivers WDK kernel , floating-point operations", "MMX WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using Floating Point in a WDM Driver


**Last updated**

-   July 2016

Kernel-mode WDM drivers for Windows must follow certain guidelines when using floating-point operations. These differ between x86 and x64 systems. By default, Windows turns off arithmetic exceptions for both systems.

## x86 systems


Kernel-mode WDM drivers for x86 systems must wrap the use of floating point calculations between calls to [**KeSaveExtendedProcessorState**](https://msdn.microsoft.com/library/windows/hardware/ff553238) and [**KeRestoreExtendedProcessorState**](https://msdn.microsoft.com/library/windows/hardware/ff553182). The floating point operations must be placed in a non-inline subroutine to make sure that floating point calculations are not performed before checking the return value of **KeSaveExtendedProcessorState** due to compiler reordering.

The compiler makes use of MMX/x87 also known as the floating-point unit (FPU) registers for such calculations, which can be concurrently used by a user-mode application. Failure to save these registers before using them, or failure to restore them when finished, may cause calculation errors in applications.

Drivers for x86 systems can call [**KeSaveExtendedProcessorState**](https://msdn.microsoft.com/library/windows/hardware/ff553238) and perform floating point calculations at IRQL &lt;= DISPATCH\_LEVEL. Floating-point operations are not supported in interrupt service routines (ISRs) on x86 systems.

## x64 systems


The 64-bit compiler does not use the MMX/x87 registers for floating point operations. Instead, it uses the SSE registers. x64 kernel mode code is not allowed to access the MMX/x87 registers. The compiler also takes care of properly saving and restoring the SSE state, therefore, calls to [**KeSaveExtendedProcessorState**](https://msdn.microsoft.com/library/windows/hardware/ff553238) and [**KeRestoreExtendedProcessorState**](https://msdn.microsoft.com/library/windows/hardware/ff553182) are unnecessary and floating point operations can be used in ISRs. Use of other extended processor features such as AVX, requires saving and restoring extended state. For more information see [Using extended processor features in Windows drivers](floating-point-support-for-64-bit-drivers.md).

## Example


The following example shows how a WDM driver should wrap its FPU access:

```cpp
__declspec(noinline)
VOID
DoFloatingPointCalculation(
    VOID
    )
{
    double Duration;
    LARGE_INTEGER Frequency;

    Duration = 1000000.0;
    DbgPrint("%I64x\n", *(LONGLONG*)&Duration);
    KeQueryPerformanceCounter(&Frequency);
    Duration /= (double)Frequency.QuadPart;
    DbgPrint("%I64x\n", *(LONGLONG*)&Duration);
}

NTSTATUS
DriverEntry(
    _In_ PDRIVER_OBJECT DriverObject,
    _In_ PUNICODE_STRING RegistryPath
    )
{

    XSTATE_SAVE SaveState;
    NTSTATUS Status;

    Status = KeSaveExtendedProcessorState(XSTATE_MASK_LEGACY, &SaveState);
    if (!NT_SUCCESS(Status)) {
        goto exit;
    }

    __try {
        DoFloatingPointCalculation();
    }
    __finally {
        KeRestoreExtendedProcessorState(&SaveState);
    }

exit:
    return Status;
}
```

In the example, the assignment to the floating-point variable occurs between calls to [**KeSaveExtendedProcessorState**](https://msdn.microsoft.com/library/windows/hardware/ff553238) and [**KeRestoreExtendedProcessorState**](https://msdn.microsoft.com/library/windows/hardware/ff553182). Because any assignment to a floating-point variable uses the FPU, drivers must ensure that **KeSaveExtendedProcessorState** has returned without error before initializing such a variable.

The preceding calls are unnecessary on an x64 system and harmless when the XSTATE\_MASK\_LEGACY flag is specified. Therefore, there is no need to change the code when compiling the driver for an x64 system.

On x86-based systems, the FPU is reset to its default state by a call to FNINIT, upon return from [**KeSaveExtendedProcessorState**](https://msdn.microsoft.com/library/windows/hardware/ff553238).

 

 




