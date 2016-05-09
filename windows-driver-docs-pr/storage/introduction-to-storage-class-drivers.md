---
title: Introduction to Storage Class Drivers
author: windows-driver-content
description: Introduction to Storage Class Drivers
ms.assetid: 0ea462a9-5e6f-419f-af36-50f50901143d
keywords: ["storage class drivers WDK , about storage class drivers", "class drivers WDK storage , about storage class drivers", "HBA WDK storage"]
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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Introduction%20to%20Storage%20Class%20Drivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


