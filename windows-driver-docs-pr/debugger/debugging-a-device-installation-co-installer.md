---
title: Debugging a Device Installation Co-Installer
description: Debugging a Device Installation Co-Installer
ms.assetid: a5cf3cec-bd61-49a6-b836-6759cd8c7d82
keywords: ["device installation co-installer debugging", "installation co-installer debugging", "co-installer debugging"]
---

# Debugging a Device Installation Co-Installer


## <span id="ddk_debugging_dual_boot_machines_dbg"></span><span id="DDK_DEBUGGING_DUAL_BOOT_MACHINES_DBG"></span>


Some hardware device installation packages include DLL files known as *co-installers*, which assist with installing the device.

You cannot debug a co-installer in the same fashion as other modules. This is because of the unique way in which a co-installer is loaded, and because many installation scenarios occur automatically without providing the developer an opportunity to break into the running process.

You can resolve this issue by programmatically installing the device. Attaching a debugger to the application which installs the device allows access to the co-installer itself. The simplest way to accomplish this is to install or reinstall the device using the [DevCon](http://go.microsoft.com/fwlink/p/?linkid=152915) tool that is included in the Windows Driver Kit (WDK). You can then debug the co-installer with WinDbg.

Use the following procedure to accomplish this task. This procedure assumes you have developed a working driver installation package for your device which uses a co-installer. It also assumes that you have the latest copy of the WDK. For information on developing drivers, driver installation packages, and driver installation co-installers, see the WDK documentation.

**Debugging a Co-installer Using DevCon and WinDbg**

1.  Plug in the hardware device.

2.  Cancel the **New Hardware Found** wizard.

3.  Start WinDbg.

4.  Select **Open Executable** from WinDbg's **File** menu.

5.  In the **Open Executable** dialog box, do the following:
    1.  In the file selection text box, select the DevCon tool (Devcon.exe). For this, browse to the WDK installation folder, then open the subdirectory tools, then open the subdirectory devcon, then open the subdirectory that matches the processor architecture of your machine, and then select Devcon.exe. Click only once on Devcon.exe and do not yet press **Open**.
    2.  In the **Arguments** text box, enter the following text, where *INFFile* is the filename of your Device Installation Information (INF) file, and *HardwareID* is the hardware ID of your device:
        ```
        update INFFile HardwareID 
        ```

    3.  In the **Start directory** text box, enter the path to your device installation package.
    4.  Click **Open**.

6.  The debugging process will begin, and WinDbg will break into the DevCon process before DevCon installs your driver.

7.  Configure the debugger to break into the co-installer process when it is loaded. You can do this by either of the following methods:
    -   In the Debugger Command window, use the [**sxe (Set Exceptions)**](sx--sxd--sxe--sxi--sxn--sxr--sx---set-exceptions-.md) command followed by **ld:** and then the filename of the co-installer, excluding the file extension. There should be no space after the colon For example, if the name of the co-installer is mycoinst.dll, you would use the following command:
        ```
        sxe ld:mycoinst 
        ```

    -   Select **Event Filters** from WinDbg's **Debug** menu. In the **Event Filters** dialog box, select **Load module**. Under **Execution**, select **Enabled.** Under **Continue**, select **Not Handled.** Click the **Argument** button, and then in the text box enter the filename of the co-installer, excluding the file extension (for example, enter "mycoinst" for mycoinst.dll). Click **OK** and then click **Close**.

8.  Resume execution by pressing F5 or entering the **g (Go)** command in the Debugger Command window.

9.  When the co-installer is loaded, execution will break back into the debugger. At this point, you can set any additional breakpoints that you need.

### <span id="limitations_of_this_procedure"></span><span id="LIMITATIONS_OF_THIS_PROCEDURE"></span>Limitations of This Procedure

In certain cases, running a device installation package under DevCon may result in slightly different behavior than that of a PnP installation, because of different security tokens and the like. If you are trying to debug a specific problem in your co-installer, it is possible that this problem will not replicate if DevCon is involved. Therefore, before using this technique, you should use DevCon to install your driver without a debugger attached to verify that this problem exists in both the PnP and the DevCon scenarios.

If the problem vanishes whenever DevCon initiates the installation, then you will have to debug your co-installer without using DevCon. One way of doing this is to use the [TList](tlist.md) tool with the **/m** option to determine which process is loading the co-installer module, and then attaching the debugger to that process.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20a%20Device%20Installation%20Co-Installer%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




