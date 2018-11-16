---
title: Introduction to Storage Class Drivers
description: Introduction to Storage Class Drivers
ms.assetid: 0ea462a9-5e6f-419f-af36-50f50901143d
keywords:
- storage class drivers WDK , about storage class drivers
- class drivers WDK storage , about storage class drivers
- HBA WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to Storage Class Drivers


## <span id="ddk_introduction_to_storage_class_drivers_kg"></span><span id="DDK_INTRODUCTION_TO_STORAGE_CLASS_DRIVERS_KG"></span>


A *storage class driver* uses the well-established SCSI class/port interface to control a mass storage device of its type on any bus for which the system supplies a storage port driver (currently SCSI, IDE, USB and IEEE 1394). The particular bus to which a storage device is connected is transparent to the storage class driver.

Any storage class driver handles I/O requests from user applications or higher-level drivers by building *SCSI request blocks* (SRBs) containing *command descriptor blocks* (CDBs) and sending them, through any intervening filter drivers, to the underlying storage port driver.

A storage class driver does not provide addressing information in the SRB. Instead, the port driver (or a still-lower driver) is responsible for any addressing required. The storage port driver translates the SRBs into the format required by the underlying host bus adapter (HBA), which might be a SCSI or 1394 host bus adapter, IDE controller, or other such hardware, and issues commands to the device. In the Windows Driver Kit (WDK), the term "HBA" stands for any such underlying adapter or controller.

To the I/O manager and any higher-level drivers layered above a storage class driver, most storage class drivers are standard kernel-mode intermediate drivers. Thus every class driver must have a [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine, an [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine, an [**Unload**](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine, one or more [**IoCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff548354) routines, plus [**DispatchPnP**](https://msdn.microsoft.com/library/windows/hardware/ff543341) and [**DispatchPower**](https://msdn.microsoft.com/library/windows/hardware/ff543354) routines to handle Plug and Play and power IRPs.

A storage class driver must also have a [**DispatchSystemControl**](https://msdn.microsoft.com/library/windows/hardware/ff543412) routine to handle system-control IRPs, and can have any other standard higher-level driver routine, such as a [**StartIo**](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine, as determined by the driver designer. For more information about system-control and standard kernel-mode driver routines, see [Standard Driver Routines](https://msdn.microsoft.com/library/windows/hardware/ff563842).

To the PnP manager, a storage class driver is a [Function Drivers](https://msdn.microsoft.com/library/windows/hardware/ff546516), that is, one that drives an individual device. A storage class driver can also act as a [Bus Drivers](https://msdn.microsoft.com/library/windows/hardware/ff540704), enumerating child devices of its devices. For example, the class driver for a partitioned media device such as a disk returns a list of PDOs representing its partitions. Each such PDO can be addressed as a target device and be serviced by its own class driver.

**Note**   A driver for a SCSI device such as a printer or a scanner should be implemented as described in this section. A driver for such a SCSI device utilizes the same SCSI class/port interface to control its device and has the same responsibilities to handle IRPs, build SRBs, and send them to the underlying port driver as does a driver for a storage device.

 

 

 




