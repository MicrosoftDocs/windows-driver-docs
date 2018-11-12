---
title: Loading a Theme
description: Loading a Theme
ms.assetid: 375b7365-6526-4282-893e-91b58a14c31f
keywords: ["themes, loading"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Loading a Theme


Before loading a theme, we recommend that you clear all of your workspace data. This can be done in three ways:

By using the WinDbg user-interface. Under the **File** menu, select **Clear Workspace...** Select **Clear All** in the pop-up window and then click **OK**.

By deleting the registry key under **HKCU\\Software\\Microsoft\\Windbg\\Workspaces**.

By running the command **reg delete HKCU\\Software\\Microsoft\\Windbg**.

After all of your workspace data has been cleared, run one of the themes. These are stored as .reg files in the Themes directory of your Debugging Tools for Windows installation. Running a theme imports its settings into the registry, redefining your base workspace.

After you have loaded a theme, you may alter it to more closely suit your preferences. For more details on some common options, see [Customizing a Theme](customizing-a-theme.md).

 

 





