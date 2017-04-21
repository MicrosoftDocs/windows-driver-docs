---
title: '\ Endif Conditional Preprocessor Directive'
author: windows-driver-content
description: '\ Endif Conditional Preprocessor Directive'
ms.assetid: dfbfdb4a-955b-4ccf-b496-c8c5ddc42d2b
keywords:
- preprocessor directives WDK GDL , conditional directives
- directives WDK GDL , conditional directives
- conditional directives WDK GDL
- Endif directive WDK GDL
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# \#Endif Conditional Preprocessor Directive


```
#Endif:
```

The \#Endif directive defines the end of the previous section and the conditional construct. No symbol is used. You can use a fake symbol name as the value of the \#Endif directive to help the reader. Consider the following code example.

```
    #Ifdef: symbolA

        #Ifdef: symbolB

        #Elseifdef: symbolD

        #Endif: symbolB

    #Endif: symbolA
```

Indentation of each nested construct might also be helpful to the reader.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20#Endif%20Conditional%20Preprocessor%20Directive%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


