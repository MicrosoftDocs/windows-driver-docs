---
title: Registering as an NDIS Intermediate Driver
description: Registering as an NDIS Intermediate Driver
ms.assetid: 4a095fa7-0d8f-4d7d-885c-bc43cd34c784
keywords:
- registering intermediate drivers
- intermediate drivers WDK networking , registering
- NDIS intermediate drivers WDK , registering
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering as an NDIS Intermediate Driver





An NDIS intermediate driver must register its *MiniportXxx* functions and its *ProtocolXxx* functions with NDIS in the context of its [**DriverEntry**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) function. To register its *MiniportXxx* functions, an intermediate driver must call [**NdisMRegisterMiniportDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver) with the NDIS\_INTERMEDIATE\_DRIVER flag set. This flag is in the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics) structure that the driver passes at *MiniportDriverCharacteristics* . This call exports the intermediate driver's *MiniportXxx* functions. For more information about registering *MiniportXxx* functions, see [Registering an Intermediate Driver as a Miniport Driver](registering-an-intermediate-driver-as-a-miniport-driver.md).

Note that the intermediate driver controls when its virtual miniports are initialized, and thus, when the driver is ready to accept sends and requests on an adapter. NDIS calls the intermediate driver's [*MiniportInitializeEx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function after the Plug and Play (PnP) manager has started the virtual miniport device and after the intermediate driver has called [**NdisIMInitializeDeviceInstanceEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisiminitializedeviceinstanceex) for that device. The call to *MiniportInitializeEx* can happen at a later time and therefore is not necessarily within the context of the call to **NdisIMInitializeDeviceInstanceEx**. If the intermediate driver exports more than one virtual miniport, the driver must call **NdisIMInitializeDeviceInstanceEx** for each virtual miniport that it makes available for network requests.

To register its *ProtocolXxx* functions, an intermediate driver must call the [**NdisRegisterProtocolDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisregisterprotocoldriver) function. For more information about registering *ProtocolXxx* functions, see [Registering an Intermediate Driver as a Protocol Driver](registering-an-intermediate-driver-as-a-protocol.md).

 

 





