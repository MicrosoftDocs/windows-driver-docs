---
title: Valid GDL Configurations
description: Valid GDL Configurations
ms.assetid: 68dbe7f7-4f6d-46e5-b2f1-27b123c4bedb
keywords:
- GDL WDK , configurations
- parser WDK GDL , validating configurations
- configurations WDK GDL , valid configurations
- validating GDL configurations WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




