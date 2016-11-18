---
title: User-Mode Functions
author: windows-driver-content
description: User-Mode Functions
MS-HAID:
- 'di\_d5a0138c-f42f-462a-840a-f43bfd4d1a44.xml'
- 'hid.user\_mode\_functions'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1faa04b1-0bf0-494c-b55f-5c90c259c8f5
keywords: ["force feedback drivers WDK HID , user-mode functions", "user-mode functions WDK force feedback"]
---

# User-Mode Functions


## <a href="" id="ddk-user-mode-functions-di"></a>


DirectInput creates an instance of the force-feedback effect driver by creating the object named by the CLSID that is stored in the **OEMForceFeedback** registry subkey of the joystick type subkey.

Because applications using DirectInput need not load OLE, the effect driver should be careful not to rely on OLE-specific behavior. For example, applications using DirectInput cannot be relied upon to call the **CoFreeUnusedLibraries** method. DirectInput performs the standard COM operations to create an instance of the effect driver object. The only visible effect this should have on the implementation of the effect driver is described following.

After DirectInput releases the last effect driver object, it manually performs a FreeLibrary of the effect driver DLL. Consequently, if the effect driver DLL creates additional resources that are not associated with the effect driver object, it should manually LoadLibrary itself to artificially increase its DLL reference count, thereby preventing the FreeLibrary from DirectInput from unloading the DLL prematurely.

In particular, if the effect driver DLL creates a worker thread, the effect driver must perform this artificial LoadLibrary operation for as long as the worker thread exists. When the worker thread is no longer needed (for example, upon notification from the last effect driver object as it is being destroyed), the worker thread should call the FreeLibraryAndExitThread method to decrement the DLL reference count and terminate the thread.

All magnitude and gain values used by DirectInput are uniform and linear across the range. Any nonlinearity in the physical device must be handled by the device driver so that the application sees a linear device.

The user-mode force feedback functions that are exposed by the [IDirectInputEffectDriver](https://msdn.microsoft.com/library/windows/hardware/ff540050)interface must be implemented by a force-feedback effect driver DLL. For more information about these functions, see IDirectInputEffectDriver.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20User-Mode%20Functions%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


