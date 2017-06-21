---
title: Using Safe String Functions
author: windows-driver-content
description: Using Safe String Functions
ms.assetid: a84008e8-e490-4640-a734-ef55cfbdfea3
keywords: ["safe string functions WDK", "string manipulation functions WDK", "buffers WDK safe string functions"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using Safe String Functions


## <a href="" id="ddk-using-safe-string-functions-kg"></a>


Many system security problems are caused by poor buffer handling and the resulting buffer overruns. Poor buffer handling is often associated with string manipulation operations. The standard string manipulation functions that are supplied by C/C++ language runtime libraries (**strcat**, **strcpy**, **sprintf**, and so on) do not prevent writing beyond the end of buffers.

Two new sets of string manipulation functions, called *safe string functions*, provide additional processing for proper buffer handling in your code. These safe string functions are available in the Windows Driver Kit (WDK) and for Microsoft Windows XP SP1 and later versions of the Driver Development Kit (DDK) and Windows SDK. They are intended to replace their built-in C/C++ counterparts and similar routines that are supplied by Windows.

One set of safe string functions are for use in kernel-mode code. These functions are prototyped in a header file named Ntstrsafe.h. This header file and an associated library are available in the WDK.

The other set of safe string functions are for use in user-mode applications. A corresponding header file, Strsafe.h, contains prototypes for these functions. That file and an associated library are available in the Windows SDK. For more information about Strsafe.h, see [Using the Strsafe.h Functions](http://go.microsoft.com/fwlink/p/?linkid=165522).

The set of kernel-mode safe string functions consists of the following two subsets:

-   [Safe string functions for Unicode and ANSI characters](https://msdn.microsoft.com/library/windows/hardware/ff563642)

    Each of these functions is available in a W-suffixed version that supports double-byte Unicode characters and an A-suffixed version that supports single-byte ANSI characters. For example, [**RtlStringCbCatN**](https://msdn.microsoft.com/library/windows/hardware/ff562801), which concatenates two strings and limits the length of the appended string, is available as **RtlStringCbCatNW** and **RtlStringCbCatNA**.

-   [Safe string functions for UNICODE\_STRING structures](https://msdn.microsoft.com/library/windows/hardware/ff563644)

    Each of these functions accepts a [**UNICODE\_STRING**](https://msdn.microsoft.com/library/windows/hardware/ff564879) structure as an input or output parameter or both. For example, [**RtlStringCbCopyUnicodeString**](https://msdn.microsoft.com/library/windows/hardware/ff562815) accepts the structure as an input parameter, [**RtlUnicodeStringCopyString**](https://msdn.microsoft.com/library/windows/hardware/ff562948) accepts the structure as an output parameter, and [**RtlUnicodeStringCopy**](https://msdn.microsoft.com/library/windows/hardware/ff562942) accepts the structure as both an input and output parameter.

The kernel-mode safe string functions provide the following features:

-   Each safe string function receives the size of the destination buffer as input. The function can thus ensure that it does not write past the end of the buffer.

-   The Unicode and ANSI string functions terminate all output strings with a NULL character, even if the operation truncates the intended result.

-   All safe string functions return an NTSTATUS value, with only one possible success code (STATUS\_SUCCESS).

-   Most safe string functions are available in both a byte-counted and a character-counted version. For example, [**RtlStringCbCat**](https://msdn.microsoft.com/library/windows/hardware/ff562795) concatenates two byte-counted strings and [**RtlStringCchCat**](https://msdn.microsoft.com/library/windows/hardware/ff562834) concatenates two character-counted strings.

-   Most safe string functions are available in an extended, Ex-suffixed version that provides additional functionality. For example, [**RtlStringCbCatEx**](https://msdn.microsoft.com/library/windows/hardware/ff562799) extends the functionality of [**RtlStringCbCat**](https://msdn.microsoft.com/library/windows/hardware/ff562795).

This section includes the following topics:

[Summary of Kernel-Mode Safe String Functions](summary-of-kernel-mode-safe-string-functions.md)

[Importing Kernel-Mode Safe String Functions](importing-kernel-mode-safe-string-functions.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20Safe%20String%20Functions%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


