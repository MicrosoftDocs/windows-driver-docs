---
title: Composite Template Data Types
description: Composite Template Data Types
ms.assetid: 5fd9218a-2827-4cca-b913-eeb6484653d9
keywords:
- templates WDK GDL , data types
- data types WDK GDL , compound
- COMPOSITE data type WDK GDL
- ElementType directive WDK GDL
- RequiredDelimiter directive WDK GDL
- OptionalDelimiter directive WDK GDL
- ElementTags directive WDK GDL
- ArraySize directive WDK GDL
- ArrayLabel directive WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Composite Template Data Types


A COMPOSITE data type consists of one or more values that have the same or different data types. Composites can have a fixed or variable (but not indefinite) length. This data type is similar to the C lLanguage structure data type.

**\*DataType: COMPOSITE** directs a template to define a compound data type whose members can be of different data types. The members of the COMPOSITE data type will be output as individual XML child elements that belong to the element that represents the enclosing context. If each child element represents a data type primitive, the data type will be defined by the XML attribute **xsi:type** in each element. If a GDL attribute is defined to be **DataType : COMPOSITE**, the enclosing context will be the &lt;GDL\_ATTRIBUTE&gt; element. The element name of each XML child element will be the corresponding tag that is defined by **Directive: \*ElementTags**.

If the COMPOSITE is itself a member of another compound data type, an element will be created to represent that enclosing context. The name of this parent element will be the corresponding tag that is assigned by the template that corresponds to the enclosing compound data type.

The following directives are used to define the COMPOSITE data type:

-   **\*ElementType** (Required). The name of the template that defines the data types of each of the elements. One data type must be specified for each element. One or more elements can have the same data type. The number of ElementTypes that are provided should equal the ArraySize or Max value that **\*ArraySize** specifies.

-   **\*RequiredDelimiter** (Required). A string that will syntactically separate each COMPOSITE element from the next. Two consecutive delimiters will be interpreted as an omitted element. Delimiters are not needed to indicate the omission of trailing elements.

    You should be very careful if you use whitespace as the delimiter or as part of the delimiter string. For example, the parser will interpret extraneous space characters as indicating omitted elements; and because you might not see extra whitespace, strange parsing errors might occur. Also, excess whitespace is routinely stripped from the source file and whitespace is often added to the input stream as a result of preprocessor, macro, and comment processing. Thus, the actual string that is parsed might have a completely different number of space characters than originally specified. You should not use tab characters as part of the required delimiter string because they are routinely converted to space characters during input processing.

-   **\*OptionalDelimiter** (Optional). Any string that consists of characters that are specified in **\*OptionalDelimiter** that appears adjacent to the **\*RequiredDelimiter** string will be considered part of the delimiter.

-   **\*ElementTags** (Required). The number of tags that are provided should equal the ArraySize or Max value that **\*ArraySize** specifies. Each member will be tagged with the corresponding tag. This tagging is useful if one or more elements are omitted. When COMPOSITE elements are omitted, the tag that corresponds to the omitted element is not used. To avoid confusing the client, do not use GDL snapshot reserved element names as tag names. These reserved names are CONSTRUCT, ATTRIBUTE, and Personality.

-   **\*ArraySize** (Optional). If this directive is omitted, a fixed-size COMPOSITE will be assumed. The size will be equal to the number of templates names in **\*ElementType**.

    Use two integers to specify the minimum and maximum allowed size for a variable-sized COMPOSITE. Note that zero is allowed for the minimum size. Unlimited-sized COMPOSITE data types are not allowed. You cannot use the GPD wildcard character (\*) to specify the size or maximum size.

-   **\*ArrayLabel** (Optional). If this directive is specified, the list of COMPOSITE elements must be enclosed by parentheses and be prefaced by the **\*ArrayLabel** label. If no label is specified in this directive, the parenthesis are optional, and no prefacing label is allowed.

Consider he following template.

```cpp
*Template:  QUALNAME_EX
{
    *Type:  DATATYPE
    *DataType:   COMPOSITE
    *ElementType: (SYMBOL, SYMBOL, INTEGER)
    *RequiredDelimiter: "."
    *ElementTags: (feature, option, resourceID)
}
```

