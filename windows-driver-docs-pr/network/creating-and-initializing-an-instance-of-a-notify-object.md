---
title: Creating and Initializing an Instance of a Notify Object
description: Creating and Initializing an Instance of a Notify Object
keywords:
- notify objects WDK networking , instances of
- network notify objects WDK , instances of
- instance of notify objects WDK networking
- initializing notify object instance
ms.date: 04/20/2017
---

# Creating and Initializing an Instance of a Notify Object





The network configuration subsystem must create an instance of the notify object and initialize the object before the subsystem can inform a notify object about changes to network configuration and display custom property pages for the component that owns the object.

The subsystem creates an instance of the notify object from the DLL's class factory. The class factory then calls the constructor for the notify class.

The class constructor should first assign initial values to class data members. Values that the constructor should initially assign include the following:

-   The constructor should set the interface pointer to an instance of a network component, [**INetCfgComponent**](/previous-versions/windows/hardware/network/ff547715(v=vs.85)), to a **NULL** value.

-   The constructor should set the interface pointer to an instance of the network configuration object, [**INetCfg**](/previous-versions/windows/hardware/network/ff547694(v=vs.85)), to a **NULL** value.

-   The constructor should set the variable that specifies the action that the notify object previously performed to a constant that identifies an unknown action. For more information about this variable, see [Defining a Notify Class](defining-a-notify-class.md).

After the network configuration subsystem creates an instance of the notify object, the subsystem calls the object's [**INetCfgComponentControl::Initialize**](/previous-versions/windows/hardware/network/ff547729(v=vs.85)) method to initialize the object instance. In this call, the subsystem passes an **INetCfgComponent** interface pointer. This **INetCfgComponent** provides the notify object with an instance of the object's component that the object can use to access and control the component. In this call, the subsystem also passes an **INetCfg** interface pointer to provide the notify object with an instance of the network configuration object that the notify object uses to access all aspects of network configuration.

The **Initialize** method should assign the **INetCfgComponent** and **INetCfg** interface pointers provided by the network configuration subsystem to data members of the notify class. **Initialize** should then call:

-   the **INetCfg::AddRef** method to increment the reference count of the network configuration object

-   the **INetCfgComponent::AddRef** method to increment the reference count of the component that owns the notify object

No other notify object interface methods are called until **Initialize** returns.

 

