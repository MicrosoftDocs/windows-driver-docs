---
title: Video Port Driver Support for AGP
description: Video Port Driver Support for AGP
keywords:
- video miniport drivers WDK Windows 2000 , AGP
- AGP WDK video miniport
- memory WDK video miniport
ms.date: 04/20/2017
---

# Video Port Driver Support for AGP


## <span id="ddk_video_port_driver_support_for_agp_gg"></span><span id="DDK_VIDEO_PORT_DRIVER_SUPPORT_FOR_AGP_GG"></span>


The video port driver implements the following functions to support Accelerated Graphics Port (AGP).

[**AgpReservePhysical**](/windows-hardware/drivers/ddi/videoagp/nc-videoagp-pagp_reserve_physical)

[**AgpCommitPhysical**](/windows-hardware/drivers/ddi/videoagp/nc-videoagp-pagp_commit_physical)

[**AgpReserveVirtual**](/windows-hardware/drivers/ddi/videoagp/nc-videoagp-pagp_reserve_virtual)

[**AgpCommitVirtual**](/windows-hardware/drivers/ddi/videoagp/nc-videoagp-pagp_commit_virtual)

[**AgpFreeVirtual**](/windows-hardware/drivers/ddi/videoagp/nc-videoagp-pagp_free_virtual)

[**AgpReleaseVirtual**](/windows-hardware/drivers/ddi/videoagp/nc-videoagp-pagp_release_virtual)

[**AgpFreePhysical**](/windows-hardware/drivers/ddi/videoagp/nc-videoagp-pagp_free_physical)

[**AgpReleasePhysical**](/windows-hardware/drivers/ddi/videoagp/nc-videoagp-pagp_release_physical)

[**AgpSetRate**](/windows-hardware/drivers/ddi/videoagp/nc-videoagp-pagp_set_rate)

Before the video miniport driver calls the functions in the preceding list, it must obtain function pointers by calling [**VideoPortQueryServices**](/windows-hardware/drivers/ddi/video/nf-video-videoportqueryservices). For more information about obtaining pointers to the AGP functions, see [AGP Functions Implemented by the Video Port Driver](/windows-hardware/drivers/ddi/videoagp/).

The video miniport driver performs the following steps to reserve and commit a portion of the AGP aperture through which the display adapter can access system memory:

1.  Call [**AgpReservePhysical**](/windows-hardware/drivers/ddi/videoagp/nc-videoagp-pagp_reserve_physical) to reserve a contiguous range of physical addresses in the AGP aperture.

2.  Call [**AgpCommitPhysical**](/windows-hardware/drivers/ddi/videoagp/nc-videoagp-pagp_commit_physical) to map a portion (or all) of the address range returned by *AgpReservePhysical* to pages in system memory. The pages in system memory are locked, but not necessarily contiguous. The video miniport driver can call *AgpCommitPhysical* several times to do several small commitments rather than one large one. However, the driver must not attempt to commit a range that is already committed.

Then, for an application to be able to see and use the committed pages in system memory, the video miniport driver performs the following steps:

1.  Call [**AgpReserveVirtual**](/windows-hardware/drivers/ddi/videoagp/nc-videoagp-pagp_reserve_virtual) to reserve a range of virtual addresses in the application's address space. The video miniport driver must pass *AgpReserveVirtual* a handle, previously returned by *AgpReservePhysical*, so that the reserved virtual address range can be associated with the physical address range created by *AgpReservePhysical*.

2.  Call [**AgpCommitVirtual**](/windows-hardware/drivers/ddi/videoagp/nc-videoagp-pagp_commit_virtual) to map a portion of the virtual address range returned by *AgpReserveVirtual* to pages in system memory. The pages that *AgpCommitVirtual* maps must have been previously mapped by a call to *AgpCommitPhysical*. Furthermore, that mapping established by *AgpCommitPhysical* must still be current; that is, those pages must not have been freed by a call to [**AgpFreePhysical**](/windows-hardware/drivers/ddi/videoagp/nc-videoagp-pagp_free_physical).

**Note**   Whenever you use the AGP functions to commit or reserve an address range (physical or virtual), the size of the range must be a multiple of 64 kilobytes.

 

The video miniport driver is responsible for releasing and freeing all memory that it has reserved and committed by calling the following functions:

-   [**AgpFreeVirtual**](/windows-hardware/drivers/ddi/videoagp/nc-videoagp-pagp_free_virtual) unmaps virtual addresses that were mapped to system memory by a prior call to [**AgpCommitVirtual**](/windows-hardware/drivers/ddi/videoagp/nc-videoagp-pagp_commit_virtual).

-   [**AgpReleaseVirtual**](/windows-hardware/drivers/ddi/videoagp/nc-videoagp-pagp_release_virtual) releases virtual addresses that were reserved by a prior call to [**AgpReserveVirtual**](/windows-hardware/drivers/ddi/videoagp/nc-videoagp-pagp_reserve_virtual).

-   [**AgpFreePhysical**](/windows-hardware/drivers/ddi/videoagp/nc-videoagp-pagp_free_physical) unmaps physical addresses that were mapped to system memory by a prior call to [**AgpCommitPhysical**](/windows-hardware/drivers/ddi/videoagp/nc-videoagp-pagp_commit_physical).

-   [**AgpReleasePhysical**](/windows-hardware/drivers/ddi/videoagp/nc-videoagp-pagp_release_physical) releases physical addresses that were reserved by a prior call to [**AgpReservePhysical**](/windows-hardware/drivers/ddi/videoagp/nc-videoagp-pagp_reserve_physical).

 

