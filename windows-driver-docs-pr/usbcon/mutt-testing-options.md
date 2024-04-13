---
title: How to Prepare the Test System to Run MUTT Test Tools
description: Before using MUTT devices, you must prepare the test system.
ms.date: 01/17/2024
---

# How to prepare the test system to run MUTT test tools

Before using MUTT devices, you must prepare the test system.

## Before you start

The instructions in this document are based on the following assumptions:

- You have an understanding of the Windows command shell. Installation of the test tools requires an elevated command window. For that window, you can open a Command Prompt window by using the **Run as administrator** option.

- You are familiar with the tools that are included with the Windows Driver Kit (WDK).

- You are familiar with kernel debugging tools.

    > [!NOTE]
    > This setup applies to the MUTT, MUTTPack, SuperMUTT and SuperMUTT Pack. For more information about those devices, see [MUTT devices](microsoft-usb-test-tool--mutt--devices.md).

## To prepare a system to run MUTT test tools for USB hardware testing

1. Connect the test system to a kernel debugger.

    For more information, see [Download and Install Debugging Tools for Windows](../download-the-wdk.md) and [Windows Debugging](../debugger/index.md).

1. Attach MUTT devices into each available port of the host controller or hub to test.

    You must attach the MUTT device to the test system before you run the installation scripts that are installed by the MUTT software package.

    For information about the recommended test configurations, see MUTT Topologies in this document.

1. Open an elevated Command Prompt window on the test system and navigate to the folder in which the test tools were copied.

1. In the elevated Command Prompt window, run the following command to install the necessary MUTT driver:

    `C:\\usbTest\\pnputil -i -a usbfx2.inf`

    If you want to test by using driver verifier then you can run **install.cmd** instead of the previous command. This will install the necessary drivers as well as configure driver verifier. Note that using **install.cmd** is optional.

1. The following dialog box appears while installing the test drivers:

    ![windows security dialog.](images/fig9-winsec.png)

    Check **Always trust software from "Microsoft Corporation"** to prevent the dialog box from appearing when the tests are running.

    The test system machine will reboot after **install.cmd** has completed installing.

1. Switch the MUTT to the new driver **C:\\usbTest\\MuttUtil –UpdateDriver usbfx2.inf**

1. Update the MUTT with the latest firmware **C:\\usbTest\\MuttUtil.exe -UpdateFirmware**

1. If your test system is running Windows 8, we suggest that you perform a quick validation of your host controller before you start the tests.

    1. From an elevated Command Prompt window, run the following command to collect information about your host controller and hubs that are connected to the system:

        `C:\\usbTest\\xhciwmi -verify`

    1. The tool displays information about the host controller in the command window. Information includes vendor ID, device ID, revision ID, and the firmware version. If known issues exist for the host controller under test, consider updating the firmware.

### Tracing and logging events in the USB driver stack

Go to [https://aka.ms/usbtrace](https://aka.ms/usbtrace) for instructions and to download a script for capturing ETW traces from the USB drivers.

## Related topics

- [Universal Serial Bus (USB)](index.md)
- [Microsoft USB Test Tool (MUTT) devices](microsoft-usb-test-tool--mutt--devices.md)
