---
title: WIA Properties
description: WIA Properties
ms.date: 05/29/2020
ms.localizationpriority: medium
---

# WIA Properties

This section contains all of the WIA properties and their attributes.

The reference topics for these properties list the following attributes: property type, valid values, and access rights.

## Property Types

The following types are used in WIA to indicate the data type of a property:

**VT\_BSTR**

A string of Unicode characters (a wide character string).

**VT\_I4**

A 4-byte integer.

**VT\_R4**

A 4-byte real number (a C **float**).

**VT\_UI2**

A 2-byte unsigned integer.

**VT\_VECTOR**

An array of elements of a particular type. If another property type is combined with VT\_VECTOR by using the OR operator, the resulting value is a counted array that consists of a DWORD count of elements, followed by a pointer to the first of the elements in the array. For example, VT\_UI2 | VT\_VECTOR has a DWORD element count, followed by a pointer to an array of 2-byte unsigned integer elements.

## Valid Values

The following types indicate whether a property exists as a single value, a range of values, a list of values, or a flag:

**WIA\_PROP\_NONE**

The property contains a single value.

**WIA\_PROP\_RANGE**

The property contains a range of values, including a minimum value, a maximum value, a nominal value, and an increment.

**WIA\_PROP\_LIST**

The property contains a list of values.

**WIA\_PROP\_FLAG**

The property contains a flag.

## Access Rights

The following list describes the possible access rights for a property:

**Read-only**

The driver has read-only access.

**Read/write** 

The driver has both read and write access.

## Remarks

The preceding lists describe only those types that are used in the WIA properties that this section includes. 

For more information about these and other property types, see [**WIA\_PROPERTY\_INFO**](/windows-hardware/drivers/ddi/wiamindr_lh/ns-wiamindr_lh-_wia_property_info).

The Windows SDK contain information about the [WIA\_RAW\_HEADER](/windows/win32/wia/-wia-wia-raw-header) structure.

It also contains information about the WIA\_EVENT\_XXX and WIA\_CMD\_XXX constants, discussed in the [WIA Event Identifiers](/windows/win32/wia/-wia-wia-event-identifiers) topic.
