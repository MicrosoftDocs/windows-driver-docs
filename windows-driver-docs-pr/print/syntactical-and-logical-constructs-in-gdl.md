---
title: Syntactical and Logical Constructs in GDL
author: windows-driver-content
description: Syntactical and Logical Constructs in GDL
ms.assetid: f0802424-319c-4ba4-a8cd-539006f4d22c
keywords:
- syntactical constructs WDK GDL
- logical constructs WDK GDL
- constructs WDK GDL , syntactical constructs
- constructs WDK GDL , logical constructs
- GDL WDK , constructs
- parser WDK GDL , handling constructs
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Syntactical and Logical Constructs in GDL


GDL distinguishes between the constructs that are literally defined by entries in the GDL source file and the representation of those constructs in GDL's internal data. The former is a syntactical representation, and the latter is a logical representation. The representations differ when constructs are defined in the source file. The GDL parser creates only one logical representation of a construct for a given construct type and construct tag, no matter how many times such a construct is defined in the GDL source file.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Syntactical%20and%20Logical%20Constructs%20in%20GDL%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


