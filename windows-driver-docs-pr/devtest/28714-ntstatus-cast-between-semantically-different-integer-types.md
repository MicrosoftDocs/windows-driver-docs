---
title: C28714
description: Warning C28714 Cast between semantically different integer types.
ms.assetid: 53acc1a1-58a9-4009-a15c-2b11f31b086d
---

# C28714


warning C28714: Cast between semantically different integer types

This warning indicates that an **NTSTATUS** value is being explicitly cast to a Boolean type. This is likely to give undesirable results. For example, the typical success value for **NTSTATUS**, **STATUS\_SUCCESS**, is **false** when tested as a Boolean.

In most cases, the **NT\_SUCCESS** macro should be used to test the value of an **NTSTATUS**. This macro returns **true** if the returned status value is neither a warning nor an error code. If a function returns a Boolean to indicate its failure/success, it should explicitly return the appropriate Boolean type rather than depend on casting of **NTSTATUS** to a Boolean type.

Also, occasionally a program may attempt to reuse a Boolean local variable to store **NTSTATUS** values. This practice is often error-prone; it is much safer (and likely more efficient) to use a separate **NTSTATUS** variable.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28714%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




