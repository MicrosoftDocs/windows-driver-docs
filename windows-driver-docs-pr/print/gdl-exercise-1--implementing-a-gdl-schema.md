---
title: GDL Exercise 1 Implementing a GDL Schema
author: windows-driver-content
description: GDL Exercise 1 Implementing a GDL Schema
ms.assetid: 0adfef5a-4211-45e9-bb65-8174822efdc5
keywords:
- GDL WDK , examples
- examples WDK GDL
- tutorials WDK GDL
- GDL WDK , tutorials
- schemas WDK GDL , implementing GDL schemas
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDL Exercise 1: Implementing a GDL Schema


### <a href="" id="exercise"></a> Exercise

Implement a schema that creates three categories of attributes and does not impose restrictions on where constructs can be located.

These attributes must be divided into the following categories:

-   Attributes that can appear at the root level and within constructs.

-   Attributes that can appear only at the root level.

-   Attributes that can appear only within constructs.

Do not define any keywords in your schema; just include the framework for the future keywords.

**Note**   By using templates, you can create a virtual schema--that is, a schema that does not define any GDL entries. The base schema that is defined in this way exerts its influence no matter how this schema is extended in the future.

 

### <a href="" id="solution"></a> Solution

The following code example demonstrates one way to complete this exercise.

```
*Template:  ATTRIBUTE
{
    *Type:  ATTRIBUTE
    *Virtual:  TRUE
}
*Template:  ROOT_ATTRIB
{
    *Inherits: ATTRIBUTE
    *Virtual:  TRUE
}
*Template:     CONSTRUCT_ATTRIB  *%  May not appear at Root level
{
    *Inherits: ATTRIBUTE
    *Virtual:  TRUE
}
*Template:     FREEFLOAT
{
    *Inherits: ATTRIBUTE
    *Virtual:  TRUE
}
*Template:  CONSTRUCTS
{
    *Type: CONSTRUCT
    *Members:  ( CONSTRUCTS, FREEFLOAT, CONSTRUCT_ATTRIB)
    *Virtual:  TRUE
}

*Template:  ROOT
{
            *Type: CONSTRUCT
            *AllowNewMembers: FALSE
            *Name:  "root"
            *Instances:  <ANY>
            *Members:  (ROOT_ATTRIB, FREEFLOAT, CONSTRUCTS)
}
```

**Note**   You can place the templates in the preceding example in a MasterTemplate.gdl file for use by the next exercise.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Exercise%201:%20Implementing%20a%20GDL%20Schema%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


