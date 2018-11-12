---
title: Applying Component Changes to the Registry
description: Applying Component Changes to the Registry
ms.assetid: f844a693-cf26-407c-b182-b652a4c585b4
keywords:
- notify objects WDK networking , registry values
- network notify objects WDK , registry values
- registry WDK notify objects
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Applying Component Changes to the Registry





After the network configuration subsystem calls a notify object's [**INetCfgComponentControl::ApplyRegistryChanges**](https://msdn.microsoft.com/library/windows/hardware/ff547727) method, the notify object should set, modify, or delete information from the registry depending on the action previously performed by the notify object. After the notify object performs specific actions related to installing, removing, or modifying parameters of the component that owns the object, the notify object should set a data member that indicates the action performed. After the subsystem calls **ApplyRegistryChanges** to apply configuration changes to the registry, **ApplyRegistryChanges** should use this data member to determine how to make registry changes. For example:

-   If a notify object previously performed operations related to installing the component that owns the object, the notify object should have set the data member that indicates the action as "install". After the subsystem calls **ApplyRegistryChanges** to apply configuration changes to the registry, **ApplyRegistryChanges** should set information about the component in the registry.

-   If a notify object previously performed operations related to removing the component that owns the object, the notify object should have set the data member that indicates the action as "remove". After the subsystem calls **ApplyRegistryChanges** to apply configuration changes to the registry, **ApplyRegistryChanges** should remove information about the component from the registry.

-   If a user displays one of a component's custom property pages and modifies one of the component's parameters, the component's notify object should have set the data member that indicates the action as "modify parameter". After the subsystem calls **ApplyRegistryChanges** to apply configuration changes to the registry, **ApplyRegistryChanges** should change information about the component's parameter in the registry.

To open and retrieve a component's registry key to modify information about the component, the **ApplyRegistryChanges** method should be implemented to call the component's [**INetCfgComponent::OpenParamKey**](https://msdn.microsoft.com/library/windows/hardware/ff547890) method. To set values in the registry under the component's registry key, implement **ApplyRegistryChanges** to write registry data using Win32 functions. For example, **ApplyRegistryChanges** can call the **RegCreateKeyEx** function to create a subkey to hold values, and the **RegSetValueEx** function to create and set those values.

For more information about the registry, writing data to it, and retrieving data from it, see the Microsoft Windows SDK.

 

 