The preceding template defines a fixed-size, COMPOSITE of two SYMBOL data types and one integer. The COMPOSITE is unlabeled. Each element in the COMPOSITE is assigned a unique ElementTag. These tags will label each element in the XML output to help the client. Each element is separated from the next by exactly one period (.); no other characters are considered part of the delimiter. **\*ArraySize** is not specified, so a fixed COMPOSITE size is assumed. Because the COMPOSITE size is fixed, no member omission is allowed.

**\*DataType: COMPOSITE** templates do not generate a corresponding schema. The schema of the templates that are named in the **\*ElementType** directive are used instead.

For example, consider a SYMBOL template that is defined as follows.

```cpp
*Template:  SYMBOL
{
    *Type:  DATATYPE
    *DataType:   FILTER_TYPE
    *ElementType:  XML_STRING
    *FilterTypeName: "SYMBOLNAME"
}
```

And consider the following GDL entry.

```cpp
*rcNameID:     ( RESDLL.stdname.467 )  
```

Or consider the following GDL entry that does not have the optional parentheses.

```cpp
*rcNameID:     RESDLL.stdname.467 
```

Assume that the GDL entry is interpreted by using the following RC\_NAME\_ID template.

```cpp
*Template:  RC_NAME_ID
{
    *Name:  "*rcNameID"
    *Type:  ATTRIBUTE
    *ValueType:  QUALNAME_EX
    *Additive: LEAST_TO_MOST_RECENT
}
```

The resulting XML output will be as follows.

```cpp
    <GDL_ATTRIBUTE Name="*rcNameID"  >
        <feature  xsi:type="GDLW_string">RESDLL</feature>
        <option  xsi:type="GDLW_string">stdname</option>
        <resourceID  xsi:type="GDLW_int">467</resourceID>
    </GDL_ATTRIBUTE>
```

The following example shows nested compound data types by using an INTERVAL data type that holds a pair of DATE data types, which represent a time interval. Each DATE data type is a COMPOSITE of a MONTH, DAY, and YEAR data type. The INTERVAL data type is used by the VACATION GDL attribute to express a time period that an employee might be absent. The following collection of templates would accomplish this situation.

### Month Template

```cpp
*Template:  MONTHS
{
    *Type:  DATATYPE
    *DataType:   ENUMERATOR
    *XMLDataType: "months"
    *EnumeratorList: (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec)
}
```

### Day Template

```cpp
*Template:  DAY
{
*Inherits: INTEGER
*MinValue: 1
*MaxValue: 31
}
```

### Year Template

```cpp
*Template:  YEAR
{
*Inherits: INTEGER
*MinValue: 1900
*MaxValue: 2100
}
```

### Date Template

```cpp
*Template:  DATE
{
    *Type:  DATATYPE
    *DataType:   COMPOSITE
    *ElementType: (MONTHS, DAY, YEAR)
    *RequiredDelimiter: "-"
    *ElementTags: (month, day, year)
}
```

### Interval Template

```cpp
*Template:  INTERVAL
{
    *Type:  DATATYPE
    *DataType:   ARRAY
    *ElementType:  DATE
    *RequiredDelimiter: "to"
    *OptionalDelimiter: "<20 09>"
    *ElementTags: (start_date, end_date)
    *ArraySize: 2
}
```

### Vacation Template

```cpp
*Template:  VACATION
{
    *Name:  "*VacationDates"
    *Type:  ATTRIBUTE
    *ValueType:  INTERVAL
}
```

Consider the following GDL entry.

```cpp
*VacationDates:  Dec-20-2001 to Jan-3-2002
```

If this GDL entry is interpreted by using the VACATION template, the resulting XML output will be as follows.

```cpp
    <GDL_ATTRIBUTE Name="*VacationDates"  >
        <start_date >
            <month  xsi:type="GDLW_months">Dec</month>
            <day  xsi:type="GDLW_int">20</day>
            <year  xsi:type="GDLW_int">2001</year>
        </start_date>
        <end_date >
            <month  xsi:type="GDLW_months">Jan</month>
            <day  xsi:type="GDLW_int">3</day>
            <year  xsi:type="GDLW_int">2002</year>
        </end_date>
    </GDL_ATTRIBUTE>
```

 

 




