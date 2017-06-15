---
title: 64-Bit Compiler
author: windows-driver-content
description: 64-Bit Compiler
MS-HAID:
- 'Other\_35b13e37-5090-4c37-b2a2-e91621b14f89.xml'
- 'kernel.64\_bit\_compiler'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c119d6b3-03e2-4ffc-b0a9-8077b141a2f1
keywords: ["64-bit WDK kernel , porting drivers to", "porting drivers to 64-bit Windows", "compilers WDK 64-bit"]
---

# 64-Bit Compiler


## <a href="" id="ddk-64-bit-compiler-kg"></a>


After you convert your 32-bit driver source code to use the [new data types](the-new-data-types.md), you can use the 64-bit compiler to identify any type-related problems that you initially missed. The first time you compile this code for 64-bit Windows, the compiler might generate many pointer-truncation or type-mismatch warnings. Use these warnings as a guide to make your code more robust. It is good practice to eliminate all warnings, especially pointer-truncation warnings.

The following is an example of such a warning:

```
warning C4311: &#39;type cast&#39; : pointer truncation from &#39;unsigned char *&#39; to &#39;unsigned long &#39;
```

For example, the following code can generate the C4311 warning:

```
buffer = (PUCHAR)srbControl;
(ULONG)buffer += srbControl->HeaderLength;
```

To correct the code, make the following changes:

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%2064-Bit%20Compiler%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


