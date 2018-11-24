---
title: C28753
description: Warning C28753 Relying on undefined order of evaluation of parameters.
ms.assetid: D8879714-63A2-4F36-B08A-1E487ACB5BC1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28753


warning C28753: Relying on undefined order of evaluation of parameters

C/C++ allows the compiler to generate code to evaluate actual parameters in any order, and the x86 and ARM compilers tend to select different orders. Code that relies on a specific order may behave differently on different platforms.

A common mistake is with the use of smart pointers where the address-of operator **&** has side effects, in calls like this:

```ManagedCPlusPlus
sp->Foo(&sp);
```

The calls to member access operator **-&gt;** and operator **&** might happen in either order. Thus side effects from operator **&** might happen before or after operator **-&gt;** is called. This warning finds these buggy calls to prevent different behavior between platforms.

## <span id="Example"></span><span id="example"></span><span id="EXAMPLE"></span>Example


The code following example generates this warning.

```ManagedCPlusPlus
sp->Foo(&sp)
```

The following code example avoids this warning.

```ManagedCPlusPlus
SmartPtr spTemp;
sp->Foo(&spTemp);
sp = spTemp;
```

 

 





