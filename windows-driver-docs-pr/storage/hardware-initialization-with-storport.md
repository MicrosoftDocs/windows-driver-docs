---
title: Hardware Initialization with Storport
description: Hardware Initialization with Storport
ms.assetid: 98930338-d192-4b25-a558-01614ef9662b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hardware Initialization with Storport


## <span id="ddk_hardware_initialization_with_storport_kg"></span><span id="DDK_HARDWARE_INITIALIZATION_WITH_STORPORT_KG"></span>


The Storport driver follows the SCSI Port driver's Plug and Play (PnP) initialization model. During the driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine, the miniport driver calls the [**StorPortInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff567108) routine with a [**HW\_INITIALIZATION\_DATA (STORPORT)**](https://msdn.microsoft.com/library/windows/hardware/ff557459) structure describing the hardware it supports. Later, when the PnP manager calls the port driver's [**StartIo**](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine, the port driver calls the miniport driver's [**HwStorFindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff557390) routine with a [**PORT\_CONFIGURATION\_INFORMATION (STORPORT)**](https://msdn.microsoft.com/library/windows/hardware/ff563901) structure, followed by a call to the miniport driver's [**HwStorInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff557396) routine to initialize the adapter.

For the most part, the Storport version of the HW\_INITIALIZATION\_DATA structure is the same as the structure by the same name that is used with SCSI Port.

As indicated in the section [Use of Mapping Buffers in the Storport I/O Model](use-of-mapping-buffers-in-the-storport-i-o-model.md), the **MapBuffers** member of both HW\_INITIALIZATION and PORT\_CONFIGURATION\_INFORMATION has a different meaning in the Storport case from that in the SCSI Port case.

 

 




