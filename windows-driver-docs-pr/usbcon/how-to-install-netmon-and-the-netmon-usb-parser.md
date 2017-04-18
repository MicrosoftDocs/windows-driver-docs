---
Description: This topic provides installation information about Netmon and the USB ETW parsers.
title: How to install Netmon and USB ETW Parsers
author: windows-driver-content
---

# How to install Netmon and USB ETW Parsers


This topic provides installation information about Netmon and the USB ETW parsers.

Install Netmon from the Microsoft Download Center, and then install USB ETW parsers from [Windows Driver Kit (WDK)](http://msdn.microsoft.com/windows/hardware/hh852362.aspx). The USB ETW parsers are supported in Netmon Version 3.3 and later versions.

Instructions
------------

### []()

**To install the Netmon tool and the Netmon USB parser**

1.  Determine whether your machine is running 32-bit Windows or 64-bit Windows:

    1.  Open the **Start** menu, right-click **Computer** and view **Properties**.
    2.  Look at the **System type** field.

    If your system type is 32-bit Operating System, you will use the x86 download. If your system type is 64-bit Operating System and your processor is Itanium, you will use the ia64 download. For other processor types, use the x64 or AMD64 download.

2.  Install Netmon:
    1.  On the [Windows Network Monitor](http://go.microsoft.com/fwlink/p/?linkid=103158) page in the Microsoft Download Center and read the description of the tool.
    2.  Under **Files in this Download** section toward the bottom of the page, click the **Download** button for your system type.
    3.  Download and run the .exe file to start the Setup Wizard.
    4.  Select **Typical** when you are asked to choose the setup type.

3.  Install the WDK from [Windows Driver Kit 8](http://msdn.microsoft.com/windows/hardware/hh852362.aspx).
4.  Allow execution of PowerShell scripts:
    1.  On the Start screen, type "powershell", right-click on the Windows PowerShell result, and select **Run as administrator**.
    2.  In the PowerShell window, type this command:

        ``` syntax
        Set-ExecutionPolicy RemoteSigned -Force
        ```

    3.  Close the PowerShell window.
    4.  Open a PowerShell window (you don't need to **Run as administrator**) and run the following commands. Adjust the path if you installed the kit to a different location:

        ``` syntax
        cd "C:\Program Files (x86)\Windows Kits\8.0\Tools\x86\Network Monitor Parsers\usb"
        ..\NplAutoProfile.ps1
        ```

    5.  Restart Netmon to apply the changes.

5.  Verify that the profile is active in Netmon.
    1.  On the **Tools** menu, select **Options**.
    2.  On the **Parser Profiles** tab, make sure that **AutoProfile (generated)** is set as active. Your settings should be similar to this image.

        ![](images/netmon-parsers1.png)

    3.  Click **OK**.

Netmon is now configured for use with a USB ETW trace file. For more information, see [How to view a USB ETW trace in Netmon](how-to-examining-a-trace-file-by-using-netmon.md).

## Related topics
[Using USB ETW](using-usb-etw.md)  
[USB Event Tracing for Windows](usb-event-tracing-for-windows.md)  
[How to open an ETW trace in Netmon](how-to-examining-a-trace-file-by-using-netmon.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20How%20to%20install%20Netmon%20and%20USB%20ETW%20Parsers%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


