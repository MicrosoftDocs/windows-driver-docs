---
title: Upgrading Network Components
description: Upgrading Network Components
ms.assetid: c183cd0a-53a7-4172-9cf8-70a93877c8a8
keywords:
- notify objects WDK networking , upgrading network components
- network notify objects WDK , upgrading network components
- network component upgrades WDK , notify objects
- upgrading network components WDK , notify objects
- notifications WDK networking , upgrading network components
- upgrading network components WDK , steps
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Upgrading Network Components





Network components are upgraded by the network configuration subsystem.

**To upgrade a network component**

1.  The network configuration subsystem creates an instance of the notify object and calls the object's [**INetCfgComponentControl::Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff547729) method. This method initializes the object and provides access to the component and all aspects of network configuration.

2.  When the operating system is installed or upgraded to a different version, the network configuration subsystem calls the notify object's [**INetCfgComponentSetup::Upgrade**](https://msdn.microsoft.com/library/windows/hardware/ff547783) method.

3.  The subsystem calls the notify object's [**INetCfgComponentControl::ApplyRegistryChanges**](https://msdn.microsoft.com/library/windows/hardware/ff547727) method to modify information about the network component in the registry and then calls the notify object's [**INetCfgComponentControl::ApplyPnpChanges**](https://msdn.microsoft.com/library/windows/hardware/ff547726) method and passes the [**INetCfgPnpReconfigCallback**](https://msdn.microsoft.com/library/windows/hardware/ff547935) interface to configure the component's driver with the upgraded information.

 

 





