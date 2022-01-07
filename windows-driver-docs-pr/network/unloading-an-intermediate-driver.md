---
title: Unloading an Intermediate Driver
description: Unloading an Intermediate Driver
keywords:
- NDIS intermediate drivers WDK , unloading
- intermediate drivers WDK networking , unloading
- unloading intermediate drivers
- cleaning up after install or uninstall WDK NDIS intermediate
ms.date: 04/20/2017
---

# Unloading an Intermediate Driver





NDIS calls the [*MiniportDriverUnload*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_unload) function to unload an intermediate driver. Intermediate drivers must perform the same operations in *MiniportDriverUnload* as other miniport drivers. In addition to calling the [**NdisMDeregisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismderegisterminiportdriver) function, an intermediate driver also calls [**NdisDeregisterProtocolDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisderegisterprotocoldriver). *MiniportDriverUnload* should also perform any necessary cleanup operations, such as deallocating any protocol driver resources.

To perform cleanup operations before a intermediate driver is uninstalled, an intermediate driver can register a [*ProtocolUninstall*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_uninstall) function. For example, the protocol lower edge of an intermediate driver might require a *ProtocolUninstall* function. The intermediate driver can release its protocol edge resources in *ProtocolUninstall* before NDIS calls its *MiniportDriverUnload* function.

A miniport-intermediate driver calls **NdisMDeregisterMiniportDriver** twice, once for its physical device interface, and again for its virtual device interface.

 

