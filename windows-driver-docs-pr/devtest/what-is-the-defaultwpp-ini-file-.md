---
title: What is the Defaultwpp.ini file
description: What is the Defaultwpp.ini file
ms.assetid: 7e2673a3-5a01-498a-a2af-e5d8ff3e088b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# What is the Defaultwpp.ini file?


The Defaultwpp.ini file is a configuration file that defines the data types that support software tracing. The Defaultwpp.ini file is located in the bin\\wppconfig\\rev1 subdirectory of the Windows Driver Kit (WDK).

The Defaultwpp.ini file includes the following:

-   Arithmetic data types, such as UBYTE and XINT64

-   Architecture-dependent data types, such as SLONGPTR

-   Predefined constants--such as COMPNAME (computer name), %!FUNC! (function name), and %!LEVEL! (provide level)--that can be included in the [trace message prefix](trace-message-prefix.md) by editing the %TRACE\_FORMAT\_PREFIX% environment variable

-   Format specification constants that let you use format specifications in trace messages like those used in **printf** statements. For example, it defines **s** is a custom string object, **ASTR**, and then defines **ASTR**, a complex data type, as a formatted string.

-   Special types for types commonly used in tracing, such as IPADDR, HRESULT, and GUID.

-   Time-related types, such as DATE, TIMESTAMP, due, and delta.

-   Enumeration types, such as b1 (set of 8 bytes) and bool (Boolean).

-   Custom types, such as irql, pnpmn, and sysctrl.

You can use the data types in the Defaultwpp.ini files and create your own custom configuration file that has simple and complex data types. For more information, see [How do you define custom data types?](how-do-you-define-custom-data-types-.md) and [What is the syntax of the complex types definition?](what-is-the-syntax-of-the-complex-types-definition-.md).

 

 





