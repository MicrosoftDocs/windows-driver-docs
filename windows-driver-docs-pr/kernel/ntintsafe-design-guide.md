---
title: Using Safe Integer Functions
description: The ntintsafe library provides a set of C functions that perform safe integer arithmetic operations with bounds checking to prevent overflows and underflows in kernel-mode code.
ms.date: 07/30/2025
ms.topic: concept-article
---

# Using Safe Integer Functions

One way to minimize security problems is to prevent integer overflows and underflows.

* Integer overflows occur when the result of an arithmetic operation is larger than the memory space of the data type that is set to receive it. This operation results in the truncation of the integer and an incorrect result. For example, if you add two 32-bit integers that result in a value larger than ```2^31-1```, the result is truncated to fit into the 32-bit integer space, which can lead to unexpected behavior in your code.

* Integer underflow occurs when an operation, usually subtraction, gives an incorrect result. For example, if you subtract a number from INT_MIN (the smallest value for a 32-bit signed integer), the result is truncated to fit into the 32-bit integer space, which can also lead to unexpected behavior.

* Casting between two data types can also cause incorrect results due to truncation of a result that doesn't fit the new memory space.

The *ntintsafe* library provides a set of C functions that perform safe integer arithmetic operations with bounds checking to prevent overflows and underflows in kernel-mode code. All functions are in the *ntintsafe.h* header file, which ships with the Windows Driver Kit (WDK). These functions correspond to the Windows IntSafe functions that are used by application code.

You use these functions to calculate an index or buffer size, or to compute some other form of bounds check. The functions are optimized for speed.

Safe integer functions offer the following advantages:

* The size of the destination buffer is always provided to the function to ensure that the function doesn't write past the end of the buffer.

* Buffers are guaranteed to be null-terminated, even if the operation truncates the intended result.

* All functions return an NTSTATUS, with only one possible success code (STATUS_SUCCESS) and one possible error condition (STATUS_INTEGER_OVERFLOW). For example, ```NTSTATUS status = RtlIntSub(INT_MIN, 1, &result);``` should return a result = -2,147,483,649 but this number can't be represented in a 32-bit field. Instead, ```result``` is undefined and ```status``` is STATUS_INTEGER_OVERFLOW, which is the status value returned to report both overflows and underflows.

The *ntintsafe* library has two categories of functions:

* **Conversion functions**—These functions perform conversions between two data types.

* **Arithmetic functions**—These functions perform addition, subtraction, and multiplication operations for each data type.

[Summary of Kernel-Mode Safe Integer Functions](summary-of-safe-integer-functions.md)

[Importing Kernel-Mode Safe Integer Functions](importing-safe-integer-functions.md)
