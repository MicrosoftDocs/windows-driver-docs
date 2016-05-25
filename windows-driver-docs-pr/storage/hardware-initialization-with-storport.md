---
title: Hardware Initialization with Storport
author: windows-driver-content
description: Hardware Initialization with Storport
ms.assetid: 98930338-d192-4b25-a558-01614ef9662b
---

# Hardware Initialization with Storport


## <span id="ddk_hardware_initialization_with_storport_kg"></span><span id="DDK_HARDWARE_INITIALIZATION_WITH_STORPORT_KG"></span>


The Storport driver follows the SCSI Port driver's Plug and Play (PnP) initialization model. During the driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine, the miniport driver calls the [**StorPortInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff567108) routine with a [**HW\_INITIALIZATION\_DATA (STORPORT)**](https://msdn.microsoft.com/library/windows/hardware/ff557459) structure describing the hardware it supports. Later, when the PnP manager calls the port driver's [**StartIo**](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine, the port driver calls the miniport driver's [**HwStorFindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff557390) routine with a [**PORT\_CONFIGURATION\_INFORMATION (STORPORT)**](https://msdn.microsoft.com/library/windows/hardware/ff563901) structure, followed by a call to the miniport driver's [**HwStorInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff557396) routine to initialize the adapter.

For the most part, the Storport version of the HW\_INITIALIZATION\_DATA structure is the same as the structure by the same name that is used with SCSI Port.

As indicated in the section [Use of Mapping Buffers in the Storport I/O Model](use-of-mapping-buffers-in-the-storport-i-o-model.md), the **MapBuffers** member of both HW\_INITIALIZATION and PORT\_CONFIGURATION\_INFORMATION has a different meaning in the Storport case from that in the SCSI Port case.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Hardware%20Initialization%20with%20Storport%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


