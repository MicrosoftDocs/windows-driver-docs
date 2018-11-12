---
title: Example 2 Setting a Flag by Using a Flag Abbreviation
description: Example 2 Setting a Flag by Using a Flag Abbreviation
ms.assetid: 3c011ca5-8901-4bf2-b95d-364d644cb476
ms.author: domars
ms.date: 10/12/2018
ms.localizationpriority: medium
---

# Example 2: Setting a Flag by Using a Flag Abbreviation


## <span id="ddk_example_2___setting_a_flag_by_using_a_flag_abbreviation_dtools"></span><span id="DDK_EXAMPLE_2___SETTING_A_FLAG_BY_USING_A_FLAG_ABBREVIATION_DTOOLS"></span>


The following command sets the [Show loader snaps](show-loader-snaps.md) flag for the notepad.exe image file. **Show Loader Snaps** takes snapshots of the load process, capturing in detail the loading and unloading of executable images and their supporting library modules.

The command uses the **/i** parameter to indicate image file mode and specifies the name of the image file notepad.exe. To identify the flag, the command uses **sls**, the abbreviation for **Show Loader Snaps**, and it precedes the abbreviation with a plus sign (+) to indicate that the flag is set. Without the plus sign, the command has no effect.

```console
gflags /i notepad.exe +sls 
```

In response, GFlags displays the flags set for notepad.exe. The display indicates that the command is successful. The **Show Loader Snaps** feature is enabled for all new sessions of the Notepad program.

```console
Current Registry Settings for notepad.exe executable are: 00000002
    sls - Show Loader Snaps
```

 

 





