---
title: Verifying the Creation of a Kernel-Mode Dump File
description: Verifying the Creation of a Kernel-Mode Dump File
ms.assetid: ea1dc18d-8974-4de8-accd-1cbc515d71d0
keywords: ["dump file, verifying kernel-mode dump creation"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Verifying the Creation of a Kernel-Mode Dump File


## <span id="ddk_verifying_the_creation_of_a_kernel_mode_dump_file_dbg"></span><span id="DDK_VERIFYING_THE_CREATION_OF_A_KERNEL_MODE_DUMP_FILE_DBG"></span>


If you have a machine that has broken into the debugger, but you are unsure whether the crash dump file was successfully written, execute the following command:

```
dd nt!IopFinalCrashDumpStatus L1
```

This displays the value of the **IopFinalCrashDumpStatus** variable.

If this value equals zero, the process was successful. If it equals -1 (0xFFFFFFFF), the dump process has not started.

Any other value is a status code indicating an error during the dump process.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Verifying%20the%20Creation%20of%20a%20Kernel-Mode%20Dump%20File%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




