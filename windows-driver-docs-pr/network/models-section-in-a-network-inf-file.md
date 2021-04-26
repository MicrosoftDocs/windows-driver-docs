---
title: Models Section in a Network INF File
description: Models Section in a Network INF File
keywords:
- INF files WDK network , Models section
- network INF files WDK , Models section
- Models section WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Models Section in a Network INF File





The **Models** section in a network INF file is based on the generic [**INF Models section**](../install/inf-models-section.md).

The **Models** section in an INF file contains an entry of the following format for each type of component installed by the INF file:

\[*device-description*= *install-section.name*, *hw-id*\[, *compatible-id*...\]

For a detailed description of this entry, see [Creating an INF File](../install/overview-of-inf-files.md).

The *hw-id* (also known as the device, hardware, or component ID) for a network adapter must match the hardware ID supplied by the adapter to the PnP manager.

The *hw-id* for a network software component should consist of a provider name, followed by an underscore, and a manufacturer name or the product name, for example:

-   MS\_DLC

-   MS\_IBMDLC

A *provider name* identifies the provider of the INF file. A *manufacturer name* identifies the manufacturer of the software component. The *product name* identifies the software component.

 

