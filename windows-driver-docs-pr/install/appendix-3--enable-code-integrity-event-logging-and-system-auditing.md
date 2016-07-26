---
title: Appendix 3 Enable Code Integrity Event Logging and System Auditing
description: .
ms.assetid: D17C64F1-B295-4EC1-B0D0-F1A119D77F64
---

# Appendix 3: Enable Code Integrity Event Logging and System Auditing


## Enable Code Integrity Event Logging and System Auditing


*Excerpt from* [Code Integrity Event Logging and System Auditing](enabling-code-integrity-event-logging-and-system-auditing.md):

Code Integrity is the kernel-mode component that implements driver signature verification. It generates system events that are related to image verification and logs the information in the Code Integrity log:

-   The Code Integrity operational log view shows only image verification error events.

-   The Code Integrity verbose log view shows the events for successful signature verifications.

The following procedure shows how to enable Code Integrity verbose event logging to view all successful operating system loader and kernel-mode image verification events:

## To enable Code Integrity verbose event logging


*Excerpt from* [Enabling the System Event Audit Log](enabling-the-system-event-audit-log.md):

To enable verbose logging, follow these steps:

1.  Open an elevated Command Prompt window.

2.  Run *Eventvwr.exe* on the command line.

3.  Under the **Event Viewer** folder in the left pane of the Event Viewer, expand the following sequence of subfolders:

    1.  **Applications and Services Logs**

    2.  **Microsoft**

    3.  **Windows**

4.  Expand the **Code Integrity** subfolder under the **Windows** folder to display its context menu.

5.  Select **View**.

6.  Select **Show Analytic and Debug Logs**. Event Viewer will then display a subtree that contains an **Operational** folder and a **Verbose** folder.

7.  Right-click **Verbose** and then select **Properties** from the pop-up context menu.

8.  Select the **General** tab on the **Properties** dialog box, and then select the **Enable Logging** option near the middle of the property page. This will enable verbose logging.

9.  Restart the computer for the changes to take effect.

System event records can also be enabled, which include Code Integrity image verification failure events. These events are generated when the Windows kernel fails to load a driver because of a signature failure. Similar events are also recorded in the Code Integrity operational event log view

## To enable the audit policy to generate audit events in the system category for failed operations


To enable security audit policy to capture load failures in the audit logs, follow these steps:

1.  Open an elevated Command Prompt window. To open an elevated Command Prompt window, create a desktop shortcut to *Cmd.exe*, right-click the *Cmd.exe* shortcut, and select **Run as administrator**.

2.  In the elevated Command Prompt window, run the following command:

    ```
    Auditpol /set /Category:System /failure:enable
    ```

3.  Restart the computer for the changes to take effect.

The following screen shot shows an how to use Auditpol to enable security auditing.

![screen shot of command-prompt window illustrating the use of auditpol to enable security auditing](images/tutorialauditpol.jpg)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Appendix%203:%20Enable%20Code%20Integrity%20Event%20Logging%20and%20System%20Auditing%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




