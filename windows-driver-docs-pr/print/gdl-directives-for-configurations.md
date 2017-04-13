---
title: GDL Directives for Configurations
author: windows-driver-content
description: GDL Directives for Configurations
ms.assetid: c7b3c364-06b2-4de8-9fe6-2c77d313a2f8
keywords: ["directives WDK GDL , configuration directives", "source files WDK GDL , configuration directives", "configuration directives WDK GDL", "parser WDK GDL , directives", "Feature directive WDK GDL", "Option directive WDK GDL", "Switch/Case directive WDK GDL", "Default directive WDK GDL", "DefaultOption directive WDK GDL", "Constraints directive WDK GDL", "InvalidCombinations directive WDK GDL", "configurations WDK GDL , directives"]
---

# GDL Directives for Configurations


GDL has directives that define and work with configurations.

GDL contains the following configuration directives:

-   **\*Feature** defines a configuration parameter that relates to features.

-   **\*Option** defines a set of allowed states that can be assigned to each configuration parameter. These allowed states are known as *options*.

-   **\*Switch**, **\*Case**, and **Default** establish a dependency on a specified configuration parameter.

-   **\*DefaultOption** constructs a default configuration.

-   **\*Constraints** and **\*InvalidCombinations** specify invalid configurations. If these directives are encountered, the GDL parser will attempt to modify them to create a valid (or unconstrained) configuration.

For more information about configuration directives, see [GDL Configurations](gdl-configurations.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Directives%20for%20Configurations%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


