---
title: WIA Properties
description: WIA Properties
ms.assetid: 3b9d4d90-775b-450e-b5d1-646ea45253d7
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA Properties


## <span id="ddk_wia_properties_si"></span><span id="DDK_WIA_PROPERTIES_SI"></span>


This section contains all of the WIA properties and their attributes.

The reference topics for these properties list the following attributes: property type, valid values, and access rights.

### <span id="property_types"></span><span id="PROPERTY_TYPES"></span>Property Types

The following types are used in WIA to indicate the data type of a property:

<span id="VT_BSTR"></span><span id="vt_bstr"></span>VT\_BSTR  
A string of Unicode characters (a wide character string).

<span id="VT_I4"></span><span id="vt_i4"></span>VT\_I4  
A 4-byte integer.

<span id="VT_R4"></span><span id="vt_r4"></span>VT\_R4  
A 4-byte real number (a C **float**).

<span id="VT_UI2"></span><span id="vt_ui2"></span>VT\_UI2  
A 2-byte unsigned integer.

<span id="VT_VECTOR"></span><span id="vt_vector"></span>VT\_VECTOR  
An array of elements of a particular type. If another property type is combined with VT\_VECTOR by using the OR operator, the resulting value is a counted array that consists of a DWORD count of elements, followed by a pointer to the first of the elements in the array. For example, VT\_UI2 | VT\_VECTOR has a DWORD element count, followed by a pointer to an array of 2-byte unsigned integer elements.

### <span id="valid_values"></span><span id="VALID_VALUES"></span>Valid Values

The following types indicate whether a property exists as a single value, a range of values, a list of values, or a flag:

<span id="WIA_PROP_NONE"></span><span id="wia_prop_none"></span>WIA\_PROP\_NONE  
The property contains a single value.

<span id="WIA_PROP_RANGE"></span><span id="wia_prop_range"></span>WIA\_PROP\_RANGE  
The property contains a range of values, including a minimum value, a maximum value, a nominal value, and an increment.

<span id="WIA_PROP_LIST"></span><span id="wia_prop_list"></span>WIA\_PROP\_LIST  
The property contains a list of values.

<span id="WIA_PROP_FLAG"></span><span id="wia_prop_flag"></span>WIA\_PROP\_FLAG  
The property contains a flag.

### <span id="access_rights"></span><span id="ACCESS_RIGHTS"></span>Access Rights

The following list describes the possible access rights for a property:

<span id="Read-only"></span><span id="read-only"></span><span id="READ-ONLY"></span>Read-only  
The driver has read-only access.

<span id="Read_write"></span><span id="read_write"></span><span id="READ_WRITE"></span>Read/write  
The driver has both read and write access.

The preceding lists describe only those types that are used in the WIA properties that this section includes. For more information about these and other property types, see [**WIA\_PROPERTY\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff552751).

The Windows SDK contain information about the [WIA\_RAW\_HEADER](http://go.microsoft.com/fwlink/p/?linkid=153316) structure. It also contains information about the WIA\_EVENT\_XXX and WIA\_CMD\_XXX constants, discussed in the [WIA Event Identifiers](http://go.microsoft.com/fwlink/p/?linkid=153318) topic.

 

 





