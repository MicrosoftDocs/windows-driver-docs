---
title: Installing, Upgrading, and Removing the Component
description: Installing, Upgrading, and Removing the Component
ms.assetid: 7069e7a0-0c7e-4f7c-a764-a83e758df1bf
keywords:
- notify objects WDK networking , removing network components
- network notify objects WDK , removing network components
- notify objects WDK networking , upgrading network components
- network notify objects WDK , upgrading network components
- notify objects WDK networking , installing network components
- network notify objects WDK , installing network components
- removing network components
- upgrading network components WDK , notify objects
- installing network components WDK , notify objects
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing, Upgrading, and Removing the Component





When the network configuration subsystem installs, upgrades, or removes a network component, the subsystem also calls the component's notify object to complete the installation, upgrade, and removal. The component's notify object can be implemented to perform operations that the component might require. For example:

-   A notify object for a multiplexer for a virtual LAN can be implemented so that when the subsystem installs the multiplexer, the notify object will install virtual adapters that the multiplexer protocol binds to.

    To install a virtual adapter, the notify object calls the network configuration's [**INetCfgClassSetup::Install**](https://msdn.microsoft.com/library/windows/hardware/ff547711) method. In this call, the notify object passes the identifier of the virtual adapter to install. The notify object can call **INetCfgClassSetup::Install**, for example, from its [**INetCfgComponentNotifyBinding::NotifyBindingPath**](https://msdn.microsoft.com/library/windows/hardware/ff547731) or [**INetCfgComponentPropertyUi::ApplyProperties**](https://msdn.microsoft.com/library/windows/hardware/ff547741) method.

    To complete the installation of the virtual adapter, the operating system requires the INF file for the virtual adapter. To ensure that this INF file can be located, it must be copied to the operating system when the multipexer is installed. For more information, see [Copying INFs](https://msdn.microsoft.com/library/windows/hardware/ff540117). This topic indicates that the **CopyINF** directive or a call to the **SetupCopyOEMInf** function by a co-installer or setup application can be used to copy INF files to the target system's INF directory. However, if the INF file for the multiplexer (original INF) is copied using **SetupCopyOEMInf**, then the INF file for the virtual adapter must also be copied using **SetupCopyOEMInf** because the operating system only handles a **CopyINF** directive if the original INF is not yet in the INF directory.

-   The multiplexer's notify object can be implemented so that when the subsystem removes the multiplexer, the notify object will remove all virtual adapters. To remove a virtual adapter, the notify object calls the network configuration's [**INetCfgClassSetup::DeInstall**](https://msdn.microsoft.com/library/windows/hardware/ff547710) method. In this call, the notify object passes the pointer to the **INetCfgComponent** interface of the virtual adapter. The notify object can call **INetCfgClassSetup::DeInstall**, for example, from its **INetCfgComponentNotifyBinding::NotifyBindingPath** or **INetCfgComponentPropertyUi::ApplyProperties** method.

-   The component's notify object can be implemented so that when the subsystem upgrades the component, the notify object will change the order of the component's binding path. To change this order, a notify object's [**INetCfgComponentSetup::Upgrade**](https://msdn.microsoft.com/library/windows/hardware/ff547783) method calls either the [**INetCfgComponentBindings::MoveBefore**](https://msdn.microsoft.com/library/windows/hardware/ff547722) or the [**INetCfgComponentBindings::MoveAfter**](https://msdn.microsoft.com/library/windows/hardware/ff547721) methods.

 

 





