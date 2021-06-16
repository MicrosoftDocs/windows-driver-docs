---
title: Provision a computer for driver deployment and testing (WDK 10)
description: Provisioning a target or test computer is the process of configuring a computer for automatic driver deployment, testing, and debugging. To provision a computer, use Microsoft Visual Studio.
ms.date: 05/08/2020
ms.localizationpriority: medium
---

# Provision a computer for driver deployment and testing (WDK 10)

*Provisioning a target or test computer* is the process of configuring a computer for automatic driver deployment, testing, and debugging. To provision a computer, use Microsoft Visual Studio.

A testing and debugging environment has two computers: the *host computer* and the *target computer*. The target computer is also called the *test computer*. You develop and build your driver in Visual Studio on the host computer. The debugger runs on the host computer and is available in the Visual Studio user interface. When you test and debug a driver, the driver runs on the target computer.

The host and target computers must be able to ping each other by name. This might be easier if both computers are joined to the same workgroup or the same network domain. If your computers are in a workgroup, we recommend that you connect the computers with a router rather than a hub or switch.

> [!TIP]
> For the latest information on the WDK and known issues, see the  [WDK support forum](https://social.msdn.microsoft.com/Forums/en-US/home?forum=wdk).

## Prepare the target computer for provisioning

1. On the target computer, install the operating system that you'll use to run and test your driver.

2. [Install the WDK](../download-the-wdk.md). You do not need to install Visual Studio, however, unless you plan on doing driver development on the target computer.

3. If Secure Boot is enabled on an x86 or x64 target computer, disable it. For information about Unified Extensible Firmware Interface (UEFI) and Secure Boot, see [UEFI Firmware](/previous-versions/windows/it-pro/windows-8.1-and-8/hh824898(v=win.10)).

    If the target computer uses an ARM processor, install the Windows Debug Policy. This can be done only by Microsoft or the manufacturer of the target computer. You do not need to disable Secure Boot.

4. On the target computer, run the WDK Test Target Setup MSI that matches the platform of the target computer. You can find the MSI in the Windows Driver Kit (WDK) installation directory under Remote.

    Example: C:\\Program Files (x86)\\Windows Kits\\10\\Remote\\x64\\WDK Test Target Setup x64-x64\_en-us.msi

5. If the target computer is running an N or KN version of Windows, install the Media Feature Pack for N and KN versions of Windows:

    - [Media Feature Pack for N and KN versions of Windows 10](https://www.microsoft.com/download/details.aspx?id=48231)
    - [Media Feature Pack for N and KN versions of Windows 8.1](https://www.microsoft.com/download/details.aspx?id=40744)
    - [Media Feature Pack for N and KN versions of Windows 8](https://www.microsoft.com/download/details.aspx?id=30685)

6. If your target computer is running Windows Server, find the DriverTest folder that was just created by WDK Test Target Setup MSI. (Example: c:\\DriverTest). Select and hold (or right-click) the **DriverTest** folder, and choose **Properties**. On the **Security** tab, give **Modify** permission to the **Authenticated Users** group.

Verify that the host and target computers can ping each other. Open a Command Prompt window, and enter **ping** *ComputerName*.

If the host and target computers are joined to a workgroup and are on different subnets, you might have to adjust some firewall settings so that the host and target computers can communicate. Follow these steps:

1. On the target computer, in Control Panel, go to **Network and Internet &gt; Network Sharing Center**. Note your active network. This will be **Public network**, **Private network**, or **Domain**.
2. On the target computer, in Control Panel, go to **System and Security &gt; Windows Firewall &gt; Advanced settings &gt; Inbound Rules**.
3. In the list of inbound rules, find all Network Discovery rules for your active network. (For example, find all Network Discovery rules that have a **Profile** of **Private**.) Double click each rule and open the **Scope** tab. Under **Remote IP address**, select **Any IP address**.
4. In the list of inbound rules, locate all File and Printer Sharing rules for your active network. For each of those rules, double click the rule, and open the **Scope** tab. Under **Remote IP address**, select **Any IP address**.

## Provision the target computer

Now you're ready to provision the target computer from the host computer in Visual Studio.

1. On the host computer, in Visual Studio, select the **Extensions** menu, point to **Driver**, point to **Test**, and select **Configure Devices**.

2. In the **Configure Devices** dialog, select **Add new device**.

3. For **Network host name**, enter the name or local IP address of your target computer. Select **Provision device and choose debugger settings**.

    ![screen shot of device configuration dialog box.](images/vs2015-device-configuration.png)

4. Select **Next**.

5. Select a type of debugging connection, and enter the required parameters.

    For more information about setting up debugging over various types of connections, see [Setting Up Kernel-Mode Debugging Manually](../debugger/setting-up-kernel-mode-debugging-in-windbg--cdb--or-ntsd.md) in the CHM or online documentation for [Debugging Tools for Windows](../debugger/index.md).

6. The provisioning process takes several minutes and might automatically reboot the target computer once or twice. When provisioning is complete, select **Finish**.

> [!NOTE]
> Provisioning virtual machines through the WDK's automatic provisioning process is not supported. However, you can test drivers on a VM by setting up the target VM manually as described in the [step by step echo lab](../debugger/debug-universal-drivers---step-by-step-lab--echo-kernel-mode-.md).

## See Also

[Deploying a Driver to a Test Computer](../develop/deploying-a-driver-to-a-test-computer.md)
