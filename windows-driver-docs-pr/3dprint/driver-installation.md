---
title: Driver installation
author: windows-driver-content
description: The print driver provided in this SDK is an experimental 3D printer device driver still under development.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8A13CD6F-DF82-4353-ADE9-06989F83BC87
---

# Driver installation


The print driver provided in this SDK is an experimental 3D printer device driver still under development.

## Driver installation


To install the printer, use the following installation instructions:

If the 3D print device implements a Microsoft OS descriptor 3DPRINT (“MS\_COMP\_3DPRINT”) or is one of the supported Vendor ID (VID)/Product ID (PID) combinations in the MS3DPrintUSB.inf file, follow the steps in *Automatic installation of the driver via PnP* section below.

If the 3D print device is currently in development, follow the steps in *Install the driver manually* section below to print to an existing COM port or print to file.

For more information, see [Microsoft OS Descriptors for USB Devices](http://msdn.microsoft.com/library/windows/hardware/ff537430.aspx).

### Automatic installation of the driver via PnP

1.  If the device does not have a MSO descriptor or a supported VID/PID, add the VID/PID combination to the MS3DPrintUSB\_{architecture}\\MS3DPrintUSB.inf file and restart Windows with advanced settings and driver signing disabled. This option should only be used temporarily and for development purposes.

2.  Execute these two commands from an elevated command prompt:

    ``` syntax
    pnputil -a {PathToSDK}\Bin\MS3DPrintUSB_{architecture}\MS3DPrintUSB.inf
    pnputil -a {PathToSDK}\Bin\RenderFilters_{architecture}\MS3DPrinter.inf
    ```

3.  Plug in the USB serial device. A new **Generic 3D Printer** device should be installed under **Devices and Printers**.

### Install the driver manually

1.  Search for printmanagement.msc in **Cortana**.

    ![print management](images/g-code-1.png)

2.  Expand **Print Servers**, expand the name of your machine, right-click on **Drivers**, then select **Add Driver…**.

    ![print management dialog](images/g-code-2.png)

3.  Click **Next**, select **(x64)**, click **Next**, then click **Have Disk**.

4.  Navigate to the RenderFilters\_x64 folder, select MS3DPrinter.inf, then click **OK**.

5.  Click **OK**, click **Next**, then click **Finish**.

6.  From **Windows Start**, type **Devices and Printers**.

7.  Click **Add a printer**.

    ![add a printer](images/g-code-3.png)

8.  Select **The printer that I want isn’t listed**.

    ![add a device](images/g-code-4.png)

9.  Select **Add a local printer or network printer with manual settings**, then click **Next**.

    ![add a local printer or network printer with manual settings](images/g-code-5.png)

10. Choose **Create a new port** and select **3D Port** for the type of port, then click **Next**.

    ![create a new port](images/g-code-6.png)

11. Enter a port name and click **OK**.

    ![enter a port name](images/g-code-7.png)

12. Click **Have Disk…**.

    ![have disk...](images/g-code-8.png)

13. Browse to the generic 3D Print Driver binary package from the SDK and click **OK**.

14. Click **Next**.

    ![install the printer driver](images/g-code-9.png)

15. You can change the 3D printer name here if you want (it will show up in the printer UI), then click **Next**, then click **OK** to allow the command to be run as an Administrator.

    ![type a printer name](images/g-code-10.png)

16. After the installation completes, click **Finish**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Driver%20installation%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


