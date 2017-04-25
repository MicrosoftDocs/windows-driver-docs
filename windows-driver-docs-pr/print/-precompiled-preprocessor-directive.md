---
title: '\ PreCompiled Preprocessor Directive'
author: windows-driver-content
description: '\ PreCompiled Preprocessor Directive'
ms.assetid: 639db56d-7677-4d21-8329-a0f35d68151e
keywords:
- preprocessor directives WDK GDL , keywords
- keywords WDK GDL
- reserved keywords WDK
- PreCompiled directive WDK GDL
- GDL WDK , source files
- source files WDK GDL
- precompiled source files WDK GDL
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# \#PreCompiled Preprocessor Directive


```
#PreCompiled:  BOOL
```

The \#PreCompiled directive specifies whether a source file is precompiled.

If *BOOL* is **TRUE**, the source file is assumed to be precompiled. Otherwise, if the source file is referenced through an [\#Include](-include-preprocessor-directive.md) directive, the file is included in-line.

The \#PreCompiled directive must appear before any [\#Include](-include-preprocessor-directive.md) directive within a GDL source file; otherwise, it is ignored. The *BOOL* value is required.

Files that are marked as precompiled will be parsed in a root context. That is, any context that is established by the host or including GDL files will be lost. For example, if the host GDL file defined preprocessor symbols before including the precompiled file, those symbols would not exist when the precompiled file is parsed. This type of parsing ensures that multiple versions of a precompiled file cannot be created by using [\#Ifdef](-ifdef-conditional-preprocessor-directive.md) blocks and having different hosts define different symbols to access the various \#Ifdef blocks. Because the precompiled file is never reparsed, there will be only one unique version. Thus, the writer of a precompiled file must not rely on any externally defined preprocessor symbols.

Also note that precompiled files must be unique and they must be independent of the host that includes them. Precompiled files do not rely on any included content that the host file references or any content that might be defined in the host file.

This preprocessor directive is new for GDL.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20#PreCompiled%20Preprocessor%20Directive%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


