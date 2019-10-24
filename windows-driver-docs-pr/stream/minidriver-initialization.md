---
title: Minidriver Initialization
description: Minidriver Initialization
ms.assetid: 5aa4e2c6-5848-45fe-8a89-686aae7e85e6
keywords:
- initializing streaming minidrivers WDK Windows 2000 Kernel
- Stream.sys class driver WDK Windows 2000 Kernel , initializing minidrivers
- streaming minidrivers WDK Windows 2000 Kernel , initializing
- minidrivers WDK Windows 2000 Kernel Streaming , initializing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Minidriver Initialization





When the operating system first initializes the minidriver, it calls the minidriver's **DriverEntry** routine. See [**DriverEntry for Stream Class Minidrivers**](https://docs.microsoft.com/previous-versions/ff558717(v=vs.85)). The minidriver must register itself with the class driver by calling [**StreamClassRegisterMinidriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/strmini/nf-strmini-streamclassregisteradapter).

The minidriver passes an [**HW\_INITIALIZATION\_DATA**](https://docs.microsoft.com/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_initialization_data) structure, which provides the class driver with preliminary information, including the device-wide callbacks, [*StrMiniReceiveDevicePacket*](https://docs.microsoft.com/windows-hardware/drivers/ddi/strmini/nc-strmini-phw_receive_device_srb), [*StrMiniCancelPacket*](https://docs.microsoft.com/windows-hardware/drivers/ddi/strmini/nc-strmini-phw_cancel_srb), [*StrMiniRequestTimeout*](https://docs.microsoft.com/windows-hardware/drivers/ddi/strmini/nc-strmini-phw_request_timeout_handler), and [*StrMiniInterrupt*](https://docs.microsoft.com/windows-hardware/drivers/ddi/strmini/nc-strmini-phw_interrupt).

The class driver then uses [*StrMiniReceiveDevicePacket*](https://docs.microsoft.com/windows-hardware/drivers/ddi/strmini/nc-strmini-phw_receive_device_srb) to signal the minidriver that it should initialize the device. It sends the SRB\_INITIALIZE\_DEVICE request, and passes a [**PORT\_CONFIGURATION\_INFORMATION**](https://docs.microsoft.com/windows-hardware/drivers/ddi/strmini/ns-strmini-_port_configuration_information) structure with the needed hardware information. When completing this request, the minidriver supplies the size in bytes of the [**HW\_STREAM\_DESCRIPTOR**](https://docs.microsoft.com/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_stream_descriptor) structure it uses to describe all of its streams.

Once the minidriver completes that request, the class driver uses [*StrMiniReceiveDevicePacket*](https://docs.microsoft.com/windows-hardware/drivers/ddi/strmini/nc-strmini-phw_receive_device_srb) to send the SRB\_GET\_STREAM\_INFO request. The minidriver then supplies information about all of its streams, including each stream's callbacks.

Once the class driver finishes processing the stream data, it uses [*StrMiniReceiveDevicePacket*](https://docs.microsoft.com/windows-hardware/drivers/ddi/strmini/nc-strmini-phw_receive_device_srb) to send the SRB\_INITIALIZATION\_COMPLETE request. At this point, the minidriver is ready to start handling requests on each stream.

 

 




