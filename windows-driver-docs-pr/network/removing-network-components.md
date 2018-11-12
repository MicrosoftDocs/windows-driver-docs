---
title: Removing Network Components
description: Removing Network Components
ms.assetid: db1928ff-7570-411c-b770-274428a0d432
keywords:
- notify objects WDK networking , removing network components
- network notify objects WDK , removing network components
- network component removal WDK
- removing network components
- notifications WDK networking , removing network components
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Removing Network Components





Network components are removed by the network configuration subsystem.

**To remove a network component**

1.  The network configuration subsystem creates an instance of the notify object and calls the object's [**INetCfgComponentControl::Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff547729) method. This method initializes the object and provides access to the component and all aspects of network configuration.

2.  The subsystem calls the notify object's [**INetCfgComponentSetup::Removing**](https://msdn.microsoft.com/library/windows/hardware/ff547769) method to perform operations required to remove the component. The **Removing** method performs cleanup operations to prepare for the component's removal.

3.  The subsystem calls the notify object's [**INetCfgComponentControl::ApplyRegistryChanges**](https://msdn.microsoft.com/library/windows/hardware/ff547727) method to remove information about the network component from the registry.

 

 





