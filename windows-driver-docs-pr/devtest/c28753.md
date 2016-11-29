---
title: C28753
description: Warning C28753 Relying on undefined order of evaluation of parameters.
ms.assetid: D8879714-63A2-4F36-B08A-1E487ACB5BC1
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28753%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




