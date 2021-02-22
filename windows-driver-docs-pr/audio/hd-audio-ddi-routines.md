---
title: HD Audio DDI Routines
description: HD Audio DDI Routines
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# HD Audio DDI Routines


As explained in [Differences Between the HD Audio DDI Versions](./differences-between-the-hd-audio-ddi-versions.md), three versions of the HD Audio DDI exist. These three DDI versions are defined by the [**HDAUDIO\_BUS\_INTERFACE**](/windows-hardware/drivers/ddi/hdaudio/ns-hdaudio-_hdaudio_bus_interface), [**HDAUDIO\_BUS\_INTERFACE\_V2**](/windows-hardware/drivers/ddi/hdaudio/ns-hdaudio-_hdaudio_bus_interface_v2), and [**HDAUDIO\_BUS\_INTERFACE\_BDL**](/windows-hardware/drivers/ddi/hdaudio/ns-hdaudio-_hdaudio_bus_interface_bdl) structures.

The three DDI versions are accessible only in kernel mode.

Each DDI version provides access to the hardware resources that the HD Audio bus controller manages. These resources include codecs, DMA engines, link bandwidth, link position registers, and a wall clock register. The HD Audio bus driver implements the DDI and exposes the DDI to its children. The children are instances of kernel-mode function drivers that use the DDI to manage the hardware codecs that are connected to the HD Audio controller.

To obtain access to a DDI version, a function driver must query the HD Audio bus driver for a DDI context object. For more information, see [Obtaining an HDAUDIO\_BUS\_INTERFACE DDI Object](./obtaining-an-hdaudio-bus-interface-ddi-object.md), [Obtaining an HDAUDIO\_BUS\_INTERFACE\_V2 DDI Object](./obtaining-an-hdaudio-bus-interface-v2-ddi-object.md), and [Obtaining an HDAUDIO\_BUS\_INTERFACE\_BDL DDI Object](./obtaining-an-hdaudio-bus-interface-bdl-ddi-object.md).

Each routine in the three DDI versions takes a pointer to the context object as its first call parameter.

The HDAUDIO\_BUS\_INTERFACE structure defines a DDI that contains the following routines:

[**AllocateCaptureDmaEngine**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pallocate_capture_dma_engine)

[**AllocateDmaBuffer**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pallocate_dma_buffer)

[**AllocateRenderDmaEngine**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pallocate_render_dma_engine)

[**ChangeBandwidthAllocation**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pchange_bandwidth_allocation)

[**FreeDmaBuffer**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pfree_dma_buffer)

[**FreeDmaEngine**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pfree_dma_engine)

[**GetDeviceInformation**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pget_device_information)

[**GetLinkPositionRegister**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pget_link_position_register)

[**GetResourceInformation**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pget_resource_information)

[**GetWallClockRegister**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pget_wall_clock_register)

[**RegisterEventCallback**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pregister_event_callback)

[**SetDmaEngineState**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pset_dma_engine_state)

[**TransferCodecVerbs**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-ptransfer_codec_verbs)

[**UnregisterEventCallback**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-punregister_event_callback)

The HDAUDIO\_BUS\_INTERFACE\_V2 structure is available in Windows Vista and later versions of Windows, and it defines a DDI that contains the following routines:

[**AllocateCaptureDmaEngine**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pallocate_capture_dma_engine)

[**AllocateDmaBuffer**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pallocate_dma_buffer)

[**AllocateDmaBufferWithNotification**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pallocate_dma_buffer_with_notification)

[**AllocateRenderDmaEngine**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pallocate_render_dma_engine)

[**ChangeBandwidthAllocation**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pchange_bandwidth_allocation)

[**FreeDmaBuffer**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pfree_dma_buffer)

[**FreeDmaBufferWithNotification**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pfree_dma_buffer_with_notification)

[**FreeDmaEngine**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pfree_dma_engine)

[**GetDeviceInformation**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pget_device_information)

[**GetLinkPositionRegister**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pget_link_position_register)

[**GetResourceInformation**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pget_resource_information)

[**GetWallClockRegister**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pget_wall_clock_register)

[**RegisterEventCallback**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pregister_event_callback)

[**RegisterNotificationEvent**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pregister_notification_event)

