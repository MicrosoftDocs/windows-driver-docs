---
title: Print device installation
description: Provides information about initial installation of your port-connected print device, and potential system states when your device is connected for the first time.
keywords:
- hot-pluggable bus WDK printer
- printer installation checks WDK
- states WDK printer
- verifying printer installations
- installed driver tests WDK printer
ms.date: 07/07/2020
ms.localizationpriority: medium
---

# Print device installation

Initial installation of your port-connected device can occur in many ways, and the system can be in a variety of states when your device is connected for the first time.

| System state | Device test scenario |
| --- | --- |
| System Off (S5) | Boot install |
| System Working State (S0) | Base Plug and Play |
| System in Sleep State (S1-S4) | See [Power management](power-management.md) |

For more information, see [System Power States](../kernel/system-power-states.md).

The most common system power state at which initial installation of your device will occur is System Working State S0. Most of your device installation testing should initially be focused here, but it is important to verify installation during other system power states as well.

Your device's Plug and Play (PnP) compatibility can best be assessed in the device's state when it is first connected. In initial installation tests, start the system with the device attached, and then install the device when the system is in System Working State S0. Finally, verify device connection and installation in all possible system power state combinations. For more details, see [Power Management](power-management.md).

## Verifying basic installation

When first connecting your printer, you should receive a Plug and Play (PnP) notification. Verify that the device is correctly identified. The device name should be properly recognized. If the correct driver is provided, the device should install successfully. If driver installation fails, open Device Manager to look for possible causes for errors. Open Device Manager by double-clicking **Computer Management** in the **Administrative Tools** Control Panel. Alternately, select and hold (or right-click) the **My Computer** icon on the desktop, and select **Properties**. On the **Hardware** tab, select **Device Manager**.

Make sure that the following two scenarios work smoothly:

- Install the driver first and then install the device.

- Install the device first and then install the driver.

## Using Control Panel applications to confirm device installation

After the driver is successfully installed, use the following Control Panel applications to verify that your printer is installed to the proper locations.

- **Device Manager:** Check that the device is installed correctly. It should be listed in the tree according to the bus on which it is connected. From Device Manager, verify that your printer responds correctly to requests to disable/re-enable and uninstall/install the device. To reinstall the device, on the Device Manager **Action** menu, select **Scan for hardware changes**.

- **Printers and Faxes:** From this Control Panel application, verify that the printer icon appears. Also verify that the printer icon can be deleted successfully. Confirm that you can reinstall the printer using the Add Printer wizard.

- **Device-specific Control Panel application:** Some buses, such as Bluetooth, have their own Control Panel application. From this Control Panel application, verify that your device is properly installed, that your device is connected over a specialized bus, and that your device can be removed and installed successfully.

## Finding, canceling, and deleting installations

Test print device installation as follows:

- While your printer is installing, try canceling the installation and then restarting it. Your printer should continue to install successfully.

- After you have successfully installed your printer, delete it, and then reinstall it. It should install without problems.

- Make sure your printer can print at the same time that other resources are being installed on the same bus that the printer shares.

- After you have successfully installed your printer, try installing it again. No dialog box should appear announcing that new hardware has been found, nor should the New Hardware Wizard launch.

- Make sure that device power-cycling is working. If your printer is on a bus that is hot-plug capable, it should show up in the **Printers and Faxes** window (in Control Panel) as offline. Also check the Device Manager to verify that the device has been removed from the system.

### Bus-specific hardware requirements

Certain buses, such as a Universal Serial Bus (USB), can have varying hardware requirements. Be sure to test your printer installation on a wide variety of hardware, covering as many variations as possible. For USB, be sure that the device is tested on open host controller interface (OHCI, USB 1.1), universal host controller interface (UHCI, USB 1.1), or enhanced host controller interface (EHCI, USB 1.1).

### Hot-pluggable buses and device chaining

Certain buses, such as USB and IEEE 1394, are "hot-pluggable," meaning that the device can be removed from the bus simply by unplugging it from the computer or turning the device off. To verify that your hot-pluggable device functions correctly, complete the following:

1. Plug the device into the computer.

1. Using Control Panel applications discussed previously, verify that the device is installed to the proper locations.

1. Verify that the device functions properly.

1. Unplug the device from the computer and make sure that the device no longer appears in Device Manager.

1. If the bus supports chaining, chain multiple devices together and verify that the device installs and functions correctly.

1. For USB devices, verify that the device can work on USB hubs of various configurations and types, including USB 1.1 and USB 2.0, and with chains of multiple devices.

To test a printer on a hub, complete the following:

1. Try installing a print device on different ports on the same hub and chained hubs.

1. Test other printers (both the same and different models) on the same hub and chained hubs.

1. Verify that the printer installs correctly when other devices are installed at the same time.

1. When you plug the printer into a new hub device, also install other port-connected devices.

1. Install multiple printers on different ports, and then verify that only one instance of each printer is installed.

1. Disconnect a printer from one port and connect it to another port, and then verify that it uninstalls successfully from the old port and reinstalls successfully to the new port
