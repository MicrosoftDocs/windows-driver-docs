---
title: Configuring the Component's Driver
description: Configuring the Component's Driver
ms.assetid: 0aab9bb0-180c-4e21-ac8e-f20db7e8201a
keywords:
- notify objects WDK networking , driver configuration
- network notify objects WDK , driver configuration
- driver configuration WDK network component
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Configuring the Component's Driver





After the network configuration subsystem calls a notify object's [**INetCfgComponentControl::ApplyPnpChanges**](https://msdn.microsoft.com/library/windows/hardware/ff547726) method, the notify object should send configuration information to the driver of the network component that owns the notify object. The network configuration subsystem calls **ApplyPnpChanges** after it calls the [**INetCfgComponentControl::ApplyRegistryChanges**](https://msdn.microsoft.com/library/windows/hardware/ff547727) method and after drivers and services for the particular network component have started. In the **ApplyPnpChanges** call, the network configuration subsystem passes the [**INetCfgPnpReconfigCallback**](https://msdn.microsoft.com/library/windows/hardware/ff547935) interface. The component's notify object can use the **INetCfgPnpReconfigCallback** interface to send configuration information to the component's driver. This driver must be either a TDI provider or an NDIS miniport driver.

The notify object can call [**INetCfgPnpReconfigCallback::SendPnpReconfig**](https://msdn.microsoft.com/library/windows/hardware/ff547943) within its **ApplyPnpChanges** implementation to send configuration information to its component's driver. **SendPnpReconfig** passes configuration information to the driver.

Alternatively, the notify object can call the Win32 [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) function to open a connection to its component's driver. The notify object can call the Win32 [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function to send a control code along with input data directly to its component's driver.

The notify object is not required to use **INetCfgPnpReconfigCallback**. But, if the notify object uses **INetCfgPnpReconfigCallback**, a user will not be required to reboot the operating system to cause configuration changes to take effect in the driver.

 

 





