---
title: Standard GDL Parsing
author: windows-driver-content
description: Standard GDL Parsing
MS-HAID:
- 'gplfiles\_cc98649a-be41-4fb6-be40-3f5eeb56b3c7.xml'
- 'print.standard\_gdl\_parsing'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 089bba58-e29f-428a-ab54-4413edca1d0c
keywords: ["GDL WDK , parser", "parser WDK GDL , standard parsing", "parsing GDL data WDK", "standard GDL parsing WDK", "default GDL parsing WDK", "standard parser-filter WDK GDL", "SPF WDK GDL"]
---

# Standard GDL Parsing


The default or standard parser-filter (SPF) takes as its input the original snapshot tree (that is, the XML snapshot that the parser generates, in which the attribute nodes contain only the raw unparsed values as CDATA elements) and performs additional semantics validation and processing.

In this processing, the SPF interprets the raw value CDATA as a data type that is specified by the template that is bound to the attribute node and adds new XML elements in the attribute node that properly represent the value as one or more standard XML data types. The result is a decorated XML snapshot tree that enables clients to access the values as XML data type elements.

The processing also includes existence checking of members, parsing of attribute values, handling of multiply defined attributes, default initialization attributes, and generation of an XML representation of the resultant tree that contains the additional elements. Warning and error messages are also generated if needed. The processing that is performed is directed by specific template directives.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Standard%20GDL%20Parsing%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


