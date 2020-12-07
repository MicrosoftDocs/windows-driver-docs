---
title: Introduction to Storage Class Drivers
description: Introduction to Storage Class Drivers
keywords:
- storage class drivers WDK , about storage class drivers
- class drivers WDK storage , about storage class drivers
- HBA WDK storage
ms.date: 12/15/2019
ms.localizationpriority: medium
---

# Introduction to Storage Class Drivers

A *storage class driver* uses the well-established SCSI class/port interface to control a mass storage device of its type on any bus for which the system supplies a storage port driver (currently SCSI, IDE, USB and IEEE 1394). The particular bus to which a storage device is connected is transparent to the storage class driver.

Any storage class driver handles I/O requests from user applications or higher-level drivers by building *SCSI request blocks* (SRBs) containing *command descriptor blocks* (CDBs) and sending them, through any intervening filter drivers, to the underlying storage port driver.

A storage class driver does not provide addressing information in the SRB. Instead, the port driver (or a still-lower driver) is responsible for any addressing required. The storage port driver translates the SRBs into the format required by the underlying host bus adapter (HBA), which might be a SCSI or 1394 host bus adapter, IDE controller, or other such hardware, and issues commands to the device. In the Windows Driver Kit (WDK), the term "HBA" stands for any such underlying adapter or controller.

To the I/O manager and any higher-level drivers layered above a storage class driver, most storage class drivers are standard kernel-mode intermediate drivers. Thus every class driver must have a [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine, an [**AddDevice**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine, an [**Unload**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) routine, one or more [**IoCompletion**](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routines, plus [**DispatchPnP**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) and [**DispatchPower**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routines to handle Plug and Play and power IRPs.

A storage class driver must also have a [**DispatchSystemControl**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine to handle system-control IRPs, and can have any other standard higher-level driver routine, such as a [**StartIo**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routine, as determined by the driver designer. For more information about system-control and standard kernel-mode driver routines, see [Standard Driver Routines](../kernel/introduction-to-standard-driver-routines.md).

To the PnP manager, a storage class driver is a [Function Drivers](../kernel/function-drivers.md), that is, one that drives an individual device. A storage class driver can also act as a [Bus Drivers](../kernel/bus-drivers.md), enumerating child devices of its devices. For example, the class driver for a partitioned media device such as a disk returns a list of PDOs representing its partitions. Each such PDO can be addressed as a target device and be serviced by its own class driver.

> [!NOTE]
> A driver for a SCSI device such as a printer or a scanner should be implemented as described in this section. A driver for such a SCSI device utilizes the same SCSI class/port interface to control its device and has the same responsibilities to handle IRPs, build SRBs, and send them to the underlying port driver as does a driver for a storage device.
