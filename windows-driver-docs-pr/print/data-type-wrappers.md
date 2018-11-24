---
title: Data Type Wrappers
description: Data Type Wrappers
ms.assetid: 8c88002b-4d0a-4e81-b50d-f765caa7cf80
keywords:
- snapshots WDK GDL , structure
- GDL WDK , enumerations
- enumerations WDK GDL
- data types WDK GDL
- GDL WDK , data types
- parser WDK GDL , data type wrappers
- snapshots WDK GDL , data type wrapers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Data Type Wrappers


The GDL parser wraps each template-defined data type in another data type that contains the appropriate declarations for the XML attributes that might appear in the actual snapshot. This additional data type is required because the XSD schema treats undeclared XML attributes that appear within an element start tag as a schema validation error. This additional data type also eliminates the need for you to know the attributes that are used internally by the parser and insulates templates from future changes in the snapshot.

 

 




