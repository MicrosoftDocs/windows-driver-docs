---
title: Initializing Virtual Miniports
description: Initializing Virtual Miniports
ms.assetid: b712fe29-fd56-4abd-bab6-e335350a20c2
keywords:
- underlying adapter opening WDK networking
- opening underlying adapters
- virtual miniports WDK networking
- initializing virtual miniports
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing Virtual Miniports





An intermediate driver initializes its virtual miniports after it has successfully opened an underlying miniport adapter and is ready to accept requests and sends on its virtual miniports. An intermediate driver calls [**NdisIMInitializeDeviceInstanceEx**](https://msdn.microsoft.com/library/windows/hardware/ff562727) from its [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function one or more times to request initialization of one or more virtual miniports.

**Note**  An intermediate driver is not required to call **NdisIMInitializeDeviceInstanceEx** when it opens an underlying miniport adapter. There does not have to be a one-to-one relationship between virtual miniports and open adapters.

 

Set the *DriverInstance* parameter of **NdisIMInitializeDeviceInstanceEx** to the device name for the virtual miniport being initialized. The intermediate driver obtains the device name from the **UpperBindings** registry key.

For an *n*-to-one MUX intermediate driver that layers multiple virtual miniports over a single physical NIC, there must be a device name for every virtual miniport. The MUX intermediate driver requires a notify object that maintains the list of virtual miniport device names. The recommended location for the list is the **UpperBindings** registry key. In this case, the **UpperBindings** registry key is a MULTI\_SZ entry that contains the list of device names. The MUX intermediate driver calls **NdisIMInitializeDeviceInstanceEx** once for each device name that is specified in the device name list.

Calling **NdisIMInitializeDeviceInstanceEx** results in a call to the intermediate driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function to perform the initialization of the specified virtual miniport, provided that NDIS receives an IRP\_MN\_START\_DEVICE to start the device. If NDIS does not receive such an IRP, NDIS will not call the intermediate driver's *MiniportInitializeEx* function. The call to *MiniportInitializeEx* can happen at a later time and therefore is not necessarily within the context of the call to **NdisIMInitializeDeviceInstanceEx**. If NDIS never calls *MiniportInitializeEx* for the virtual miniport referenced in a call to **NdisIMInitializeDeviceInstanceEx**, and the intermediate driver no longer requires the virtual miniport, the intermediate driver should call [**NdisIMCancelInitializeDeviceInstance**](https://msdn.microsoft.com/library/windows/hardware/ff562719) to cancel the initialization of the virtual miniport. For example, suppose that an intermediate driver creates a virtual miniport in response to a successful binding to an underlying miniport. If that binding is removed before NDIS calls *MiniportInitializeEx*, the intermediate driver should call **NdisIMCancelInitializeDeviceInstance** to cancel the initialization of the miniport.

*MiniportInitializeEx* must allocate and initialize a virtual-miniport-specific context area. For more information about specifying the context area, see [Initializing a Virtual Miniport](initializing-a-virtual-miniport.md).

An intermediate driver must operate as a deserialized driver. For more information about deserialized drivers, see [Deserialized NDIS Miniport Drivers](deserialized-ndis-miniport-drivers.md).

An intermediate driver should verify that the state information it maintains is properly initialized. If the driver requires send-related resources--for example, new [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures for network data that [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) will transmit to the next lower layer--the NET\_BUFFER\_LIST structure pool can be allocated at this time.

 

 





