---
title: Additive Template Directive
description: Additive Template Directive
ms.assetid: 94883a51-a3a6-492e-9597-6a2f913d40bc
keywords: ["Additive directive WDK GDL", "templates WDK GDL , order of definitions"]
---

# Additive Template Directive


The \***Additive**: directive defines the order of template definitions.

The **Additive** directive can have one of the following values:

-   MOST\_RECENT. Only the most recent definition appears.

-   LEAST\_RECENT. Only the least recent (first) definition appears.

-   MOST\_TO\_LEAST\_RECENT. All definitions appear ordered from most to least recent.

-   LEAST\_TO\_MOST\_RECENT. All definitions appear ordered from least to most recent.

If this directive is absent, a default value of MOST\_RECENT will be assumed.

If this directive is itself multiply defined within a template or appears in several templates that are related by inheritance, only the most recently defined directive in the most derived template will be honored.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Additive%20Template%20Directive%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




