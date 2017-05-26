---
title: Defining the Configuration-Dependent Data Parameters
author: windows-driver-content
description: Defining the Configuration-Dependent Data Parameters
ms.assetid: a5bb2e3a-22e0-41d7-8035-5437ac473b21
keywords:
- GDL WDK , configurations
- configurations WDK GDL , defining configuration-dependent data
- defining configuration-dependent data WDK GDL
- PICKMANY parameters WDK GDL
- PICKONE parameters WDK GDL
- null-value parameters WDK GDL
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Defining the Configuration-Dependent Data Parameters


Parameters are introduced by using the **\*Features** construct. The construct tag of the **\*Features** construct identifies the parameter (or defines the parameter name, which is also referred to as the *feature name*).

The content of the **\*Features** construct can consist of one or more **\*Option** constructs. The **\*Option** constructs define the allowed values or states that the parameter can be in. The construct tag of the **\*Option** construct identifies an allowed value or state. This construct tag is also called the *option name*.

For example,you can define a parameter named *Today* that can take a day of the week as its value, as the following code example shows.:

```
*Feature: Today
{
  *Option: Sunday{}
  *Option: Monday{}
  *Option: Tuesday{}
  *Option: Wednesday{}
  *Option: Thursday{}
  *Option: Friday{}
  *Option: Saturday{}
}
```

In the preceding example, the *Today* parameter can take only one value at any given time. *Today* cannot be both **Sunday** and **Tuesday**. However, not all parameters are not limited to exclusive values; they can take one or more values at a time. For example, if you have a robot that can hold more than one color of pen in its hand at the same time, you can define a *PenColors* parameter to describe the colors that are currently in its hand. You might specify **PenColors: (Red AND Green AND Yellow)** and that might be perfectly valid.

The **\*UIType** reserved directive enables you to designate whether a parameter can take only a single value at any time (PICKONE) or whether multiple values can be assigned to that parameter at a given time (PICKMANY). The **\*UIType** directive is positioned as a child entry of the **\*Features** construct.

**Note**   GDL does not allow "nothing" to be assigned to a parameter. Thus, to describe the robot holding no pens, you must declare an option called None or Off for PICKMANY parameters. The option name that is used is not important; you can designate which option is assigned this property by using the **\*NoneOption** directive. The option that **\*NoneOption** designates is not compatible with any of the other options.

 

You can define as many **\*Feature** constructs as you have parameters. All **\*Feature** constructs must reside at the *root context*. The root context has no parent construct.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Defining%20the%20Configuration-Dependent%20Data%20Parameters%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


