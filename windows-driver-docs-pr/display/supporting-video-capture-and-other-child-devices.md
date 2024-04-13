---
title: Supporting Video Capture and Other Child Devices
description: Supporting Video Capture and Other Child Devices
keywords:
- video capture WDK display
- capturing video WDK display
- interfaces WDK display
- child video capture drivers WDK display
- MDLs WDK display
- memory descriptor lists WDK display
- capture buffers WDK display
- display driver model WDK Windows Vista , child video capture drivers
- Windows Vista display driver model WDK , child video capture drivers
ms.date: 04/20/2017
---

# Supporting Video Capture and Other Child Devices


A display miniport driver and the driver for a video capture device or another child device can mutually define a private interface that the child driver can use to communicate with its device through the parent miniport driver. A child video capture driver must be tightly coupled to the parent display miniport driver. In fact, video capture could possibly be implemented as part of the display miniport driver. A video capture driver can use the private interface with the display miniport driver to access the *I2C* bus and for other purposes.

To initialize the private interface, the video capture driver sends a [**IRP\_MN\_QUERY\_INTERFACE**](../kernel/irp-mn-query-interface.md) request to the display port driver (part of *Dxgkrnl.sys*) for the display miniport driver. After the display port driver receives such a request, it calls the miniport driver's [**DxgkDdiQueryInterface**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_interface) function and passes a pointer to a [**QUERY\_INTERFACE**](/windows-hardware/drivers/ddi/video/ns-video-_query_interface) structure that contains information to initialize the private interface.

**Note**   If video capture is implemented as part of the display miniport driver, the video capture might call *DxgkDdiQueryInterface* directly.

 

Each driver of a child device (including video capture devices) must return the adapter GUID that indicates the hardware that the device is associated with. The adapter GUID is supplied to the display miniport driver in the **AdapterGuid** member of the [**DXGK\_START\_INFO**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_start_info) structure that is pointed to by the *DxgkStartInfo* parameter of the [**DxgkDdiStartDevice**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_start_device) function that is sent when the adapter is initialized. User-mode capture components can subsequently map this adapter GUID to a display adapter.

In the Microsoft [Windows 2000 Display Driver Model](windows-2000-display-driver-model-design-guide.md), video capture applications send system memory capture buffers to kernel mode. Kernel mode then describes the system memory buffers by using *memory descriptor list (MDL)* structures and sends the MDLs to the video capture driver. In addition to supporting capture to system memory, the Windows Vista display driver model supports capture to video memory. The Direct3D runtime calls DirectX Video Acceleration 2.0-type functions to direct the GPU to perform post processing on capture data. Instead of sending MDLs to describe the video memory buffers, the user-mode display driver will send D3DKMT\_HANDLE-type values that are handles to capture buffer allocations. Therefore, the video capture driver and display miniport driver combination can use existing callback functions like [**DxgkCbGetHandleData**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_gethandledata) to reference private data that describes the capture buffer. The driver combination can also use the [**DxgkCbGetCaptureAddress**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_getcaptureaddress) callback function to return the physical address of the capture buffer.

Video capture applications call into the Direct3D runtime to create capture buffers; the runtime subsequently calls into the user-mode display driver. The runtime calls the user-mode display driver's [**CreateResource**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createresource) function with the **CaptureBuffer** bit-field flag set in the **Flags** member of the [**D3DDDIARG\_CREATERESOURCE**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddiarg_createresource) structure to create capture buffers. The display miniport driver must also specify the **Capture** bit-field flag for the video memory manager when the memory manager calls the display miniport driver's [**DxgkDdiCreateAllocation**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createallocation) function to create allocations for the capture buffers. When capture buffers are created, they are immediately pinned in memory and are not unpinned until they are released. Because the capture stack must send kernel-mode allocation handles for capture buffers to the capture driver, the runtime calls the user-mode display driver's [**GetCaptureAllocationHandle**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_getcaptureallocationhandle) function to map each resource handle to the kernel-mode allocation handle for that resource.

The capture driver can report whether it supports capturing to system memory directly. If the capture driver supports capturing directly to system memory, MDLs are sent to the capture driver for this purpose. If the capture driver does not support direct capture to system memory, the runtime creates video memory capture buffers, and the capture driver must fill them. The user-mode display driver's [**CaptureToSysMem**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_capturetosysmem) function is called to copy the contents of a capture buffer to a system memory surface. The runtime can use *CaptureToSysMem* rather than the [**Blt**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_blt) function to take advantage of special hardware for bit-block transfers (bitblt) that do not require that the user-mode display driver call the [**pfnRenderCb**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_rendercb) function.

Because AVStream controls video capture, the DirectX graphics kernel subsystem is not aware of when video capture occurs. However, the graphics kernel subsystem is aware of the allocations that are used as capture buffers. When a capture buffer is about to be destroyed, the graphics kernel subsystem calls the display miniport driver's [**DxgkDdiStopCapture**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_stopcapture) function to indicate that the capture operation must immediately stop using an allocation as the capture buffer. If the capture operation has already been stopped through the capture stack, the driver can safely ignore the call.

