---
title: 64-Bit Compiler
description: 64-Bit Compiler
ms.assetid: c119d6b3-03e2-4ffc-b0a9-8077b141a2f1
keywords: ["64-bit WDK kernel , porting drivers to", "porting drivers to 64-bit Windows", "compilers WDK 64-bit"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# 64-Bit Compiler





After you convert your 32-bit driver source code to use the [new data types](the-new-data-types.md), you can use the 64-bit compiler to identify any type-related problems that you initially missed. The first time you compile this code for 64-bit Windows, the compiler might generate many pointer-truncation or type-mismatch warnings. Use these warnings as a guide to make your code more robust. It is good practice to eliminate all warnings, especially pointer-truncation warnings.

The following is an example of such a warning:

```cpp
warning C4311: &#39;type cast&#39; : pointer truncation from &#39;unsigned char *&#39; to &#39;unsigned long &#39;
```

For example, the following code can generate the C4311 warning:

```cpp
buffer = (PUCHAR)srbControl;
(ULONG)buffer += srbControl->HeaderLength;
```

To correct the code, make the following changes:

```cpp
buffer = (PUCHAR)srbControl;
(ULONG_PTR)buffer += srbControl->HeaderLength;
```

### Predefined macros

The compiler defines the following macros to identify the platform.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Macro</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>_WIN64</p></td>
<td><p>A 64-bit platform.</p></td>
</tr>
<tr class="even">
<td><p>_WIN32</p></td>
<td><p>A 32-bit platform. This value is also defined by the 64-bit compiler for backward compatibility.</p></td>
</tr>
<tr class="odd">
<td><p>_WIN16</p></td>
<td><p>A 16-bit platform.</p></td>
</tr>
</tbody>
</table>

 

The following macros are specific to the architecture.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Macro</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>_M_IA64</p></td>
<td><p>A 64-bit Intel platform.</p></td>
</tr>
<tr class="even">
<td><p>_M_IX86</p></td>
<td><p>A 32-bit Intel platform.</p></td>
</tr>
</tbody>
</table>

 

Do not use these macros except with architecture-specific code. Instead, use \_WIN64, \_WIN32, and \_WIN16 whenever possible.

### 64-Bit compiler switches and warnings

There is a warning option to assist porting to 64-bit Windows. The -Wp64-W3 switch enables the following warnings:

-   **C4305**: Truncation warning. For example, "return": truncation from "unsigned int64" to "long."

-   **C4311**: Truncation warning. For example, "type cast": pointer truncation from "int\*\_ptr64" to "int."

-   **C4312**: Conversion to bigger-size warning. For example, "type cast": conversion from "int" to "int\*\_ptr64" of greater size.

-   **C4318**: Passing zero length. For example, passing constant zero as the length to the **memset** function.

-   **C4319**: Not operator. For example, "~": zero extending "unsigned long" to "unsigned \_int64" of greater size.

-   **C4313**: Calling the **printf** family of functions with conflicting conversion type specifiers and arguments. For example, "printf": "%p" in format string conflicts with argument 2 of type "\_int64." Another example is the call printf("%x", pointer\_value); this causes a truncation of the upper 32 bits. The correct call is printf("%p", pointer\_value).

-   **C4244**: Same as the existing warning C4242. For example, "return": conversion from "\_int64" to "unsigned int," possible loss of data.

 

 




