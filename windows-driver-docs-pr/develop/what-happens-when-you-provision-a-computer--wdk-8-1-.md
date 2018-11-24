---
ms.assetid: 92F58B13-3447-4715-A6D2-69E63FE04A77
title: What happens when you provision a computer (WDK 8.1)
description: Here we show what happens when you use version 8.1 of the Windows Driver Kit (WDK) to provision a target computer.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# What happens when you provision a computer (WDK 8.1)

Using Microsoft Visual Studio to configure and set up driver deployment and driver testing is called *provisioning a target computer* or *provisioning a test computer*. For information about provisioning, see [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/Library/Windows/Hardware/Dn745909). Here we show what happens when you use version 8.1 of the Windows Driver Kit (WDK) to provision a target computer.

## <span id="when_you_provision_a_computer_wdk_8_0"></span><span id="WHEN_YOU_PROVISION_A_COMPUTER_WDK_8_0"></span>When you provision a computer (WDK 8.1)


Provisioning a computer performs the following tasks:

-   Copies installation files to %SystemDrive%\\DriverTest
-   Creates a user named WDKRemoteUser and switches to that user
-   Installs .NET 4.0 if it is not already installed
-   Installs Microsoft Visual C++ Redistributable
-   Installs [Test Authoring and Execution Framework (TAEF)](https://msdn.microsoft.com/Library/Windows/Hardware/Hh439725) (WDK Client)
-   Installs debuggers
-   Installs [Windows Device Testing Framework](https://msdn.microsoft.com/Library/Windows/Hardware/Ff539547) (WDTF)
-   Turns off AutoReboot
-   Enables kernel memory crash dumps
-   Disables Screen Saver
-   Disables workstation lock policy
-   Disables ForceGuest
-   Sets the power policy to a high power configuration, which prevents the system from entering Standby or Hibernate Mode when idle
-   Enables the RTC Wake timer
-   Enables and configures kernel debugging
-   Enables test signing of drivers
-   Reboots the target computer if necessary
-   Creates a system restore point

## <span id="Removing_provisioning_from_the_target_computer"></span><span id="removing_provisioning_from_the_target_computer"></span><span id="REMOVING_PROVISIONING_FROM_THE_TARGET_COMPUTER"></span>Removing provisioning from the target computer


Once you have provisioned a target computer, you cannot completely remove the provisioning. However, you can remove most of the provisioning from the target computer by using Visual Studio on the host computer. Here are the steps.

1.  On the host computer, in Visual Studio, on the **Driver** menu, choose **Test &gt; Configure Computers**.
2.  Select the name of the target computer, and click **Delete computer**.
3.  Select **Remove provisioning and delete computer**. Click **Next**.
4.  When the removal process is complete, click **Finish**.
5.  Uninstall WDK Test Target Setup from the target computer.

## <span id="when_you_remove_provisioning__wdk_8.1_"></span><span id="WHEN_YOU_REMOVE_PROVISIONING__WDK_8.1_"></span>When you remove provisioning (WDK 8.1)


When you remove provisioning from the target computer, these items are removed:

-   Test Automation Framework
-   Debuggers
-   Windows Driver Testing Framework
-   %SystemDrive%\\DriverTest folder and contents
-   WDKRemoteUser account
-   Workstation lock policy

Removing provisioning does not change these items:

-   Visual C++ Redistributable
-   AutoReboot setting
-   Kernel memory crash dump setting
-   Screen saver setting
-   ForceGuest setting
-   Power policy
-   RTC Wake timer setting
-   Kernel debugging settings
-   Test signing setting

 

 





