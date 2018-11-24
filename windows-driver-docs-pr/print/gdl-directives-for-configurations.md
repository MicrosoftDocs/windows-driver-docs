---
title: GDL Directives for Configurations
description: GDL Directives for Configurations
ms.assetid: c7b3c364-06b2-4de8-9fe6-2c77d313a2f8
keywords:
- directives WDK GDL , configuration directives
- source files WDK GDL , configuration directives
- configuration directives WDK GDL
- parser WDK GDL , directives
- Feature directive WDK GDL
- Option directive WDK GDL
- Switch/Case directive WDK GDL
- Default directive WDK GDL
- DefaultOption directive WDK GDL
- Constraints directive WDK GDL
- InvalidCombinations directive WDK GDL
- configurations WDK GDL , directives
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




