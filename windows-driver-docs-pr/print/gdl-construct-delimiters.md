---
title: GDL Construct Delimiters
author: windows-driver-content
description: GDL Construct Delimiters
ms.assetid: 6f759534-3dc2-4e04-afe0-3f377790be21
keywords: ["constructs WDK GDL , delimiters", "GDL WDK , constructs", "parser WDK GDL , handling construct delimiters"]
---

# GDL Construct Delimiters


The *construct delimiter* characters are the curly braces: { and }. Construct delimiter characters additionally behave like linebreaks, so you must follow or precede a construct delimiter with a linebreak sequence.

The following two code examples show the use of construct delimiters. The first example has the value spread over several lines.

```
*Person: FlorenceF
{
 *Company:Contoso Pharmaceuticals
 {
 *Location: Redmond, WA
 }
}
```

The second example combines the value into one line but still uses the curly braces to delimit the parts of the value.

```
*Person: FlorenceF{*Company:Contoso Pharmaceuticals{*Location: Redmond, WA}}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Construct%20Delimiters%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


