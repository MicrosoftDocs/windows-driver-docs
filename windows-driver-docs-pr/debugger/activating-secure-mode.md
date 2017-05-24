---
title: Activating Secure Mode
description: Activating Secure Mode
ms.assetid: bb7cd081-f032-4af4-bb4d-efa96917088b
keywords: ["Secure Mode, how to activate"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Activating Secure Mode


## <span id="ddk_activating_secure_mode_dbg"></span><span id="DDK_ACTIVATING_SECURE_MODE_DBG"></span>


Secure Mode is only available for kernel-mode debugging. It must be activated before the debugging session has begun -- either on the debugger's command line, or when the debugger is completely dormant and is not yet being used as a server.

To activate Secure Mode, use one of the following methods:

-   The **-secure** [command-line option](command-line-options.md)

-   The [**.secure 1**](-secure--activate-secure-mode-.md) command

-   The [**.symopt+0x40000**](-symopt--set-symbol-options-.md) command

If you have an existing kernel debugging session and need to discover whether you are already in Secure Mode, use the [**.secure**](-secure--activate-secure-mode-.md) command with no arguments. This will tell you the current status of Secure Mode.

After Secure Mode has been activated, it cannot be turned off. Even ending the debugging session will not turn it off. Secure Mode persists as long as the debugger itself is running.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Activating%20Secure%20Mode%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




