---
title: Using Safe Integer Functions
description: The ntintsafe library provides a set of C functions that perform safe integer arithmetic operations with bounds checking to prevent overflows and underflows in kernel-mode code.
ms.assetid: AFB7A078-814D-49EF-ABF9-2C621590F43B
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Using Safe Integer Functions


One way to minimize security problems is to prevent integer overflows and underflows. Integer overflows occur when the result of an arithmetic operation is larger than the memory space of the data type that is set to receive it. This results in the truncation of the integer and an incorrect result. An underflow occurs when an operation, usually subtraction, gives an incorrect result. Casting between two data types can also cause incorrect results due to truncation of a result that does not fit the new memory space.

The ntintsafe library provides a set of C functions that perform safe integer arithmetic operations with bounds checking to prevent overflows and underflows in kernel-mode code. These functions correspond to the Windows IntSafe functions that are used by application code. You use these functions to calculate an index or buffer size, or to compute some other form of bounds check. The functions are optimized for speed.

Safe integer functions offer the following advantages:

-   The size of the destination buffer is always provided to the function to ensure that the function does not write past the end of the buffer.
-   Buffers are guaranteed to be null-terminated, even if the operation truncates the intended result.
-   All functions return an NTSTATUS, with only one possible success code (STATUS\_SUCCESS) and one possible error condition (STATUS\_INTEGER\_OVERFLOW).

The ntintsafe library has two categories of functions:

-   **Conversion functions**—These functions perform conversions between two data types.
-   **Arithmetic functions**—These functions perform addition, subtraction, and multiplication operations for each data type. There are no division operations because there are no overflow conditions.

[Summary of Kernel-Mode Safe Integer Functions](summary-of-safe-integer-functions.md)

[Importing Kernel-Mode Safe Integer Functions](importing-safe-integer-functions.md)

 

 




