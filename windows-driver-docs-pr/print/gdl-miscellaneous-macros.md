---
title: GDL Miscellaneous Macros
author: windows-driver-content
description: GDL Miscellaneous Macros
MS-HAID:
- 'gplfiles\_1420028c-d872-4342-8fde-5324e66aedd8.xml'
- 'print.gdl\_miscellaneous\_macros'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d3c66bc1-815d-484b-b69b-6616d2b43069
keywords: ["GDL WDK , macros", "macros WDK GDL , miscellaneous macros", "IgnoreBlock directive WDK GDL", "macros WDK GDL , examples", "constructs WDK GDL , disabling processing of constructs", "disabling processing of GDL constructs WDK GDL"]
---

# GDL Miscellaneous Macros


GDL uses a **\*IgnoreBlock** directive to disable processing of the contents of the construct. This directive is useful when implementing divide and conquer debugging strategies or to comment out obsolete code. The contents of **\*IgnoreBlock** must still conform to the basic syntax rules. Invalid GDL or large comment blocks can be enclosed within &lt;Begin/EndValue:&gt; delimiters and made the value of the **\*IgnoreBlock**.

The following code example shows how to use **\*IgnoreBlock**.

```
*IgnoreBlock: <BeginValue:garbage> The code in between does not even need to be valid GDL. }{ " % !!! 
This directive is great for large blocks of comments 
or when you do not want to mark each line with *%  <EndValue:garbage> {}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Miscellaneous%20Macros%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


