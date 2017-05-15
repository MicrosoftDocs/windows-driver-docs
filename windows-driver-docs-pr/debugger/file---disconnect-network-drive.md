---
title: File Disconnect Network Drive
description: File Disconnect Network Drive
ms.assetid: 65d78f9b-0c3c-4ec8-906d-afdfa64beebb
keywords: ["File Disconnect Network Drive", "shell commands, File Disconnect Network Drive"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20File%20|%20Disconnect%20Network%20Drive%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




