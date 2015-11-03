Developing, Testing, and Deploying Drivers
==================================================================================================================

Starting with Windows Driver Kit (WDK) 8, the Windows driver development environment and the Windows debuggers are integrated into Microsoft Visual Studio. In this integrated driver development environment, most of the tools you need for coding, building, packaging, deploying, debugging, and testing a driver are available in the Visual Studio user interface. This is a departure from previous releases of the Windows Driver Kit (WDK), where the various stages of the driver life cycle were performed as separate tasks with stand-alone tools.

<iframe 
src="https://hubs-video.ssl.catalog.video.msn.com/embed/9673727b-89ef-4a54-8228-dad41dbd8201/IA?csid=ux-en-us&MsnPlayerLeadsWith=html&PlaybackMode=Inline&MsnPlayerDisplayShareBar=false&MsnPlayerDisplayInfoButton=false&iframe=true&QualityOverride=HD" width="720" height="405" allowFullScreen="true" frameBorder="0" scrolling="no"></iframe> 

To set up the integrated development environment, first install Visual Studio and then install the WDK. You can find information about how to get Visual Studio and the WDK [here](http://go.microsoft.com/fwlink/p/?linkid=239721). [Debugging Tools for Windows](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff551063) is included when you install the WDK. For more information, see [Download and Install Debugging Tools for Windows](http://go.microsoft.com/fwlink/p/?linkid=235427).

WDK 8 uses MSBuild.exe, which is a different build utility from the one used in previous releases. (Previous releases used Build.exe, which was available only in a command-line environment.) MSBuild is available both in the Visual Studio user interface and as a command-line tool. Driver projects created with previous releases of the WDK used Sources (and possibly Dirs) files to describe a project or group of projects. Drivers created with the Visual Studio environment use Project and Solution files instead of Sources and Dirs files. The Visual Studio environment provides a tool for converting Sources and Dirs files to Project and Solution files.

The Visual Studio environment provides templates for:

-   New drivers
-   Driver packages
-   New tests
-   Enhancement of existing tests
-   Custom driver deployment scripts

In the Visual Studio environment, you can configure the build process so that it automatically creates and signs a driver package. Static and run-time analysis tools are available in Visual Studio. You can configure a target computer for testing your driver and automatically deploy your driver to the target computer each time you rebuild. In Visual Studio you can establish a kernel-mode debugging session with a target computer. You can choose from an extensive set of run-time tests, and you can write your own tests.

These topics show you how to use Visual Studio to perform several of the tasks involved in driver development, deployment, and testing.

-   [Getting Started with Universal Windows Drivers](getting_started_with_universal_drivers.md)
-   [Validating Universal Windows Drivers](validating_universal_drivers.md)
-   [Installing a Universal Windows Driver](installing_a_universal_driver.md)
-   [Target platform on MSDN driver reference pages](windows_10_editions_for_universal_drivers.md)
-   [Driver convergence model for Windows 10](driver_model_convergence.md)
-   [Creating a New Device Function Driver](creating_a_new_driver.md)
-   [Creating a New Filter Driver](creating_a_new_filter_driver.md)
-   [Creating a New Software Driver](creating_a_new_software_driver.md)
-   [Creating a Driver From Existing Source Files](creating_a_driver_from_existing_source_files.md)
-   [Building a Driver with the WDK](building_a_driver.md)
-   [Converting WDK 8.1 Projects to WDK 10](converting_wdk_8_1_projects_to_wdk_10.md)
-   [Analyzing a Driver Using Code Analysis and Verification Tools](analyzing_driver_quality_by_using_code_analysis_tools.md)
-   [Preparing a Computer for Manual Driver Deployment](preparing_a_computer_for_manual_driver_deployment.md)
-   [What happens when you provision a computer (WDK 8.1)](what_happens_when_you_provision_a_computer__wdk_8_1_.md)
-   [What happens when you provision a computer (WDK 8.0)](what_happens_when_you_provision_a_computer__wdk_8_0_.md)
-   [Troubleshooting Configuration of Driver Deployment, Testing and Debugging](troubleshooting_configuration_of_driver_deployment__testing_and_debugging.md)
-   [Creating a Driver Package](creating_a_driver_package.md)
-   [Creating a Device Metadata Package](creating_a_device_metadata_package.md)
-   [Signing a Driver](signing_a_driver.md)
-   [Deploying a Driver to a Test Computer](deploying_a_driver_to_a_test_computer.md)
-   [Debugging a Driver](debugging_a_driver.md)
-   [Testing a Driver](testing_a_driver.md)
-   [Creating a driver verification log](creating_a_driver_verification_log.md)
-   [Distributing a driver package](distributing_a_driver_package_win8.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[VsDriver\vsdriver]:%20Developing,%20Testing,%20and%20Deploying%20Drivers%20%20RELEASE:%20%289/30/2015%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default. "Send comments about this topic to Microsoft")


