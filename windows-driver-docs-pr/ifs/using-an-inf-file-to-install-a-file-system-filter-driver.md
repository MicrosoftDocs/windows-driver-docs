---
title: Using an INF File to Install a File System Filter Driver
description: Using an INF File to Install a File System Filter Driver
ms.assetid: 0bc70cdb-d115-4329-9fcc-a085a57c5f78
keywords: ["INF files WDK file system , installation steps"]
---

# Using an INF File to Install a File System Filter Driver


## <span id="ddk_using_an_inf_file_to_install_a_file_system_filter_driver_if"></span><span id="DDK_USING_AN_INF_FILE_TO_INSTALL_A_FILE_SYSTEM_FILTER_DRIVER_IF"></span>


After you have created an INF file, you can use it to install, upgrade, and uninstall your file system filter driver. You can use the INF file alone or together with a batch file or a user-mode setup application.

### <span id="Right-Click_Install"></span><span id="right-click_install"></span><span id="RIGHT-CLICK_INSTALL"></span>Right-Click Install

To execute the [**DefaultInstall**](https://msdn.microsoft.com/library/windows/hardware/ff547356) and [**DefaultInstall.Services**](https://msdn.microsoft.com/library/windows/hardware/ff547360) sections of your INF file, you should do the following:

1.  In Windows Explorer, right-click the INF file name. A shortcut menu will appear.

2.  Click **Install**.

**Note**   The shortcut menu appears only if the INF file contains a **DefaultInstall** section.

 

### <span id="Command-Line_or_Batch_File_Install"></span><span id="command-line_or_batch_file_install"></span><span id="COMMAND-LINE_OR_BATCH_FILE_INSTALL"></span>Command-Line or Batch File Install

To execute the **DefaultInstall** and **DefaultInstall.Services** sections of your INF file on the command line or by using a batch file installation, type the following command at the command prompt, or create and run a batch file that contains this command:

```
RUNDLL32.EXE SETUPAPI.DLL,InstallHinfSection DefaultInstall 132 path-to-inf\infname.inf
```

"Rundll32" and "InstallHinfSection" are described in the Tools and Setup and System Administration sections, respectively, of the Microsoft Windows SDK documentation.

### <span id="Setup_Application"></span><span id="setup_application"></span><span id="SETUP_APPLICATION"></span>Setup Application

[**InstallHinfSection**](https://msdn.microsoft.com/library/windows/desktop/aa376957) can also be called from a setup application, as shown in the following code example:

```
InstallHinfSection(NULL,NULL,TEXT("DefaultInstall 132 path-to-inf\infname.inf"),0); 
```

If you use a setup application to install your driver, observe the following guidelines:

-   To prepare for eventual uninstall, the setup application should copy the driver INF file to an uninstall directory.

-   If the setup application installs a user-mode application with the driver, this application should be listed in Add or Remove Programs in Control Panel so that the user can uninstall it if desired. Only one item should be listed, representing both the application and the driver.

    For more information about how to list your application in Add or Remove Programs, see "Removing an Application" in the Setup and System Administration section of the Windows SDK documentation.

-   Setup applications should never copy driver INF files to the Windows INF file directory (*%windir%\\INF*). SetupAPI copies the files there automatically as part of the [**InstallHinfSection**](https://msdn.microsoft.com/library/windows/desktop/aa376957) call.

For more information about setup applications, see [Writing a Device Installation Application](https://msdn.microsoft.com/library/windows/hardware/ff554015).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Using%20an%20INF%20File%20to%20Install%20a%20File%20System%20Filter%20Driver%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




