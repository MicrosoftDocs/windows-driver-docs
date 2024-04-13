---
title: What Happens when you Provision a Computer (WDK 8.0)
description: Here we show what happens when you use version 8.0 of the Windows Driver Kit (WDK) to provision a target computer.
ms.date: 04/20/2017
---

# What happens when you provision a computer (WDK 8.0)

Using Microsoft Visual Studio to configure and set up driver deployment and driver testing is called *provisioning a target computer* or *provisioning a test computer*. For information about provisioning with Windows Driver Kit (WDK) 8 , see [Provision a computer for driver deployment and testing (WDK 8)](/previous-versions/hh698272(v=vs.85)). Here we show what happens when you use version 8.0 of the Windows Driver Kit (WDK) to provision a target computer.

**Note**  WDK 8 is not the most current version of the WDK. We recommend that you get the current version of the WDK and provision your target computer according to the [provisioning instructions here](/previous-versions/hh698272(v=vs.85)).

 

## <span id="when_you_provision_a_computer_wdk_8_0"></span><span id="WHEN_YOU_PROVISION_A_COMPUTER_WDK_8_0"></span>When you provision a computer (WDK 8.0)


Provisioning a computer performs the following tasks:

-   Copies installation files to %SystemDrive%\\DriverTest
-   Creates a user named WDKRemoteUser and switches to that user
-   Installs .NET 4.0 if it is not already installed
-   Installs Microsoft Visual C++ Redistributable
-   Installs [Test Authoring and Execution Framework (TAEF)](../taef/index.md) (WDK Client)
-   Installs debuggers
-   Installs [Windows Device Testing Framework](../wdtf/index.md) (WDTF)
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
2.  Select the name of the target computer, and select **Delete computer**.
3.  Select **Remove provisioning and delete computer**. Select **Next**.
4.  When the removal process is complete, select **Finish**.

## <span id="when_you_remove_provisioning__wdk_8.0_"></span><span id="WHEN_YOU_REMOVE_PROVISIONING__WDK_8.0_"></span>When you remove provisioning (WDK 8.0)


When you remove provisioning from the target computer, these items are removed:

-   Visual C++ Redistributable
-   Test Automation Framework
-   Debuggers
-   Windows Driver Testing Framework
-   %SystemDrive%\\DriverTest folder and contents
-   WDKRemoteUser account

Removing provisioning does not change these items:

-   AutoReboot setting
-   Kernel memory crash dump setting
-   Screen saver setting
-   Workstation lock policy
-   ForceGuest setting
-   Power policy
-   RTC Wake timer setting
-   Kernel debugging settings
-   Test signing setting

 

