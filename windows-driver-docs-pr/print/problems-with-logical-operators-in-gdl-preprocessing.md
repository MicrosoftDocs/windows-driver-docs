---
title: Problems with Logical Operators in GDL Preprocessing
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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Problems with Logical Operators in GDL Preprocessing


Logical operators in GDL preprocessor conditionals are not currently supported, but they can be simulated.

### <a href="" id="simulating-the-not-operator"></a> Simulating the NOT operator

You might typically use the NOT operator as the following code example shows.

```cpp
#Ifdef:  symbol
--do this--
#Endif: 
```

However, you should use the following code example instead.

```cpp
#Ifdef:  symbol
#Else:
--do this--
#Endif: 
```

### <a href="" id="simulating-the-and-operator"></a> Simulating the AND operator

You might typically use the AND operator as the following code example shows.

```cpp
#Ifdef:  (symbolA  *AND* symbolB)
--do this--
#Endif: 
```

However, you should use the following code example instead.

```cpp
#Ifdef:  symbolA
#Ifdef:  symbolB
--do this--
#Endif: 
#Endif: 
```

### <a href="" id="simulating-the-or-operator"></a> Simulating the OR operator

You might typically use the OR operator as the following code example shows.

```cpp
#Ifdef:  (symbolA  *OR* symbolB)
--do this--
#Endif: 
```

However, you should use the following code example instead.

```cpp
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

 

 




