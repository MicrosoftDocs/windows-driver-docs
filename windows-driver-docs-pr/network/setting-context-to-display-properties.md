---
title: Setting Context to Display Properties
description: Setting Context to Display Properties
ms.assetid: 9a5835b2-19a2-47fb-aa5b-87c3a9b955de
keywords:
- notify objects WDK networking , context
- network notify objects WDK , context
- context WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting Context to Display Properties





A notify object can set the context in which to display properties for the network component that owns the object. The notify object sets the display context after the network configuration subsystem calls the object's [**INetCfgComponentPropertyUi::SetContext**](https://msdn.microsoft.com/library/windows/hardware/ff547752) method but before the subsystem calls the object's [**INetCfgComponentPropertyUi::MergePropPages**](https://msdn.microsoft.com/library/windows/hardware/ff547746) method.

When the network configuration subsystem calls **SetContext**, it passes an **IUnknown** interface. **SetContext** calls the **QueryInterface** method on this **IUnknown** interface to determine the interface of the specific object that the subsystem supplied.

For example, the network configuration subsystem can supply the [**INetLanConnectionUiInfo**](https://msdn.microsoft.com/library/windows/hardware/ff548005) interface when it calls **SetContext**. **SetContext** can use the [**GetDeviceGuid**](https://msdn.microsoft.com/library/windows/hardware/ff548012) method of **INetLanConnectionUiInfo** to retrieve the GUID of a LAN device. The notify object can subsequently display properties for its network component in the context of this LAN device. For example, the notify object for the TCP/IP protocol can display an IP address that is associated with a particular LAN adapter in the context of that adapter. Doing so enables users to specify an IP address for that adapter.

 

 





