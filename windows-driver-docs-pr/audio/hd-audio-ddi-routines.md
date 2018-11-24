---
title: HD Audio DDI Routines
description: HD Audio DDI Routines
ms.assetid: 2f360031-39bd-457e-8b64-04b37e21a7fe
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# HD Audio DDI Routines


As explained in [Differences Between the HD Audio DDI Versions](https://msdn.microsoft.com/library/windows/hardware/ff536258), three versions of the HD Audio DDI exist. These three DDI versions are defined by the [**HDAUDIO\_BUS\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff536413), [**HDAUDIO\_BUS\_INTERFACE\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff536418), and [**HDAUDIO\_BUS\_INTERFACE\_BDL**](https://msdn.microsoft.com/library/windows/hardware/ff536416) structures.

The three DDI versions are accessible only in kernel mode.

Each DDI version provides access to the hardware resources that the HD Audio bus controller manages. These resources include codecs, DMA engines, link bandwidth, link position registers, and a wall clock register. The HD Audio bus driver implements the DDI and exposes the DDI to its children. The children are instances of kernel-mode function drivers that use the DDI to manage the hardware codecs that are connected to the HD Audio controller.

To obtain access to a DDI version, a function driver must query the HD Audio bus driver for a DDI context object. For more information, see [Obtaining an HDAUDIO\_BUS\_INTERFACE DDI Object](https://msdn.microsoft.com/library/windows/hardware/ff537589), [Obtaining an HDAUDIO\_BUS\_INTERFACE\_V2 DDI Object](https://msdn.microsoft.com/library/windows/hardware/ff537592), and [Obtaining an HDAUDIO\_BUS\_INTERFACE\_BDL DDI Object](https://msdn.microsoft.com/library/windows/hardware/ff537586).

Each routine in the three DDI versions takes a pointer to the context object as its first call parameter.

The HDAUDIO\_BUS\_INTERFACE structure defines a DDI that contains the following routines:

[**AllocateCaptureDmaEngine**](https://msdn.microsoft.com/library/windows/hardware/ff536177)

[**AllocateDmaBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536179)

[**AllocateRenderDmaEngine**](https://msdn.microsoft.com/library/windows/hardware/ff536181)

[**ChangeBandwidthAllocation**](https://msdn.microsoft.com/library/windows/hardware/ff536229)

[**FreeDmaBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536391)

[**FreeDmaEngine**](https://msdn.microsoft.com/library/windows/hardware/ff536393)

[**GetDeviceInformation**](https://msdn.microsoft.com/library/windows/hardware/ff536397)

[**GetLinkPositionRegister**](https://msdn.microsoft.com/library/windows/hardware/ff536398)

[**GetResourceInformation**](https://msdn.microsoft.com/library/windows/hardware/ff536399)

[**GetWallClockRegister**](https://msdn.microsoft.com/library/windows/hardware/ff536401)

[**RegisterEventCallback**](https://msdn.microsoft.com/library/windows/hardware/ff537803)

[**SetDmaEngineState**](https://msdn.microsoft.com/library/windows/hardware/ff537889)

[**TransferCodecVerbs**](https://msdn.microsoft.com/library/windows/hardware/ff538596)

[**UnregisterEventCallback**](https://msdn.microsoft.com/library/windows/hardware/ff538663)

The HDAUDIO\_BUS\_INTERFACE\_V2 structure is available in Windows Vista and later versions of Windows, and it defines a DDI that contains the following routines:

[**AllocateCaptureDmaEngine**](https://msdn.microsoft.com/library/windows/hardware/ff536177)

[**AllocateDmaBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536179)

[**AllocateDmaBufferWithNotification**](https://msdn.microsoft.com/library/windows/hardware/ff536180)

[**AllocateRenderDmaEngine**](https://msdn.microsoft.com/library/windows/hardware/ff536181)

[**ChangeBandwidthAllocation**](https://msdn.microsoft.com/library/windows/hardware/ff536229)

[**FreeDmaBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536391)

[**FreeDmaBufferWithNotification**](https://msdn.microsoft.com/library/windows/hardware/ff536392)

[**FreeDmaEngine**](https://msdn.microsoft.com/library/windows/hardware/ff536393)

[**GetDeviceInformation**](https://msdn.microsoft.com/library/windows/hardware/ff536397)

[**GetLinkPositionRegister**](https://msdn.microsoft.com/library/windows/hardware/ff536398)

[**GetResourceInformation**](https://msdn.microsoft.com/library/windows/hardware/ff536399)

[**GetWallClockRegister**](https://msdn.microsoft.com/library/windows/hardware/ff536401)

[**RegisterEventCallback**](https://msdn.microsoft.com/library/windows/hardware/ff537803)

[**RegisterNotificationEvent**](https://msdn.microsoft.com/library/windows/hardware/ff537809)

[**SetDmaEngineState**](https://msdn.microsoft.com/library/windows/hardware/ff537889)

[**TransferCodecVerbs**](https://msdn.microsoft.com/library/windows/hardware/ff538596)

[**UnregisterEventCallback**](https://msdn.microsoft.com/library/windows/hardware/ff538663)

[**UnregisterNotificationEvent**](https://msdn.microsoft.com/library/windows/hardware/ff538669)

The HDAUDIO\_BUS\_INTERFACE version of the HD Audio DDI is supported in Windows Vista and later versions of Windows. In addition, a version of the HD Audio bus driver that supports this DDI can be installed in Windows 2000, Windows XP, and Windows Server 2003.

The HDAUDIO\_BUS\_INTERFACE\_BDL structure defines a DDI that contains the following routines:

[**AllocateCaptureDmaEngine**](https://msdn.microsoft.com/library/windows/hardware/ff536177)

[**AllocateContiguousDmaBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536178)

[**AllocateRenderDmaEngine**](https://msdn.microsoft.com/library/windows/hardware/ff536181)

[**ChangeBandwidthAllocation**](https://msdn.microsoft.com/library/windows/hardware/ff536229)

[**FreeContiguousDmaBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536390)

[**FreeDmaEngine**](https://msdn.microsoft.com/library/windows/hardware/ff536393)

[**GetDeviceInformation**](https://msdn.microsoft.com/library/windows/hardware/ff536397)

[**GetLinkPositionRegister**](https://msdn.microsoft.com/library/windows/hardware/ff536398)

[**GetResourceInformation**](https://msdn.microsoft.com/library/windows/hardware/ff536399)

[**GetWallClockRegister**](https://msdn.microsoft.com/library/windows/hardware/ff536401)

[**RegisterEventCallback**](https://msdn.microsoft.com/library/windows/hardware/ff537803)

[**SetDmaEngineState**](https://msdn.microsoft.com/library/windows/hardware/ff537889)

[**SetupDmaEngineWithBdl**](https://msdn.microsoft.com/library/windows/hardware/ff537894)

[**TransferCodecVerbs**](https://msdn.microsoft.com/library/windows/hardware/ff538596)

[**UnregisterEventCallback**](https://msdn.microsoft.com/library/windows/hardware/ff538663)

A version of the HD Audio bus driver that supports the HDAUDIO\_BUS\_INTERFACE\_BDL version of the HD Audio DDI can be installed in Windows 2000, Windows XP, and Windows Server 2003. However, Windows Vista provides no support for this DDI version.

Most of the routines in the two DDIs are identical in both name and operation. However, the following two routines, which are part of the HDAUDIO\_BUS\_INTERFACE version of the DDI, are not included in the HDAUDIO\_BUS\_INTERFACE\_BDL version:

[**AllocateDmaBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536179)

[**FreeDmaBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536391)

Similarly, the following three routines in the HDAUDIO\_BUS\_INTERFACE\_BDL version of the DDI are not part of the HDAUDIO\_BUS\_INTERFACE version:

[**AllocateContiguousDmaBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536178)

[**FreeContiguousDmaBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536390)

[**SetupDmaEngineWithBdl**](https://msdn.microsoft.com/library/windows/hardware/ff537894)

This section describes the following DDI routines:

[**AllocateCaptureDmaEngine**](https://msdn.microsoft.com/library/windows/hardware/ff536177)

[**AllocateContiguousDmaBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536178)

[**AllocateDmaBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536179)

[**AllocateRenderDmaEngine**](https://msdn.microsoft.com/library/windows/hardware/ff536181)

[**ChangeBandwidthAllocation**](https://msdn.microsoft.com/library/windows/hardware/ff536229)

[**FreeContiguousDmaBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536390)

[**FreeDmaBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff536391)

[**FreeDmaEngine**](https://msdn.microsoft.com/library/windows/hardware/ff536393)

[**GetDeviceInformation**](https://msdn.microsoft.com/library/windows/hardware/ff536397)

[**GetLinkPositionRegister**](https://msdn.microsoft.com/library/windows/hardware/ff536398)

[**GetResourceInformation**](https://msdn.microsoft.com/library/windows/hardware/ff536399)

[**GetWallClockRegister**](https://msdn.microsoft.com/library/windows/hardware/ff536401)

[**RegisterEventCallback**](https://msdn.microsoft.com/library/windows/hardware/ff537803)

[**SetDmaEngineState**](https://msdn.microsoft.com/library/windows/hardware/ff537889)

[**SetupDmaEngineWithBdl**](https://msdn.microsoft.com/library/windows/hardware/ff537894) which works with [**PHDAUDIO\_BDL\_ISR**](https://msdn.microsoft.com/library/windows/hardware/mt750609)

[**TransferCodecVerbs**](https://msdn.microsoft.com/library/windows/hardware/ff538596)

[**UnregisterEventCallback**](https://msdn.microsoft.com/library/windows/hardware/ff538663)

The preceding list contains all the routines that appear in either or both versions of the DDI.

 

 





