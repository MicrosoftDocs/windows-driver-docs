---
title: GDL Preprocessor Guidelines
author: windows-driver-content
description: GDL Preprocessor Guidelines
ms.assetid: dc8450ca-cacc-458c-a05b-8566d04d8bae
keywords:
- preprocessor directives WDK GDL , guidelines
- directives WDK GDL , source file preprocessor directives
- source files WDK GDL , preprocessor directives
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDL Preprocessor Guidelines


Use the following guidelines when you are writing GDL preprocessor directives:

To prevent unintended consequences, writers of GDL files should observe the following guidelines when defining preprocessor symbols and prefixes.

Never undefine any symbol that you did not explicitly define in the file, and before your file ends, always undefine any symbol that you defined in the file. In other words, always leave the symbol and prefix stacks as you found them. If this guideline is followed, there will never be namespace collisions that involve the preprocessor.

The GDL parser interface will enable the client to inject an arbitrary-sized fragment of GDL text that will be processed ahead of the root GDL file. This opportunity will enable clients to define any preprocessor symbols that are needed so the parser processes the appropriate sections of the GDL file. This fragment might include other GDL standard templates or define standard macros.

**Note**   When a file is included in-line, all preprocessor symbols and prefixes that are defined in the host remain defined during preprocessing of the included file. When a file is processed as precompiled, an entirely new parsing environment is created. Thus, all symbols and prefixes are returned to their defaults. Files that will be processed as precompiled should not have any dependencies on externally or host file-defined preprocessor symbols.

 

**Note**   Preprocessor directives and macros are unaffected by switch/case constructs because the directives are evaluated separately before any switch/case constructs.

 

Logical operators are not supported in GDL preprocessor directives. For more information about to solve this situation, see [Problems with Logical Operators in GDL Preprocessing](problems-with-logical-operators-in-gdl-preprocessing.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Preprocessor%20Guidelines%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


