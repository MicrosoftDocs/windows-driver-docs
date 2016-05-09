---
title: ATA Port Driver
description: ATA Port Driver
ms.assetid: c7b9d794-a8cb-4bdd-bb93-bff473ea26a7
keywords: ["storage port drivers WDK , ATA Port driver", "ATA Port drivers WDK", "ATA Port drivers WDK , about ATA Port drivers", "IDE controllers WDK ATA Port driver"]
---

# ATA Port Driver


## <span id="ddk_ata_port_driver_kg"></span><span id="DDK_ATA_PORT_DRIVER_KG"></span>


In addition to the [SCSI Port Driver](scsi-port-driver.md) and the [Storport Driver](storport-driver.md), Windows Vista and later versions of the Windows operating system provide the ATA port driver (*Ataport.sys*), a storage port driver that is especially suitable for use with IDE controllers.

The most significant difference between the ATA port driver and other system-supplied storage port drivers is the protocol that the ATA port driver uses to communicate with other drivers. All other system-supplied storage port drivers use SCSI request blocks (SRBs) to communicate both with higher-level drivers, such as storage class drivers, and with miniport drivers. The ATA port driver uses SRBs to communicate with higher-level drivers only. To communicate with its miniport drivers, ATA port uses a packet called an IDE request block (IRB), which is defined by the [**IDE\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559140) structure. IRBs are better designed than SRBs to the characteristics of ATA devices.

Another difference between the ATA port driver and other system-supplied storage drivers is that the ATA port driver shields ATA miniport drivers from certain requirements that are defined by the SCSI standard. For example, the ATA port driver uses ATA commands to collect the equivalent of SCSI sense data from the ATA miniport driver, translates the data so that it complies with a SCSI sense data format, and passes the data to higher-level drivers as if it were SCSI sense data. Therefore, ATA miniport drivers do not have to respond directly to requests from higher-level drivers for SCSI sense data.

The ATA miniport driver interface closely resembles the SCSI port driver interface. Therefore, if you have already written a SCSI miniport driver, you should be able to easily learn how to write an ATA miniport driver. Drivers for current ATA/ATAPI technologies, such as Serial ATA (SATA), should use the higher performance Storport minport interface.

Together with the ATA port driver, the operating system provides a default ATA miniport driver and a default controller minidriver. The system-supplied default drivers work for most controller hardware, and we strongly recommend that the default minidrivers be used wherever possible.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20ATA%20Port%20Driver%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




