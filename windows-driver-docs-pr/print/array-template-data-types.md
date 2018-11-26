---
title: Array Template Data Types
description: Array Template Data Types
ms.assetid: d6be4ec3-1980-4e55-bd52-5249cd93deb8
keywords:
- templates WDK GDL , data types
- data types WDK GDL , compound
- ARRAY data type WDK GDL
- ElementType directive WDK GDL
- RequiredDelimiter directive WDK GDL
- OptionalDelimiter directive WDK GDL
- ElementTags directive WDK GDL
- ArraySize directive WDK GDL
- ArrayLabel directive WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Array Template Data Types


ARRAY data types consist of one or more values that all have the same data type. Arrays can be defined to be fixed, variable, or indefinite length.

**\*DataType: ARRAY** directs a template to define a compound data type whose members are all of the same data type (also known as the members' data type). The members of the array data type will be output as individual XML child elements that belong to the element that represents the enclosing context.

If each child element represents a data type primitive, the data type will be defined by the XML attribute **xsi:type** in each element. If a GDL attribute is defined to be of data type ARRAY, the enclosing context will be the &lt;GDL\_ATTRIBUTE&gt; element. The element name of each XML child element will be the corresponding tag that the **\*ElementTags** directive defines. If the COMPOSITE is itself a member of another compound data type, an element will be created to represent that enclosing context. The name of this parent element will be the corresponding tag that is assigned by the template that defined the enclosing compound data type.

The following directives are used to define the ARRAY data type:

-   **\*ElementType** (Required). The name of template that defines the data type of all of the elements. You can specify only one data type.

-   **\*RequiredDelimiter** (Required). A string that will syntactically separate each array element from the next. Two consecutive delimiters will be interpreted as an omitted element. Delimiters are not needed to indicate the omission of trailing elements. Be very careful if whitespace is used as the delimiter or as part of the delimiter string. For example, extraneous space characters will be interpreted by the parser as indicating omitted elements; and because you might not be able to see such extra whitespace characters, you might encounter unexpected parsing errors.

    Also, excess whitespace is routinely stripped from the source file and whitespace is often added to the input stream as a result of preprocessor, macro, and comment processing. Thus, the actual string that is parsed might have a completely different number of space characters than originally specified.

    You should not use tab characters as part of the required delimiter string because they are routinely converted to space characters during input processing.

-   **\*OptionalDelimiter** (Optional). Any string that consists of characters that are specified in **\*OptionalDelimiter** and that appear adjacent to the **\*RequiredDelimiter** string will be considered part of the delimiter. The first character that is defined in the **\*RequiredDelimiter** string must not appear within the **\*OptionalDelimiter**.

-   **\*ElementTags** (Required). If you want to assign every element in the array the same element name (or if the array can be of unlimited size), provide only one tag. Otherwise, provide a number equal to the maximum value that **\*ArraySize** specifies.

    Each member of the array will be named with the corresponding tag. This naming is useful if one or more array elements are omitted. When array elements are omitted, the tag that corresponds to the omitted element is not used. To avoid confusing the client, do not use GDL snapshot reserved element names (that is, CONSTRUCT, ATTRIBUTE, and Personality,) as tag names.

-   **\*ArraySize** (Required). Use one integer to specify the size of a fixed-size array, or use two integers to specify the minimum and maximum allowed size for a variable-sized array. Note that zero is allowed for the minimum size and the GPD wildcard character (\*) can be used to specify the size or maximum size. Indicate omitted values in the instance data with consecutive commas (for example, `*DaysOfWeek: (Sunday, Monday,  ,  Wednesday,  , Friday,`).

-   **\*ArrayLabel** (Optional). If this directive is specified, the list of array elements must be enclosed by parentheses and be prefaced by the **\*ArrayLabel** label. If no label is specified in this directive, the parentheses are optional, and no prefacing label is allowed.

Consider the following template.

```GDL
*Template:  RECTANGLE
{
    *Type:  DATATYPE
    *DataType:   ARRAY
    *ElementType:  INTEGER
    *RequiredDelimiter: ","
    *OptionalDelimiter: "<20 09>"
    *ArrayLabel: "rect"
    *ElementTags: (left, top, right, bottom)
    *ArraySize: 4
}
```

This template defines a fixed-size, array of four integers. The array is assigned a label (`rect`) and each element in the array is assigned a unique element tag. These tags will label each element in the XML output to help the client. Each element is separated from the next by a comma or a comma plus any combination of space and tab characters. Because the array size is fixed, no element omission is allowed.

**\*DataType: ARRAY** templates do not generate a corresponding schema. The schema of the template that is named in the **\*ElementType** directive is used instead.

Consider the following GDL entry.

```GDL
*ImageableArea:   rect( - 10, 20 , +30, 0x40  )  
```

And consider the IMAGERECT template.

```GDL
*Template:  IMAGERECT
{
    *Name:  "*ImageableArea"
    *Type:  ATTRIBUTE
    *ValueType:  RECTANGLE
}
```

If the GDL entry is interpreted by the IMAGERECT template, the resulting XML output will be.

```xml
<GDL_ATTRIBUTE Name="*ImageableArea"  >
<left  xsi:type="GDLW_int">-10</left>
   <top  xsi:type="GDLW_int">20</top>
   <right  xsi:type="GDLW_int">30</right>
   <bottom  xsi:type="GDLW_int">64</bottom>
</GDL_ATTRIBUTE> 
```

Note that the reference is to the wrapped type **GDLW\_int** rather than the original **int**.
