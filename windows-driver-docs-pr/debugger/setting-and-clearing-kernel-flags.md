---
title: Setting and Clearing Kernel Flags
description: Setting and Clearing Kernel Flags
keywords: ["GFlags, kernel flags", "GFlags, run-time settings"]
ms.date: 05/23/2017
---

# Setting and Clearing Kernel Flags


## <span id="ddk_setting_and_clearing_kernel_mode_flags_dtools"></span><span id="DDK_SETTING_AND_CLEARING_KERNEL_MODE_FLAGS_DTOOLS"></span>


Kernel flag settings, also known as "run-time settings," affect the entire system. They take effect immediately without rebooting, but they are lost if you shut down or restart the system.

Kernel settings take precedence over registry settings during run time, but when you shut down or restart the system, the kernel flag settings are lost and the registry settings are effective again.

**To set and clear kernel flags**

1.  Click the **Kernel Flags** tab.

    The following screen shot shows the **Kernel Flags** tab in Windows Vista.

    :::image type="content" source="images/gflags-kernel.png" alt-text="Screenshot of the Kernel Flags tab in Windows Vista.":::

2.  Set or clear a flag by selecting or clearing the check box associated with the flag.

3.  When you have selected or cleared all of the flags that you want, click **Apply**.

 

 