---
title: Finding a Kernel-Mode Memory Leak
description: Finding a Kernel-Mode Memory Leak
ms.assetid: 7e707b89-8614-46d7-9c2e-bea2ddf16164
keywords: ["memory leak, kernel-mode", "memory leak, kernel-mode, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Finding a Kernel-Mode Memory Leak


Use the following techniques to determine the cause of a kernel-mode memory leak:

[Using PoolMon to Find a Kernel-Mode Memory Leak](using-poolmon-to-find-a-kernel-mode-memory-leak.md)

[Using the Kernel Debugger to Find a Kernel-Mode Memory Leak](using-the-kernel-debugger-to-find-a-kernel-mode-memory-leak.md)

[Using Driver Verifier to Find a Kernel-Mode Memory Leak](using-driver-verifier-to-find-a-kernel-mode-memory-leak.md)

If you do not know which kernel-mode driver or component is responsible for the leak, you should use the PoolMon technique first. This technique reveals the pool tag associated with the memory leak; the driver or component that uses this pool tag is responsible for the leak.

If you have already identified the responsible driver or component, use the second and third techniques in the preceding list to determine the cause of the leak more specifically.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Finding%20a%20Kernel-Mode%20Memory%20Leak%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




