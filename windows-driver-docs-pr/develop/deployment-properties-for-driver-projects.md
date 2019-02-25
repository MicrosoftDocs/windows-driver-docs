---
ms.assetid: 7193DA4B-2461-4E00-90B4-C31B93C8E9BD
title: Deployment Properties for Driver Package Projects
description: You can configure the automatic deployment of a driver package on a remote test computer in each configuration of your project.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deployment Properties for Driver Package Projects

You can configure the automatic deployment of a driver package on a remote test computer in each configuration of your project. From the project property pages for your driver, you have additional control over how you want to deploy your driver for testing. You can choose to deploy the driver automatically whenever you build the driver solution in each configuration. For more information about deployment, see [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/Library/Windows/Hardware/Dn745909) and [Deploying a Driver to a Test Computer](deploying-a-driver-to-a-test-computer.md).

## <span id="Setting_deployment_properties_for_driver_package_projects"></span><span id="setting_deployment_properties_for_driver_package_projects"></span><span id="SETTING_DEPLOYMENT_PROPERTIES_FOR_DRIVER_PACKAGE_PROJECTS"></span>Setting deployment properties for driver package projects


1.  Open the property pages for your driver package. Right-click the driver package project in Solution Explorer and select **Properties**.

    **Note**  If your driver solution does not have a driver package project, you need to add one. See [Creating a Driver Package](creating-a-driver-package.md). The deployment properties are only available if you have a driver package.
2.  In the property pages for the driver package, click **Configuration Properties**, click **Driver Install**, and then click **Deployment**.
3.  Select the **Enable deployment** option. When this option is selected, you can select the test computer to use, and you can configure options for driver installation and deployment.

## <span id="Project_Configuration_and_Platform"></span><span id="project_configuration_and_platform"></span><span id="PROJECT_CONFIGURATION_AND_PLATFORM"></span>Project Configuration and Platform


The configuration list and platform list enables you to apply different deployment settings for different project configuration and platform combinations. For example, you can deploy a driver to one test computer using a set of deployment options for debug builds and to a different test computer and deployment options for release builds.

## <span id="Enabling_deployment"></span><span id="enabling_deployment"></span><span id="ENABLING_DEPLOYMENT"></span>Enabling deployment


You can choose to deploy your driver package on a test computer by selecting **Enable deployment**. In combination with the configuration list, you could choose to disable deployment for debug builds and enable it for release builds.

To ensure that you are testing the latest version of the driver, select **Remove previous driver versions before deployment**.

## <span id="Target_computer_name"></span><span id="target_computer_name"></span><span id="TARGET_COMPUTER_NAME"></span>Target computer name


You can choose the target computer to use for deployment and testing. If you have already configured your test computers, you can select one from this list. If you have not configured a test computer, you can configure one using the **Browse** button. For more information about configuring a test computer, see [Deploying a Driver to a Test Computer](deploying-a-driver-to-a-test-computer.md). Make sure that the project configuration and platform match the target architecture of your test system. A common deployment error occurs when you attempt to install an x86 (Win32) driver on a system running an x64 version of Windows. When you configure the test computer, you can also run a kernel-mode debugger. For more information, see [Setting Up Kernel-Mode Debugging in Visual Studio](https://msdn.microsoft.com/windows/hardware/hh439376).

## <span id="Driver_installation_options"></span><span id="driver_installation_options"></span><span id="DRIVER_INSTALLATION_OPTIONS"></span>Driver installation options


**Do not install -** This is the default option. You can choose not to install if you are importing the driver package to the [Driver Store](https://msdn.microsoft.com/Library/Windows/Hardware/Ff544868) or if you are enabling and setting driver verifier options on the test computer.

**Hardware ID Driver Update -** To deploy a driver for an actual hardware device, use **Install and Verify** instead. To deploy a driver for a root-enumerated driver, you can use either **Hardware ID Driver Update** or **Install and Verify**. If you choose to use Hardware ID Driver Update, you must enter the same hardware ID that appears in your INF file, and that hardware ID must have the form Root\\Xxx. If you choose this option, the files are copied to the %*Systemdrive*%\\drivertest\\drivers folder on the remote computer. The Device Console utility, [Devcon](https://msdn.microsoft.com/Library/Windows/Hardware/Ff544707), installs the driver for that hardware ID and INF file from the package. For example, you can select **Hardware ID Driver Update** and set the HWID to **Root\\**<em>yourprojectname</em>. Make sure to exclude any spaces in your project name.

**Custom Command Line -** You can choose to run your own custom command scripts upon installation. If you want to run a custom command script, make sure to add the necessary files under the **Additional Files** section. The additional files are copied to the *%Systemdrive%*\\drivertest\\drivers folder on the remote computer.

**Install and Verify -** You can choose to test your installation using an automated test script. When you select this option and specify the **Default Driver Package Installation Task (possible reboot)** or **Default Printer Driver Package Installation Task (possible reboot)**, the test reads the driver's INF file and installs the driver. The test then verifies that the driver is up and running. Upon completion, the test provides detailed information about the success or failure of the installation task.

**Optional Device Query -** The default value is *%PathToInf%*. The path to the driver's INF files is substituted automatically. There should be no need to change this value unless you have a need to place the INF files in a different location.

## <span id="Additional_Files"></span><span id="additional_files"></span><span id="ADDITIONAL_FILES"></span>Additional Files


You can use the **Additional Files** box to specify custom installation scripts or applications that you want to copy to the remote test computer. The files that you specify here are added to the *%Systemdrive%*\\drivertest\\drivers folder on the remote computer.

## <span id="related_topics"></span>Related topics


* [Deploying a Driver to a Test Computer](deploying-a-driver-to-a-test-computer.md)
* [How to test a driver at runtime using Visual Studio](testing-a-driver-at-runtime.md)
* [Setting Up Kernel-Mode Debugging in Visual Studio](https://msdn.microsoft.com/windows/hardware/hh439376)
 

 






