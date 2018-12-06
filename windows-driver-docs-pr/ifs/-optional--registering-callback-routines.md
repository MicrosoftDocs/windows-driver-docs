---
title: '[Optional] Registering Callback Routines'
description: '[Optional] Registering Callback Routines'
ms.assetid: 59d15b37-e31e-45fc-bdb0-fed6f791839c
keywords:
- registering callback routines
- callback routines WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# \[Optional\] Registering Callback Routines


## <span id="ddk_registering_callback_routines_if"></span><span id="DDK_REGISTERING_CALLBACK_ROUTINES_IF"></span>


Filter drivers can call [**IoRegisterFsRegistrationChange**](https://msdn.microsoft.com/library/windows/hardware/ff548499) to register a callback routine to be called whenever a file system driver calls [**IoRegisterFileSystem**](https://msdn.microsoft.com/library/windows/hardware/ff548494) or [**IoUnregisterFileSystem**](https://msdn.microsoft.com/library/windows/hardware/ff548552) to register or unregister itself. Filter drivers register this callback routine so they can see new file systems enter the system and choose whether to attach to them.

**Note**   File system filter drivers must never call [**IoRegisterFileSystem**](https://msdn.microsoft.com/library/windows/hardware/ff548494) or [**IoUnregisterFileSystem**](https://msdn.microsoft.com/library/windows/hardware/ff548552). These routines are only for file systems.

 

Filter drivers that attach to volumes only when explicitly directed (for example, by a user-mode application) should not call [**IoRegisterFsRegistrationChange**](https://msdn.microsoft.com/library/windows/hardware/ff548499). Note, however, that a filter that uses this routine has the ability to attach to any given volume immediately after that volume is mounted. Using this routine does not guarantee that the filter will attach directly to the volume device object. But it does ensure that such a filter attaches before (and thus below) any filter that instead waits for a command from a user-mode application, because filters can attach only at the top of the current file system volume device stack.

 

 




