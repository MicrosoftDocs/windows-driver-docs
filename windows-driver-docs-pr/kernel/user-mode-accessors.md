---
title: User-mode Accessors
description: Learn about user-mode accessors that provide safe access to user-mode memory from kernel-mode code
keywords: ["user-mode accessors", "kernel-mode", "user-mode memory", "probing", "volatile access", "memory safety", "UMA"]
ms.date: 07/25/2025
ms.topic: concept-article
ai-usage: ai-assisted
---

# User-mode accessors

User-mode accessors (UMA) are a set of DDIs designed to safely access and manipulate user-mode memory from kernel-mode code. These DDIs address common security vulnerabilities and programming errors that can occur when kernel-mode drivers access user-mode memory.

Kernel-mode code that accesses/manipulates user-mode memory will soon be required to use UMA.

## Possible issues when accessing user-mode memory from kernel mode

When kernel-mode code needs to access user-mode memory, several challenges arise:

* User-mode applications can pass malicious or invalid pointers to kernel-mode code. Lack of proper validation can lead to memory corruption, crashes, or security vulnerabilities.

* User-mode code is multithreaded. As a result, different threads might modify the same user-mode memory between separate kernel-mode accesses to it, possibly leading to corrupt kernel memory.

* Kernel-mode developers often forget to probe user-mode memory before accessing it, which is a security issue.

* Compilers assume single-threaded execution and might optimize away what appear to be redundant memory accesses. Programmers unaware of such optimizations can write unsafe code.

The following code snippets illustrate these issues.

### Example 1: Possible memory corruption due to multithreading in user mode

Kernel-mode code that needs to access user-mode memory must do so within a `__try/__except` block to ensure the memory is valid. The following code snippet shows a typical pattern for accessing user-mode memory:

```c

// User-mode structure definition
typedef struct _StructWithData {
        ULONG Size;
        CHAR* Data[1];
} StructWithData;

// Kernel-mode call that accesses user-mode memory
void MySysCall(StructWithData* Ptr) {
    __try {
        // Probe user-mode memory to ensure it's valid
        ProbeForRead (Ptr, sizeof(StructWithData), 1);

        // Allocate memory in the kernel
        PVOID LocalData = ExAllocatePool2(POOL_FLAG_PAGED, Ptr->Size);
        
        //Copy user-mode data into the heap allocation
        RtlCopyMemory(LocalData, Ptr->Data, Ptr->Size);
    } __except (…) {
        // Handle exceptions
    }
}
```

This snippet probes the memory first, which is an important first but frequently overlooked step.

However, one problem that can occur in this code is due to multithreading in user mode. Specifically, ```Ptr->Size``` might change after the call to **ExAllocatePool2** but before the call to **RtlCopyMemory**, potentially leading to memory corruption in the kernel.

### Example 2: Possible issues due to compiler optimizations

An attempt to address the multithreading issue in Example 1 might be to copy ```Ptr->Size``` into a local variable before the allocation and copy:

``` c

void MySysCall(StructWithData* Ptr) {
    __try {
        // Probe user-mode memory to ensure it's valid
        ProbeForRead (Ptr, sizeof(StructWithData), 1);
        
        // Read Ptr->Size once to avoid possible memory change in user mode
        ULONG LocalSize = Ptr->Size;
        
        // Allocate memory in the kernel
        PVOID LocalData = ExAllocatePool2(POOL_FLAG_PAGED, LocalSize);
        
        //Copy user-mode data into the heap allocation
        RtlCopyMemory(LocalData, Ptr, LocalSize);
    } __except (…) {}
}
```

While this approach mitigates the issue caused by multithreading, it still isn't safe because the compiler isn't aware of multiple threads and thus assumes a single thread of execution. As an optimization, the compiler might see that it already has a copy of the value that ```Ptr->Size``` points to on its stack and therefore not do the copy to ```LocalSize```.

## User-mode accessors solution

The UMA interface solves the issues encountered when accessing user-mode memory from kernel mode. UMA provides:

