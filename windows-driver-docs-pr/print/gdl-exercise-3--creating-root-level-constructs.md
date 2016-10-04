---
title: GDL Exercise 3 Creating Root-Level Constructs
author: windows-driver-content
description: GDL Exercise 3 Creating Root-Level Constructs
MS-HAID:
- 'gplfiles\_ef3fd893-cd46-4312-a815-6528236e1e46.xml'
- 'print.gdl\_exercise\_3\_\_creating\_root\_level\_constructs'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3c7ad284-b77c-4ad3-8334-2fe5b026e340
keywords: ["GDL WDK , examples", "examples WDK GDL", "tutorials WDK GDL", "GDL WDK , tutorials", "constructs WDK GDL , creating constructs", "creating GDL constructs WDK"]
---

# GDL Exercise 3: Creating Root-Level Constructs


### <a href="" id="exercise"></a> Exercise

Modify the schema of [Exercise 1](gdl-exercise-1--implementing-a-gdl-schema.md) to introduce a construct named \*PFeature that can be found only at the root level.

Use the following conditions:

-   \*PFeature can have any instance name.

-   \*PFeature members are the attributes named **\*Name** and **\*DefaultOption**.

-   \*PFeature has a construct member named **\*Poption** that should be declared as virtual.

### <a href="" id="solution"></a> Solution

The following template satisfies the preceding conditions.

```
*Template:  POPTION
{
    *Name:  "*POption"
    *Type: CONSTRUCT
    *Virtual:  TRUE
}

*Template:  NAME
{
    *Name:  "*Name"
    *Type:  ATTRIBUTE
    *ValueType:  NORMAL_STRING
}

*Template:  SYMBOL
{
    *Type:  DATATYPE
    *DataType:   FILTER_TYPE
    *ElementType:  XML_STRING
    *FilterTypeName: "SYMBOLNAME"
}
*Template:  DEFAULT_OPT
{
    *Name: "*DefaultOption"
    *Type:  ATTRIBUTE
    *ValueType:  SYMBOL
}

*Template:  PFEATURE 
{
    *Name:  "*PFeature"
    *Type: CONSTRUCT
    *Members:  (POPTION, NAME, DEFAULT_OPT)
    *Instances:  <ANY>
}
*Template:  ROOT2
{
    *Inherits: ROOT
    *Members:  (PFEATURE)
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Exercise%203:%20Creating%20Root-Level%20Constructs%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


