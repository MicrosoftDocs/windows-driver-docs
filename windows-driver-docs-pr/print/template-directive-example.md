---
title: Template Directive Example
author: windows-driver-content
description: Template Directive Example
MS-HAID:
- 'gplfiles\_f46d574c-d104-4610-a99c-fdae9d362c3a.xml'
- 'print.template\_directive\_example'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ae8fe5e6-ee79-424d-80b3-fd6300257977
keywords: ["Production directive WDK GDL", "templates WDK GDL , examples"]
---

# Template Directive Example


The following example shows a simple production.

```
  *Production: EXACTLY_ONE
  {
        *Production: SATISFY_ALL
        {
            *Member: GENERIC_OPTION {*Occurs: [1-*] }
            *Member: DEFAULT_OPT {*Occurs: [0-*] }
        }
        *Production: SATISFY_ALL
        {
            *Member: GENERIC_OPTION {*Occurs: [0] }
            *Member: DEFAULT_OPT {*Occurs: [0] }
        }
  }
```

The construct instances that are bound to the host template by this production can contain any of the following combinations:

-   No instances of either DEFAULT\_OPT or GENERIC\_OPTION.

-   One or more instances of GENERIC\_OPTION and no instances of DEFAULT\_OPT.

-   One or more instances of GENERIC\_OPTION and one or more instances of DEFAULT\_OPT.

-   The construct instances cannot have one or more instances of DEFAULT\_OPT without at least one instance of GENERIC\_OPTION.

If the host template inherits from other templates, the productions that are defined in the inherited templates are also evaluated and must also be **TRUE** for the production in the host template to evaluate to **TRUE**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Template%20Directive%20Example%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


