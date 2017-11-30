---
title: Example 13 Listing Image Files with Global Flags
description: Example 13 Listing Image Files with Global Flags
ms.assetid: 1b1285d5-ed73-49c4-a123-de9cbdb3090c
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Example 13: Listing Image Files with Global Flags


## <span id="ddk_example_13___listing_image_files_with_global_flags_dtools"></span><span id="DDK_EXAMPLE_13___LISTING_IMAGE_FILES_WITH_GLOBAL_FLAGS_DTOOLS"></span>


GFlags displays the flags set for a particular image file, but it does not display all image files that have flags set.

Windows stores flags for an image file that the **GlobalFlag** registry entry in a registry subkey named for the image file in the following registry path, **HKEY\_LOCAL\_MACHINE\\ SOFTWARE\\ Microsoft\\ Windows NT\\ CurrentVersion\\ Image File Execution Options\\*ImageFileName*\\GlobalFlag**.

To determine which image files have flags set, use Reg (reg.exe), a tool included in Windows Server 2003.

The following Reg **Query** command searches for the **GlobalFlag** registry entry in the specified registry path. The **-v** parameter specifies the **GlobalFlag** registry entry. The **/s** parameter makes the search recursive.

```
reg query "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options" /v GlobalFlag /s
```

In response, Reg displays all instances of the **GlobalFlag** registry entry in the path and the value of the entry.

```
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe
    GlobalFlag    REG_SZ    0x00001000

HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\photohse.EXE
    GlobalFlag    REG_SZ    0x00200000

HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\printhse.EXE
    GlobalFlag    REG_SZ    0x00200000
```

**Tip**   Type the **Reg** command into Notepad, then save the file as imageflags.bat. Thereafter, to find image files for which flags have been set, just type **ImageFlags**.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Example%2013:%20%20Listing%20Image%20Files%20with%20Global%20Flags%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




