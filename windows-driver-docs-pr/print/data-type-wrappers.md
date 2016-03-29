---
title: Data Type Wrappers
description: Data Type Wrappers
ms.assetid: 8c88002b-4d0a-4e81-b50d-f765caa7cf80
keywords: ["snapshots WDK GDL , structure", "GDL WDK , enumerations", "enumerations WDK GDL", "data types WDK GDL", "GDL WDK , data types", "parser WDK GDL , data type wrappers", "snapshots WDK GDL , data type wrapers"]
---

# Data Type Wrappers


The GDL parser wraps each template-defined data type in another data type that contains the appropriate declarations for the XML attributes that might appear in the actual snapshot. This additional data type is required because the XSD schema treats undeclared XML attributes that appear within an element start tag as a schema validation error. This additional data type also eliminates the need for you to know the attributes that are used internally by the parser and insulates templates from future changes in the snapshot.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Data%20Type%20Wrappers%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




