---
title: Using extended processor features in Windows drivers
description: Windows drivers for x86 and x64 systems that use extended processor features must wrap floating point calculations between calls to KeSaveExtendedProcessorState and KeRestoreExtendedProcessorState in order to avoid errors in concurrent applications that might be using the registers.
ms.assetid: a42e86cf-47a2-44ed-8bf1-7407633af8b7
keywords: ["floating point WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using extended processor features in Windows drivers


**Last updated**

-   July 2016

Windows drivers for x86 and x64 systems that use extended processor features must wrap floating point calculations between calls to [**KeSaveExtendedProcessorState**](https://msdn.microsoft.com/library/windows/hardware/ff553238) and [**KeRestoreExtendedProcessorState**](https://msdn.microsoft.com/library/windows/hardware/ff553182) in order to avoid errors in concurrent applications that might be using the registers.

## Legacy MMX/x87 Registers


These registers correspond to the XSTATE\_MASK\_LEGACY\_FLOATING\_POINT mask and are unavailable to drivers for x64 systems. For more information on these registers see [Using Floating Point in a WDM Driver](using-floating-point-or-mmx-in-a-wdm-driver.md).

## SSE Registers


These registers correspond to the XSTATE\_MASK\_LEGACY\_SSE flag and are used by the x64 compiler for floating point operations. Drivers for x86 systems that use these registers must save them before use by passing the XSTATE\_MASK\_LEGACY or XSTATE\_MASK\_LEGACY\_SSE flag in the [**KeSaveExtendedProcessorState**](https://msdn.microsoft.com/library/windows/hardware/ff553238) call and when finished, restore them with [**KeRestoreExtendedProcessorState**](https://msdn.microsoft.com/library/windows/hardware/ff553182). This is unnecessary on x64 systems, but not harmful. For more information about these registers see [Using Floating Point in a WDM Driver](using-floating-point-or-mmx-in-a-wdm-driver.md).

## AVX Registers


These registers correspond to the XSTATE\_MASK\_GSSE or XSTATE\_MASK\_AVX masks. New x86 processors, such as the Intel Sandy Bridge (formerly Gesher) processor, support the AVX instructions and register set (YMM0-YMM15). In Windows 7 with Service Pack 1 (SP1), Windows Server 2008 R2, and newer versions of Windows, both x86 and x64 versions of the operating system preserve the AVX registers across thread (and process) switches. To use the AVX registers in kernel mode, drivers (x86 and x64) must explicitly save and restore the AVX registers. AVX registers cannot be used in an interrupt service routine, and arithmetic exceptions are turned off by default.

```cpp
include ksamd64.inc

        subttl "Set YMM State."
;++
;
; Routine Description:
;   
;   This routine loads the first four YMM registers with the state supplied.
;
; Arguments;
;
;   rcx - Supplies a pointer to the values we want to load.
;
; Return Value:
;
;   None
;
;--

LEAF_ENTRY SetYmmValues, _TEXT$00

        vmovdqa    ymm0,  ymmword ptr[rcx + 0]
        vmovdqa    ymm1,  ymmword ptr[rcx + 32]
        vmovdqa    ymm2,  ymmword ptr[rcx + 64]
        vmovdqa    ymm3,  ymmword ptr[rcx + 96]

        ret

LEAF_END SetYmmValues, _TEXT$00

        end
```

```cpp
typedef DECLSPEC_ALIGN(32) struct _YMM_REGISTERS {
    ULONG64 Ymm4Registers[16];
} YMM_REGISTERS, *PYMM_REGISTERS;

VOID
FASTCALL
SetYmmValues(
    __in PYMM_REGISTERS YmmRegisterValues
    );

NTSTATUS
DriverEntry (
    __in PDRIVER_OBJECT DriverObject,
    __in PUNICODE_STRING RegistryPath
    )
{

    NTSTATUS Status;
    XSTATE_SAVE SaveState;
    ULONG64 EnabledFeatures;

    //
    // Load the first 4 YMM registers as 4 vectors of 4 64-bit integers.
    //

    YMM_REGISTERS RegisterValues = { 0, 1, 2, 3,        // YMM0
                                     4, 5, 6, 7,        // YMM1
                                     8, 9, 10, 11,      // YMM2
                                     12, 13, 14, 15 };  // YMM3

    //
    // Check to see if AVX is available. Bail if it is not.
    //

    EnabledFeatures = RtlGetEnabledExtendedFeatures(-1);
    if ((EnabledFeatures & XSTATE_MASK_GSSE) == 0) {
        Status = STATUS_FAILED_DRIVER_ENTRY;
        goto exit;
    }

    Status = KeSaveExtendedProcessorState(XSTATE_MASK_GSSE, &SaveState);

    if (!NT_SUCCESS(Status)) {
        goto exit;
    }

    __try {
        SetYmmValues(&RegisterValues);
    }
    __finally {
        KeRestoreExtendedProcessorState(&SaveState);
    }

exit:
    return Status;
}
```

## Related topics
[**KeSaveExtendedProcessorState**](https://msdn.microsoft.com/library/windows/hardware/ff553238)  
[**KeRestoreExtendedProcessorState**](https://msdn.microsoft.com/library/windows/hardware/ff553182)  
[Using Floating Point in a WDM Driver](using-floating-point-or-mmx-in-a-wdm-driver.md)  



