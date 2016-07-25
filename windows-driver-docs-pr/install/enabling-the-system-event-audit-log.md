---
title: Enabling the System Event Audit Log
description: Enabling the System Event Audit Log
ms.assetid: a4206f06-0c81-407e-80aa-4f6b08cb2a70
keywords: ["verbose logging WDK driver signing", "security audit policy WDK driver signing", "system audit policy WDK driver signing"]
---

# Enabling the System Event Audit Log


This topic includes the following information:

[How to Enable Security Audit Policy](#how-to-enable-security-audit-policy)

[How to Enable Verbose Logging of Code Integrity Diagnostic Events](#how-to-enable-verbose-logging-of-code-integrity-diagnostic-events)

### <a href="" id="how-to-enable-security-audit-policy"></a> How to Enable Security Audit Policy

To enable security audit policy to capture load failures in the audit logs, follow these steps:

1.  Open an elevated Command Prompt window. To open an elevated Command Prompt window, create a desktop shortcut to *Cmd.exe*, right-click the *Cmd.exe* shortcut, and select **Run as administrator**.

2.  In the elevated Command Prompt window, run the following command:

    ```
    Auditpol /set /Category:System /failure:enable
    ```

3.  Restart the computer for the changes to take effect.

The following screen shot shows an how to use Auditpol to enable security auditing.

![screen shot of command-prompt window illustrating the use of auditpol to enable security auditing](images/driver-signing-enable-auditpol.png)

### <a href="" id="how-to-enable-verbose-logging-of-code-integrity-diagnostic-events"></a> How to Enable Verbose Logging of Code Integrity Diagnostic Events

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Enabling%20the%20System%20Event%20Audit%20Log%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




