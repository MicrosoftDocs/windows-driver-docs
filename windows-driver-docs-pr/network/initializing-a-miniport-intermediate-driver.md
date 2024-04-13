---
title: Initializing a Miniport-Intermediate Driver
description: Initializing a Miniport-Intermediate Driver
keywords:
- NDIS intermediate drivers WDK , initializing
- intermediate drivers WDK networking , initializing
- initializing miniport-intermediate drivers
- miniport-intermediate drivers WDK NDIS
ms.date: 04/20/2017
---

# Initializing a Miniport-Intermediate Driver





A miniport-intermediate driver combines a miniport driver for a virtual device, a protocol driver, and a miniport driver for a physical device. A miniport-intermediate driver functions similarly to an intermediate driver layered over a miniport driver. Such a driver allows an intermediate driver to communicate directly with an underlying miniport driver without incurring the performance penalties that might result with two separate drivers.

To register its physical miniport driver, a miniport-intermediate driver calls the [**NdisMRegisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver) function with appropriate parameters just as for any miniport driver. To register its virtual miniport, the driver calls **NdisMRegisterMiniportDriver** again, but with the NDIS\_INTERMEDIATE\_DRIVER flag set in the structure at *MiniportDriverCharacteristics* .

For each virtual or physical device instance of a miniport-intermediate driver, if the **IMMiniport** registry key is set to **DWORD:0x0000001**, NDIS calls the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function that the driver registered for the virtual device. Otherwise, NDIS calls the driver's *MiniportInitializeEx* function that the driver registered for the physical device.

 

