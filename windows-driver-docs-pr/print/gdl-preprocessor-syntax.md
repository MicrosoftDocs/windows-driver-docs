---
title: GDL Preprocessor Syntax
author: windows-driver-content
description: GDL Preprocessor Syntax
MS-HAID:
- 'gplfiles\_a30c3136-f95b-4cb8-ab3f-8d3313806d5a.xml'
- 'print.gdl\_preprocessor\_syntax'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 14e9a595-3b6f-43b9-b670-7c9324619974
keywords: ["directives WDK GDL , source file preprocessor directives", "source files WDK GDL , preprocessor directives", "preprocessor directives WDK GDL , syntax", "syntax WDK GDL"]
---

# GDL Preprocessor Syntax


GDL preprocessor directives must adhere to the following rules:

-   All preprocessor directives must occupy a separate line and must be the only statement on that line. Only optional whitespace can precede the preprocessor directive. Any extraneous characters that follow the directive on the same line are deleted before the file is submitted to the second (main) phase of parsing.

-   All directives must be prefixed with the current preprocessor prefix. The preprocessor prefix is initially set by the parser to an asterisk (\*) or number sign (\#), but you can change the prefix to any character or token by using the **\#SetPPPrefix** directive.

-   To be recognized as a preprocessor directive, the preprocessor prefix must be immediately followed by the directive, and if the directive expects a value, the value must be separated by a colon (:).

-   The value of the directive is terminated by any whitespace or linebreak character.

**Note**   GDL syntax is more relaxed than GPD syntax. If you are writing for both parsers, you should follow the stricter syntax that is required for GPD.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Preprocessor%20Syntax%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