[**SetDmaEngineState**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pset_dma_engine_state)

[**TransferCodecVerbs**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-ptransfer_codec_verbs)

[**UnregisterEventCallback**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-punregister_event_callback)

[**UnregisterNotificationEvent**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-punregister_notification_event)

The HDAUDIO\_BUS\_INTERFACE version of the HD Audio DDI is supported in Windows Vista and later versions of Windows. In addition, a version of the HD Audio bus driver that supports this DDI can be installed in Windows 2000, Windows XP, and Windows Server 2003.

The HDAUDIO\_BUS\_INTERFACE\_BDL structure defines a DDI that contains the following routines:

[**AllocateCaptureDmaEngine**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pallocate_capture_dma_engine)

[**AllocateContiguousDmaBuffer**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pallocate_contiguous_dma_buffer)

[**AllocateRenderDmaEngine**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pallocate_render_dma_engine)

[**ChangeBandwidthAllocation**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pchange_bandwidth_allocation)

[**FreeContiguousDmaBuffer**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pfree_contiguous_dma_buffer)

[**FreeDmaEngine**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pfree_dma_engine)

[**GetDeviceInformation**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pget_device_information)

[**GetLinkPositionRegister**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pget_link_position_register)

[**GetResourceInformation**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pget_resource_information)

[**GetWallClockRegister**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pget_wall_clock_register)

[**RegisterEventCallback**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pregister_event_callback)

[**SetDmaEngineState**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pset_dma_engine_state)

[**SetupDmaEngineWithBdl**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-psetup_dma_engine_with_bdl)

[**TransferCodecVerbs**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-ptransfer_codec_verbs)

[**UnregisterEventCallback**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-punregister_event_callback)

A version of the HD Audio bus driver that supports the HDAUDIO\_BUS\_INTERFACE\_BDL version of the HD Audio DDI can be installed in Windows 2000, Windows XP, and Windows Server 2003. However, Windows Vista provides no support for this DDI version.

Most of the routines in the two DDIs are identical in both name and operation. However, the following two routines, which are part of the HDAUDIO\_BUS\_INTERFACE version of the DDI, are not included in the HDAUDIO\_BUS\_INTERFACE\_BDL version:

[**AllocateDmaBuffer**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pallocate_dma_buffer)

[**FreeDmaBuffer**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pfree_dma_buffer)

Similarly, the following three routines in the HDAUDIO\_BUS\_INTERFACE\_BDL version of the DDI are not part of the HDAUDIO\_BUS\_INTERFACE version:

[**AllocateContiguousDmaBuffer**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pallocate_contiguous_dma_buffer)

[**FreeContiguousDmaBuffer**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pfree_contiguous_dma_buffer)

[**SetupDmaEngineWithBdl**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-psetup_dma_engine_with_bdl)

This section describes the following DDI routines:

[**AllocateCaptureDmaEngine**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pallocate_capture_dma_engine)

[**AllocateContiguousDmaBuffer**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pallocate_contiguous_dma_buffer)

[**AllocateDmaBuffer**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pallocate_dma_buffer)

[**AllocateRenderDmaEngine**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pallocate_render_dma_engine)

[**ChangeBandwidthAllocation**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pchange_bandwidth_allocation)

[**FreeContiguousDmaBuffer**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pfree_contiguous_dma_buffer)

[**FreeDmaBuffer**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pfree_dma_buffer)

[**FreeDmaEngine**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pfree_dma_engine)

[**GetDeviceInformation**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pget_device_information)

[**GetLinkPositionRegister**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pget_link_position_register)

[**GetResourceInformation**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pget_resource_information)

[**GetWallClockRegister**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pget_wall_clock_register)

[**RegisterEventCallback**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pregister_event_callback)

[**SetDmaEngineState**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pset_dma_engine_state)

[**SetupDmaEngineWithBdl**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-psetup_dma_engine_with_bdl) which works with [**PHDAUDIO\_BDL\_ISR**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-phdaudio_bdl_isr)

[**TransferCodecVerbs**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-ptransfer_codec_verbs)

[**UnregisterEventCallback**](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-punregister_event_callback)

The preceding list contains all the routines that appear in either or both versions of the DDI.

 

