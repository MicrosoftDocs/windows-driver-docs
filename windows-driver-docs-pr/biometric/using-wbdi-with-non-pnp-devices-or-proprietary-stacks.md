---
title: Using WBDI with Non-PnP Devices or Proprietary Stacks
description: Using WBDI with Non-PnP Devices or Proprietary Stacks
ms.assetid: 0143eae4-4ca8-4b25-9a97-2cace74f8de9
keywords:
- biometric drivers WDK , legacy
- biometric drivers WDK , non-PnP devices
- biometric drivers WDK , proprietary stacks
- legacy driver stacks WDK biometric
- non-PnP devices WDK biometric
- proprietary stacks WDK biometric
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using WBDI with Non-PnP Devices or Proprietary Stacks


WBDI does not support non-PnP devices. However, non-PnP biometric devices and devices that use a non-WBDI driver stack can still interface with WBDI.

There are two primary methods to use a legacy driver stack with WBDI:

1.  Create a new sensor plug-in to manage biometric reader arrivals and departures.

2.  Install a bus filter on the existing device stack that detects biometric capabilities or events. The bus filter then creates a PDO for a WBDI driver.

Creating a filter to manage WBDI PDOs is the simpler of the two solutions, and this is the method recommended by Microsoft.

 

 





