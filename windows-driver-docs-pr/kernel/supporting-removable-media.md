---
title: Supporting Removable Media
author: windows-driver-content
description: Supporting Removable Media
ms.assetid: f70c404c-8a38-4f53-8681-6efb52b30656
keywords: ["removable media WDK kernel", "removable media WDK kernel , about removable-media devices", "IRPs WDK kernel , removable media", "kernel-mode drivers WDK , removable media"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting Removable Media


## <a href="" id="ddk-supporting-removable-media-kg"></a>


File systems and removable-media device drivers share the responsibility for ensuring that the correct media is mounted when a file is opened on a removable-media device and that the correct media remains mounted during operations that access the media. Any intermediate driver layered between a file system and a removable-media device driver also shares this responsibility.

Drivers that work with removable-media devices therefore should be capable of doing one or more of the following:

[Responding to check-verify requests from the file system](responding-to-check-verify-requests-from-the-file-system.md)

[Notifying the file system of possible media changes](notifying-the-file-system-of-possible-media-changes.md)

[Checking flags in the device object](checking-flags-in-the-device-object.md)

[Setting up IRPs in intermediate drivers](setting-up-irps-in-intermediate-drivers.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Supporting%20Removable%20Media%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


