---
title: Configuring the Component's Driver
description: Configuring the Component's Driver
keywords:
- notify objects WDK networking , driver configuration
- network notify objects WDK , driver configuration
- driver configuration WDK network component
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Configuring the Component's Driver





After the network configuration subsystem calls a notify object's [**INetCfgComponentControl::ApplyPnpChanges**](/previous-versions/windows/hardware/network/ff547726(v=vs.85)) method, the notify object should send configuration information to the driver of the network component that owns the notify object. The network configuration subsystem calls **ApplyPnpChanges** after it calls the [**INetCfgComponentControl::ApplyRegistryChanges**](/previous-versions/windows/hardware/network/ff547727(v=vs.85)) method and after drivers and services for the particular network component have started. In the **ApplyPnpChanges** call, the network configuration subsystem passes the [**INetCfgPnpReconfigCallback**](/previous-versions/windows/hardware/network/ff547935(v=vs.85)) interface. The component's notify object can use the **INetCfgPnpReconfigCallback** interface to send configuration information to the component's driver. This driver must be either a TDI provider or an NDIS miniport driver.

The notify object can call [**INetCfgPnpReconfigCallback::SendPnpReconfig**](/previous-versions/windows/hardware/network/ff547943(v=vs.85)) within its **ApplyPnpChanges** implementation to send configuration information to its component's driver. **SendPnpReconfig** passes configuration information to the driver.

Alternatively, the notify object can call the Win32 [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) function to open a connection to its component's driver. The notify object can call the Win32 [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) function to send a control code along with input data directly to its component's driver.

The notify object is not required to use **INetCfgPnpReconfigCallback**. But, if the notify object uses **INetCfgPnpReconfigCallback**, a user will not be required to reboot the operating system to cause configuration changes to take effect in the driver.

 

