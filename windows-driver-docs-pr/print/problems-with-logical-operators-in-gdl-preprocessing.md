---
title: Problems with Logical Operators in GDL Preprocessing
author: windows-driver-content
description: Problems with Logical Operators in GDL Preprocessing
ms.assetid: 8ba1758c-8b8e-4eb2-8625-ffee213025aa
keywords:
- preprocessor directives WDK GDL , problems with preprocessing
- directives WDK GDL , source file preprocessor directives
- source files WDK GDL , problems with preprocessing
- preprocessor directives WDK GDL , logical operators
- logical operators WDK GDL
- NOT operator WDK GDL
- AND operator WDK GDL
- OR operator WDK GDL
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Problems with Logical Operators in GDL Preprocessing


Logical operators in GDL preprocessor conditionals are not currently supported, but they can be simulated.

### <a href="" id="simulating-the-not-operator"></a> Simulating the NOT operator

You might typically use the NOT operator as the following code example shows.

```
#Ifdef:  symbol
--do this--
#Endif: 
```

However, you should use the following code example instead.

```
#Ifdef:  symbol
#Else:
--do this--
#Endif: 
```

### <a href="" id="simulating-the-and-operator"></a> Simulating the AND operator

You might typically use the AND operator as the following code example shows.

```
#Ifdef:  (symbolA  *AND* symbolB)
--do this--
#Endif: 
```

However, you should use the following code example instead.

```
#Ifdef:  symbolA
#Ifdef:  symbolB
--do this--
#Endif: 
#Endif: 
```

### <a href="" id="simulating-the-or-operator"></a> Simulating the OR operator

You might typically use the OR operator as the following code example shows.

```
#Ifdef:  (symbolA  *OR* symbolB)
--do this--
#Endif: 
```

However, you should use the following code example instead.

```
#Ifdef:  symbolA
#Define: TempSymbol
#Elseifdef: symbolB
#Define: TempSymbol
#Endif: 
#Ifdef:  TempSymbol
--do this--
#Endif: 
#Undefine: TempSymbol
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Problems%20with%20Logical%20Operators%20in%20GDL%20Preprocessing%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


