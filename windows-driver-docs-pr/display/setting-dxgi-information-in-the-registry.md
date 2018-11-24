---
title: Setting DXGI Information in the Registry
description: Setting DXGI Information in the Registry
ms.assetid: 2d116c89-02dd-4104-be75-70a00fa5e06a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting DXGI Information in the Registry


DXGI and the reference rasterizer use the following registry keys:

<span id="DWORD_Software_Microsoft_DXGI_DisableFullscreenWatchdog"></span><span id="dword_software_microsoft_dxgi_disablefullscreenwatchdog"></span><span id="DWORD_SOFTWARE_MICROSOFT_DXGI_DISABLEFULLSCREENWATCHDOG"></span>DWORD Software\\Microsoft\\DXGI\\DisableFullscreenWatchdog  
Set to 1 to disable the watchdog thread.

<span id="DWORD_Software_Microsoft_Direct3D_ReferenceDevice_FlushOften"></span><span id="dword_software_microsoft_direct3d_referencedevice_flushoften"></span><span id="DWORD_SOFTWARE_MICROSOFT_DIRECT3D_REFERENCEDEVICE_FLUSHOFTEN"></span>DWORD Software\\Microsoft\\Direct3D\\ReferenceDevice\\FlushOften  
Set to 1 to flush often.

<span id="DWORD_Software_Microsoft_Direct3D_ReferenceDevice_FenceEachEntryPoint"></span><span id="dword_software_microsoft_direct3d_referencedevice_fenceeachentrypoint"></span><span id="DWORD_SOFTWARE_MICROSOFT_DIRECT3D_REFERENCEDEVICE_FENCEEACHENTRYPOINT"></span>DWORD Software\\Microsoft\\Direct3D\\ReferenceDevice\\FenceEachEntryPoint  
Set to 1 to make each call to a DDI function fence with the GPU. Fencing with the GPU means to flush the command batch and block until the GPU is idle.

<span id="DWORD_Software_Microsoft_Direct3D_ReferenceDevice_Debug"></span><span id="dword_software_microsoft_direct3d_referencedevice_debug"></span><span id="DWORD_SOFTWARE_MICROSOFT_DIRECT3D_REFERENCEDEVICE_DEBUG"></span>DWORD Software\\Microsoft\\Direct3D\\ReferenceDevice\\Debug  
Set to 1 to:

-   Flush often and make each call to a DDI function fence with the GPU.

-   Run the reference rasterizer (RefRast) single threaded.

<span id="DWORD_Software_Microsoft_Direct3D_ReferenceDevice_D3D10RefGdiDisplayMask"></span><span id="dword_software_microsoft_direct3d_referencedevice_d3d10refgdidisplaymask"></span><span id="DWORD_SOFTWARE_MICROSOFT_DIRECT3D_REFERENCEDEVICE_D3D10REFGDIDISPLAYMASK"></span>DWORD Software\\Microsoft\\Direct3D\\ReferenceDevice\\D3D10RefGdiDisplayMask  
Each bit in the DWORD mask enables (if set to 1) or disables (if set to 0) the display monitor, which is controlled by the reference device.

<span id="DWORD_Software_Microsoft_Direct3D_ReferenceDevice_SingleThreaded"></span><span id="dword_software_microsoft_direct3d_referencedevice_singlethreaded"></span><span id="DWORD_SOFTWARE_MICROSOFT_DIRECT3D_REFERENCEDEVICE_SINGLETHREADED"></span>DWORD Software\\Microsoft\\Direct3D\\ReferenceDevice\\SingleThreaded  
Set to 1 to enable running RefRast single threaded.

<span id="DWORD_Software_Microsoft_Direct3D_ReferenceDevice_ForceHeapAlloc"></span><span id="dword_software_microsoft_direct3d_referencedevice_forceheapalloc"></span><span id="DWORD_SOFTWARE_MICROSOFT_DIRECT3D_REFERENCEDEVICE_FORCEHEAPALLOC"></span>DWORD Software\\Microsoft\\Direct3D\\ReferenceDevice\\ForceHeapAlloc  
Set to 1 to make the reference device create resources by using the regular process heap, versus other allocation mechanisms.

<span id="DWORD_Software_Microsoft_Direct3D_ReferenceDevice_AllowAsync"></span><span id="dword_software_microsoft_direct3d_referencedevice_allowasync"></span><span id="DWORD_SOFTWARE_MICROSOFT_DIRECT3D_REFERENCEDEVICE_ALLOWASYNC"></span>DWORD Software\\Microsoft\\Direct3D\\ReferenceDevice\\AllowAsync  
Set to 1 to allow the reference device's second thread to run asynchronously (that is, multiple command buffers are allowed to be outstanding).

The reference hardware typically runs in a second thread; however, this second thread completes all its work before the primary thread can continue.

<span id="DWORD_Software_Microsoft_Direct3D_ReferenceDevice_SimulateInfinitelyFastHW"></span><span id="dword_software_microsoft_direct3d_referencedevice_simulateinfinitelyfasthw"></span><span id="DWORD_SOFTWARE_MICROSOFT_DIRECT3D_REFERENCEDEVICE_SIMULATEINFINITELYFASTHW"></span>DWORD Software\\Microsoft\\Direct3D\\ReferenceDevice\\SimulateInfinitelyFastHW  
Set to 1 to make the reference device's simulated hardware process only a few limited commands to give the appearance that the reference device is really fast (by essentially doing nothing).

The driver can use this key as a performance tool.

 

 





