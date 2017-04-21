---
title: Port Deletion
description: Port Deletion
ms.assetid: a6c5d14f-3b4c-4332-a89d-33e374e1463f
keywords:
- port-based network access WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Port Deletion


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The operating system deletes the port for the current association with the access point (AP) or peer station under the following conditions:

-   The miniport driver performs an explicit disassociation operation. For more information about this operation, see [Explicit Disassociation Operations](explicit-disassociation-operations.md).

    In this situation, the operating system deletes the port when the miniport driver makes an [NDIS\_STATUS\_DOT11\_DISASSOCIATION](https://msdn.microsoft.com/library/windows/hardware/ff567334) indication.

-   The miniport driver performs an implicit disassociation operation. For more information about this operation, see [Implicit Disassociation Operations](implicit-disassociation-operations.md).

    In this situation, the operating system deletes the port when the miniport driver makes an [NDIS\_STATUS\_DOT11\_ASSOCIATION\_START](https://msdn.microsoft.com/library/windows/hardware/ff567321) indication under the following conditions:

    -   The miniport driver performs an association operation by reassociating with the same AP or peer station. In this situation, the operating system deletes the port for the previous association and creates a new one for the reassociation.
    -   The miniport driver performs an association operation with another AP during a roaming operation. In this situation, the operating system deletes the port for the association with the first AP and creates a port for the association with the new AP.

        For more information about the roaming operation, see [Roaming Operations](roaming-operations.md).

    For more information about the association operation, see [Association Operations](association-operations.md).

If the independent hardware vendor (IHV) installed an IHV Extensions DLL to manage the port-based authentication, the operating system notifies the DLL of the port deletion through a call to the DLL's [*Dot11ExtIhvStopPostAssociate*](https://msdn.microsoft.com/library/windows/hardware/ff547521) function.

**Note**  If the operating system deletes a port following a disassociation operation by the miniport driver, the operating system will not issue a set request of [OID\_DOT11\_PORT\_STATE\_NOTIFICATION](https://msdn.microsoft.com/library/windows/hardware/ff569401) to notify the miniport driver about the port deletion. In this situation, the miniport driver must assume that the port will be deleted when it performs the disassociation operation.

 

For more information about the IHV Extensions DLL, see [Native 802.11 IHV Extensions DLL](https://msdn.microsoft.com/library/windows/hardware/ff560614).

 

 





