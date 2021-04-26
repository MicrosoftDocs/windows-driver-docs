---
title: Synchronizing Video Decode Operations
description: Synchronizing Video Decode Operations
keywords:
- video decoding WDK DirectX VA , synchronization
- decoding video WDK DirectX VA , synchronization
- synchronization WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Synchronizing Video Decode Operations


## <span id="ddk_synchronizing_video_decode_operations_gg"></span><span id="DDK_SYNCHRONIZING_VIDEO_DECODE_OPERATIONS_GG"></span>


The synchronization mechanism for DirectX VA 2.0 is improved from the 1.0 version and is more similar to the synchronization mechanisms used by Microsoft Direct3D operations.

In DirectX VA 1.0, synchronization is performed mainly by the decoder. Before the decoder can use a compressed buffer, it calls the [*DdMoCompQueryStatus*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_mocompcb_querystatus) function to determine if the buffer is available for use (that is, the hardware is not accessing the buffer). If the buffer is not available, the decoder must sleep, poll, or perform another operation.

DirectX VA 2.0 uses the synchronization model that Direct3D already uses on vertex buffers and index buffers. In DirectX VA 2.0, synchronization is performed by the decoder locking the compressed buffer. If the user-mode display driver attempts to lock the compressed buffer and the buffer is in use, the driver can either fail the lock or rename the buffer. The user-mode display driver requests that the video memory manager rename the buffer when the driver sets the **Discard** member of the [**D3DDDICB\_LOCKFLAGS**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddicb_lockflags) structure in a call to the [**pfnLockCb**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_lockcb) function. If the user-mode display driver renames the buffer, the driver returns a pointer to an alternative buffer so that the decoder can continue without being blocked.

Typically, for DirectX VA 2.0, synchronization is only an issue if the hardware can consume the compressed buffers directly without additional buffer copies.

 

