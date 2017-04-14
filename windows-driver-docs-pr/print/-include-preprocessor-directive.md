---
title: \ Include Preprocessor Directive
author: windows-driver-content
description: \ Include Preprocessor Directive
ms.assetid: 6c3e4de7-2007-4a1a-bdb0-fd5b2b64f489
keywords: ["preprocessor directives WDK GDL , keywords", "keywords WDK GDL", "reserved keywords WDK", "Include directive WDK GDL", "GDL WDK , source files", "source files WDK GDL"]
---

# \#Include Preprocessor Directive


```
#Include: Quoted String
```

The \#Include directive causes the GDL source file that is named by *Quoted String* to be loaded and processed. Preprocessing of the current GDL file is paused until the included file has been processed. The included file can influence the preprocessing of the remainder of the host GDL file by defining or undefining symbols.

The syntax of the quoted string is defined by GDL. The quoted string value, unlike the values of the other directives, can extend across more than one line. *Quoted String* is required.

\#Include and all directives must be terminated by a line break rather than a curly brace (}).

If you use **\*Include**, which is an old GPD keyword, the include file will be preprocessed after the host file. This processing might cause problems if the host file requires the included file to be preprocessed first. To avoid such potential problems, always prefix the \#Include directive with the current preprocessor prefix.

The current implementation of the parser allows three forms of naming a file: file name only, fully qualified path, and partially qualified path. If you use a partially qualified path, the starting point for the path is established by the current execution environment. If only a file name is used, two starting points will be tried: the path that the root source file uses, and then the path that the current execution environment establishes.

Note that if a precompiled file includes another file, the precompiled file is considered the root source file relative to its included files are concerned. The installation and setup code might impose additional restrictions.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20#Include%20Preprocessor%20Directive%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


