---
title: Hardware Initialization with Storport
description: Hardware Initialization with Storport
ms.assetid: 98930338-d192-4b25-a558-01614ef9662b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hardware Initialization with Storport


## <span id="ddk_hardware_initialization_with_storport_kg"></span><span id="DDK_HARDWARE_INITIALIZATION_WITH_STORPORT_KG"></span>


The Storport driver follows the SCSI Port driver's Plug and Play (PnP) initialization model. During the driver's [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine, the miniport driver calls the [**StorPortInitialize**](/windows-hardware/drivers/ddi/storport/nf-storport-storportinitialize) routine with a [**HW\_INITIALIZATION\_DATA (STORPORT)**](https://docs.microsoft.com/windows-hardware/drivers/ddi/storport/ns-storport-_hw_initialization_data) structure describing the hardware it supports. Later, when the PnP manager calls the port driver's [**StartIo**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routine, the port driver calls the miniport driver's [**HwStorFindAdapter**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_find_adapter) routine with a [**PORT\_CONFIGURATION\_INFORMATION (STORPORT)**](/previous-versions/windows/hardware/drivers/ff563901(v=vs.85)) structure, followed by a call to the miniport driver's [**HwStorInitialize**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_initialize) routine to initialize the adapter.

For the most part, the Storport version of the HW\_INITIALIZATION\_DATA structure is the same as the structure by the same name that is used with SCSI Port.

As indicated in the section [Use of Mapping Buffers in the Storport I/O Model](use-of-mapping-buffers-in-the-storport-i-o-model.md), the **MapBuffers** member of both HW\_INITIALIZATION and PORT\_CONFIGURATION\_INFORMATION has a different meaning in the Storport case from that in the SCSI Port case.

 

