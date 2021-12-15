---
title: Hardware Initialization with Storport
description: Hardware Initialization with Storport
ms.date: 04/20/2017
---

# Hardware Initialization with Storport

The Storport driver follows the SCSI Port driver's Plug and Play (PnP) initialization model. During the driver's [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine, the miniport driver calls the [**StorPortInitialize**](/windows-hardware/drivers/ddi/storport/nf-storport-storportinitialize) routine with a [**HW_INITIALIZATION_DATA (STORPORT)**](/windows-hardware/drivers/ddi/storport/ns-storport-_hw_initialization_data-r1) structure describing the hardware it supports. Later, when the PnP manager calls the port driver's [**StartIo**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routine, the port driver calls the miniport driver's [**HwStorFindAdapter**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_find_adapter) routine with a [**PORT_CONFIGURATION_INFORMATION (STORPORT)**](/windows-hardware/drivers/ddi/storport/ns-storport-_port_configuration_information) structure, followed by a call to the miniport driver's [**HwStorInitialize**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_initialize) routine to initialize the adapter.

For the most part, the Storport version of the HW_INITIALIZATION_DATA structure is the same as the structure by the same name that is used with SCSI Port.

As indicated in the section [Use of Mapping Buffers in the Storport I/O Model](use-of-mapping-buffers-in-the-storport-i-o-model.md), the **MapBuffers** member of both HW_INITIALIZATION and PORT_CONFIGURATION_INFORMATION has a different meaning in the Storport case from that in the SCSI Port case.
