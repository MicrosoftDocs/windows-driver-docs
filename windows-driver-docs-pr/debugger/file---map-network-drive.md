---
title: File Map Network Drive
description: File Map Network Drive
ms.assetid: 55a5523f-5735-4b44-8d98-ded9932e630a
keywords: ["File Map Network Drive", "shell commands, File Map Network Drive"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20File%20|%20Map%20Network%20Drive%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




