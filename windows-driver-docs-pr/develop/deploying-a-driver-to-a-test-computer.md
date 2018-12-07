---
ms.assetid: 328404BD-E888-4AAA-AA24-B57FD01E9E54
title: Deploying a Driver to a Test Computer
description: In Visual Studio, the WDK provides a test feature that enables you to build, deploy, and debug a driver on a test computer.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deploying a Driver to a Test Computer

Taking advantage of the Visual Studio development environment, the WDK provides a test feature that enables you to build, deploy, and debug a driver on a test computer. To successfully deploy a driver to a test system using the WDK, you must first set up and configure a test computer. You can set up and configure multiple computers if you want to test your driver under different testing scenarios.

## <span id="Setting_up_the_test_computer"></span><span id="setting_up_the_test_computer"></span><span id="SETTING_UP_THE_TEST_COMPUTER"></span>Setting up the test computer


-   Follow the instructions for [Provision a computer for driver deployment and testing (WDK 10)](https://msdn.microsoft.com/Library/Windows/Hardware/Dn745909).

**Note**  If you run into difficulties setting up the test computer, see [Troubleshooting Configuration of Driver Deployment, Testing and Debugging](troubleshooting-configuration-of-driver-deployment--testing-and-debugging.md).

 

## <span id="Setting_deployment_properties_for_your_driver_solution"></span><span id="setting_deployment_properties_for_your_driver_solution"></span><span id="SETTING_DEPLOYMENT_PROPERTIES_FOR_YOUR_DRIVER_SOLUTION"></span>Setting deployment properties for your driver solution


From the property pages for your driver project, you have additional control over how you want your driver deployed for testing. You can choose to deploy the driver automatically whenever you build the driver solution in each configuration.

1.  Open the property pages for your driver project. Right-click the driver project in Solution Explorer and select **Properties**.
2.  In the property pages for the driver project, click **Configuration Properties**, click **Driver Install**, and then click **Deployment**.
3.  Select a test computer that you have configured, or select the name of a computer that you want to configure for testing. See [Provision a computer for driver deployment and testing (WDK 10)](https://msdn.microsoft.com/Library/Windows/Hardware/Dn745909).

    When you enable deployment for your driver package project, the driver is automatically deployed to the test computer you have selected when you build your solution. You can use the **Deployment** property page to configure options for driver installation and deployment. See [Deployment Properties for Driver Package Projects](deployment-properties-for-driver-projects.md).

4.  When you enable deployment on a test computer, you can also automatically enable and configure [Driver Verifier](https://msdn.microsoft.com/Library/Windows/Hardware/Ff545448), KMDF Verifier, or UMDF Verifier on the test computer to enhance the effectiveness of testing. To set these options for the driver package project, click **Configuration Properties**, click **Driver Install**, and then click the following property pages.
    -   [Driver Verifier Properties for Driver Package Projects](driver-verifier-properties-for--driver-projects.md)
    -   [KMDF Verifier Properties for Driver Package Projects](kmdf-verifier-properties-for-driver-package-projects.md)
    -   [UMDF Verifier Properties for Driver Package Projects](umdf-verifier-properties-for-driver-package-projects.md)

## <span id="Building_a_driver_and_deploying_the_driver_to__test_computer"></span><span id="building_a_driver_and_deploying_the_driver_to__test_computer"></span><span id="BUILDING_A_DRIVER_AND_DEPLOYING_THE_DRIVER_TO__TEST_COMPUTER"></span>Building a driver and deploying the driver to test computer


1.  Before you deploy your driver, make sure that you can build your driver solution. A driver solution must include the driver and driver package so that the driver can be installed on the test computer. For more information, see [Creating a Driver Package](creating-a-driver-package.md) and [Building a Driver](building-a-driver.md).
2.  Before you deploy the driver to the test computer, you also need to sign the driver package. See [Signing a Driver During Development and Testing](signing-a-driver-during-development-and-testing.md).
3.  Select the test computer that you have configured.
4.  To deploy the driver, click **Build Solution** or **Deploy Solution** from the **Build** menu, or press **F5** to build, deploy, and start debugging.
5.  On the test computer, you might see a dialog box asking you to confirm that changes should be made.  In this case, deployment is paused until you confirm.

When you deploy a driver, the driver files are copied to the %Systemdrive%\\drivertest\\drivers folder on the test computer. If something goes wrong during deployment, you can check to see if the files are copied to the test computer. Verify that the .inf, .cat, test cert, and .sys files, and any other necessary files, are present %systemdrive%\\drivertest\\drivers folder.

## <span id="Troubleshooting_driver_deployment_"></span><span id="troubleshooting_driver_deployment_"></span><span id="TROUBLESHOOTING_DRIVER_DEPLOYMENT_"></span>Troubleshooting driver deployment


Here are some tips for troubleshooting driver deployment to a test computer when you use Visual Studio and the WDK.

**Deployment fails due to Error code: 2**

Add the following registry key:

**HKLM\Software\Microsoft\DriverTest\Service**

Under this key, create a DWORD value **DebugSession**, and set it to 0.

You only need to set this value once, and it persists for future deployments.


<span id="Can_t_find_the_deployment_properties_for_the_driver_project"></span><span id="can_t_find_the_deployment_properties_for_the_driver_project"></span><span id="CAN_T_FIND_THE_DEPLOYMENT_PROPERTIES_FOR_THE_DRIVER_PROJECT"></span>**Can't find the deployment properties for the driver project**  
The deployment properties are only available if you have a driver package. If your driver solution does not have a driver package project, you need to add one. The driver package contains components, such as the INF file that are needed for installation. For more information, see [Driver Packages](https://msdn.microsoft.com/Library/Windows/Hardware/Ff544840) and [Creating a Driver Package](creating-a-driver-package.md).

Afer you have added the driver package, you can right-click the driver package project in Solution Explorer and select **Properties**. In the property pages for the driver package, click **Configuration Properties**, click **Driver Install**, and then click **Deployment**.

<span id="Problems_selecting__configuring_or_locating_the_target_computer"></span><span id="problems_selecting__configuring_or_locating_the_target_computer"></span><span id="PROBLEMS_SELECTING__CONFIGURING_OR_LOCATING_THE_TARGET_COMPUTER"></span>**Problems selecting, configuring or locating the target computer**  
For instruction on how to set up the target computer, using Windows Driver Kit (WDK) 8.1 and Windows Driver Kit (WDK) 8, see [Provision a computer for driver deployment and testing (WDK 10)](https://msdn.microsoft.com/Library/Windows/Hardware/Dn745909). If you have problems with provisioning the target computer, see [Troubleshooting Configuration of Driver Deployment, Testing and Debugging](troubleshooting-configuration-of-driver-deployment--testing-and-debugging.md).

If the target computer is running an N or KN version of Windows, you must install the Media Feature Pack for N and KN versions of Windows. See [Provision a computer for driver deployment and testing (WDK 10)](https://msdn.microsoft.com/Library/Windows/Hardware/Dn745909) for more information.

<span id="Problems_installing_the_driver_on_64-bit_version_of_Windows"></span><span id="problems_installing_the_driver_on_64-bit_version_of_windows"></span><span id="PROBLEMS_INSTALLING_THE_DRIVER_ON_64-BIT_VERSION_OF_WINDOWS"></span>**Problems installing the driver on 64-bit version of Windows**  
Starting with Windows Vista, all 64-bit versions of Windows require driver code to have a digital signature for the driver to load. See [Signing a Driver](signing-a-driver.md) and [Signing a Driver During Development and Testing](signing-a-driver-during-development-and-testing.md).

<span id="Problems_installing_the_driver__general_"></span><span id="problems_installing_the_driver__general_"></span><span id="PROBLEMS_INSTALLING_THE_DRIVER__GENERAL_"></span>**Problems installing the driver (general)**  
The WDK can deploy and install a driver package on a test computer, but only if the driver has all the necessary components for installation, such as an INF file. See [Driver Packages](https://msdn.microsoft.com/Library/Windows/Hardware/Ff544840) more information. Make sure you can install the driver outside of Visual Studio and the WDK. For example, use the Device Console utility, [Devcon](https://msdn.microsoft.com/Library/Windows/Hardware/Ff544707) to test whether you can install the driver. Make sure the device (if you have one) is connected to the target computer. For more information, see [Device and Driver Installation](https://msdn.microsoft.com/Library/Windows/Hardware/Ff549731) and [Creating a Driver Package](creating-a-driver-package.md).
