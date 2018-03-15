---
title: Take Part in a Remote Debugging Session
description: Take Part in a Remote Debugging Session
ms.assetid: d2f298a4-71f8-49d5-a45b-79e3b094e7cb
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Take Part in a Remote Debugging Session


Applies To: Windows 8.1, Windows 8

The administrator who hosts a remote debugging session using the Windows® Remote Debugging client, and the people who have been invited, all have access to a shared kernel debugger (KD) command window. Whatever your role, you can enter debug commands and view the results.

## <span id="Using_the_shared_KD_window"></span><span id="using_the_shared_kd_window"></span><span id="USING_THE_SHARED_KD_WINDOW"></span>Using the shared KD window


The shared KD window includes a command line in which both host and guests can enter debug commands. The commands are run in the order in which they are received.

For information about all KD commands and meta-commands, see the KD.chm file that is downloaded with the Windows Remote Debugging client.

**To enter a debug command**

1.  Before you start, you may review the list of KD commands in the KD Help file.

2.  In the footer of the KD window, enter the command you want and then press **Enter**.

The name and company of the user issuing the command is displayed in the window, along with the output.

### <span id="Using_KD_commands_in_the_Windows_Remote_Debugging_client_window"></span><span id="using_kd_commands_in_the_windows_remote_debugging_client_window"></span><span id="USING_KD_COMMANDS_IN_THE_WINDOWS_REMOTE_DEBUGGING_CLIENT_WINDOW"></span>Using KD commands in the Windows Remote Debugging client window

Commands in the Windows Remote Debugging client window work similarly to commands in the KD window, with the following exceptions:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Control keys</p></td>
<td><p>Use the same control keys in the Windows Remote Debugging client that you use in KD, with the addition of the Alt key. For example, if you press Ctrl+B in KD, you press Ctrl+Alt+B in the Windows Remote Debugging client window.</p></td>
</tr>
<tr class="even">
<td><p>Command history</p></td>
<td><p>Use the up and down arrow keys on your keyboard to scroll through the KD command history.</p></td>
</tr>
<tr class="odd">
<td><p>Context menu commands</p></td>
<td><p>When you right-click in the output area of the <strong>Command</strong> window, the context menu displays the standard options, such as <strong>Copy</strong>, <strong>Paste</strong>, and <strong>Find</strong>. In addition, you can click <strong>Open/Close Log File</strong> to bring up a dialog box where you can create a file on your local disk to log output data from the <strong>Command</strong> window, append data to an existing log, or close a log.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Prepare for Remote Debugging](https://msdn.microsoft.com/library/windows/hardware/br230785.aspx)

[Host a Remote Debugging Session](https://msdn.microsoft.com/library/windows/hardware/br230799.aspx)

[Join a Remote Debugging Session](https://msdn.microsoft.com/library/windows/hardware/br230787.aspx)

[Known Issues with the Remote Debugging Client](https://msdn.microsoft.com/library/windows/hardware/br230769.aspx)

 

 






