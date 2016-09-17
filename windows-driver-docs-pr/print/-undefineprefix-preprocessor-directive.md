---
title: \ UndefinePrefix Preprocessor Directive
author: windows-driver-content
description: \ UndefinePrefix Preprocessor Directive
MS-HAID:
- 'gplfiles\_6c271a60-8846-47f7-b4b8-c3ee55a5eb50.xml'
- 'print.\_undefineprefix\_preprocessor\_directive'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 7c99c2cf-6609-4fec-ae21-1477699ba5c8
keywords: ["preprocessor directives WDK GDL , keywords", "keywords WDK GDL", "reserved keywords WDK", "UndefinePrefix directive WDK GDL"]
---

# \#UndefinePrefix Preprocessor Directive


```
#UndefinePrefix:
```

The \#UndefinePrefix directive deletes the current prefix. The previously defined prefix becomes the current prefix. Only prefixes that you define by using the [\#SetPPPrefix](-setppprefix-preprocessor-directive.md) directive can be undefined. The system default prefix cannot be undefined. This directive does not use a symbol.

This preprocessor prefix is new for GDL.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20#UndefinePrefix%20Preprocessor%20Directive%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


