---
title: Displaying and Changing Properties
description: Displaying and Changing Properties
keywords:
- notify objects WDK networking , property pages
- network notify objects WDK , property pages
- property pages WDK networking
- properties WDK networking
- displaying network configuration properties
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Displaying and Changing Properties





The network configuration subsystem displays Property pages for a network component and changes the component's parameters.

A component's properties can be displayed and modified from Control Panel. When you click the **Network** icon, you start the network configuration subsystem, which creates an instance of the notify object and calls the object's [**INetCfgComponentControl::Initialize**](/previous-versions/windows/hardware/network/ff547729(v=vs.85)) method. This method initializes the object and provides access to the component and all aspects of network configuration.

The application calls the component's [**INetCfgComponent::RaisePropertyUi**](/previous-versions/windows/hardware/network/ff547895(v=vs.85)) method to display the component's properties. The **RaisePropertyUi** method then calls the following notify object methods:

-   [**INetCfgComponentPropertyUi::QueryPropertyUi**](/previous-versions/windows/hardware/network/ff547749(v=vs.85)) method to determine if a specific context is appropriate to display properties for the component.

-   [**INetCfgComponentPropertyUi::SetContext**](/previous-versions/windows/hardware/network/ff547752(v=vs.85)) method to direct the component's notify object to display the component's properties in the specified context.

-   [**INetCfgComponentPropertyUi::MergePropPages**](/previous-versions/windows/hardware/network/ff547746(v=vs.85)) method to create and merge custom pages for the component's property sheet into the default set.

If the user changes one of the component's parameters on one of the custom pages, **RaisePropertyUi** calls the notify object's [**INetCfgComponentPropertyUi::ApplyProperties**](/previous-versions/windows/hardware/network/ff547741(v=vs.85)) method to store the change in memory.

To apply the change, the network configuration subsystem calls the notify object's [**INetCfgComponentControl::ApplyRegistryChanges**](/previous-versions/windows/hardware/network/ff547727(v=vs.85)) method to modify information about the network component in the registry. To configure the component's driver with the modified information, the network configuration subsystem calls the notify object's [**INetCfgComponentControl::ApplyPnpChanges**](/previous-versions/windows/hardware/network/ff547726(v=vs.85)) method and passes the [**INetCfgPnpReconfigCallback**](/previous-versions/windows/hardware/network/ff547935(v=vs.85)) interface.

 

