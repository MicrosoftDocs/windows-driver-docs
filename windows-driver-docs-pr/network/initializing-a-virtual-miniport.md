---
title: Initializing a Virtual Miniport
description: Initializing a Virtual Miniport
keywords:
- initializing virtual miniports
- virtual miniports WDK networking
- NDIS intermediate drivers WDK , virtual miniports
- intermediate drivers WDK networking , virtual miniports
ms.date: 04/20/2017
---

# Initializing a Virtual Miniport





To initiate the initialization of a virtual miniport, an intermediate driver calls the [**NdisIMInitializeDeviceInstanceEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisiminitializedeviceinstanceex) function. The intermediate driver usually makes this call from its [*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex) function. After the intermediate driver calls **NdisIMInitializeDeviceInstanceEx** and the Plug an Play manager requests NDIS to start the virtual device, NDIS calls the driver's [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function.

The call to *MiniportInitializeEx* can be in the context of **NdisIMInitializeDeviceInstanceEx** if the Plug and Play manager starts the virtual device before **NdisIMInitializeDeviceInstanceEx** returns. If the intermediate driver provides more than one virtual miniport, the driver must call **NdisIMInitializeDeviceInstanceEx** for each virtual miniport that it makes available.

NDIS passes initialization parameters to *MiniportInitializeEx* in an [**NDIS\_MINIPORT\_INIT\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_init_parameters) structure at *MiniportInitParameters* . The **IMDeviceInstanceContext** member of the structure specifies a pointer to the context area for a virtual device. The driver passed this pointer to the [**NdisIMInitializeDeviceInstanceEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisiminitializedeviceinstanceex) function at the *DeviceContext* parameter.

In *MiniportInitializeEx*, the intermediate driver performs the operations required to initialize a virtual miniport. This initialization is similar to the initialization of any other miniport adapter.

 

