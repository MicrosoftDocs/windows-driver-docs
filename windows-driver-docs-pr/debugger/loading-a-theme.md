---
title: Loading a Theme
description: Loading a Theme
ms.assetid: 375b7365-6526-4282-893e-91b58a14c31f
keywords: ["themes, loading"]
---

# Loading a Theme


Before loading a theme, we recommend that you clear all of your workspace data. This can be done in three ways:

By using the WinDbg user-interface. Under the **File** menu, select **Clear Workspace...** Select **Clear All** in the pop-up window and then click **OK**.

By deleting the registry key under **HKCU\\Software\\Microsoft\\Windbg\\Workspaces**.

By running the command **reg delete HKCU\\Software\\Microsoft\\Windbg**.

After all of your workspace data has been cleared, run one of the themes. These are stored as .reg files in the Themes directory of your Debugging Tools for Windows installation. Running a theme imports its settings into the registry, redefining your base workspace.

After you have loaded a theme, you may alter it to more closely suit your preferences. For more details on some common options, see [Customizing a Theme](customizing-a-theme.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Loading%20a%20Theme%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




