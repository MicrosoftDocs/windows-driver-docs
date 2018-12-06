---
title: Installing Network Components
description: Installing Network Components
ms.assetid: b4e5d73a-4943-498d-bf59-a08e3732baa8
keywords:
- notify objects WDK networking , installing network components
- network notify objects WDK , installing network components
- installing network components WDK , steps
- network component installations WDK , steps
- notifications WDK networking , installing network components
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing Network Components





Network components are installed by the network configuration subsystem.

**To install a network component**

1.  The network configuration subsystem calls the class installer for the particular component type. The class installer then calls the Setup API to retrieve information from the component's INF file and to install the component.

    If the component owns a notify object, the class installer retrieves the name of the DLL that houses the notify object. This DLL appears in the component's INF file as follows:

    ```cpp
    HKR, Ndi, ComponentDll,     0,     "notifyobject.dll"
    ```

    The class installer calls the DLL's entry-point function to register the notify object. The network configuration subsystem creates an instance of the notify object and calls the object's [**INetCfgComponentControl::Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff547729) method. This method initializes the object and provides access to the component and all aspects of network configuration.

2.  <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code></code></pre></td>
    </tr>
    </tbody>
    </table>

3.  To perform operations required to install the component, the network configuration subsystem calls the notify object's [**INetCfgComponentSetup::Install**](https://msdn.microsoft.com/library/windows/hardware/ff547762) method.

    If installation of the component is unattended, the network configuration subsystem calls the notify object's [**INetCfgComponentSetup::ReadAnswerFile**](https://msdn.microsoft.com/library/windows/hardware/ff547765) method. This method opens and retrieves the component's parameters from a file for unattended setup that is known as an *answer file*.

4.  After the network configuration subsystem creates an instance of and initializes the notify object, the subsystem calls the notify object's [**INetCfgComponentNotifyGlobal::GetSupportedNotifications**](https://msdn.microsoft.com/library/windows/hardware/ff547734) method to retrieve the types of notifications required by the object. The subsystem uses this information to send required notifications to the object. The object can use these notifications to control aspects of networking setup and configuration that might affect the component that owns the object. For example, if the subsystem calls the [**INetCfgComponentNotifyGlobal::SysNotifyComponent**](https://msdn.microsoft.com/library/windows/hardware/ff547736) method to notify the object that the subsystem installed or removed another network component, the object has the opportunity to perform operations related to the change.

    After the network configuration subsystem creates an instance of and initializes the notify object, the subsystem also calls any of the methods of the notify object's [INetCfgComponentNotifyBinding](https://msdn.microsoft.com/library/windows/hardware/ff547730) interface to notify the object about changes to the way the subsystem binds other network components to the component that owns the notify object.

5.  When the network configuration subsystem is ready to apply the component's properties to the operating system, it calls the notify object's [**INetCfgComponentControl::ApplyRegistryChanges**](https://msdn.microsoft.com/library/windows/hardware/ff547727) method to assign the component's parameters under the component's registry key. The notify object calls its component's [**INetCfgComponent::OpenParamKey**](https://msdn.microsoft.com/library/windows/hardware/ff547890) method to open and retrieve the component's registry key.

6.  To configure the component's driver, the network configuration subsystem calls the notify object's [**INetCfgComponentControl::ApplyPnpChanges**](https://msdn.microsoft.com/library/windows/hardware/ff547726) method and passes the [**INetCfgPnpReconfigCallback**](https://msdn.microsoft.com/library/windows/hardware/ff547935) interface. The notify object calls the [**INetCfgPnpReconfigCallback::SendPnpReconfig**](https://msdn.microsoft.com/library/windows/hardware/ff547943) method to send configuration information to its component's driver.

```cpp

```

For more information about the Setup API and on files for unattended setup, see the Microsoft Windows SDK.

 

 





