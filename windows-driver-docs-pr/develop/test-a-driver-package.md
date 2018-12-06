---
ms.assetid: 5BA0A193-1147-4BAD-A6CA-453856E621A2
title: How to test a driver package
description: You can use Visual Studio to deploy and install a driver package on a test computer, and then verify that the driver is installed and running.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to test a driver package

You can use Visual Studio to deploy and install a driver package on a test computer, and then verify that the driver is installed and running.

### <span id="Prerequisites"></span><span id="prerequisites"></span><span id="PREREQUISITES"></span>Prerequisites

-   A driver package that is ready to install. You must first create and build your driver and then create a driver package for installation. For more information, see [Building a Driver](building-a-driver.md) and [Creating a Driver Package](creating-a-driver-package.md).
-   If you have not already done so, follow the instructions to [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/Library/Windows/Hardware/Dn745909).
-   After you have configured and provisioned a test computer, you can use Visual Studio to deploy drivers, schedule tests, and debug drivers on the test computer. For information about deployment and about how you can deploy a driver automatically at build time, see [Deploying a Driver to a Test Computer](deploying-a-driver-to-a-test-computer.md).

Instructions
------------

### <span id="To_test_the_driver_installation_on_a_test_computer"></span><span id="to_test_the_driver_installation_on_a_test_computer"></span><span id="TO_TEST_THE_DRIVER_INSTALLATION_ON_A_TEST_COMPUTER"></span>Step 1: To test the driver installation on a test computer

After you have configured and provisioned a test computer, you can configure the driver package project so that it is automatically deployed and installed on the test computer.

1.  Open the property pages for your driver project. Right-click the driver project in Solution Explorer and select **Properties**.
2.  In the property pages for the driver, click **Configuration Properties**, click **Driver Install**, and then click **Deployment**.
3.  Select the **Enable deployment** option. For more information, see [Deployment Properties for Driver Projects](deployment-properties-for-driver-projects.md).
4.  Select the test computer you have configured as the **Remote Computer**.
5.  Under **Driver Installation Options**, click **Install and Verify**, and then select the **Default Driver Installation Task**.

## <span id="related_topics"></span>Related topics


* [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/Library/Windows/Hardware/Dn745909)
* [Deploying a Driver to a Test Computer](deploying-a-driver-to-a-test-computer.md)
* [Testing a Driver](testing-a-driver.md)
 

 






