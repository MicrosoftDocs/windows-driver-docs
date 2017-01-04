---
title: Host a Remote Debugging Session
description: Host a Remote Debugging Session
MS-HAID:
- 'p\_dashboard.host\_a\_remote\_debugging\_session'
- 'hw\_dashboard.host\_a\_remote\_debugging\_session'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b26f4037-e6c9-4510-b4b2-b718b070d201
---

# Host a Remote Debugging Session


Applies To: Windows 8.1, Windows 8

With the appropriate permissions, you can host a remote debugging session using the Windows® Remote Debugging client, and invite other people to take part in the session with you. These invited users are also known as "clients" during the debugging process.

Only the host can review and run debug commands.

## <span id="Before_you_begin"></span><span id="before_you_begin"></span><span id="BEFORE_YOU_BEGIN"></span>Before you begin


In order to host a remote debugging session using the Windows Remote Debugging client, you need:

-   Hosting permissions.

-   The Kernel Debugger (KD) installed on your local computer.

For more information about how to download the Windows Remote Debugger, get host session permissions and the KD, see [Prepare for Remote Debugging](https://msdn.microsoft.com/library/windows/hardware/br230785.aspx).

**To host a remote debugging session**

1.  Sign in to the Windows Remote Debugging client with the Microsoft account that you use to sign in to the dashboard.

2.  Open the **Host Sessions** tab.

3.  On the **Actions** menu, click **Host Session**.

4.  In the **Host Session** dialog box, complete the following:

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Text box</th>
    <th>Enter</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p><strong>Debugger location</strong></p></td>
    <td><p>Point to the location of the kd.exe file on your machine.</p></td>
    </tr>
    <tr class="even">
    <td><p><strong>Arguments</strong></p></td>
    <td><p>Enter an argument command to start a KD process, such as one of the following:</p>
    <ul>
    <li><p>To connect to a KD server started on a TCP port:</p>
    <p><code>–remote tcp:server=&lt;ServerMachineName&gt;,port=&lt;ServerPortNumber&gt;</code></p></li>
    <li><p>To connect to a KD server started with a pipe:</p>
    <p><code>–remote npipe:server=&lt;ServerMachineName&gt;,pipe=&lt;PipeName&gt;</code></p></li>
    </ul>
    <div class="alert">
    <strong>Note</strong>  
    <p>Although you can run the KD tool directly from the Windows Remote Debugging client, we strongly recommend that you start a KD process from the Windows Remote Debugging client to access an open KD session on a remote computer.</p>
    </div>
    <div>
     
    </div></td>
    </tr>
    <tr class="odd">
    <td><p><strong>Session name</strong></p></td>
    <td><p>Create a name for your session that can be easily identified by your clients.</p></td>
    </tr>
    <tr class="even">
    <td><p><strong>Session description</strong></p></td>
    <td><p>If you want, you can enter a description of the session and any notes that can help you with debugging.</p></td>
    </tr>
    </tbody>
    </table>

     

5.  To open a new **Command** window where you can enter and run debug commands, click **OK**.

    The results are available to any client who connects to this session.

## <span id="Invite_a_client_to_a_remote_debugging_session"></span><span id="invite_a_client_to_a_remote_debugging_session"></span><span id="INVITE_A_CLIENT_TO_A_REMOTE_DEBUGGING_SESSION"></span>Invite a client to a remote debugging session


As host, you can invite up to ten clients to a single session.

Before you can invite a client to a session:

-   You must be the host of the session.

-   The client must have permission to join sessions.

-   You must know the dashboard email address for the client.

**To invite a client to a session**

1.  In the Windows Remote Debugging client, on the **Host Sessions** tab, select a session.

2.  On the **Actions** menu, click **Invite Client**.

3.  In the **Invite Client** dialog box, in the **Winqual Email Address** text box, enter the dashboard email address for the client you want to invite, and then click **Find**.

4.  If the client is eligible to join the session, the client's details are added to the dialog box. If the client is not eligible, direct the client to [Prepare for Remote Debugging](https://msdn.microsoft.com/library/windows/hardware/br230785.aspx).

    Continue to add more clients if you want.

5.  Select up to ten clients that you want to invite, and then click **OK**.

An email message with details about the session is sent to each client and to the host.

As a host, you can also invite yourself to a session. This allows you to join the session from a remote location and view the debugging history.

## <span id="Close_or_terminate_a_session"></span><span id="close_or_terminate_a_session"></span><span id="CLOSE_OR_TERMINATE_A_SESSION"></span>Close or terminate a session


As a host, you can either close a session temporarily, or terminate it permanently.

You can't reactivate a session after it has been terminated. A session can be closed temporarily, and then re-opened by either a client or a host.

You may want to close a session temporarily because you want to move to a different computer, or you want to return to the debugging session at a later time. The session will continue to be active.

When you no longer need a session, you can terminate it permanently.

**To close a session**

-   Close the **Command** window.

**To terminate a session**

1.  When you are using a KD process from the Windows Remote Debugging client to access an open KD session on a remote computer, in the Windows Remote Debugging client, on the **Host Sessions** tab, select a session.

2.  On the **Actions** menu, click **Terminate Session**.

This terminates the session in the Windows Remote Debugging client, but the KD session on the remote machine remains active. This allows you to reconnect to the session if necessary.

You or a client can also terminate a session through KD either by using Windows Task Manager or by entering one of the following commands in the **Command** window:

-   **qq**

-   **qqd**

-   **.detach**

-   **^B**

-   **.remote\_exit**

Sessions that are no longer active are marked as terminated and displayed on the **Host Session** tab. Clients can see only those sessions to which they were invited for up to seven days after termination.

**Caution**  
If you choose to connect directly from your Windows Remote Debugging client and local KD to the target computer, and you or a client use one of these methods to terminate a session, all the other clients will be disconnected and you cannot restore the session. To avoid this, we strongly recommend that you connect instead to an open KD session on another computer.

 

## <span id="related_topics"></span>Related topics


[Prepare for Remote Debugging](https://msdn.microsoft.com/library/windows/hardware/br230785.aspx)

[Take Part in a Remote Debugging Session](https://msdn.microsoft.com/library/windows/hardware/br230804.aspx)

[Known Issues with the Remote Debugging Client](https://msdn.microsoft.com/library/windows/hardware/br230769.aspx)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Host%20a%20Remote%20Debugging%20Session%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





