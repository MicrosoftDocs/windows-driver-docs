---
title: "!cppexr (WinDbg)"
description: "The !cppexr extension displays the contents of a C++ exception record."
keywords: ["exception records", "!cppexr Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- cppexr
api_type:
- NA
---

# !cppexr


The **!cppexr** extension displays the contents of a C++ exception record.

```dbgsyntax
    !cppexr Address 
```

## Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the C++ exception record to display.

## DLL


Ext.dll



 

## Additional Information

For more information about exceptions, see [Controlling Exceptions and Events](../debugger/controlling-exceptions-and-events.md), the Windows Driver Kit (WDK) documentation, the Windows SDK documentation, and *Microsoft Windows Internals* by Mark Russinovich and David Solomon. Use the [**.exr**](-exr--display-exception-record-.md) command to display other exception records.

## Remarks

The **!cppexr** extension displays information that is related to a C++ exception that the target encounters, including the exception code, the address of the exception, and the exception flags. This exception must be one of the standard C++ exceptions that are defined in Msvcrt.dll.

You can typically obtain the *Address* parameter by using the [**!analyze -v**](-analyze.md) command.

The **!cppexr** extension is useful for determining the type of a C++ exception.

