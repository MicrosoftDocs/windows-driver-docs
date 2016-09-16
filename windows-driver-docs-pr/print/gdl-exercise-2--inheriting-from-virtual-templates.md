---
title: GDL Exercise 2 Inheriting from Virtual Templates
author: windows-driver-content
description: GDL Exercise 2 Inheriting from Virtual Templates
MS-HAID:
- 'gplfiles\_002b8198-7dcd-421c-8273-4762ef34fc9c.xml'
- 'print.gdl\_exercise\_2\_\_inheriting\_from\_virtual\_templates'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 89878438-bea4-4d6f-bf3b-88d5bef0e6ab
keywords: ["GDL WDK , examples", "examples WDK GDL", "tutorials WDK GDL", "GDL WDK , tutorials", "schemas WDK GDL , implementing GDL schemas", "templates WDK GDL , inheritance", "templates WDK GDL , examples", "inheritance WDK GDL", "virtual templates WDK GDL"]
---

# GDL Exercise 2: Inheriting from Virtual Templates


### <a href="" id="exercise"></a> Exercise

Define a data type that accepts a Unicode string that is encoded by using 2 bytes to represent 1 Unicode character. Then, define non-virtual templates that inherit from the previously defined virtual templates. Do not modify the schema that you created in [Exercise 1](gdl-exercise-1--implementing-a-gdl-schema.md). Create a sample GDL data file and verify the schema is applied correctly. Create a sample GDL data file that does not conform to the schema and verify the errors are detected.

### <a href="" id="solution"></a> Solution

The following two templates define the Unicode data type.

```
*Include: MasterTemplate.gdl
 
*Template:  XML_STRING
{
    *Type:  DATATYPE
    *DataType:   XML_TYPE
    *XMLDataType: "string"
}
```

```
*Template:  NORMAL_STRING
{
    *Type:  DATATYPE
    *DataType:   FILTER_TYPE
    *ElementType:  XML_STRING
    *FilterTypeName: "NORMAL_STRING"
}
```

The following template inherits from the templates that are defined in Exercise 1. There is a construct named \*Command and three types of attributes: **\*Name** (which appears at the root level), **\*CommandName** (which can appear within a \*Command construct), and **\*UniName** (which can appear within both contexts).

```
*Template:  COMMAND
{
    *Name:  "*Command"
    *Inherits: CONSTRUCTS
    *Instances:  <ANY>
}
*Template:  ROOT_NAME
{
    *Name:  "*Name"
    *Inherits: ROOT_ATTRIB
    *ValueType:  NORMAL_STRING
}
*Template:  CMD_NAME
{
    *Name:  "*CommandName"
    *Inherits: CONSTRUCT_ATTRIB
    *ValueType:  NORMAL_STRING
}
*Template:  UNIVERSAL_NAME
{
    *Name:  "*UniName"
    *Inherits: FREEFLOAT
    *ValueType:  NORMAL_STRING
}
```

The following GDL file conforms to the given schema.

```
*Name: "can only appear at root level"
*UniName:  "can appear anywhere"
*Command: X
{
    *CommandName:  "May only appear within a command"
    *UniName:  "can appear anywhere, even in a command"
    *Command: nested
    {
        *CommandName:  "nested commands are ok."
        *UniName:  "template defined a recursive nesting" 100 %
    }
}
```

The following GDL file does not conform to the given schema.

```
*CommandName:  "Error! May only appear within a command"
*Command: X
{
    *Name: "Error! can only appear at root level"
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Exercise%202:%20Inheriting%20from%20Virtual%20Templates%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


