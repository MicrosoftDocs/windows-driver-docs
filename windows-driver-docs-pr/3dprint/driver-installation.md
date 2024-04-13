---
title: Driver Installation
description: The print driver provided in this SDK is an experimental 3D printer device driver still under development.
ms.date: 03/17/2023
---

# Driver installation

> [!NOTE]
> The print driver provided in the 3D printing SDK is an experimental 3D printer device driver still under development.

## Driver installation instructions

To install the printer, use the following installation instructions:

- If the 3D printer implements a Microsoft OS descriptor 3DPRINT ("MS\_COMP\_3DPRINT") or is one of the supported Vendor ID (VID)/Product ID (PID) combinations in the MS3DPrintUSB.inf file, follow the steps in *Automatic installation of the driver via PnP* section below.

- If the 3D printer is experimental or in development, follow the steps in *Install the driver manually* section below to print to an existing COM port or print G-Code to file.

For information on MS_COMP_3DPRINT, see [Getting started guide - Microsoft Standard Driver for 3D Printers](./microsoft-standard-driver-for-3d-printers-.md).

For more information on OS descriptors, see [Microsoft OS Descriptors for USB Devices](../usbcon/microsoft-defined-usb-descriptors.md).

### Automatic installation of the driver via PnP

1. If the device does not have a MSO descriptor or a supported hardware ID (VID/PID), add the new VID/PID combination to the MS3DPrintUSB\_{architecture}\\MS3DPrintUSB.inf file and restart Windows with advanced settings and driver signing disabled. This option should only be used temporarily and for development purposes.

1. Execute these two commands from an elevated command prompt:

    ```console
    pnputil -a {PathToSDK}\Bin\MS3DPrintUSB_{architecture}\MS3DPrintUSB.inf
    pnputil -a {PathToSDK}\Bin\RenderFilters_{architecture}\MS3DPrinter.inf
    ```

1. Plug in the USB serial device. A new **Generic 3D Printer** device should be installed under **Devices and Printers**.

### Install the driver manually

1. Search for printmanagement.msc in **Cortana**.

    ![print management.](images/g-code-1.png)

1. Expand **Print Servers**, expand the name of your machine, right-click on **Drivers**, then select **Add Driver…**.

    ![print management dialog.](images/g-code-2.png)

1. Click **Next**, select **(x64)**, click **Next**, then click **Have Disk**.

1. Navigate to the RenderFiltersV4\_x64 folder, select MS3DPrinter.inf, then click **OK**.

1. Click **OK**, click **Next**, then click **Finish**.

1. From **Windows Start**, type **Devices and Printers**.

1. Click **Add a printer**.

    ![add a printer.](images/g-code-3.png)

1. Select **The printer that I want isn't listed**.

    ![add a device.](images/g-code-4.png)

1. Select **Add a local printer or network printer with manual settings**, then click **Next**.

    ![add a local printer or network printer with manual settings.](images/g-code-5.png)

1. Choose **Create a new port** and select **3D Port** for the type of port, then click **Next**.

    ![create a new port.](images/g-code-6.png)

1. Enter a port name and click **OK**.

    ![enter a port name.](images/g-code-7.png)

1. Click **Have Disk…**.

    ![have disk...](images/g-code-8.png)

1. Browse to the generic 3D Print Driver binary package from the SDK and click **OK**.

1. Click **Next**.

    ![install the printer driver.](images/g-code-9.png)

1. You can change the 3D printer name here if you want (it will show up in the printer UI), then click **Next**, then click **OK** to allow the command to be run as an Administrator.

    ![type a printer name.](images/g-code-10.png)

1. After the installation completes, click **Finish**.
