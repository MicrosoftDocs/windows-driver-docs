How to create a custom driver installation script
=======================================================================================================================

If your deployment scenario requires more than installing the driver package on the test computers, you can choose to run your own custom command scripts upon installation.

### <span id="Prerequisites"></span><span id="prerequisites"></span><span id="PREREQUISITES"></span>Prerequisites

-   Driver package that is test signed and ready to install. You must first create and build your driver and then create a driver package for installation. For more information, see [Building a Driver](building_a_driver.md) and [Creating a Driver Package](creating_a_driver_package.md).
-   Test computers that are configured and provisioned for deployment. See [How to test a driver at runtime using Visual Studio](testing_a_driver_at_runtime.md).

Instructions
------------

### <span id="To_run_your_own_custom_command_scripts_upon_installation"></span><span id="to_run_your_own_custom_command_scripts_upon_installation"></span><span id="TO_RUN_YOUR_OWN_CUSTOM_COMMAND_SCRIPTS_UPON_INSTALLATION"></span>Step 1: To run your own custom command scripts upon installation

From the project property pages for your driver package, you can configure whether you want to automatically deploy a driver package on a test computer. You can also run a custom installation script from these pages. You can choose to deploy the driver automatically whenever you build the driver solution in each configuration. For more information about deployment, see [Deploying a Driver to a Test Computer](deploying_a_driver_to_a_test_computer.md) and [Deployment Properties for Driver Projects](deployment_properties_for_driver_projects.md).

1.  Open the property pages for your driver package project. Right-click the driver project in Solution Explorer and select **Properties**.

2.  In the property pages for the driver package, click **Configuration Properties**, click **Driver Settings**, and then click **Deployment**.

3.  Click **Enable deployment** and then select the test computer to use.

4.  Click **Custom Command Line**. In the box, type custom command scripts that you want to run upon installation.

5.  In the **Additional Files** text box, add the command script and other installation files to be copied to the test computer. When the driver is deployed, the additional files are copied to the *%Systemdrive%*\\drivertest\\drivers folder on the remote computer.

<span id="related_topics"></span>Related topics
-----------------------------------------------

* [Deploying a Driver to a Test Computer](deploying_a_driver_to_a_test_computer.md)
* [Deployment Properties for Driver Projects](deployment_properties_for_driver_projects.md)
* [How to test a driver at runtime using Visual Studio](testing_a_driver_at_runtime.md)
* [Building a Driver](building_a_driver.md)
* [Creating a Driver Package](creating_a_driver_package.md)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[VsDriver\vsdriver]:%20How%20to%20create%20a%20custom%20driver%20installation%20script%20%20RELEASE:%20%289/30/2015%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default. "Send comments about this topic to Microsoft")


