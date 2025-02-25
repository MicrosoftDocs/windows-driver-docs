---
title: How to Test a Driver Package
description: You can use Visual Studio to deploy and install a driver package on a test computer, and then verify that the driver is installed and running.
ms.date: 02/20/2025
---

# How to test a driver package

You can use Visual Studio to deploy and install a driver package on a test computer, and then verify that the driver is installed and running.

## Prerequisites

-   A driver package that is ready to install. You must first create and build your driver and then create a driver package for installation. For more information, see [Building a Driver](building-a-driver.md) and [Creating a Driver Package](creating-a-driver-package.md).
-   If you have not already done so, follow the instructions to [Provision a computer for driver deployment and testing (WDK 8.1)](../gettingstarted/provision-a-target-computer-wdk-8-1.md).
-   After you have configured and provisioned a test computer, you can use Visual Studio to deploy drivers, schedule tests, and debug drivers on the test computer. For information about deployment and about how you can deploy a driver automatically at build time, see [Deploying a Driver to a Test Computer](deploying-a-driver-to-a-test-computer.md).

## Test the driver installation on a test computer

After you have configured and provisioned a test computer, you can configure the driver package project so that it is automatically deployed and installed on the test computer.

1.  Open the property pages for your driver project. select and hold (or right-click) the driver project in Solution Explorer and select **Properties**.
2.  In the property pages for the driver, select **Configuration Properties**, select **Driver Install**, and then select **Deployment**.
3.  Select the **Enable deployment** option. For more information, see [Deployment Properties for Driver Projects](deployment-properties-for-driver-projects.md).
4.  Select the test computer you have configured as the **Remote Computer**.
5.  Under **Driver Installation Options**, select **Install and Verify**, and then select the **Default Driver Installation Task**.

## Related topics

* [How to test a driver package (Manual Deployment)](test-a-driver-package-manual-deployment.md)
* [Provision a computer for driver deployment and testing (WDK 8.1)](../gettingstarted/provision-a-target-computer-wdk-8-1.md)
* [Deploying a Driver to a Test Computer](deploying-a-driver-to-a-test-computer.md)
* [Testing a Driver](testing-a-driver.md)

