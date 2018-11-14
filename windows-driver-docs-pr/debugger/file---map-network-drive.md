---
title: File Map Network Drive
description: File Map Network Drive
ms.assetid: 55a5523f-5735-4b44-8d98-ded9932e630a
keywords: ["File Map Network Drive", "shell commands, File Map Network Drive"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# File | Map Network Drive


## <span id="ddk_file_map_network_drive_dbg"></span><span id="DDK_FILE_MAP_NETWORK_DRIVE_DBG"></span>


Click **Map Network Drive** on the **File** menu to add network connections and assign drive letters to these connections.

### <span id="dialog_box"></span><span id="DIALOG_BOX"></span>Dialog Box

When you click **Map Network Drive**, the **Map Network Drive** dialog box appears. Use the **Drive** and **Folder** menus to choose a server and share and assign a drive letter to it.

This dialog box works exactly like the corresponding feature of Windows Explorer.

The **File | Map Network Drive** command affects only the network connections of the computer on which WinDbg is running. If you are using WinDbg as a client in a remote debugging session and you want to change the network connections of the server, you must use a **.shell net use** command.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about accessing the command shell, see [Using Shell Commands](using-shell-commands.md).

 

 





