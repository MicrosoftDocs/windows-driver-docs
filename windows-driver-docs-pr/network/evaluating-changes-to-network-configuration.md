---
title: Evaluating Changes to Network Configuration
description: Evaluating Changes to Network Configuration
keywords:
- notify objects WDK networking , change processing
- network notify objects WDK , change processing
- changes to network configuration WDK
ms.date: 04/20/2017
---

# Evaluating Changes to Network Configuration





After the network configuration subsystem calls the methods of a notify object's [**INetCfgComponentNotifyGlobal**](/previous-versions/windows/hardware/network/ff547733(v=vs.85)) and [INetCfgComponentNotifyBinding](/previous-versions/windows/hardware/network/ff547730(v=vs.85)) interfaces, the notify object should evaluate the proposed change in network configuration that the subsystem sends and should perform operations related to the change. The methods of a notify object's **INetCfgComponentNotifyGlobal** and **INetCfgComponentNotifyBinding** interfaces should be implemented to process only the changes that affect the component that owns the object.

The following topics describe examples of how a notify object processes changes to network configuration:

[Adding a Component](adding-a-component.md)

[Changing Bindings for a Component](changing-bindings-for-a-component.md)

 

