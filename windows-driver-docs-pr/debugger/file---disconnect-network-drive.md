---
title: File Disconnect Network Drive
description: File Disconnect Network Drive
ms.assetid: 65d78f9b-0c3c-4ec8-906d-afdfa64beebb
keywords: ["File Disconnect Network Drive", "shell commands, File Disconnect Network Drive"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# File | Disconnect Network Drive


## <span id="ddk_file_disconnect_network_drive_dbg"></span><span id="DDK_FILE_DISCONNECT_NETWORK_DRIVE_DBG"></span>


Click **Disconnect Network Drive** on the **File** menu to remove network connections.

### <span id="dialog_box"></span><span id="DIALOG_BOX"></span>Dialog Box

When you click **Disconnect Network Drive**, the **Disconnect Network Drives** dialog box appears. In the **Network Drives** box, select the connection you want to remove and click **OK**.

This dialog box works exactly like the corresponding feature of Windows Explorer.

The **File | Disconnect Network Drive** command affects only the network connections of the computer on which WinDbg is running. If you are using WinDbg as a client in a remote debugging session and you want to change the network connections of the server, you must use a **.shell net use** command.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about accessing the command shell, see [Using Shell Commands](using-shell-commands.md).

 

 





