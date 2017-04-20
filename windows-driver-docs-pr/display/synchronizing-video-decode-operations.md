---
title: Synchronizing Video Decode Operations
description: Synchronizing Video Decode Operations
ms.assetid: 4c88bf8f-0f10-4281-b856-a0e056d69d0e
keywords:
- video decoding WDK DirectX VA , synchronization
- decoding video WDK DirectX VA , synchronization
- synchronization WDK DirectX VA
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Synchronizing Video Decode Operations


## <span id="ddk_synchronizing_video_decode_operations_gg"></span><span id="DDK_SYNCHRONIZING_VIDEO_DECODE_OPERATIONS_GG"></span>


The synchronization mechanism for DirectX VA 2.0 is improved from the 1.0 version and is more similar to the synchronization mechanisms used by Microsoft Direct3D operations.

In DirectX VA 1.0, synchronization is performed mainly by the decoder. Before the decoder can use a compressed buffer, it calls the [*DdMoCompQueryStatus*](https://msdn.microsoft.com/library/windows/hardware/ff550243) function to determine if the buffer is available for use (that is, the hardware is not accessing the buffer). If the buffer is not available, the decoder must sleep, poll, or perform another operation.

DirectX VA 2.0 uses the synchronization model that Direct3D already uses on vertex buffers and index buffers. In DirectX VA 2.0, synchronization is performed by the decoder locking the compressed buffer. If the user-mode display driver attempts to lock the compressed buffer and the buffer is in use, the driver can either fail the lock or rename the buffer. The user-mode display driver requests that the video memory manager rename the buffer when the driver sets the **Discard** member of the [**D3DDDICB\_LOCKFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff544214) structure in a call to the [**pfnLockCb**](https://msdn.microsoft.com/library/windows/hardware/ff568914) function. If the user-mode display driver renames the buffer, the driver returns a pointer to an alternative buffer so that the decoder can continue without being blocked.

Typically, for DirectX VA 2.0, synchronization is only an issue if the hardware can consume the compressed buffers directly without additional buffer copies.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Synchronizing%20Video%20Decode%20Operations%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




