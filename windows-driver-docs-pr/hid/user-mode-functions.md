---
title: User-Mode Functions
description: User-Mode Functions
ms.assetid: 1faa04b1-0bf0-494c-b55f-5c90c259c8f5
keywords: ["force feedback drivers WDK HID , user-mode functions", "user-mode functions WDK force feedback"]
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# User-Mode Functions





DirectInput creates an instance of the force-feedback effect driver by creating the object named by the CLSID that is stored in the **OEMForceFeedback** registry subkey of the joystick type subkey.

Because applications using DirectInput need not load OLE, the effect driver should be careful not to rely on OLE-specific behavior. For example, applications using DirectInput cannot be relied upon to call the **CoFreeUnusedLibraries** method. DirectInput performs the standard COM operations to create an instance of the effect driver object. The only visible effect this should have on the implementation of the effect driver is described following.

After DirectInput releases the last effect driver object, it manually performs a FreeLibrary of the effect driver DLL. Consequently, if the effect driver DLL creates additional resources that are not associated with the effect driver object, it should manually LoadLibrary itself to artificially increase its DLL reference count, thereby preventing the FreeLibrary from DirectInput from unloading the DLL prematurely.

In particular, if the effect driver DLL creates a worker thread, the effect driver must perform this artificial LoadLibrary operation for as long as the worker thread exists. When the worker thread is no longer needed (for example, upon notification from the last effect driver object as it is being destroyed), the worker thread should call the FreeLibraryAndExitThread method to decrement the DLL reference count and terminate the thread.

All magnitude and gain values used by DirectInput are uniform and linear across the range. Any nonlinearity in the physical device must be handled by the device driver so that the application sees a linear device.

The user-mode force feedback functions that are exposed by the [IDirectInputEffectDriver](https://msdn.microsoft.com/library/windows/hardware/ff540050)interface must be implemented by a force-feedback effect driver DLL. For more information about these functions, see IDirectInputEffectDriver.

 

 




