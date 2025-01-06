---
title: Setting DXGI Information in the Registry
description: Setting DXGI Information in the Registry
ms.date: 12/19/2024
---

# Setting DXGI Information in the Registry

DXGI and the reference rasterizer use the following registry keys under the `HKEY_LOCAL_MACHINE\Software\Microsoft\` subkey to control behavior.

| Name | Type |Description |
| ---- | ---- | ---------- |
| DXGI\\DisableFullscreenWatchdog  | DWORD | Set to 1 to disable the watchdog thread. |
| Direct3D\\ReferenceDevice\\FlushOften | DWORD | Set to 1 to flush often. |
| Direct3D\\ReferenceDevice\\FenceEachEntryPoint | DWORD | Set to 1 to make each call to a DDI function fence with the GPU. Fencing with the GPU means to flush the command batch and block until the GPU is idle. |
| Direct3D\\ReferenceDevice\\Debug  | DWORD | Set to 1 to: a. Flush often and make each call to a DDI function fence with the GPU. b. Run the reference rasterizer (RefRast) single threaded. |
| Direct3D\\ReferenceDevice\\D3D10RefGdiDisplayMask | DWORD | Each bit in the DWORD mask enables (set to 1) or disables (set to 0) the display monitor that the reference device controls. |
| Direct3D\\ReferenceDevice\\SingleThreaded | DWORD | Set to 1 to enable running RefRast single threaded. |
| Direct3D\\ReferenceDevice\\ForceHeapAlloc | DWORD | Set to 1 to make the reference device create resources by using the regular process heap, versus other allocation mechanisms. |
| Direct3D\\ReferenceDevice\\AllowAsync | DWORD | Set to 1 to allow the reference device's second thread to run asynchronously (that is, multiple command buffers are allowed to be outstanding). The reference hardware typically runs in a second thread; however, this second thread completes all its work before the primary thread can continue. |
| Direct3D\\ReferenceDevice\\SimulateInfinitelyFastHW | DWORD | Set to 1 to make the reference device's simulated hardware process only a few limited commands to give the appearance that the reference device is really fast (by essentially doing nothing). The driver can use this key as a performance tool. |
