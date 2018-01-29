---
title: Launching a Program with Flags
description: Launching a Program with Flags
ms.assetid: 81c0ac6a-3114-4b6a-b154-248801a07f8b
keywords: ["GFlags, launching a program with flags"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Launching a Program with Flags


## <span id="ddk_launching_a_program_with_flags_dtools"></span><span id="DDK_LAUNCHING_A_PROGRAM_WITH_FLAGS_DTOOLS"></span>


This feature runs a program once with the specified flags. These settings affect only the instance of the program launched. They are not saved in the registry.

**To launch a program with flags**

1.  Click the **Image File** tab.

2.  In the **Image** box, type the name of an executable file or DLL, including the file name extension, and any commands for the program, and then press the TAB key.

    This activates the **Launch** button and the check boxes on the **Image File** tab.

3.  Set or clear a flag by selecting or clearing the check box associated with the flag.

4.  Click the **Launch** button.

    The following screen shot shows the **Launch** button on the **Image File** tab in Windows Vista.

    ![screen shot of the image file tab in windows vista ](images/gflags-launch.png)

**Note**   Flags set in the registry do not affect the instance of the program that is launched.
Flags set in the dialog box are used for the launched instance even when they are not image file flags.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Launching%20a%20Program%20with%20Flags%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




