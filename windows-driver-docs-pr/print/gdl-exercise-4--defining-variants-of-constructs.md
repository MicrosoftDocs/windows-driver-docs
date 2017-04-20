---
title: GDL Exercise 4 Defining Variants of Constructs
author: windows-driver-content
description: GDL Exercise 4 Defining Variants of Constructs
ms.assetid: b923b5f8-6e60-44a0-a38e-8bfa315281c5
keywords:
- GDL WDK , examples
- examples WDK GDL
- tutorials WDK GDL
- GDL WDK , tutorials
- constructs WDK GDL , creating constructs
- creating GDL constructs WDK
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDL Exercise 4: Defining Variants of Constructs


### <a href="" id="exercise"></a> Exercise

Modify the construct \*PFeature from [Exercise 3](gdl-exercise-3--creating-root-level-constructs.md) by defining two variants: \*PFeature: PaperSize and \*PFeature InputTray.

The POption that is contained in \*PFeature: PaperSize has the following attributes: **\*Name**, **\*Command**, **\*Papersize**.

The POption that is contained in \*PFeature: InputTray has the following attributes: **\*Name**, **\*Command**, and **\*Capacity:** *\# of sheets*.

Create a template to abstract the common properties of these two types of \*POptions.

### <a href="" id="solution"></a> Solution

The following template satisfies the conditions.

```
*Template:  COMMAND_TYPE
{
    *Type:  DATATYPE
    *DataType:   FILTER_TYPE
    *ElementType:  XML_STRING
    *FilterTypeName: "COMMAND_STRING"
}
*Template:  ACOMMAND
{
    *Name:  "*Command"
    *Type:  ATTRIBUTE
    *ValueType:  COMMAND_TYPE
}
```

The following derived option template further defines properties of the virtual template POPTION.

```
*Template:  GENERIC_OPTION
{
    *Inherits: POPTION
    *Members:  (NAME, ACOMMAND)
    *Instances:  <ANY>
}
*Template:  XML_INT4
{
    *Type:  DATATYPE
    *DataType:   XML_TYPE
    *XMLDataType: "int"
}
*Template:  INTEGER
{
    *Type:  DATATYPE
    *DataType:   FILTER_TYPE
    *ElementType:  XML_INT4
    *FilterTypeName: "HEX_OR_INT"
}
*Template:  XML_FLOAT
{
    *Type:  DATATYPE
    *DataType:   XML_TYPE
    *XMLDataType: "float"
}
*Template:  PAIR_OF_FLOAT
{
    *Type:  DATATYPE
    *DataType:   ARRAY
    *ElementType:  XML_FLOAT
    *RequiredDelimiter: ","
    *OptionalDelimiter: "<20 09>"
    *ArrayLabel: "PAIR"
    *ElementTags: (width, height)
    *ArraySize: 2
}
*Template:  LEN_UNITS
{
    *Type:  DATATYPE
    *DataType:   ENUMERATOR
    *XMLDataType: "LengthUnits"
    *EnumeratorList: (inches, mm, microns, pixels)
}
*Template:  PAGE_DIM
{
    *Type:  DATATYPE
    *DataType:   COMPOSITE
    *ElementType: (PAIR_OF_FLOAT, LEN_UNITS)
    *RequiredDelimiter: ","
    *OptionalDelimiter: "<20 09>"
    *ElementTags: (dimensions, units)
}
*Template:  PAPERDIMENSIONS
{
    *Name: "*PaperSize"
    *Type:  ATTRIBUTE
    *ValueType:  PAGE_DIM
}
```

The following derived option template further specializes properties of the template GENERIC\_OPTION.

```
*Template:  PAPERSIZE_OPTION
{
    *Name:  "*POption"  *%  Isolate branch from Base Templates
    *Inherits: GENERIC_OPTION
    *Members:  (PAPERDIMENSIONS)
    *Instances:  <ANY>
}


*Template:  PAPERSIZE_FEATURE
{
    *Inherits: PFEATURE
    *Members:  (PAPERSIZE_OPTION)
    *Instances:  PaperSize
}

*Template:  TRAY_CAPACITY
{
    *Name: "*Capacity"
    *Type:  ATTRIBUTE
    *ValueType:  INTEGER
}
```

The following derived option template further specializes properties of the template GENERIC\_OPTION.

```
*Template:  INPUTTRAY_OPTION
{
    *Name:  "*POption"   *%  Isolate branch from Base Templates
    *Inherits: GENERIC_OPTION
    *Members:  (TRAY_CAPACITY)
    *Instances:  <ANY>
}

*Template:  INPUTTRAY_FEATURE
{
    *Inherits: PFEATURE
    *Members:  (INPUTTRAY_OPTION)
    *Instances:  InputTray
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Exercise%204:%20Defining%20Variants%20of%20Constructs%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


