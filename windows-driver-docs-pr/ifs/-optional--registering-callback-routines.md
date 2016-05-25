---
title: \ Optional\ Registering Callback Routines
author: windows-driver-content
description: \ Optional\ Registering Callback Routines
ms.assetid: 59d15b37-e31e-45fc-bdb0-fed6f791839c
keywords: ["registering callback routines", "callback routines WDK file system"]
---

# \[Optional\] Registering Callback Routines


## <span id="ddk_registering_callback_routines_if"></span><span id="DDK_REGISTERING_CALLBACK_ROUTINES_IF"></span>


Filter drivers can call [**IoRegisterFsRegistrationChange**](https://msdn.microsoft.com/library/windows/hardware/ff548499) to register a callback routine to be called whenever a file system driver calls [**IoRegisterFileSystem**](https://msdn.microsoft.com/library/windows/hardware/ff548494) or [**IoUnregisterFileSystem**](https://msdn.microsoft.com/library/windows/hardware/ff548552) to register or unregister itself. Filter drivers register this callback routine so they can see new file systems enter the system and choose whether to attach to them.

**Note**   File system filter drivers must never call [**IoRegisterFileSystem**](https://msdn.microsoft.com/library/windows/hardware/ff548494) or [**IoUnregisterFileSystem**](https://msdn.microsoft.com/library/windows/hardware/ff548552). These routines are only for file systems.

 

Filter drivers that attach to volumes only when explicitly directed (for example, by a user-mode application) should not call [**IoRegisterFsRegistrationChange**](https://msdn.microsoft.com/library/windows/hardware/ff548499). Note, however, that a filter that uses this routine has the ability to attach to any given volume immediately after that volume is mounted. Using this routine does not guarantee that the filter will attach directly to the volume device object. But it does ensure that such a filter attaches before (and thus below) any filter that instead waits for a command from a user-mode application, because filters can attach only at the top of the current file system volume device stack.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20[Optional]%20Registering%20Callback%20Routines%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


