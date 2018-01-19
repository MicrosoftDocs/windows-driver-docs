---
title: Debugging Using KD and NTKD
description: This section describes how to perform basic debugging tasks using the KD and NTKD debuggers.
ms.assetid: 625BE34B-5A3C-4E22-BC2F-5375601E629A
ms.author: domars
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Debugging Using KD and NTKD


This section describes how to perform basic debugging tasks using the KD and NTKD debuggers.

KD and NTKD are identical in every way, except that NTKD spawns a new text window when it is started, whereas KD inherits the Command Prompt window from which it was invoked. The instructions in this section are given for KD, but they work equally well for NTKD. For a discussion of when to use KD or NTKD, see [Debugging Environments](debuggers-in-the-debugging-tools-for-windows-package.md).

Details are given in the following topics:

-   [Opening a Dump File Using KD](opening-a-crash-dump-file-using-kd.md)

-   [Live Kernel-Mode Debugging Using KD](performing-kernel-mode-debugging-using-kd.md)

-   [Ending a Debugging Session in KD](ending-a-debugging-session-in-kd.md)

-   [Setting Symbol and Executable Image Paths in KD](setting-symbol-and-source-paths-in-kd.md)

-   [Setting Breakpoints in KD](setting-breakpoints-in-kd.md)

-   [Viewing the Call Stack in KD](viewing-the-call-stack-in-kd.md)

-   [Viewing and Editing Memory in KD](viewing-memory--variables--and-registers-in-kd.md)

-   [Viewing and Editing Registers in KD](viewing-and-editing-registers-in-kd.md)

-   [Remote Debugging Using KD](remote-debugging-using-kd.md)

-   [Configuring Exceptions and Events in KD](configuring-exceptions-and-events-in-kd.md)

-   [Keeping a Log File in KD](keeping-a-log-file-in-kd.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20KD%20and%20NTKD%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




