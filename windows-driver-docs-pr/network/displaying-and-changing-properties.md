---
title: Displaying and Changing Properties
description: Displaying and Changing Properties
ms.assetid: 657b687d-b0c0-46e0-a948-242509590a4b
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

A component's properties can be displayed and modified from Control Panel. When you click the **Network** icon, you start the network configuration subsystem, which creates an instance of the notify object and calls the object's [**INetCfgComponentControl::Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff547729) method. This method initializes the object and provides access to the component and all aspects of network configuration.

The application calls the component's [**INetCfgComponent::RaisePropertyUi**](https://msdn.microsoft.com/library/windows/hardware/ff547895) method to display the component's properties. The **RaisePropertyUi** method then calls the following notify object methods:

-   [**INetCfgComponentPropertyUi::QueryPropertyUi**](https://msdn.microsoft.com/library/windows/hardware/ff547749) method to determine if a specific context is appropriate to display properties for the component.

-   [**INetCfgComponentPropertyUi::SetContext**](https://msdn.microsoft.com/library/windows/hardware/ff547752) method to direct the component's notify object to display the component's properties in the specified context.

-   [**INetCfgComponentPropertyUi::MergePropPages**](https://msdn.microsoft.com/library/windows/hardware/ff547746) method to create and merge custom pages for the component's property sheet into the default set.

If the user changes one of the component's parameters on one of the custom pages, **RaisePropertyUi** calls the notify object's [**INetCfgComponentPropertyUi::ApplyProperties**](https://msdn.microsoft.com/library/windows/hardware/ff547741) method to store the change in memory.

To apply the change, the network configuration subsystem calls the notify object's [**INetCfgComponentControl::ApplyRegistryChanges**](https://msdn.microsoft.com/library/windows/hardware/ff547727) method to modify information about the network component in the registry. To configure the component's driver with the modified information, the network configuration subsystem calls the notify object's [**INetCfgComponentControl::ApplyPnpChanges**](https://msdn.microsoft.com/library/windows/hardware/ff547726) method and passes the [**INetCfgPnpReconfigCallback**](https://msdn.microsoft.com/library/windows/hardware/ff547935) interface.

 

 





