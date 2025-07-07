---
title: SIM toolkit features and usage in Windows 10 Mobile
description: Learn about SIM toolkit features, components, and usage in Windows 10 Mobile. Discover how to use SIM toolkit commands and customize settings.
ms.date: 05/23/2025
ms.topic: concept-article
---

# SIM toolkit features and usage in Windows 10 Mobile

SIM toolkit is a set of applications on the SIM card that activate based on network events or user actions in Windows 10 Mobile. This article explains SIM toolkit features, supported commands, and how to use and customize SIM toolkit applications for better device management. For a list of supported commands, see [SIM toolkit commands](sim-toolkit-commands.md).

## SIM toolkit components and architecture

The three main components of SIM toolkit are:

-   The modem and the radio interface layer (RIL) software provided by the silicon vendor.
-   The service, which is a native-code DLL.
-   The user interface (UI).

Both the SIM toolkit service and user interface are provided by Microsoft.

The following diagram illustrates the main components of SIM toolkit.

:::image type="content" source="images/sim-toolkit-components.png" alt-text="Screenshot of diagram showing main components of SIM toolkit.":::

### SIM toolkit service

The SIM toolkit service is part of Windows 10 Mobile. It runs as a background task and interprets commands between the SIM and the SIM toolkit UI application.

### SIM toolkit UI application

The SIM toolkit UI displays text as directed by the SIM toolkit service.

The SIM toolkit UI application shows two types of text strings:

- Application management strings are part of the SIM toolkit UI. Microsoft localizes these strings into the languages Windows supports.
- Text strings shown as part of message interaction with the SIM come from the mobile operator. Microsoft doesn't localize these text strings.

The SIM toolkit UI application can also play tones and open the browser.

### SIM toolkit customizations

OEMs can change the display period for certain dialogs or messages if the default values don't meet the mobile operator's requirements. These customization settings are available in both MCSF and Windows provisioning, so you can choose which method to use. The default display times are:

-   GETINPUT: 120 seconds
-   DISPLAYTEXT: 60 seconds
-   SELECTITEM: 60 seconds
-   GETINKEY: 60 seconds

### Example of processing a SIM toolkit command

Here's an example of how the SIM toolkit processes the DISPLAY TEXT command:

1. The SIM sends the DISPLAY TEXT command.
1. The SIM toolkit service receives the DISPLAY TEXT command and passes it to the SIM toolkit UI.
1. The SIM toolkit UI shows the text string.

## Start the SIM toolkit UI application

When you install the SIM toolkit UI application, a **SIM applications** button appears on the **Settings** > **network & wireless** > **Cellular & SIM** > **advanced options** screen. To start the application, select the button.

The **SIM applications** button is hidden if any of these apply:

- SIM PIN is locked (for 2G SIM).
- PUK (personal unlock key) is locked (for 2G SIM).
- No SIM applications are on the SIM.
- No SIM is present.

When the SIM toolkit UI application starts, the SIM toolkit UI shows options you can select. The applications on the SIM determine the options.

## Launch the SIM toolkit from another app

To make the SIM toolkit easier to find, partners can use a reserved URI scheme to let a UWP app open the SIM applications CPL. For more information, see [Reserved URI to launch SIM toolkit](reserved-uri-to-launch-sim-toolkit.md).

## SIM toolkit UI notifications and alerts

The SIM application UI doesn't show if the device receives a SIM command while you're on the phone dialer screen. In this case, a notification toast appears at the top of the screen. If you tap the toast, the SIM application UI opens. In all other cases, the SIM toolkit UI application opens and shows on the entire screen.

## Additional SIM toolkit reference

We recommend these settings:

- Set the lock screen time-out to **Never** while running tests, so the lock screen doesn't interfere with the tests. By default, it's set to 1 minute.
- For CDMA devices, make sure the APN is set on the device.
- Some test suites use a default timer value of 90 seconds. If needed, set the time-out customization registry values accordingly.

## Related content

[SIM toolkit commands](sim-toolkit-commands.md)



