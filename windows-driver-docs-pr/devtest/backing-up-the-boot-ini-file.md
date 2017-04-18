---
title: Backing Up the Boot.ini File
description: When you install or upgrade an NT-based Windows operating system prior to Windows Vista, the Windows installer creates a new Boot.ini file for the computer. The new file retains some, but not all, of the changes you might have made to the file.
ms.assetid: c4881f5d-3404-4e87-b130-33bc57b45ec9
keywords: ["Boot.ini files WDK , backing up", "back ups WDK boot options", "back ups WDK boot options , Boot.ini files", "copying boot options", "saving boot options", "boot options WDK , backing up"]
---

# Backing Up the Boot.ini File


\[This topic describes the boot options supported in Windows XP and Windows Server 2003. If you are changing boot options for Windows 8, Windows Server 2012, Windows 7, Windows Server 2008, or Windows Vista, see [Boot Options in Windows Vista and Later](boot-options-in-windows-vista-and-later.md).\]

When you install or upgrade an NT-based Windows operating system prior to Windows Vista, the Windows installer creates a new *Boot.ini* file for the computer. The new file retains some, but not all, of the changes you might have made to the file.

To preserve an edited *Boot.ini* file, make a backup copy before upgrading or installing an operating system.

## <span id="ddk_backing_up_the_boot_ini_file_tools"></span><span id="DDK_BACKING_UP_THE_BOOT_INI_FILE_TOOLS"></span>


After an update completes, you can replace the new file with your backup copy. If you have installed a new operating system, you can copy customized entries from your backup copy and then paste them into the new *Boot.ini* file.

An update or installation restores the default security attributes on the *Boot.ini* file, including the read-only attribute. To edit the file, use the Bootcfg command or change the file attributes. For more information, see [Editing the Boot.ini File](editing-the-boot-ini-file.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Backing%20Up%20the%20Boot.ini%20File%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




