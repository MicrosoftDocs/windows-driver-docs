---
title: What is the Defaultwpp.ini file
description: What is the Defaultwpp.ini file
ms.assetid: 7e2673a3-5a01-498a-a2af-e5d8ff3e088b
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20What%20is%20the%20Defaultwpp.ini%20file?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




