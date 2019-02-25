---
title: Video Port Driver Support for AGP
description: Video Port Driver Support for AGP
ms.assetid: 445dbe4a-7f7b-4dcc-9891-17fd8fb03a6c
keywords:
- video miniport drivers WDK Windows 2000 , AGP
- AGP WDK video miniport
- memory WDK video miniport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Video Port Driver Support for AGP


## <span id="ddk_video_port_driver_support_for_agp_gg"></span><span id="DDK_VIDEO_PORT_DRIVER_SUPPORT_FOR_AGP_GG"></span>


The video port driver implements the following functions to support Accelerated Graphics Port (AGP).

[**AgpReservePhysical**](https://msdn.microsoft.com/library/windows/hardware/ff538223)

[**AgpCommitPhysical**](https://msdn.microsoft.com/library/windows/hardware/ff538215)

[**AgpReserveVirtual**](https://msdn.microsoft.com/library/windows/hardware/ff538224)

[**AgpCommitVirtual**](https://msdn.microsoft.com/library/windows/hardware/ff538216)

[**AgpFreeVirtual**](https://msdn.microsoft.com/library/windows/hardware/ff538219)

[**AgpReleaseVirtual**](https://msdn.microsoft.com/library/windows/hardware/ff538221)

[**AgpFreePhysical**](https://msdn.microsoft.com/library/windows/hardware/ff538217)

[**AgpReleasePhysical**](https://msdn.microsoft.com/library/windows/hardware/ff538220)

[**AgpSetRate**](https://msdn.microsoft.com/library/windows/hardware/ff538226)

Before the video miniport driver calls the functions in the preceding list, it must obtain function pointers by calling [**VideoPortQueryServices**](https://msdn.microsoft.com/library/windows/hardware/ff570337). For more information about obtaining pointers to the AGP functions, see [AGP Functions Implemented by the Video Port Driver](https://msdn.microsoft.com/library/windows/hardware/ff538227).

The video miniport driver performs the following steps to reserve and commit a portion of the AGP aperture through which the display adapter can access system memory:

1.  Call [**AgpReservePhysical**](https://msdn.microsoft.com/library/windows/hardware/ff538223) to reserve a contiguous range of physical addresses in the AGP aperture.

2.  Call [**AgpCommitPhysical**](https://msdn.microsoft.com/library/windows/hardware/ff538215) to map a portion (or all) of the address range returned by *AgpReservePhysical* to pages in system memory. The pages in system memory are locked, but not necessarily contiguous. The video miniport driver can call *AgpCommitPhysical* several times to do several small commitments rather than one large one. However, the driver must not attempt to commit a range that is already committed.

Then, for an application to be able to see and use the committed pages in system memory, the video miniport driver performs the following steps:

1.  Call [**AgpReserveVirtual**](https://msdn.microsoft.com/library/windows/hardware/ff538224) to reserve a range of virtual addresses in the application's address space. The video miniport driver must pass *AgpReserveVirtual* a handle, previously returned by *AgpReservePhysical*, so that the reserved virtual address range can be associated with the physical address range created by *AgpReservePhysical*.

2.  Call [**AgpCommitVirtual**](https://msdn.microsoft.com/library/windows/hardware/ff538216) to map a portion of the virtual address range returned by *AgpReserveVirtual* to pages in system memory. The pages that *AgpCommitVirtual* maps must have been previously mapped by a call to *AgpCommitPhysical*. Furthermore, that mapping established by *AgpCommitPhysical* must still be current; that is, those pages must not have been freed by a call to [**AgpFreePhysical**](https://msdn.microsoft.com/library/windows/hardware/ff538217).

**Note**   Whenever you use the AGP functions to commit or reserve an address range (physical or virtual), the size of the range must be a multiple of 64 kilobytes.

 

The video miniport driver is responsible for releasing and freeing all memory that it has reserved and committed by calling the following functions:

-   [**AgpFreeVirtual**](https://msdn.microsoft.com/library/windows/hardware/ff538219) unmaps virtual addresses that were mapped to system memory by a prior call to [**AgpCommitVirtual**](https://msdn.microsoft.com/library/windows/hardware/ff538216).

-   [**AgpReleaseVirtual**](https://msdn.microsoft.com/library/windows/hardware/ff538221) releases virtual addresses that were reserved by a prior call to [**AgpReserveVirtual**](https://msdn.microsoft.com/library/windows/hardware/ff538224).

-   [**AgpFreePhysical**](https://msdn.microsoft.com/library/windows/hardware/ff538217) unmaps physical addresses that were mapped to system memory by a prior call to [**AgpCommitPhysical**](https://msdn.microsoft.com/library/windows/hardware/ff538215).

-   [**AgpReleasePhysical**](https://msdn.microsoft.com/library/windows/hardware/ff538220) releases physical addresses that were reserved by a prior call to [**AgpReservePhysical**](https://msdn.microsoft.com/library/windows/hardware/ff538223).

 

 





