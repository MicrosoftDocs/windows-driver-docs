---
title: SCSI Miniport Initialization Under Plug and Play
description: SCSI Miniport Initialization Under Plug and Play
ms.assetid: bf2f9809-8271-4f0f-a2c4-25127fe9c4aa
keywords:
- SCSI miniport drivers WDK storage , PnP
- PnP WDK SCSI
- Plug and Play WDK SCSI
- initializing SCSI miniport drivers
- SCSI miniport drivers WDK storage , initializing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SCSI Miniport Initialization Under Plug and Play


## <span id="ddk_scsi_miniport_initialization_under_plug_and_play_kg"></span><span id="DDK_SCSI_MINIPORT_INITIALIZATION_UNDER_PLUG_AND_PLAY_KG"></span>


For Windows 2000 and later, a legacy miniport driver is initialized in exactly the same way as for Microsoft Windows NT 4.0. When a legacy miniport driver calls [**ScsiPortInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff564645), the port driver calls the miniport driver to locate and initialize its HBA. This is done either once for each HBA it finds (if the HBA is on an enumerable bus) or repeatedly until the miniport driver reports that it cannot find any more devices. Control then returns to the miniport driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff552654) routine, where the miniport driver can call **ScsiPortInitialize** again for a different type of HBA (for example, a different interface or a different vendor and product ID). All of the initialization calls are made within the context of the miniport driver's **DriverEntry** routine and are made in the order that **ScsiPortInitialize** was called. Initialization of legacy drivers occurs at system startup and at no other time.

In Plug and Play, the order of initialization cannot be preserved. When a miniport driver that is enabled for Plug and Play calls **ScsiPortInitialize**, the port driver stores the initialization data for future reference, then returns STATUS\_SUCCESS. This is done for each interface type that is listed in the miniport driver's **PnPInterface** registry key -- any interfaces *not* listed in that key are still initialized immediately.

Later, when the Plug and Play manager detects an HBA for the miniport driver, it notifies the port driver. The port driver allocates the necessary system resources (such as memory for the miniport driver's device extension) and calls the miniport driver to find the HBA and then to initialize it. This usually happens during system startup, but it might also happen when the system detects a docking operation or when an HBA such as a CardBus is hot-plugged into the system.

By the time the Plug and Play manager reports a device, it has already allocated bus resources (such as I/O ports, memory addresses, and interrupts) for that device *and that device alone*. These resources are supplied to the miniport driver, which must either use these resources or report that no device was found. In particular, the miniport driver must not attempt to access ports or memory locations other than the ones specified to find a device.

A miniport driver that has been started as a Plug and Play driver might be asked to detect devices that are on nonenumerable buses. This includes buses such as ISA, which require that the miniport driver issue commands on the bus to find its HBA. Devices located during such detection are recorded in the registry and initialized as Plug and Play devices the next time the system is started.

For more information about Plug and Play, see [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125).

 

 




