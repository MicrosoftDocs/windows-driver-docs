---
title: Removing Network Components
description: Removing Network Components
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

1.  The network configuration subsystem creates an instance of the notify object and calls the object's [**INetCfgComponentControl::Initialize**](/previous-versions/windows/hardware/network/ff547729(v=vs.85)) method. This method initializes the object and provides access to the component and all aspects of network configuration.

2.  The subsystem calls the notify object's [**INetCfgComponentSetup::Removing**](/previous-versions/windows/hardware/network/ff547769(v=vs.85)) method to perform operations required to remove the component. The **Removing** method performs cleanup operations to prepare for the component's removal.

3.  The subsystem calls the notify object's [**INetCfgComponentControl::ApplyRegistryChanges**](/previous-versions/windows/hardware/network/ff547727(v=vs.85)) method to remove information about the network component from the registry.

 

