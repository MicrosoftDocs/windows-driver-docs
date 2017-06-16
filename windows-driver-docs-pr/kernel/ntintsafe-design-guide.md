---
title: Using Safe Integer Functions
author: windows-driver-content
description: The ntintsafe library provides a set of C functions that perform safe integer arithmetic operations with bounds checking to prevent overflows and underflows in kernel-mode code.
ms.assetid: AFB7A078-814D-49EF-ABF9-2C621590F43B
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20Safe%20Integer%20Functions%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


