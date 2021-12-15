---
title: EvtIddCxMonitorAssignSwapChain error handling
description: Error handling associated with EvtIddCxMonitorAssignSwapChain
ms.date: 09/28/2020
keywords:
- EvtIddCxMonitorAssignSwapChain, error handling
- EvtIddCxMonitorAssignSwapChain error handling, indirect display driver
- EvtIddCxMonitorAssignSwapChain error handling, IDD
---

# EvtIddCxMonitorAssignSwapChain error handling

## Change in EvtIddCxMonitorAssignSwapChain error handling

In Windows 10 releases before version 1903, the rest of the desktop composition was unaware if [**EvtIddCxMonitorAssignSwapChain**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_assign_swapchain) failed. It continued to render and present frames that the indirect display adapter did not process, resulting in IddCx terminating the indirect display driver (IDD) after some time.

Starting with Windows 10, version 1903, IddCx error handling for this callback changed for all driver versions, and introduced the **STATUS_GRAPHICS_INDIRECT_DISPLAY_ABANDON_SWAPCHAIN** status code. See [**EvtIddCxMonitorAssignSwapChain**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_assign_swapchain) for details.

## Handling errors in the frame processing loop-thread

Once the IDD successfully returns from [**EvtIddCxMonitorAssignSwapChain**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_assign_swapchain) it owns the **hSwapChain** object.
If the driver encounters an error that prevents it from continuing to process the frame, it can call [**WdfObjectDelete**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete) to release ownership. The OS will detect the deletion and cause a new swapchain to be created.

If the driver knows it cannot recover from this error it should call [**IddCxReportCriticalError**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxreportcriticalerror) to stop the device.

## Suggested approach to handle swapchain errors

There are several reasons for failure within the [**EvtIddCxMonitorAssignSwapChain**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_assign_swapchain) callback or while processing frames. Failure categorizations include:

* Transient issues specific to your solution, such as a temporary issue with the hardware. This type of issue can be fixed with lightweight recovery mechanisms that will not impact the user experience because recovery happens quickly (typically well under a second in time) and will not affect the visual content on screen (for example, no flickers).  
* Permanent issues specific to your solution, such as a deadlock in the driver or a serious issue with the hardware. This type of issue typically cannot be recovered from quickly if at all.
* DirectX API errors caused by events external to your driver. For example, your driver has no control over events such as when the adapter on which your D3D device is to process the desktop image was PnpStopped or there was a GPU-wide fault and it was reset.
* DirectX API errors caused by your driver. Driver bugs can cause the D3D device to be put in error or hang. For example, calling **CopySubResource** with co-ordinates outside of the bound of the texture will put the device into an error state.
* DirectX API errors caused by another IHV GPU driver. These errors might be a result of correct calling patterns in the IDD that trigger IHV GPU driver bugs.

It is difficult for a driver to accurately distinguish between the different DirectX errors. The main difference is that errors caused by external DirectX components are likely to be transient and the system will recover into a stable state; whereas, if the error is caused by the indirect display or GPU driver, bugs are likely to occur again.

See [**EvtIddCxMonitorAssignSwapChain**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_assign_swapchain) for more information on how to propagate these errors back to the OS such that the OS will retry.

Below is some guidance on how to deal with each type of error in your driver.

### Transient issues specific to your solution

The driver should fix the issue while processing the frame. This action might result in a small delay in processing the frame. If the error happens regularly then the driver could consider preempting the error to a permanent issue.

### Permanent issues specific to your solution

The driver should call [**IddCxReportCriticalError**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxreportcriticalerror) using a major code equal to or above 0x100 and using unique major/minor codes to represent the type of error to help customer/telemetry investigations.

### DirectX error

The simplest way to handle DirectX errors is to propagate them back to the OS so that it will retry again. The driver should return **STATUS_GRAPHICS_INDIRECT_DISPLAY_ABANDON_SWAPCHAIN** from [**EvtIddCxMonitorAssignSwapChain**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_assign_swapchain), or, if the error occurs while processing a frame, the driver should release the swapchain by calling [**WdfObjectDelete**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete).

This simple approach handles errors triggered by external events, as the OS will stabilize and create a new swapchain (possibly on a new Dxgi adapter). If the driver’s use of DirectX is limited, then this approach works well.

For more complex drivers that might hit DirectX errors caused by bugs in the IDD or for drivers running on old/buggy DirectX drivers, this approach could end in an endless loop of ID swapchain failures. To avoid an endless loop, the IDD could monitor the frequency of these errors and move through stages of recovery when a given stage has hit enough error cycles. If DirectX errors are encountered, it is important that the driver destroy that DX device and create a new one, because once a DX device
is in a error state it will never recover and needs to be recreated.

| Current stage | Driver action if it detects too many consecutive swapchain DirectX errors |
| ------------- | ------------------------------------------------------------------------- |
| Render adapter LUID provided in [**EvtIddCxMonitorAssignSwapChain**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_assign_swapchain) is a hardware adapter | Use Dxgi to find the LUID of the software adapter and call [**IddCxAdapterSetRenderAdapter**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxadaptersetrenderadapter) to request that the OS use the software adapter for rendering the desktop. |
| Render adapter LUID provided in **EvtIddCxMonitorAssignSwapChain** is a software  adapter | The driver should call [**IddCxReportCriticalError**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxreportcriticalerror) using a major code equal or above 0x100 and using unique major/minor codes to represent the type of error to help customer/telemetry investigations |

For example, the driver could consider five consecutive DirectX failures in [**EvtIddCxMonitorAssignSwapChain**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_assign_swapchain) or five failures while processing frames with 1 minute as criteria to take the recovery action for the current stage in table above.
