---
title: Using Safe String Functions
description: Using Safe String Functions
keywords: ["safe string functions WDK", "string manipulation functions WDK", "buffers WDK safe string functions"]
ms.date: 06/16/2017
---

# Using Safe String Functions





Many system security problems are caused by poor buffer handling and the resulting buffer overruns. Poor buffer handling is often associated with string manipulation operations. The standard string manipulation functions that are supplied by C/C++ language runtime libraries (**strcat**, **strcpy**, **sprintf**, and so on) do not prevent writing beyond the end of buffers.

Two new sets of string manipulation functions, called *safe string functions*, provide additional processing for proper buffer handling in your code. These safe string functions are available in the Windows Driver Kit (WDK) and for Microsoft Windows XP SP1 and later versions of the Driver Development Kit (DDK) and Windows SDK. They are intended to replace their built-in C/C++ counterparts and similar routines that are supplied by Windows.

One set of safe string functions are for use in kernel-mode code. These functions are prototyped in a header file named Ntstrsafe.h. This header file and an associated library are available in the WDK.

The other set of safe string functions are for use in user-mode applications. A corresponding header file, Strsafe.h, contains prototypes for these functions. That file and an associated library are available in the Windows SDK. For more information about Strsafe.h, see [Using the Strsafe.h Functions](/windows/win32/menurc/strsafe-ovw).

The set of kernel-mode safe string functions consists of the following two subsets:

-   [Safe string functions for Unicode and ANSI characters](/windows-hardware/drivers/ddi/_kernel/#safe-string-functions-for-unicode-and-ansi-characters)

    Each of these functions is available in a W-suffixed version that supports double-byte Unicode characters and an A-suffixed version that supports single-byte ANSI characters. For example, [**RtlStringCbCatN**](/windows-hardware/drivers/ddi/ntstrsafe/nf-ntstrsafe-rtlstringcbcatna), which concatenates two strings and limits the length of the appended string, is available as [**RtlStringCbCatNW**](/windows-hardware/drivers/ddi/ntstrsafe/nf-ntstrsafe-rtlstringcbcatnw) and [**RtlStringCbCatNA**](/windows-hardware/drivers/ddi/ntstrsafe//nf-ntstrsafe-rtlstringcbcatna).

-   [Safe string functions for UNICODE\_STRING structures](/windows-hardware/drivers/ddi/_kernel/#safe-string-functions-for-unicode_string-structures)

    Each of these functions accepts a [**UNICODE\_STRING**](/windows-hardware/drivers/ddi/wudfwdm/ns-wudfwdm-_unicode_string) structure as an input or output parameter or both. For example, [**RtlStringCbCopyUnicodeString**](/windows-hardware/drivers/ddi/ntstrsafe/nf-ntstrsafe-rtlstringcbcopyunicodestring) accepts the structure as an input parameter, [**RtlUnicodeStringCopyString**](/windows-hardware/drivers/ddi/ntstrsafe/nf-ntstrsafe-rtlunicodestringcopystring) accepts the structure as an output parameter, and [**RtlUnicodeStringCopy**](/windows-hardware/drivers/ddi/ntstrsafe/nf-ntstrsafe-rtlunicodestringcopy) accepts the structure as both an input and output parameter.

The kernel-mode safe string functions provide the following features:

-   Each safe string function receives the size of the destination buffer as input. The function can thus ensure that it does not write past the end of the buffer.

-   The Unicode and ANSI string functions terminate all output strings with a NULL character, even if the operation truncates the intended result.

-   All safe string functions return an NTSTATUS value, with only one possible success code (STATUS\_SUCCESS).

-   Most safe string functions are available in both a byte-counted and a character-counted version. For example, [**RtlStringCbCata**](/windows-hardware/drivers/ddi/ntstrsafe/nf-ntstrsafe-rtlstringcbcata) concatenates two byte-counted strings and [**RtlStringCchCata**](/windows-hardware/drivers/ddi/ntstrsafe/nf-ntstrsafe-rtlstringcchcata) concatenates two character-counted strings.

-   Most safe string functions are available in an extended, Ex-suffixed version that provides additional functionality. For example, [**RtlStringCbCatExa**](/windows-hardware/drivers/ddi/ntstrsafe/nf-ntstrsafe-rtlstringcbcatexa) extends the functionality of [**RtlStringCbCata**](/windows-hardware/drivers/ddi/ntstrsafe/nf-ntstrsafe-rtlstringcbcata).

This section includes the following topics:

[Summary of Kernel-Mode Safe String Functions](summary-of-kernel-mode-safe-string-functions.md)

[Importing Kernel-Mode Safe String Functions](importing-kernel-mode-safe-string-functions.md)

