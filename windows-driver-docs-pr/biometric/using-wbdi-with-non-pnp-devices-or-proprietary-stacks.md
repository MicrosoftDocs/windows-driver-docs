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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using WBDI with Non-PnP Devices or Proprietary Stacks


WBDI does not support non-PnP devices. However, non-PnP biometric devices and devices that use a non-WBDI driver stack can still interface with WBDI.

There are two primary methods to use a legacy driver stack with WBDI:

1.  Create a new sensor plug-in to manage biometric reader arrivals and departures.

2.  Install a bus filter on the existing device stack that detects biometric capabilities or events. The bus filter then creates a PDO for a WBDI driver.

Creating a filter to manage WBDI PDOs is the simpler of the two solutions, and this is the method recommended by Microsoft.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[biometric\biometric]:%20Using%20WBDI%20with%20Non-PnP%20Devices%20or%20Proprietary%20Stacks%20%20RELEASE:%20%288/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




