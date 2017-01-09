---
title: Take Part in a Remote Debugging Session
description: Take Part in a Remote Debugging Session
MS-HAID:
- 'p\_dashboard.take\_part\_in\_a\_remote\_debugging\_session'
- 'hw\_dashboard.take\_part\_in\_a\_remote\_debugging\_session'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d2f298a4-71f8-49d5-a45b-79e3b094e7cb
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Take%20Part%20in%20a%20Remote%20Debugging%20Session%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





