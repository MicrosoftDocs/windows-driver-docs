---
title: Standard GDL Parsing
description: Standard GDL Parsing
ms.assetid: 089bba58-e29f-428a-ab54-4413edca1d0c
keywords:
- GDL WDK , parser
- parser WDK GDL , standard parsing
- parsing GDL data WDK
- standard GDL parsing WDK
- default GDL parsing WDK
- standard parser-filter WDK GDL
- SPF WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Standard GDL Parsing


The default or standard parser-filter (SPF) takes as its input the original snapshot tree (that is, the XML snapshot that the parser generates, in which the attribute nodes contain only the raw unparsed values as CDATA elements) and performs additional semantics validation and processing.

In this processing, the SPF interprets the raw value CDATA as a data type that is specified by the template that is bound to the attribute node and adds new XML elements in the attribute node that properly represent the value as one or more standard XML data types. The result is a decorated XML snapshot tree that enables clients to access the values as XML data type elements.

The processing also includes existence checking of members, parsing of attribute values, handling of multiply defined attributes, default initialization attributes, and generation of an XML representation of the resultant tree that contains the additional elements. Warning and error messages are also generated if needed. The processing that is performed is directed by specific template directives.

 

 