* Automatic probing: Explicit probing (**ProbeForRead**/**ProbeForWrite**) is no longer required, as all the UMA functions ensure address safety.

* Volatile access: All UMA DDIs use volatile semantics to prevent compiler optimizations.

* Ease of portability: The comprehensive set of UMA DDIs makes it easy for customers to port their existing code to use UMA DDIs, ensuring that user-mode memory is accessed safely and correctly.

### Example using UMA DDI

Using the previously defined user-mode structure, the following code snippet demonstrates how to use UMA to safely access user-mode memory.

```c
void MySysCall(StructWithData* Ptr) {
    __try {

        // This UMA call probes the passed user-mode memory and does a
        // volatile read of Ptr->Size to ensure it isn't optimized away by the compiler.
        ULONG LocalSize =  ReadULongFromUser(&Ptr->Size);
        
        // Allocate memory in the kernel
        PVOID LocalData = ExAllocatePool2(POOL_FLAG_PAGED, LocalSize);
        
        //This UMA call safely copies UM data into the KM heap allocation.
        CopyFromUser(&LocalData, Ptr, LocalSize);
        
        // To be safe, set LocalData.Size to be LocalSize, which was the value used
        // to make the pool allocation just in case LocalData.Size was changed.
        LocalData.Size = LocalSize;
        
    } __except (…) {}
}
```

## UMA implementation and usage

The UMA interface ships as part of the Windows Driver Kit (WDK):

* The function declarations are found in the *usermode_accessors.h* header file.
* The function implementations are found in a static library named *umaccess.lib*.

UMA works on all versions of Windows, not just the latest. You need to consume the latest WDK to get the function declarations and implementations from *usermode_accessors.h* and *umaccess.lib*, respectively. The resulting driver will run fine on older versions of Windows.

It's recommended that all drivers built with the UMA library enable function overrides. Doing so results in a more performant scenario on the latest version of Windows. *Umaccess.lib* provides a safe, down-level implementation for all DDIs. On UMA-aware versions of the Windows kernel, drivers will have all of their functions redirected to a safer version implemented in *ntoskrnl.exe*. This redirection is achieved either by function overrides, or by updating the driver's load configuration at load time.

All user-mode accessor functions must be executed within a structured exception handler (SEH) due to potential exceptions when accessing user-mode memory.

## Types of user-mode accessor DDIs

UMA provides various DDIs for different types of user-mode memory access. Most these DDIs are for fundamental data types, such as BOOLEAN, ULONG, and pointers. Additionally, UMA provides DDIs for bulk memory access, string length retrieval, and interlocked operations.

### Generic DDIs for fundamental data types

UMA provides six function variants for reading and writing simple data types. For example, the following functions are available for BOOLEAN values:

| Function Name | Description |
| ------------- |-------------|
| [**ReadBooleanFromUser**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-readbooleanfromuser) | Read a value from user-mode memory. |
| [**ReadBooleanFromUserAcquire**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-readbooleanfromuseracquire) | Read a value from user-mode memory with acquire semantics for memory ordering. |
| [**ReadBooleanFromMode**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-readbooleanfrommode) | Read from either user-mode or kernel-mode memory based on a mode parameter. |
| [**WriteBooleanToUser**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-writebooleantouser) | Write a value to user-mode memory. |
| [**WriteBooleanToUserRelease**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-writebooleantouserrelease) | Write a value to user-mode memory with release semantics for memory ordering. |
| [**WriteBooleanToMode**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-writebooleantomode) | Write to either user-mode or kernel-mode memory based on a mode parameter. |

For **Read*Xxx*FromUser** functions, the **Source** parameter must point into the user-mode virtual address space (VAS). The same is true in the **Read*Xxx*FromMode** versions when ```Mode == UserMode```.  

For **Read*Xxx*FromMode**, when ```Mode == KernelMode```, the **Source** parameter must point into the kernel-mode VAS. If the preprocessor definition DBG is defined, the operation fast fails with the FAST_FAIL_KERNEL_POINTER_EXPECTED code.

In the **Write*Xxx*ToUser** functions, the **Destination** parameter must point into the user-mode VAS. The same is true in the **Write*Xxx*ToMode** versions when ```Mode == UserMode```.

### Copy and memory manipulation DDIs

UMA provides functions for copying and moving memory between user and kernel modes, including variants for nontemporal and aligned copies. These functions are marked with annotations indicating potential SEH exceptions and IRQL requirements (max APC_LEVEL).

Examples include [**CopyFromUser**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-copyfromuser), [**CopyToMode**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-copytomode), and [**CopyFromUserToMode**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-copyfromusertomode).

Macros such as [**CopyFromModeAligned**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-copyfrommodealigned) and [**CopyFromUserAligned**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-copyfromuseraligned) include alignment probing for safety before performing the copy operation.

Macros such as [**CopyFromUserNonTemporal**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-copyfromusernontemporal) and [**CopyToModeNonTemporal**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-copytomodenontemporal) provide nontemporal copies that avoid cache pollution.

### Structure read/write macros

Macros for reading and writing structures between modes ensure type compatibility and alignment, calling helper functions with size and mode parameters. Examples include [**WriteStructToMode**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-writestructtomode), [**ReadStructFromUser**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-readstructfromuser), and their aligned variants.

### Fill and zero memory functions

DDIs are provided to fill or zero memory in user or mode address spaces, with parameters specifying destination, length, fill value, and mode. These functions also carry SEH and IRQL annotations.

Examples include [**FillUserMemory**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-fillusermemory) and [**ZeroModeMemory**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-zeromodememory).

### Interlocked operations

UMA includes interlocked operations for atomic memory access, which are essential for thread-safe memory manipulations in concurrent environments. DDIs are provided for both 32-bit and 64-bit values, with versions targeting user or mode memory.

Examples include [**InterlockedCompareExchangeToUser**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-interlockedcompareexchangetouser), [**InterlockedOr64ToMode**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-interlockedor64tomode), and [**InterlockedAndToUser**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-interlockedandtouser).

### String length DDIs

Functions to determine string lengths safely from user or mode memory are included, supporting both ANSI and wide-character strings. These functions are designed to raise exceptions on unsafe memory access and are IRQL constrained.

Examples include [**StringLengthFromUser**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-stringlengthfromuser) and [**WideStringLengthFromMode**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-widestringlengthfrommode).

### Large integer and Unicode string accessors

UMA provides DDIs to read and write LARGE_INTEGER, ULARGE_INTEGER, and UNICODE_STRING types between user and mode memory. Variants have acquire and release semantics with mode parameters for safety and correctness.

Examples include [**ReadLargeIntegerFromUser**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-readlargeintegerfromuser), [**WriteUnicodeStringToMode**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-writeunicodestringtomode), and [**WriteULargeIntegerToUser**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-writeulargeintegertouser).

### Acquire and release semantics

On some architectures such as ARM, the CPU can reorder memory accesses. The generic DDIs all have an Acquire/Release implementation if you need a guarantee that memory accesses aren't reordered for the user-mode access.

* Acquire semantics prevent reordering of the load relative to other memory operations.
* Release semantics prevent reordering of the store relative to other memory operations.

Examples of acquire and release semantics in UMA include [**ReadULongFromUserAcquire**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-readulongfromuseracquire) and [**WriteULongToUserRelease**](/windows-hardware/drivers/ddi/usermode_accessors/nf-usermode_accessors-writeulongtouserrelease).

For more information, see [Acquire and Release Semantics](acquire-and-release-semantics.md).

## Best practices

- **Always use UMA DDIs** when accessing user-mode memory from kernel code.
- **Handle exceptions** with appropriate `__try/__except` blocks.
- **Use mode-based DDIs** when your code might handle both user-mode and kernel-mode memory.
- **Consider acquire/release semantics** when memory ordering is important for your use case.
- **Validate copied data** after copying it to kernel memory to ensure consistency.

## Future hardware support

User-mode accessors are designed to support future hardware security features like:

* SMAP (Supervisor Mode Access Prevention): Prevents kernel code from accessing user-mode memory except through designated functions such as UMA DDIs.
* ARM PAN (Privileged Access Never): Similar protection on ARM architectures.

By using UMA DDIs consistently, drivers will be compatible with these security enhancements when they're enabled in future Windows versions.
