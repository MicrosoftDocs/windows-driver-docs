---
title: Example 13 Listing Image Files with Global Flags
description: Example 13 Listing Image Files with Global Flags
ms.assetid: 1b1285d5-ed73-49c4-a123-de9cbdb3090c
ms.author: domars
ms.date: 10/12/2018
ms.localizationpriority: medium
---

# Example 13: Listing Image Files with Global Flags


## <span id="ddk_example_13___listing_image_files_with_global_flags_dtools"></span><span id="DDK_EXAMPLE_13___LISTING_IMAGE_FILES_WITH_GLOBAL_FLAGS_DTOOLS"></span>


GFlags displays the flags set for a particular image file, but it does not display all image files that have flags set.

Windows stores flags for an image file that the **GlobalFlag** registry entry in a registry subkey named for the image file in the following registry path, **HKEY\_LOCAL\_MACHINE\\ SOFTWARE\\ Microsoft\\ Windows NT\\ CurrentVersion\\ Image File Execution Options\\*ImageFileName*\\GlobalFlag**.

To determine which image files have flags set, use Reg (reg.exe), a tool included in Windows Server 2003.

The following Reg **Query** command searches for the **GlobalFlag** registry entry in the specified registry path. The **-v** parameter specifies the **GlobalFlag** registry entry. The **/s** parameter makes the search recursive.

```console
reg query "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options" /v GlobalFlag /s
```

In response, Reg displays all instances of the **GlobalFlag** registry entry in the path and the value of the entry.

```console
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe
    GlobalFlag    REG_SZ    0x00001000

HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\photohse.EXE
    GlobalFlag    REG_SZ    0x00200000

HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\printhse.EXE
    GlobalFlag    REG_SZ    0x00200000
```

**Tip**   Type the **Reg** command into Notepad, then save the file as imageflags.bat. Thereafter, to find image files for which flags have been set, just type **ImageFlags**.

 

 

 





