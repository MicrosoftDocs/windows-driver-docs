---
title: Example 7 Clearing All Flags for an Image File
description: Example 7 Clearing All Flags for an Image File
ms.assetid: 832c79de-07ca-4212-b3b3-ace396986ebb
ms.author: domars
ms.date: 10/12/2018
ms.localizationpriority: medium
---

# Example 7: Clearing All Flags for an Image File


## <span id="ddk_example_7___clearing_all_flags_for_an_image_file_dtools"></span><span id="DDK_EXAMPLE_7___CLEARING_ALL_FLAGS_FOR_AN_IMAGE_FILE_DTOOLS"></span>


The following command clears all flags and image debugger options for an image file. The command adds high-values (0xFFFFFFFF) to the current flag value. GFlags responds by deleting the **GlobalFlag** registry entry for the image file, thereby deleting all of the values it stores.

This command does not affect flags set in the system-wide **GlobalFlag** registry entry or flags set for the session (kernel mode).

```console
gflags /i notepad.exe ffffffff 
```

In response, GFlags displays a message indicating that there are no flags set for the image file:

```console
No Registry Settings for notepad.exe executable 
```

 

 





