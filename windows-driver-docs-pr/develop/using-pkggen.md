---
title: Installing a Driver on Windows 10 Mobile
description: Describes driver installation on Windows 10 Mobile.
ms.date: 06/02/2017
---

# Installing a driver on Windows 10 Mobile

To install a driver on Windows 10 Mobile, use an .spkg file. An .spkg ("*package file*") is a standalone module that contains your driver package.

WDK 10 includes PkgGen, a tool that generates package files. You run PkgGen in Visual Studio when you build your driver, using the following procedure.

**Using PkgGen to generate a package file**

1.  Select and hold (or right-click) the driver project and choose **Add-&gt;New Item**. Next, under **Visual C++-&gt;Windows Driver**, choose **Package Manifest**. Select **Add**.
2.  Visual Studio adds a file called Package.pkg.xml to your driver project. You can select and hold (or right-click) the file and choose properties to verify that the item type is **PkgGen**. (On this same property page, you can set **Excluded from Build** to **Yes** if you decide later that you want to build this driver project and not generate a package file.) Select **OK**.
3.  Select and hold (or right-click) the driver project and choose **Properties**. Under Configuration Properties, open the PackageGen node and change Version to any value you like.
4.  Save your work and restart Visual Studio as administrator.
5.  Build your driver. Visual Studio links against the required libraries and generates a .cat file, an .inf file, a driver binary, and an .spkg file.

To view the contents of the package file, append a .cab suffix to the file name and then open the cab file in Windows Explorer.

To learn about running PkgGen outside of Visual Studio, see [Creating mobile packages](/previous-versions/windows/hardware/packaging/dn756642(v=vs.85)).

To install a mobile driver package (.spkg file), you have two options.

-   If you are updating an existing package on a target system or adding a new package to the target, use IUTool.exe to install an .spkg driver package.
-   If you are combining packages into a mobile OS image, use ImgGen to add the .spkg driver package to a full flash update (FFU) image that can then be flashed to a mobile device.

**Using IUTool to add a mobile driver package (.spkg) to a running device**

1.  IUTool.exe is in the \\tools\\bin\\*&lt;architecture&gt;* subdirectory of WDK 10.

    Attach your mobile device to the PC. Then, from an elevated command prompt, issue the following command:

       ```cpp
       IUTool -p MyKmdfDriver.spkg
       ```

2.  For more information, see [Adding a driver to a test image](/previous-versions/mt131832(v=vs.85)).

**Using ImgGen to add a driver package (.spkg) to a mobile OS image (.ffu)**

1.  After you install Visual Studio, on the Start screen, select the Visual Studio 2015 folder. Select and hold (or right-click) **Developer Command Prompt for VS2015**, and choose **Run as Administrator**.

## <span id="flashing_a_mobile_os_image__.ffu_"></span><span id="FLASHING_A_MOBILE_OS_IMAGE__.FFU_"></span>Flashing a mobile OS image (.ffu)

To flash the image to the device, either use the Microsoft-supplied FFUTool, or develop custom OEM flashing tools.
