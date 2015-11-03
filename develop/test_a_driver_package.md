How to test a driver package
=============================================================================

You can use Visual Studio to deploy and install a driver package on a test computer, and then verify that the driver is installed and running.

### <span id="Prerequisites"></span><span id="prerequisites"></span><span id="PREREQUISITES"></span>Prerequisites

-   A driver package that is ready to install. You must first create and build your driver and then create a driver package for installation. For more information, see [Building a Driver](building_a_driver.md) and [Creating a Driver Package](creating_a_driver_package.md).
-   If you have not already done so, follow the instructions to [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Dn745909).
-   After you have configured and provisioned a test computer, you can use Visual Studio to deploy drivers, schedule tests, and debug drivers on the test computer. For information about deployment and about how you can deploy a driver automatically at build time, see [Deploying a Driver to a Test Computer](deploying_a_driver_to_a_test_computer.md).

Instructions
------------

### <span id="To_test_the_driver_installation_on_a_test_computer"></span><span id="to_test_the_driver_installation_on_a_test_computer"></span><span id="TO_TEST_THE_DRIVER_INSTALLATION_ON_A_TEST_COMPUTER"></span>Step 1: To test the driver installation on a test computer

After you have configured and provisioned a test computer, you can configure the driver package project so that it is automatically deployed and installed on the test computer.

1.  Open the property pages for your driver project. Right-click the driver project in Solution Explorer and select **Properties**.
2.  In the property pages for the driver, click **Configuration Properties**, click **Driver Install**, and then click **Deployment**.
3.  Select the **Enable deployment** option. For more information, see [Deployment Properties for Driver Projects](deployment_properties_for_driver_projects.md).
4.  Select the test computer you have configured as the **Remote Computer**.
5.  Under **Driver Installation Options**, click **Install and Verify**, and then select the **Default Driver Installation Task**.

<span id="related_topics"></span>Related topics
-----------------------------------------------

* [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Dn745909)
* [Deploying a Driver to a Test Computer](deploying_a_driver_to_a_test_computer.md)
* [Testing a Driver](testing_a_driver.md)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[VsDriver\vsdriver]:%20How%20to%20test%20a%20driver%20package%20%20RELEASE:%20%289/30/2015%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default. "Send comments about this topic to Microsoft")


