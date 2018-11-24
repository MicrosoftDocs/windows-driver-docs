---
title: '#Include Preprocessor Directive'
description: '#Include Preprocessor Directive'
ms.assetid: 6c3e4de7-2007-4a1a-bdb0-fd5b2b64f489
keywords:
- preprocessor directives WDK GDL , keywords
- keywords WDK GDL
- reserved keywords WDK
- Include directive WDK GDL
- GDL WDK , source files
- source files WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# \#Include Preprocessor Directive


```GDL
#Include: Quoted String
```

The \#Include directive causes the GDL source file that is named by *Quoted String* to be loaded and processed. Preprocessing of the current GDL file is paused until the included file has been processed. The included file can influence the preprocessing of the remainder of the host GDL file by defining or undefining symbols.

The syntax of the quoted string is defined by GDL. The quoted string value, unlike the values of the other directives, can extend across more than one line. *Quoted String* is required.

\#Include and all directives must be terminated by a line break rather than a curly brace (}).

If you use **\*Include**, which is an old GPD keyword, the include file will be preprocessed after the host file. This processing might cause problems if the host file requires the included file to be preprocessed first. To avoid such potential problems, always prefix the \#Include directive with the current preprocessor prefix.

The current implementation of the parser allows three forms of naming a file: file name only, fully qualified path, and partially qualified path. If you use a partially qualified path, the starting point for the path is established by the current execution environment. If only a file name is used, two starting points will be tried: the path that the root source file uses, and then the path that the current execution environment establishes.

Note that if a precompiled file includes another file, the precompiled file is considered the root source file relative to its included files are concerned. The installation and setup code might impose additional restrictions.
