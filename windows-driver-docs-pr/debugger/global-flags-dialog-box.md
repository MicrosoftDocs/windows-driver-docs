---
title: Global Flags Dialog Box
description: Global Flags Dialog Box
ms.assetid: c6987d72-4141-45f2-af06-f4c7040a7e6b
keywords: ["GFlags, dialog box"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Global Flags Dialog Box


## <span id="ddk_global_flags_dialog_box_dtools"></span><span id="DDK_GLOBAL_FLAGS_DIALOG_BOX_DTOOLS"></span>


You can use the **Global Flags** dialog box to set and clear global flags from a user interface that lists all flags by name. There is no need to look up flag abbreviations or hexadecimal values.

Also, the dialog box provides access to the following features that are not available from the command line:

-   **Debugger** − Specifies that a particular program always runs in a debugger.

-   **Launch** − Runs a program with the specified debugging settings.

-   **Kernel Special Pool Tag** − Configures the Special Pool feature.

This topic includes instructions for the following procedures:

[Opening the Dialog Box](opening-the-dialog-box.md)

[Setting and Clearing System-wide Flags](setting-and-clearing-system-wide-flags.md)

[Setting and Clearing Kernel Flags](setting-and-clearing-kernel-flags.md)

[Setting and Clearing Image File Flags](setting-and-clearing-image-file-flags.md)

[Launching a Program with Flags](launching-a-program-with-flags.md)

[Running a Program in a Debugger](running-a-program-in-a-debugger.md)

[Configuring Special Pool](configuring-special-pool.md)

[Configuring Object Reference Tracing](configuring-object-reference-tracing.md)

Pool tagging is permanently enabled on Windows Server 2003 and later versions of Windows. On these systems, the **Enable pool tagging** check box on the **Global Flags** dialog box is dimmed, and commands to enable or disable pool tagging fail.

Use care in interpreting the **Enable page heap** check box for an image file in the **Global Flags** dialog box. This check box indicates that page heap verification is enabled for an image file, but it does not indicate whether it is full or standard page heap verification. If the check results from selecting the check box, then full page heap verification is enabled for the image file. However, if the check results from use of the command-line interface, then the check can represent the enabling of either full or standard page heap verification for the image file.

To determine whether a full or standard page heap verification is enabled for a program, at the command line, type **gflags /p**. In the resulting display, **traces** indicates that standard page heap verification is enabled for the program and **full traces** indicates that full page heap verification is enabled for the program.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Global%20Flags%20Dialog%20Box%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




