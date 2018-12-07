---
title: Multiple Personality Template Data Types
description: Multiple Personality Template Data Types
ms.assetid: ee550416-9185-41fa-b113-6a1d22c3aa96
keywords:
- templates WDK GDL , data types
- data types WDK GDL , compound
- MULTIPLE_PERSONALITY data type WDK GDL
- ElementType directive WDK GDL
- ElementTags directive WDK GDL
- unions WDK GDL
- GDL WDK , unions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Multiple Personality Template Data Types


A MULTIPLE\_PERSONALITY data type represents a value that can hold different data types at different times. This data type is similar to the C language **union** data type.

\*DataType: MULTIPLE\_PERSONALITY directs a template to define a data type that can accept values that belong to several different data types, much like a C language **union** data type. The MULTIPLE\_PERSONALITY data type attempts to determine the identity (that is, data type) of the value and will output the same XML as if the value was explicitly defined in the template to belong to the identified data type. In other words, if a MULTIPLE\_PERSONALITY data type were defined to hold a string or integer or SYMBOL, and if the value actually held an integer, the XML output will be that for an integer data type.

A personality tag attribute is also emitted to help clients determine the data type of the value that was emitted. The filter determines the data type of the value by parsing the value by using each potential data type. The data type that successfully matches the largest amount of the input value is chosen. In the event of a tie, the element type that appears first in the list will be selected.

**Note**   You can construct value syntaxes that can trick this evaluation algorithm, so be careful when you select the element types to list. The types must be sufficiently distinguishable by the parsing algorithm. For example, because the parser filter does not recognize any XML syntax, it cannot distinguish between two XML\_TYPE data types. However, in these cases, the definition of the candidate data types can include an \*ArrayLabel directive that will help the parser distinguish between them.

 

The following directives are used to define the MULTIPLE\_PERSONALITY data type:

-   \*ElementType (Required). A list of template names that defines the potential data types that this value could assume.

-   \*ElementTags (Required). A list of tags to help the client identify the data type that is actually assigned to the value. The number of tags that are provided should equal the number of templates that are listed in \*ElementType. The tag will appear in a personality attribute in the generated XML element that represents the value. For example, if the data type is an array of multiple personality data types, the elements that represent the individual members of the array will contain the personality attribute. The element that represents the entire array will not contain the personality attribute because the array itself does not have a defined personality; instead, the individual members of the array have their own distinct personality attribute value.

Consider the following template.

```cpp
*Template:  INT_OR_QUALNAME_EX
{
    *Type:  DATATYPE
    *DataType:   MULTIPLE_PERSONALITY
    *ElementType:  (INTEGER, QUALNAME_EX, QUOTEDSTRING)
    *ElementTags: (integer, QualNameEx, QuotedString)
}
```

This template defines a data type that can hold an INTEGER value, QUALNAME\_EX value, or a QUOTEDSTRING value. Whatever data type is selected will be identified with the corresponding user-defined ElementTag.

Consider the following GDL entries.

```cpp
*rcNameID:     ( RESDLL.stdname.467 )  
*rcNameID:      (0x117 )  
```

And consider the following RC\_NAME\_ID2 template.

```cpp
*Template:  RC_NAME_ID2
{
    *Name:  "*rcNameID"
    *Type:  ATTRIBUTE
    *ValueType:  INT_OR_QUALNAME_EX
    *Additive: LEAST_TO_MOST_RECENT
}
```

If the GDL entries are interpreted by the preceding template, the resulting XML output will be as follows.

```cpp
<GDL_ATTRIBUTE Name="*rcNameID"  Personality="QualNameEx" >
   <feature  xsi:type="GDLW_string">RESDLL</feature>
   <option  xsi:type="GDLW_string">stdname</option>
   <resourceID  xsi:type="GDLW_int">467</resourceID>
</GDL_ATTRIBUTE>
<GDL_ATTRIBUTE Name="*rcNameID"  Personality="integer" 
xsi:type="GDLW_int" >279</GDL_ATTRIBUTE>
```

The only difference between the XML output that is generated from the MULTIPLE\_PERSONALITY type and the actual type is the additional personality tag attribute that is added to inform the client of the value's actual data type.

For example, you can create an array where each member of the array is a MULTIPLE\_PERSONALITY type, as follows.

```cpp
*Template:  DT_ARRAY_OF_MP
{
    *Type:  DATATYPE
    *DataType:   ARRAY
    *ElementType:  INT_OR_QUALNAME_EX
    *RequiredDelimiter: ","
    *OptionalDelimiter: "<20 09>"
    *ElementTags: (ArrayMember)
    *ArraySize: *
}
*Template:  ARRAY_OF_MP
{
    *Name:  "*rcNameID_List"
    *Type:  ATTRIBUTE
    *ValueType:  DT_ARRAY_OF_MP
}
```

And you can use the preceding template to process the following instance data, which is an array that contains three multiple personality objects, each of which happens to have a different personality.

```cpp
*rcNameID_List:( RESDLL.stdname.467, 0x117, "Quote" )
```

This processing will produce the following XML snapshot.

```cpp
    <GDL_ATTRIBUTE Name="*rcNameID_List"  >
        <ArrayMember  Personality="QualNameEx">
            <feature  xsi:type="GDLW_string">RESDLL</feature>
            <option  xsi:type="GDLW_string">stdname</option>
            <resourceID  xsi:type="GDLW_int">467</resourceID>
        </ArrayMember>
        <ArrayMember  Personality="integer" xsi:type="GDLW_int">279</ArrayMember>
        <ArrayMember  Personality="QuotedString" xsi:type="GDLW_string">Quote</ArrayMember>
    </GDL_ATTRIBUTE>
```

As the snapshot shows, the parser determined the correct personality for each of the three array members and set the personality attribute in each member's element to indicate the appropriate personality.

 

 




