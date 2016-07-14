---
Description: 'In Windows 10 you can write a universal audio driver that will work across many types of hardware.'
MS-HAID: 'audio.audio\_universal\_drivers'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Universal Windows Drivers for Audio
---

# Universal Windows Drivers for Audio


In Windows 10 you can write a universal audio driver that will work across many types of hardware. This topics discusses the benefits of this approach as well as the differences between different platforms. In addition to the Universal Windows drivers for audio, Windows continues to support previous audio driver technologies, such as WDM.

## <span id="Getting_Started_with_Universal_Windows_drivers_for_Audio"></span><span id="getting_started_with_universal_windows_drivers_for_audio"></span><span id="GETTING_STARTED_WITH_UNIVERSAL_WINDOWS_DRIVERS_FOR_AUDIO"></span>Getting Started with Universal Windows drivers for Audio


IHVs can develop a Universal Windows driver that works on all devices (desktops, laptops, tablets, phones). This can reduces development time and cost for initial development and later code maintenance.

These tools are available to develop Universal Windows driver support:

-   Visual Studio 2015 Support: There is a driver setting to set “Target Platform” equal to “Universal”. For more information about setting up the driver development environment, see [Getting Started with Universal Windows Drivers](https://msdn.microsoft.com/windows-drivers/develop/getting_started_with_universal_drivers).

-   APIValidator Tool: You can use the ApiValidator.exe tool to verify that the APIs that your driver calls are valid for a Universal Windows driver. This tool is part of the Windows Driver Kit (WDK) for Windows 10, and runs automatically if you are using Visual Studio 2015 . For more information, see [Validating Universal Windows Drivers](https://msdn.microsoft.com/windows-drivers/develop/validating_universal_drivers).

-   Updated DDI reference documentation: The DDI reference documentation is being updated to indicate which DDIs are supported by Universal Windows drivers. For more information, see [Audio Devices Reference](audio.audio_devices_reference).

## <span id="Create_a_Universal_Audio_Driver"></span><span id="create_a_universal_audio_driver"></span><span id="CREATE_A_UNIVERSAL_AUDIO_DRIVER"></span>Create a Universal Audio Driver


For step-by-step guidance, see [Getting Started with Universal Windows Drivers](https://msdn.microsoft.com/windows-drivers/develop/getting_started_with_universal_drivers). Here is a summary of the steps:

1. Load the universal audio sysvad sample to use as starting point for your universal audio driver. Alternatively, start with the empty WDM driver template and add in code from the universal sysvad sample as needed for your audio driver.

2. In the project properties, set Target Platform to "Universal".

3. Create an installation package: If your target is device running Windows 10 for desktop editions (Home, Pro, Enterprise, and Education), use a configurable INF file. If your target is device running Windows 10 Mobile, use PkgGen to generate an .spkg file.

4. Build, install, deploy, and debug the driver for Windows 10 for desktop editions or Windows 10 Mobile.

## <span id="Sample_Code"></span><span id="sample_code"></span><span id="SAMPLE_CODE"></span>Sample Code


Sysvad and SwapAPO have been converted to be Universal Windows driver samples. For more information, see [Sample Audio Drivers](sample-audio-drivers.md).

## <span id="Available_Programming_Interfaces_for_Universal_Windows_drivers_for_Audio"></span><span id="available_programming_interfaces_for_universal_windows_drivers_for_audio"></span><span id="AVAILABLE_PROGRAMMING_INTERFACES_FOR_UNIVERSAL_WINDOWS_DRIVERS_FOR_AUDIO"></span>Available Programming Interfaces for Universal Windows drivers for Audio


Starting with Windows 10, the driver programming interfaces are part of OneCoreUAP-based editions of Windows. By using that common set, you can write a Universal Windows driver. Those drivers will run on both Windows 10 for desktop editions and Windows 10 Mobile, and other Windows 10 versions.

The following DDIs to are available when working with universal audio drivers.

-   [Audio Drivers Event Sets](audio.audio_drivers_event_sets)

-   [Audio Drivers Interfaces](audio.audio_drivers_interfaces)

-   [Audio Drivers Property Sets](audio.audio_drivers_property_sets)

-   [Audio Drivers Structures](audio.audio_drivers_structures)

-   [Audio Topology Nodes](audio.audio_topology_nodes)

-   [High Definition Audio DDI Reference](audio.high_definition_audio_ddi_reference)

-   [Port Class Audio Driver Reference](audio.port_class_audio_driver_reference)

## <span id="_Convert_an_Existing_Audio_Driver_to_a_Universal_Windows_driver"></span><span id="_convert_an_existing_audio_driver_to_a_universal_windows_driver"></span><span id="_CONVERT_AN_EXISTING_AUDIO_DRIVER_TO_A_UNIVERSAL_WINDOWS_DRIVER"></span> Convert an Existing Audio Driver to a Universal Windows driver


Follow this process to convert an existing audio driver to a Universal Windows driver.

1. Determine whether your existing driver calls will run on OneCoreUAP Windows. Check the requirements section of the reference pages. For more information see [Audio Devices Reference](audio.audio_devices_reference).

2. Recompile your driver as a Universal Windows driver. In the project properties, set Target Platform to "Universal".

3. Use the ApiValidator.exe tool to verify that the DDIs that your driver calls are valid for a Universal Windows driver. This tool is part of the Windows Driver Kit (WDK) for Windows 10, and runs automatically if you are using Visual Studio 2015. For more information, see [Validating Universal Windows Drivers](https://msdn.microsoft.com/windows-drivers/develop/validating_universal_drivers).

4. If the driver calls interfaces that are not part of OneCoreUAP, compiler displays errors.

5. Replace those calls with alternate calls, or create a code workaround, or write a new driver.

## <span id="Building_the_Sysvad_Universal_Audio_Sample_for_Windows_10_Desktop"></span><span id="building_the_sysvad_universal_audio_sample_for_windows_10_desktop"></span><span id="BUILDING_THE_SYSVAD_UNIVERSAL_AUDIO_SAMPLE_FOR_WINDOWS_10_DESKTOP"></span>Building the Sysvad Universal Audio Sample for Windows 10 Desktop


Complete the following steps to build the sysvad sample for Windows 10 desktop.

1. Locate the desktop inf file (tabletaudiosample.inf) and set the manufacturer name to a value such as "Contoso"

2. In Solution Explorer, right-click Solution 'sysvad' , and choose Configuration Manager. If you are deploying to a 64 bit version of Windows, set the target platform to x64. Make sure that the configuration and platform settings are the same for all of the projects.

3. Build the all of the projects in the sysvad solution.

4. Locate the output directory for the build from the build. For example it could be located in a directory like this:

` C:\Program Files (x86)\Windows Kits\10\src\audio\sysvad\x64\Debug\package`
5. Navigate to the Tools folder in your WDK installation and locate the PnpUtil tool. For example, look in the following folder: C:\\Program Files (x86)\\Windows Kits\\10\\Tools\\x64\\PnpUtil.exe .

6. Copy the following files to the system that you want to install the sysvad driver:

|                            |                                                                                   |
|----------------------------|-----------------------------------------------------------------------------------|
| TabletAudioSample.sys      | The driver file.                                                                  |
| tabletaudiosample.inf      | An information (INF) file that contains information needed to install the driver. |
| sysvad.cat                 | The catalog file.                                                                 |
| SwapAPO.dll                | A sample driver extension for a UI to manage APOs.                                |
| PropPageExt.dll            | A sample driver extension for a property page.                                    |
| KeywordDetectorAdapter.dll | A sample keyword detector.                                                        |

 

## <span id="Install_and_test_the_driver"></span><span id="install_and_test_the_driver"></span><span id="INSTALL_AND_TEST_THE_DRIVER"></span>Install and test the driver


Follow these steps to install the driver using the PnpUtil on the target system.

1. Open and Administrator command prompt and type the following in the directory that you copied the driver files to.

**pnputil -i -a tabletaudiosample.inf**

2. The sysvad driver install should complete. If there are any errors you can examine this file for additional information: `%windir%\inf\setupapi.dev.log`

3. In Device Manager, on the View menu, choose Devices by type. In the device tree, locate Microsoft Virtual Audio Device (WDM) - Sysvad Sample. This is typically under the Sound, video and game controllers node.

4. On the target computer, open Control Panel and navigate to **Hardware and Sound** &gt; **Manage audio devices**. In the Sound dialog box, select the speaker icon labeled as Microsoft Virtual Audio Device (WDM) - Sysvad Sample, then click Set Default, but do not click OK. This will keep the Sound dialog box open.

5. Locate an MP3 or other audio file on the target computer and double-click to play it. Then in the Sound dialog box, verify that there is activity in the volume level indicator associated with the Microsoft Virtual Audio Device (WDM) - Sysvad Sample driver.

## <span id="Building_the_Sysvad_Universal_Audio_Sample_for_Windows_10_Mobile"></span><span id="building_the_sysvad_universal_audio_sample_for_windows_10_mobile"></span><span id="BUILDING_THE_SYSVAD_UNIVERSAL_AUDIO_SAMPLE_FOR_WINDOWS_10_MOBILE"></span>Building the Sysvad Universal Audio Sample for Windows 10 Mobile


Complete the following steps to build the sysvad sample for Windows 10 Mobile.

1. Locate the Mobile inf file (phoneaudiosample.inf) and set the manufacturer name to a value such as "Contoso"

2. Build the following projects in the sysvad solution:

-   EndPointsCommon

-   PhoneAudioSample

3. Locate the output directory for the build from the . For example with a default location of Visual Studio in could be located in a directory like this:

` C:\Program Files (x86)\Windows Kits\10\src\audio\sysvad\x64\Debug\package`
4. Follow the guidance in [Creating packages](p_phPackaging.creating_packages) to create a package that contains the driver files for a mobile image.

5. To install a mobile driver package (.spkg file), you will need to combine packages into a mobile OS image. Use ImgGen to add the .spkg driver package to a full flash update (FFU) image that can then be flashed to a mobile device. It may be necessary to remove other audio drivers that exist in the mobile image to allow for testing of the sysvad virtual audio driver.

6. After the OS image contains the driver package is running, play a sound clip and validate that the sysvad phone audio sample is functional. You can establish a kernel debugger connection to monitor the sysvad virtual driver on a mobile device.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Universal%20Windows%20Drivers%20for%20Audio%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



