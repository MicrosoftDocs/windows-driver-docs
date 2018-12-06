---
title: '#PreCompiled Preprocessor Directive'
description: '#PreCompiled Preprocessor Directive'
ms.assetid: 639db56d-7677-4d21-8329-a0f35d68151e
keywords:
- preprocessor directives WDK GDL , keywords
- keywords WDK GDL
- reserved keywords WDK
- PreCompiled directive WDK GDL
- GDL WDK , source files
- source files WDK GDL
- precompiled source files WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# \#PreCompiled Preprocessor Directive


```GDL
#PreCompiled:  BOOL
```

The \#PreCompiled directive specifies whether a source file is precompiled.

If *BOOL* is **TRUE**, the source file is assumed to be precompiled. Otherwise, if the source file is referenced through an [\#Include](-include-preprocessor-directive.md) directive, the file is included in-line.

The \#PreCompiled directive must appear before any [\#Include](-include-preprocessor-directive.md) directive within a GDL source file; otherwise, it is ignored. The *BOOL* value is required.

Files that are marked as precompiled will be parsed in a root context. That is, any context that is established by the host or including GDL files will be lost. For example, if the host GDL file defined preprocessor symbols before including the precompiled file, those symbols would not exist when the precompiled file is parsed. This type of parsing ensures that multiple versions of a precompiled file cannot be created by using [\#Ifdef](-ifdef-conditional-preprocessor-directive.md) blocks and having different hosts define different symbols to access the various \#Ifdef blocks. Because the precompiled file is never reparsed, there will be only one unique version. Thus, the writer of a precompiled file must not rely on any externally defined preprocessor symbols.

Also note that precompiled files must be unique and they must be independent of the host that includes them. Precompiled files do not rely on any included content that the host file references or any content that might be defined in the host file.

This preprocessor directive is new for GDL.
