---
title: Bypassing Boot Options
description: Bypassing Boot Options
ms.assetid: 7991fed3-943e-4d43-acba-e2462f7e9d03
keywords: ["boot options WDK , bypassing", "F8 key (bypassing boot options) WDK", "bypassing boot options", "kernel debugging support WDK boot options", "Debugging Mode WDK boot options", "skipping boot options"]
---

# Bypassing Boot Options


## <span id="ddk_bypassing_boot_options_dbg"></span><span id="DDK_BYPASSING_BOOT_OPTIONS_DBG"></span>


Under normal circumstances, to debug a program or driver on an NT-bsed operating system prior to Windows Vista, you would create a boot option for debugging, reboot the computer, and then select the debugging option from the boot menu. However, sometimes you are unable to edit the boot options on a computer that needs to be debugged.

For example, you may have a computer that encounters a bug check before the login screen is reached, preventing you from editing the Boot.ini file through Windows. You can start Microsoft MS-DOS from a floppy disk, but if the boot partition of your hard disk is in NTFS format, you will not be able to edit the Boot.ini file from MS-DOS.

If you are unable to edit the boot options directly, restart the computer and wait until the initial BIOS procedures are complete. At this point, if you have multiple operating systems installed, you will see the boot menu. When this menu appears, press the F8 key. If you do not have multiple boot options, you will not see the boot menu, but you can still press the F8 key during the first two seconds of the loading of Windows -- you may find it easiest to just begin pressing F8 repeatedly when the BIOS procedures are nearly complete and keep pressing it until the menu appears.

Pressing F8 will cause the Troubleshooting and Advanced Startup Options menu to appear. One of the choices on this menu is **Debugging Mode**. If you select this option, you will be able to start Windows with kernel debugging support. The kernel debugger connection will be active at a baud rate of 19200 through the highest enumerated COM port (for example, COM2 if you have two ports).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Bypassing%20Boot%20Options%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




