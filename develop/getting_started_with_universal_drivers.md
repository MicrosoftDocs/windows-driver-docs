Getting Started with Universal Windows drivers
================================================================================================================

<span class="sidebar_heading" style="font-weight: bold;">In this article</span>

-   [Introduction to Universal Windows drivers](#introduction_to_universal_windows_drivers)
-   [Building a Universal Windows driver](#building_a_universal_windows_driver)
-   [Installing a Universal Windows driver](#installing_a_universal_windows_driver)
-   [Flashing a mobile OS image (.ffu)](#flashing_a_mobile_os_image__.ffu_)
-   [Debugging a Universal Windows driver](#debugging_a_universal_windows_driver)
-   [Related topics](#related_topics)

Universal Windows drivers allow developers to create a single driver that runs across multiple different device types, from embedded systems to tablets and desktop PCs. Hardware developers can use their existing components and device drivers across different form factors. Universal Windows drivers run on Windows 10 for desktop editions (Home, Pro, and Enterprise), Windows 10 Mobile, Windows 10 IoT Core, Windows Server 2016 Technical Preview, as well as other Windows 10 editions that share a common set of interfaces.

<span id="Introduction_to_Universal_Windows_drivers"></span><span id="introduction_to_universal_windows_drivers"></span><span id="INTRODUCTION_TO_UNIVERSAL_WINDOWS_DRIVERS"></span>Introduction to Universal Windows drivers
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Windows 10 provides a set of API and DDI interfaces that is common to multiple editions of Windows. This set of interfaces is called the Universal Windows Platform (UWP).

A Universal Windows driver is a kernel-mode or user-mode driver binary that installs and runs on UWP-based editions of Windows 10.

A Universal Windows driver calls only device driver interfaces (DDIs) that are part of UWP. These DDIs are marked as **Universal** on the corresponding MSDN reference pages.

To determine if your existing driver calls any interfaces outside of UWP, recompile your driver as a Universal Windows driver. The compiler displays [ApiValidator errors](validating_universal_drivers.md) if the driver calls interfaces that are not part of UWP. In some cases, you can replace these calls with alternate DDIs that are listed on the MSDN reference pages for the desktop-only DDI. If you cannot find a suitable replacement, please submit [feedback](http://go.microsoft.com/fwlink/p/?linkid=529549).

In other cases, you may have to code a workaround if there is not a suitable replacement. If you need to, write a new Universal Windows driver starting from the driver templates in the unified WDK.

The compiler might also display [INF validation errors](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Dn929320) if you are not [using a universal INF file](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Dn941087).

A Universal Windows driver can use [KMDF](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff557565), [UMDF 2](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Dn384105) or the Windows Driver Model (WDM).

<span id="Building_a_Universal_Windows_driver"></span><span id="building_a_universal_windows_driver"></span><span id="BUILDING_A_UNIVERSAL_WINDOWS_DRIVER"></span>Building a Universal Windows driver
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can use Microsoft Visual Studio 2015 in conjunction with Windows Driver Kit (WDK) 10 to build drivers for desktop, mobile, or universal. You can download kits and tools from the [Windows Hardware Dev Center](http://go.microsoft.com/fwlink/p/?LinkId=524487).

In many cases, you can recompile an existing kernel-mode driver that runs on Windows 8.1 as a Universal Windows driver, as long as the driver does not work with any user-mode components. WDM and KMDF drivers that work with Windows 8.1 should recompile as Universal Windows drivers targeting Windows 10 with no conversion required.

In contrast, existing user-mode drivers may require modification to compile as Universal Windows drivers. Specifically, your driver package must not have any dependencies outside of UWP. For example, only some of the Win32 APIs are part of UWP.

![](common/wedge.gif)**Converting an existing driver project to a Universal Windows driver project**

1.  In Visual Studio 2015, open the existing driver project.
2.  In the Solution Explorer pane, right-click the solution and choose **Configuration Manager**. Set the target operating system to Windows 10.
3.  Right-click the driver project and choose **Properties**. Under Configuration Properties-&gt;Driver, verify that **Target Platform** is set to **Universal**. Other choices include **Desktop**, to build a driver that runs on Windows 10 for desktop editions only, and **Mobile**, to build a driver that runs on Windows 10 Mobile only.
4.  Build the driver. You might see linker errors.
5.  Fix the errors one by one by going through the error log. Refer to individual reference pages in the documentation for possible alternate APIs. If replacements are not available, you may need to redesign your driver.

![](common/wedge.gif)**Creating a New Universal Windows driver Project in Microsoft Visual Studio**

1.  Create a new driver from a template (**File&gt;New Project-&gt;Templates-&gt;Visual C++-&gt;Windows Driver-&gt;WDF**) and choose either **User Mode Driver (UMDF V2)** or **Kernel Mode Driver (KMDF)**.
2.  After you create the project, in the Solution Explorer pane, right-click the solution and choose **Configuration Manager**. Set **Active solution configuration** to the desired target Windows version, and set **Active solution platform** to **Win32** or **x64**. If **ARM** is not listed, choose **&lt;New...&gt;** to build for ARM.

    If you choose Windows 10, the driver model defaults to **Universal**.

    To change driver model manually, right-click the driver project and choose Properties. Under **Configuration Properties-&gt;Driver Settings-&gt;General**, find the **Target Platform** entry. Choose **Universal**, **Desktop**, or **Mobile**. Microsoft Visual Studio uses this setting to determine what libraries to link against.

    **Note**  You cannot build a Universal Windows driver for Windows versions earlier than Windows 10.
3.  You might need to modify the .inf file to specify the provider, specified as an **%***ManufacturerName***%** token that is expanded later in the INF file's [**Strings**](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff547485) section. For example:

    ``` syntax
    Provider="Contoso"
    ```

4.  You can now build the solution. Visual Studio links against the required libraries and generates a .cat file, an .inf file, and a driver binary.

For information about the configuration settings you can use in Visual Studio when building your driver, see [Building a Driver with the WDK](building_a_driver.md).

<span id="Installing_a_Universal_Windows_driver"></span><span id="installing_a_universal_windows_driver"></span><span id="INSTALLING_A_UNIVERSAL_WINDOWS_DRIVER"></span>Installing a Universal Windows driver
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Note**  The SetupAPI component is not part of UWP, so a Universal Windows driver cannot call functions in this API set.

 

If you want to install a Universal Windows driver on a device that is running Windows 10 for desktop editions, you can still use an INF file, with a few caveats. An INF for a Universal Windows driver cannot include any of the following:

-   Coinstallers
-   Class installers
-   RegisterDLL, DelFile, or DelReg directives
-   Non-HKR AddReg directives

For more information, see [Using a Universal INF File](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Dn941087).

If you want to install your Universal Windows driver on Windows 10 Mobile, you can use an .spkg file. An .spkg ("*package file*") is a standalone module that contains your driver package. If you are not deploying to Windows 10 Mobile, you do not need to generate a package file. You can still compile a Universal Windows driver (as defined by the driver source code) without a package file.

WDK 10 includes PkgGen, a tool that generates package files. You run PkgGen in Visual Studio when you build your driver, using the following procedure.

![](common/wedge.gif)**Using PkgGen to generate a package file**

1.  Right-click the driver project and choose **Add-&gt;New Item**. Next, under **Visual C++-&gt;Windows Driver**, choose **Package Manifest**. Click **Add**.
2.  Visual Studio adds a file called Package.pkg.xml to your driver project. You can right-click the file and choose properties to verify that the item type is **PkgGen**. (On this same property page, you can set **Excluded from Build** to **Yes** if you decide later that you want to build this driver project and not generate a package file.) Click **OK**.
3.  Right-click the driver project and choose **Properties**. Under Configuration Properties, open the PackageGen node and change Version to any value you like.
4.  Save your work and restart Visual Studio as administrator.
5.  Build your driver. Visual Studio links against the required libraries and generates a .cat file, an .inf file, a driver binary, and an .spkg file.

To view the contents of the package file, append a .cab suffix to the file name and then open the cab file in Windows Explorer.

To learn about running PkgGen outside of Visual Studio, see [Creating packages](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Dn756642).

To install a mobile driver package (.spkg file), you have two options.

-   If you are updating an existing package on a target system or adding a new package to the target, use IUTool.exe to install an .spkg driver package.
-   If you are combining packages into a mobile OS image, use ImgGen to add the .spkg driver package to a full flash update (FFU) image that can then be flashed to a mobile device.

![](common/wedge.gif)**Using IUTool to add a mobile driver package (.spkg) to a running device**

1.  [IUTool.exe](http://go.microsoft.com/fwlink/p/?linkid=617385) is in the \\tools\\bin\\*&lt;architecture&gt;* subdirectory of WDK 10.

    Attach your mobile device to the PC. Then, from an elevated command prompt, issue the following command:

       ``` syntax
       IUTool -p MyKmdfDriver.spkg
       ```

2.  For more information, see [IUTool.exe: Update packages on a phone](http://go.microsoft.com/fwlink/p/?linkid=617385) and [Adding a driver to a test image](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Mt131832).

![](common/wedge.gif)**Using ImgGen to add a driver package (.spkg) to a mobile OS image (.ffu)**

1.  After you install Visual Studio, on the Start screen, click the Visual Studio 2015 folder. Right-click **Developer Command Prompt for VS2015**, and choose **Run as Administrator**.
2.  For more information about ImgGen, see [Building a phone image using ImgGen.cmd](http://go.microsoft.com/fwlink/p/?linkid=617386).

<span id="Flashing_a_mobile_OS_image__.ffu_"></span><span id="flashing_a_mobile_os_image__.ffu_"></span><span id="FLASHING_A_MOBILE_OS_IMAGE__.FFU_"></span>Flashing a mobile OS image (.ffu)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To flash the image to the device, either use the Microsoft-supplied FFUTool, or develop custom OEM flashing tools. For more information, see [Update packages in an .FFU image file](http://go.microsoft.com/fwlink/p/?linkid=617387).

<span id="Debugging_a_Universal_Windows_driver"></span><span id="debugging_a_universal_windows_driver"></span><span id="DEBUGGING_A_UNIVERSAL_WINDOWS_DRIVER"></span>Debugging a Universal Windows driver
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Starting in Windows 10, you can build your KMDF or UMDF driver so that it gets additional driver debugging information through the [Inflight Trace Recorder](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Dn914610). Universal Windows drivers can take advantage of this feature.

In addition, if you used the Visual Studio KMDF template, your driver uses Windows software trace preprocessor (WPP) to write trace messages. Your driver is an ETW provider with a provider GUID.

To send a trace message from your driver, use this code:

   ``` syntax
   TraceEvents(TRACE_LEVEL_INFORMATION, TRACE_DRIVER, &quot;%!FUNC! Entry&quot;);
   ```
       
You can access the ETW logs either using Tracelog via the [TShell tool](http://go.microsoft.com/fwlink/p/?linkid=617388) on a phone, or by using [!wmitrace](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff561362) in a debugger session.

To use Tracelog on a phone:

1.  Establish a kernel-mode debugging session between a host computer and the phone.
2.  On the host computer, in TShell, enter this command:

       ``` syntax
       exec-device tracelog -addautologger MyLogger05 -guid c:\SteveGuid.txt -level 4 -flag 0xF –kd
       ```
       
3.  Reboot the phone, and watch for trace messages in the debugger.

All existing kernel mode debug transports continue to work on Windows 10 for desktop editions. However, for both user-mode and kernel-mode drivers, you must use a remote debugger session over KDNET to test Windows 10 Mobile. For more info, see [Setting Up Kernel-Mode Debugging over a Network Cable Manually](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh439346) in Visual Studio.

<span id="related_topics"></span>Related topics
-----------------------------------------------

* [Building a Driver with the WDK](building_a_driver.md)
* [Windows 10 Editions for Universal Windows drivers](windows_10_editions_for_universal_drivers.md)
* [Write a Universal Windows driver (UMDF 2) based on a template](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh439659)
* [Write a universal Hello World driver (KMDF)](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh439665)
* [Write a Universal Windows driver (KMDF) based on a template](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh439654)
* [Provision a computer for driver deployment and testing (WDK 10)](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Dn745909)
* [What's new in driver development](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Dn927349)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[VsDriver\vsdriver]:%20Getting%20Started%20with%20Universal%20Windows%20drivers%20%20RELEASE:%20%289/30/2015%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default. "Send comments about this topic to Microsoft")


