---
title: Valid GDL Configurations
author: windows-driver-content
description: Valid GDL Configurations
MS-HAID:
- 'gplfiles\_0e19717b-da9f-4a93-805a-e9c1f12e1455.xml'
- 'print.valid\_gdl\_configurations'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 68dbe7f7-4f6d-46e5-b2f1-27b123c4bedb
keywords: ["GDL WDK , configurations", "parser WDK GDL , validating configurations", "configurations WDK GDL , valid configurations", "validating GDL configurations WDK"]
---

# Valid GDL Configurations


The GDL parser interface functions will always validate the incoming configuration because the parser assumes that the client might sometimes make a mistake and provide it with an invalid configuration. For more information about invalid configurations, see [Using Invalid GDL Configurations](using-invalid-gdl-configurations.md).

A valid configuration satisfies the following conditions:

-   The configuration contains an entry for each parameter that is defined in the GDL.

-   The configuration does not contain entries for parameters that are not defined in the GDL.

-   Each value that is assigned to a parameter is defined by an \*Option construct for that parameter.

-   PICKONE parameters have one and only one value assigned.

-   PICKMANY parameters have at least one value assigned.

To prevent loss of the intent of your configuration because of the parser's validation process, you should pass a valid configuration to the parser functions.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Valid%20GDL%20Configurations%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


