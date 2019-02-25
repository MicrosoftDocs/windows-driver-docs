---
title: Configuring the Network
description: Configuring the Network
ms.assetid: 9529467b-353d-41c3-9d4e-bb5df5c43665
keywords:
- notify objects WDK networking , network configuration
- network notify objects WDK , network configuration
- notifications WDK networking , network configuration
- network configuration WDK notify ofbject
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Configuring the Network





A notify object can provide the network component that owns it with programmatic control over network configuration.

A network component's properties can be configured from the Network Control Panel application. When you click the **Network** icon, you start the network configuration subsystem, which creates an instance of the notify object and calls the object's [**INetCfgComponentControl::Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff547729) method. This method initializes the object and provides access to the component and all aspects of network configuration.

After the network configuration subsystem creates an instance of and initializes the notify object, the subsystem calls the notify object's [**INetCfgComponentNotifyGlobal::GetSupportedNotifications**](https://msdn.microsoft.com/library/windows/hardware/ff547734) method to retrieve the types of notifications required by the object. Using this information, the subsystem can send required notifications to the object. The object can use these notifications to control aspects of networking setup and configuration that might affect the component that owns the object. For example, if the subsystem calls the notify object's [**INetCfgComponentNotifyGlobal::SysQueryBindingPath**](https://msdn.microsoft.com/library/windows/hardware/ff547737) method to notify the object that the subsystem is about to add a binding path to which other network components belong, the object has the opportunity to request that the subsystem disable that binding path. In addition, the subsystem calls any of the methods of the notify object's [INetCfgComponentNotifyBinding](https://msdn.microsoft.com/library/windows/hardware/ff547730) interface. These methods notify the object about changes to the way the subsystem binds other network components to the component that owns the notify object.

 

 





