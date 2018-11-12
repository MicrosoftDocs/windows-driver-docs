---
title: Using the DECLARE_API Macro
description: Using the DECLARE_API Macro
ms.assetid: 469f5ae4-2da8-4bbe-b5c0-75fcef227ba5
keywords: ["WdbgExts extensions, DECLARE_API macro", "DECLARE_API macro (WdbgExts)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using the DECLARE\_API Macro


## <span id="ddk_using_the_declare_api_macro_dbwx"></span><span id="DDK_USING_THE_DECLARE_API_MACRO_DBWX"></span>


Each extension command in a WdbgExts extension DLL is declared using the DECLARE\_API macro. This macro is defined in wdbgexts.h.

The basic format of the code for an extension command is:

```cpp
DECLARE_API( myextension )
{
    code for myextension
}
```

The DECLARE\_API macro sets up a standard interface for extension commands. For example, if the user passed any arguments to the extension command, the entire argument string will be stored as a string, and a pointer to this string (PCSTR) will be passed to the extension function as **args**.

If you are using 64-bit pointers, the DECLARE\_API macro is defined as follows:

```cpp
#define DECLARE_API(s)                             \
    CPPMOD VOID                                    \
    s(                                             \
        HANDLE                 hCurrentProcess,    \
        HANDLE                 hCurrentThread,     \
        ULONG64                dwCurrentPc,        \
        ULONG                  dwProcessor,        \
        PCSTR                  args                \
     )
```

If you are using 32-bit pointers, DECLARE\_API remains the same, except that **dwCurrentPc** will be of the type ULONG instead of ULONG64. However, 64-bit pointers are recommended for any extension that you are writing. See [32-Bit Pointers and 64-Bit Pointers](32-bit-pointers-and-64-bit-pointers.md) for details.

 

 





