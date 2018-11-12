---
title: File Attach to a Process
description: File Attach to a Process
ms.assetid: 6bd438a3-e9fb-444d-baf6-fffdee0487f2
keywords: ["File Attach to a Process", "starting the debugger, File Attach to a Process"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# File | Attach to a Process


## <span id="ddk_file_attach_to_a_process_dbg"></span><span id="DDK_FILE_ATTACH_TO_A_PROCESS_DBG"></span>


Click **Attach to a Process** on the **File** menu to debug a user-mode application that is currently running.

This command is equivalent to pressing F6. You can use this command only when WinDbg is in dormant mode.

### <span id="dialog_box"></span><span id="DIALOG_BOX"></span>Dialog Box

When you click **Attach to a Process**, the **Attach to Process** dialog box appears,and you can do the following:

- Select the line that contains the proper process ID and name (or enter the process ID in the **Process ID** box).
    **Note**  Each listed process has an associated plus sign (**+**). You can click the plus sign to display information about that process' command line, services, and child processes.

    **Note**   If WinDbg is connected to a process server, the **Attach to Process** dialog box will display processes that are running on the remote computer. For more information about process servers, see [**Activating a Smart Client**](activating-a-smart-client.md).

- If you want to attach noninvasively to a process, select the **Noninvasive** check box.

After you make your selections, click **OK**.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information and other methods of attaching to a process, see [Debugging a User-Mode Process Using WinDbg](debugging-a-user-mode-process-using-windbg.md) and [Noninvasive Debugging (User Mode)](noninvasive-debugging--user-mode-.md).

 

 





