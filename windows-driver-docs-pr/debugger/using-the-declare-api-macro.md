---
title: Using the DECLARE_API Macro
description: Using the DECLARE_API Macro
ms.assetid: 469f5ae4-2da8-4bbe-b5c0-75fcef227ba5
keywords: ["WdbgExts extensions, DECLARE_API macro", "DECLARE_API macro (WdbgExts)"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using the DECLARE\_API Macro


## <span id="ddk_using_the_declare_api_macro_dbwx"></span><span id="DDK_USING_THE_DECLARE_API_MACRO_DBWX"></span>


Each extension command in a WdbgExts extension DLL is declared using the DECLARE\_API macro. This macro is defined in wdbgexts.h.

The basic format of the code for an extension command is:

```
DECLARE_API( myextension )
{
    code for myextension
}
```

The DECLARE\_API macro sets up a standard interface for extension commands. For example, if the user passed any arguments to the extension command, the entire argument string will be stored as a string, and a pointer to this string (PCSTR) will be passed to the extension function as **args**.

If you are using 64-bit pointers, the DECLARE\_API macro is defined as follows:

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20the%20DECLARE_API%20Macro%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




