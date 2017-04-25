---
title: Kernel-Mode Dump Files
description: Kernel-Mode Dump Files
ms.assetid: f04dc580-0e14-41aa-88a2-e04f4406add8
keywords: ["dump file, kernel mode"]
---

# Kernel-Mode Dump Files


## <span id="ddk_kernel_mode_dump_files_dbg"></span><span id="DDK_KERNEL_MODE_DUMP_FILES_DBG"></span>


When a kernel-mode error occurs, the default behavior of Microsoft Windows is to display the blue screen with bug check data.

However, there are several alternative behaviors that can be selected:

-   A kernel debugger (such as WinDbg or KD) can be contacted.

-   A memory dump file can be written.

-   The system can automatically reboot.

-   A memory dump file can be written, and the system can automatically reboot afterwards.

This section covers how to create and analyze a kernel-mode memory dump file. There are three different varieties of crash dump files. However, it should be remembered that no dump file can ever be as useful and versatile as a live kernel debugger attached to the system that has failed.

This section includes:

[Varieties of Kernel-Mode Dump Files](varieties-of-kernel-mode-dump-files.md)

[Creating a Kernel-Mode Dump File](creating-a-kernel-mode-dump-file.md)

[Analyzing a Kernel-Mode Dump File](analyzing-a-kernel-mode-dump-file.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Kernel-Mode%20Dump%20Files%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




