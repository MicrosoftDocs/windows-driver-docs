---
title: Unloading an Intermediate Driver
description: Unloading an Intermediate Driver
ms.assetid: e3c1dad4-4262-4449-8dcd-2e2f5d6c8e25
keywords:
- NDIS intermediate drivers WDK , unloading
- intermediate drivers WDK networking , unloading
- unloading intermediate drivers
- cleaning up after install or uninstall WDK NDIS intermediate
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Unloading an Intermediate Driver





NDIS calls the [*MiniportDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff559378) function to unload an intermediate driver. Intermediate drivers must perform the same operations in *MiniportDriverUnload* as other miniport drivers. In addition to calling the [**NdisMDeregisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563578) function, an intermediate driver also calls [**NdisDeregisterProtocolDriver**](https://msdn.microsoft.com/library/windows/hardware/ff561743). *MiniportDriverUnload* should also perform any necessary cleanup operations, such as deallocating any protocol driver resources.

To perform cleanup operations before a intermediate driver is uninstalled, an intermediate driver can register a [*ProtocolUninstall*](https://msdn.microsoft.com/library/windows/hardware/ff570279) function. For example, the protocol lower edge of an intermediate driver might require a *ProtocolUninstall* function. The intermediate driver can release its protocol edge resources in *ProtocolUninstall* before NDIS calls its *MiniportDriverUnload* function.

A miniport-intermediate driver calls **NdisMDeregisterMiniportDriver** twice, once for its physical device interface, and again for its virtual device interface.

 

 





