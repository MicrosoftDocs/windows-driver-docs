---
title: Installing NDIS-WDM Miniport Drivers
description: Installing NDIS-WDM Miniport Drivers
ms.assetid: 7b87d8e3-cefa-49d7-ae66-0c3d771e24ef
keywords:
- NDIS-WDM miniport driver WDK networking , installing
- lower edge of NDIS miniport drivers WDK networking , driver installations
- WDM lower edge WDK networking , driver installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing NDIS-WDM Miniport Drivers





When you implement the installation mechanism for an NDIS-WDM miniport driver, you should keep the following items in mind:

-   Create an information (INF) file for a **Net** class of network component as described in [Creating Network INF Files](creating-network-inf-files.md).

-   Include Plug and Play (PnP) identifiers (ID) of devices as is typically done for any **Net** class of network component; however, make these IDs specific to the bus type to which the devices are attached.

 

 





