---
title: Upgrading Network Components
description: Upgrading Network Components
keywords:
- notify objects WDK networking , upgrading network components
- network notify objects WDK , upgrading network components
- network component upgrades WDK , notify objects
- upgrading network components WDK , notify objects
- notifications WDK networking , upgrading network components
- upgrading network components WDK , steps
ms.date: 04/20/2017
---

# Upgrading Network Components





Network components are upgraded by the network configuration subsystem.

**To upgrade a network component**

1.  The network configuration subsystem creates an instance of the notify object and calls the object's [**INetCfgComponentControl::Initialize**](/previous-versions/windows/hardware/network/ff547729(v=vs.85)) method. This method initializes the object and provides access to the component and all aspects of network configuration.

2.  When the operating system is installed or upgraded to a different version, the network configuration subsystem calls the notify object's [**INetCfgComponentSetup::Upgrade**](/previous-versions/windows/hardware/network/ff547783(v=vs.85)) method.

3.  The subsystem calls the notify object's [**INetCfgComponentControl::ApplyRegistryChanges**](/previous-versions/windows/hardware/network/ff547727(v=vs.85)) method to modify information about the network component in the registry and then calls the notify object's [**INetCfgComponentControl::ApplyPnpChanges**](/previous-versions/windows/hardware/network/ff547726(v=vs.85)) method and passes the [**INetCfgPnpReconfigCallback**](/previous-versions/windows/hardware/network/ff547935(v=vs.85)) interface to configure the component's driver with the upgraded information.

 

