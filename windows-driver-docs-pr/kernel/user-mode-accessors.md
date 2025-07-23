---
title: User-mode Accessors
description: Learn about user-mode accessors that provide safe access to user-mode memory from kernel-mode code
keywords: ["user-mode accessors", "kernel-mode", "user-mode memory", "probing", "volatile access", "memory safety", "UMA"]
ms.date: 12/19/2024
ms.topic: concept-article
---

# User-mode accessors

User-mode accessors (UMA) are a set of APIs that provide safe access to user-mode memory from kernel-mode code. These APIs address common security vulnerabilities and programming errors that can occur when kernel-mode drivers access user-mode memory.

## Why user-mode accessors are needed

When kernel-mode code needs to access user-mode memory, several challenges arise:

### Security concerns

User-mode applications can pass malicious or invalid pointers to kernel-mode code. Without proper validation, this can lead to:

- **Memory corruption**: User-mode code might pass pointers to kernel memory, allowing potential corruption of critical system data
- **System crashes**: Invalid memory addresses can cause page faults that crash the system if not properly handled

### Concurrency issues

User-mode memory can be modified by multiple threads while kernel-mode code is accessing it. This creates race conditions where:

- Values read from user-mode memory might change between accesses
- Compiler optimizations can eliminate seemingly redundant reads, leading to security vulnerabilities

### Compiler optimization problems

Compilers assume single-threaded execution and may optimize away what appear to be redundant memory accesses. This can cause security issues when user-mode memory is modified by other threads during kernel execution.

## Traditional approach and its limitations

Traditionally, kernel-mode code accessing user-mode memory follows this pattern:

```c
__try {
    ProbeForRead(userPtr, sizeof(DATA), 1);
    
    // This is unsafe - compiler might optimize away the second read
    ULONG size = userPtr->Size;
    PVOID localData = ExAllocatePool2(POOL_FLAG_PAGED, size);
    RtlCopyMemory(localData, userPtr, userPtr->Size); // Potential vulnerability
    
} __except (...) {
    // Handle exceptions
}
```

This approach has several problems:

1. **Forgot to probe**: Developers might forget to call `ProbeForRead` or `ProbeForWrite`
2. **Compiler optimizations**: The compiler might reuse the value of `userPtr->Size` instead of reading it again, creating a time-of-check-time-of-use (TOCTOU) vulnerability
3. **Manual volatile casting**: Developers must remember to use volatile accesses to prevent compiler optimizations

## User-mode accessor solution

User-mode accessors solve these problems by:

1. **Automatic probing**: All UMA APIs automatically probe memory before accessing it
2. **Volatile access**: APIs use volatile semantics to prevent compiler optimizations
3. **Type safety**: Separate APIs for different data types and access patterns

### Example with user-mode accessors

```c
__try {
    ULONG localSize = ReadULongFromUser(&userPtr->Size);
    PVOID localData = ExAllocatePool2(POOL_FLAG_PAGED, localSize);
    CopyFromUser(localData, userPtr, localSize);
    
    // Ensure consistency
    ((PDATA)localData)->Size = localSize;
    
} __except (...) {
    // Handle exceptions
}
```

## Types of user-mode accessor APIs

### Scalar type accessors

For reading and writing simple data types (ULONG, USHORT, UCHAR, etc.), UMA provides six variants for each type:

- **ReadXxxFromUser**: Read a value from user-mode memory
- **ReadXxxFromUserAcquire**: Read with acquire semantics for memory ordering
- **ReadXxxFromMode**: Read from either user-mode or kernel-mode memory based on a mode parameter
- **WriteXxxToUser**: Write a value to user-mode memory
- **WriteXxxToUserRelease**: Write with release semantics for memory ordering
- **WriteXxxToMode**: Write to either user-mode or kernel-mode memory based on a mode parameter

### Bulk memory accessors

For copying larger amounts of data:

- **CopyFromUser**: Copy data from user-mode memory to kernel-mode memory
- **CopyToUser**: Copy data from kernel-mode memory to user-mode memory
- **CopyUserToUser**: Copy data within user-mode memory
- **FillUserMemory**: Fill user-mode memory with a specific value
- **ZeroUserMemory**: Zero out user-mode memory
- **StringLengthFromUser**: Get the length of a string in user-mode memory
- **WideStringLengthFromUser**: Get the length of a wide string in user-mode memory

## Mode-based APIs

Some kernel code needs to handle both user-mode and kernel-mode memory depending on the context. Mode-based APIs accept a `KPROCESSOR_MODE` parameter:

```c
KPROCESSOR_MODE previousMode = KeGetPreviousMode();
ULONG value = ReadULongFromMode(&ptr->Field, previousMode);
```

The mode can be determined from:
- `KeGetPreviousMode()` for system calls
- `IRP->RequestorMode` for I/O requests

## Acquire and release semantics

On ARM architectures, memory accesses can be reordered by the CPU. Acquire and release semantics provide memory ordering guarantees:

- **Acquire semantics**: Prevents reordering of the load relative to other memory operations
- **Release semantics**: Prevents reordering of the store relative to other memory operations

For more information, see [Acquire and Release Semantics](acquire-and-release-semantics.md).

## Best practices

1. **Always use UMA APIs** when accessing user-mode memory from kernel code
2. **Handle exceptions** with appropriate `__try/__except` blocks
3. **Use mode-based APIs** when your code might handle both user-mode and kernel-mode memory
4. **Consider acquire/release semantics** when memory ordering is important for your use case
5. **Validate copied data** after copying it to kernel memory to ensure consistency

## Future hardware support

User-mode accessors are designed to support future hardware security features like:

- **Intel SMAP (Supervisor Mode Access Prevention)**: Prevents kernel code from accessing user-mode memory except through designated functions
- **ARM PAN (Privileged Access Never)**: Similar protection on ARM architectures

By using UMA APIs consistently, drivers will be compatible with these security enhancements when they're enabled in future Windows versions.

## See also

- [Acquire and Release Semantics](acquire-and-release-semantics.md)
- [RtlCopyVolatileMemory](../ddi/wdm/nf-wdm-rtlcopyvolatilememory.md)
- [RtlFillVolatileMemory](../ddi/wdm/nf-wdm-rtlfillvolatilememory.md)

