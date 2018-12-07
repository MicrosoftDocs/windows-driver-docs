---
title: GDL Preprocessor Syntax
description: GDL Preprocessor Syntax
ms.assetid: 14e9a595-3b6f-43b9-b670-7c9324619974
keywords:
- directives WDK GDL , source file preprocessor directives
- source files WDK GDL , preprocessor directives
- preprocessor directives WDK GDL , syntax
- syntax WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Preprocessor Syntax


GDL preprocessor directives must adhere to the following rules:

-   All preprocessor directives must occupy a separate line and must be the only statement on that line. Only optional whitespace can precede the preprocessor directive. Any extraneous characters that follow the directive on the same line are deleted before the file is submitted to the second (main) phase of parsing.

-   All directives must be prefixed with the current preprocessor prefix. The preprocessor prefix is initially set by the parser to an asterisk (\*) or number sign (\#), but you can change the prefix to any character or token by using the **\#SetPPPrefix** directive.

-   To be recognized as a preprocessor directive, the preprocessor prefix must be immediately followed by the directive, and if the directive expects a value, the value must be separated by a colon (:).

-   The value of the directive is terminated by any whitespace or linebreak character.

**Note**   GDL syntax is more relaxed than GPD syntax. If you are writing for both parsers, you should follow the stricter syntax that is required for GPD.

 

 

 




