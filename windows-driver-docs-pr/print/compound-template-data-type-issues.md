---
title: Compound Template Data Type Issues
author: windows-driver-content
description: Compound Template Data Type Issues
ms.assetid: 61f26465-c79d-42e3-94c8-26c2c61ecb98
keywords:
- templates WDK GDL , data types
- data types WDK GDL , problems with template data types
- data types WDK GDL , compound
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Compound Template Data Type Issues


When compound data types are created from other data types and parentheses are used to enclose one of the data types, all data types that enclose a parentheses-bracketed data type must also be enclosed by parentheses.

For example, assume that you define a list of GPD integers by using the following templates.

```
*Template:  LIST_OF_INTS
{
    *Type:  DATATYPE
    *DataType:   ARRAY
    *ElementType:  INTEGER
    *RequiredDelimiter: ","
    *OptionalDelimiter: "<20 09>"
    *ElementTags: (int)
    *ArraySize: *
}
*Template:  LIST_OF_LIST_OF_INTS
{
    *Type:  DATATYPE
    *DataType:   ARRAY
    *ElementType:  LIST_OF_INTS
    *RequiredDelimiter: ":"
    *OptionalDelimiter: "<20 09>"
    *ElementTags: (IntList)
    *ArraySize: *
}
```

Then, the following values are valid and equivalent expressions of the LIST\_OF\_LIST\_OF\_INTS data type.

```
*ListList: 1,2,3:10,11,12:20,21,22 
*ListList: (1,2,3:10,11,12:20,21,22)
*ListList: ((1,2,3):(10,11,12):(20,21,22))
```

However, the following value violates the nesting of parenthesis rule.

```
*ListList: (1,2,3):(10,11,12):(20,21,22)
```

The preceding example will generate a syntax error because the parser filter assumes any parenthesis that it encounters belongs to the outermost context, the next parenthesis belongs to the next context, and so on.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Compound%20Template%20Data%20Type%20Issues%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


