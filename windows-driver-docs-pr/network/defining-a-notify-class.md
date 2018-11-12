---
title: Defining a Notify Class
description: Defining a Notify Class
ms.assetid: e21cf020-0bf8-4091-aac4-6324a680194a
keywords:
- notify objects WDK networking , notify classes
- network notify objects WDK , notify classes
- notify classes WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Defining a Notify Class





Notify classes must be implemented so that they inherit from the [**INetCfgComponentControl**](https://msdn.microsoft.com/library/windows/hardware/ff547725) interface. However, if notify objects perform certain operations their notify classes must also be implemented to inherit from the following interfaces:

-   If a notify object performs operations related to installing, upgrading, and removing the component that owns the object, the associated notify class must inherit from the [**INetCfgComponentSetup**](https://msdn.microsoft.com/library/windows/hardware/ff547758) interface.

-   If a notify object displays custom property pages for the component that owns the object, the associated notify class must inherit from the [**INetCfgComponentPropertyUi**](https://msdn.microsoft.com/library/windows/hardware/ff547738) interface.

-   If a notify object evaluates changes to the way the network configuration subsystem binds the component that owns the object to other network components, the associated notify class must inherit from the [INetCfgComponentNotifyBinding](https://msdn.microsoft.com/library/windows/hardware/ff547730) interface.

-   If a notify object evaluates changes to network configuration that might affect the component that owns the object, the associated notify class must inherit from the [**INetCfgComponentNotifyGlobal**](https://msdn.microsoft.com/library/windows/hardware/ff547733) interface.

Certain data members within notify classes should be defined as common to all notify objects. Certain data members should be defined as specific to their component. Data members that all notify objects should define include:

-   A pointer to an instance of the network component that owns the object of type [**INetCfgComponent**](https://msdn.microsoft.com/library/windows/hardware/ff547715) interface. An instance of a notify object uses this pointer to access and control the component that owns the object.

-   A pointer to an instance of the network configuration object of type [**INetCfg**](https://msdn.microsoft.com/library/windows/hardware/ff547694) interface. An instance of a notify object uses this pointer to access all aspects of network configuration.

-   Variables to store parameter information for the component that owns the notify object

-   A variable that specifies the action that a notify object previously performed. Define constants to indicate the different actions that notify objects might perform. When the network configuration subsystem calls the notify object's [**INetCfgComponentControl::ApplyRegistryChanges**](https://msdn.microsoft.com/library/windows/hardware/ff547727) method to apply configuration changes to the registry, **ApplyRegistryChanges** uses this variable to determine how to make registry changes. For example, if a notify object previously performed operations relating to installing the component that owns the object in its [**INetCfgComponentSetup::Install**](https://msdn.microsoft.com/library/windows/hardware/ff547762) method, **Install** should set this variable to indicate the action as install.

-   A registry key of type **HKEY**. A notify object calls the [**INetCfgComponent::OpenParamKey**](https://msdn.microsoft.com/library/windows/hardware/ff547890) method of the component that owns the object to open and retrieve the registry key that contains parameters for the component. The notify object then sets the **HKEY** member to that key.

Define a constructor and a destructor for your notify class. Also consider defining private methods that only the notify class can use.

All the **IUnknown** interface methods should be implemented for a notify class. If a notify class inherits from any of the optional interfaces noted in the preceding list, all the methods of those interfaces must be implemented. Note that E\_NOTIMPL is not a valid return type for any of the methods of the notify object interfaces. If a notify object does not require an implementation for a particular method, simply implement the method to return S\_OK.

 

 





