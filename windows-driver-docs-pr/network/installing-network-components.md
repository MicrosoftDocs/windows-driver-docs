---
title: Installing Network Components
description: Installing Network Components
keywords:
- notify objects WDK networking , installing network components
- network notify objects WDK , installing network components
- installing network components WDK , steps
- network component installations WDK , steps
- notifications WDK networking , installing network components
ms.date: 01/07/2019
---

# Installing Network Components

Network components are installed by the network configuration subsystem.

**To install a network component**

1.  The network configuration subsystem calls the class installer for the particular component type. The class installer then calls the Setup API to retrieve information from the component's INF file and to install the component.

    If the component owns a notify object, the class installer retrieves the name of the DLL that houses the notify object. This DLL appears in the component's INF file as follows:

    ```INF
    HKR, Ndi, ComponentDll,     0,     "notifyobject.dll"
    ```

    The class installer calls the DLL's entry-point function to register the notify object. The network configuration subsystem creates an instance of the notify object and calls the object's [**INetCfgComponentControl::Initialize**](/previous-versions/windows/hardware/network/ff547729(v=vs.85)) method. This method initializes the object and provides access to the component and all aspects of network configuration.

    On older versions of Windows you can't create a driver package with a notify object that is executed from the [Driver Store](../install/driver-store.md). To successfully install a driver package in this scenario, you need to have a minimum OS build number of 25341.

2.  To perform operations required to install the component, the network configuration subsystem calls the notify object's [**INetCfgComponentSetup::Install**](/previous-versions/windows/hardware/network/ff547762(v=vs.85)) method.

    If installation of the component is unattended, the network configuration subsystem calls the notify object's [**INetCfgComponentSetup::ReadAnswerFile**](/previous-versions/windows/hardware/network/ff547765(v=vs.85)) method. This method opens and retrieves the component's parameters from a file for unattended setup that is known as an *answer file*.

3.  After the network configuration subsystem creates an instance of and initializes the notify object, the subsystem calls the notify object's [**INetCfgComponentNotifyGlobal::GetSupportedNotifications**](/previous-versions/windows/hardware/network/ff547734(v=vs.85)) method to retrieve the types of notifications required by the object. The subsystem uses this information to send required notifications to the object. The object can use these notifications to control aspects of networking setup and configuration that might affect the component that owns the object. For example, if the subsystem calls the [**INetCfgComponentNotifyGlobal::SysNotifyComponent**](/previous-versions/windows/hardware/network/ff547736(v=vs.85)) method to notify the object that the subsystem installed or removed another network component, the object has the opportunity to perform operations related to the change.

    After the network configuration subsystem creates an instance of and initializes the notify object, the subsystem also calls any of the methods of the notify object's [INetCfgComponentNotifyBinding](/previous-versions/windows/hardware/network/ff547730(v=vs.85)) interface to notify the object about changes to the way the subsystem binds other network components to the component that owns the notify object.

4.  When the network configuration subsystem is ready to apply the component's properties to the operating system, it calls the notify object's [**INetCfgComponentControl::ApplyRegistryChanges**](/previous-versions/windows/hardware/network/ff547727(v=vs.85)) method to assign the component's parameters under the component's registry key. The notify object calls its component's [**INetCfgComponent::OpenParamKey**](/previous-versions/windows/hardware/network/ff547890(v=vs.85)) method to open and retrieve the component's registry key.

5.  To configure the component's driver, the network configuration subsystem calls the notify object's [**INetCfgComponentControl::ApplyPnpChanges**](/previous-versions/windows/hardware/network/ff547726(v=vs.85)) method and passes the [**INetCfgPnpReconfigCallback**](/previous-versions/windows/hardware/network/ff547935(v=vs.85)) interface. The notify object calls the [**INetCfgPnpReconfigCallback::SendPnpReconfig**](/previous-versions/windows/hardware/network/ff547943(v=vs.85)) method to send configuration information to its component's driver.

For more information about the Setup API and on files for unattended setup, see the Microsoft Windows SDK.
