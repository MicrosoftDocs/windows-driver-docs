---
ms.assetid: 9F1E79FF-D38E-484A-8AEB-FC9A105BF709
title: How to create a custom driver installation script
description: If you need to install more than the driver package on a test computer, you can run custom command scripts at installation.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to create a custom driver installation script

If your deployment scenario requires more than installing the driver package on the test computers, you can choose to run your own custom command scripts upon installation.

### <span id="Prerequisites"></span><span id="prerequisites"></span><span id="PREREQUISITES"></span>Prerequisites

-   Driver package that is test signed and ready to install. You must first create and build your driver and then create a driver package for installation. For more information, see [Building a Driver](building-a-driver.md) and [Creating a Driver Package](creating-a-driver-package.md).
-   Test computers that are configured and provisioned for deployment. See [How to test a driver at runtime using Visual Studio](testing-a-driver-at-runtime.md).

Instructions
------------

### <span id="To_run_your_own_custom_command_scripts_upon_installation"></span><span id="to_run_your_own_custom_command_scripts_upon_installation"></span><span id="TO_RUN_YOUR_OWN_CUSTOM_COMMAND_SCRIPTS_UPON_INSTALLATION"></span>Step 1: To run your own custom command scripts upon installation

From the project property pages for your driver package, you can configure whether you want to automatically deploy a driver package on a test computer. You can also run a custom installation script from these pages. You can choose to deploy the driver automatically whenever you build the driver solution in each configuration. For more information about deployment, see [Deploying a Driver to a Test Computer](deploying-a-driver-to-a-test-computer.md) and [Deployment Properties for Driver Projects](deployment-properties-for-driver-projects.md).

1.  Open the property pages for your driver package project. Right-click the driver project in Solution Explorer and select **Properties**.

2.  In the property pages for the driver package, click **Configuration Properties**, click **Driver Settings**, and then click **Deployment**.

3.  Click **Enable deployment** and then select the test computer to use.

4.  Click **Custom Command Line**. In the box, type custom command scripts that you want to run upon installation.

5.  In the **Additional Files** text box, add the command script and other installation files to be copied to the test computer. When the driver is deployed, the additional files are copied to the *%Systemdrive%*\\drivertest\\drivers folder on the remote computer.

## <span id="related_topics"></span>Related topics


* [Deploying a Driver to a Test Computer](deploying-a-driver-to-a-test-computer.md)
* [Deployment Properties for Driver Projects](deployment-properties-for-driver-projects.md)
* [How to test a driver at runtime using Visual Studio](testing-a-driver-at-runtime.md)
* [Building a Driver](building-a-driver.md)
* [Creating a Driver Package](creating-a-driver-package.md)
 

 






