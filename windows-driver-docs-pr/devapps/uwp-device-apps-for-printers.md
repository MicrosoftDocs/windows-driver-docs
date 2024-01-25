---
title: UWP Device Apps for Printers
description: This section introduces UWP device apps for printers.
ms.date: 03/17/2023
---

# UWP device apps for printers

> [!IMPORTANT]
> Starting with the release of Windows 11 SDK (22000.1), Print Support Apps (PSA) are the recommended method of developing UWP apps for printers. See the [Print support app design guide](print-support-app-design-guide.md) and the [Print support app association](print-support-app-association.md) topics for more information on using PSA with your print devices.

The following section describes UWP device apps for printers that support the v4 print driver model. UWP device apps can highlight the special features of printers through customized print settings flyouts and notifications support. UWP device apps can also display printer status, manage print jobs, and perform printer maintenance tasks. To learn more about UWP device apps in general, see [Meet UWP device apps](meet-uwp-device-apps.md).

To use the UWP device app features discussed in the following topics, your printer must support the v4 print driver model. For more info, see [Developing v4 print drivers](../print/v4-printer-driver.md).

## In this section

| Topic | Description |
|--|--|
| [How to display printer status](how-to-display-printer-status.md) | This topic uses the C# version of the [Print settings and print notifications](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Print%20settings%20and%20print%20notifications) sample to demonstrate how to query the printer status and display it. |
| [How to customize print settings](how-to-customize-print-settings.md) | This topic introduces the advanced print settings flyout, and shows how the C# version of the [Print settings and print notifications](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Print%20settings%20and%20print%20notifications) sample replaces the default flyout with a custom flyout. |
| [Working with print notifications](working-with-print-notifications.md) | This topic introduces print notifications, and shows how the C# version of the [Print settings and print notifications](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Print%20settings%20and%20print%20notifications) sample uses a background task to respond to print notification. The background task demonstrates how to save notification details in the local app data store, send toasts, and update a tile and badge. |
| [How to manage print jobs](how-to-manage-print-jobs.md) | In Windows 8.1, UWP device apps for printers can manage print jobs. This topic uses the C# version of the [Print job management and printer maintenance](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Print%20job%20management%20and%20printer%20maintenance) sample to demonstrate how to create a view of print jobs, monitor those jobs, and if necessary, cancel a job. |
| [How to do printer maintenance](how-to-do-printer-maintenance.md) | In Windows 8.1, UWP device apps can perform printer maintenance, such as aligning print heads and cleaning nozzles. This topic uses the C# version of the [Print job management and printer maintenance](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Print%20job%20management%20and%20printer%20maintenance) sample to demonstrate how bidirectional communication (Bidi) can be used to perform such device maintenance. |
| [Printer extension library overview](printer-extension-library-overview.md) | This topic introduces the printer extension library, a library that helps device manufacturers write UWP device apps for their printer. |

## Usage scenarios for UWP device apps for printers

Use a UWP device app for a printer if you'd like to:

- Highlight advanced device capabilities, such as printing multiple photos per page.

- Make device-specific recommendations. For example, you could use your device app to present image management options or provide methods for setting and saving printer-specific defaults.

## General recommendations

- After you call window.print(), check for and handle error messages from within the onClick event handler for your app's Print button. This allows your app to abort a print request if, for example, no printer is available.

- Notify the user if printing fails and, if possible, explain the reason for the failure.

- If you plan to customize the print experience, separate this code into a print companion app. This allows you to componentize your code and eases the test and debugging process.

- Don't try to customize your print experience to use the V3 print driver.

- Don't advertise accessories for the print device in your customized print UI.

- Don't show items for sale that aren't related to the reason the Microsoft Store device app was invoked. For example, it's relevant to show print cartridges for purchase after a user clicks a notification alerting them that ink is low. However, it's not appropriate to also try to sell print cords or photo printing kits in this same scenario.

- Don't redirect the user to your company's website for more product sales.

- Don't present information that isn't relevant to the task of setting printing preferences. For example, don't provide info about how to clean the print heads or how to align and test the print nozzles.

## Samples

The UWP device app samples for printers demonstrate the printer-related features that you can implement in your own UWP device app. Each sample also includes the `PrinterExtensionLibrary` project, that you can reuse in your own app to help with printer extensions. The printer extension library wraps the COM implementation of the [printer extension interfaces](/windows-hardware/drivers/ddi/_print/) from the v4 print driver.

### Windows 8 Samples

- The [Print job management and printer maintenance](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Print%20job%20management%20and%20printer%20maintenance) sample demonstrates how to manage print jobs and perform printer maintenance tasks using bidirectional communications (Bidi).

- The [Print settings and print notifications](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Print%20settings%20and%20print%20notifications) sample shows how to create a UWP device app that provides a customized flyout for advanced print settings, can display printer status, and can display printer notifications in tiles or toasts.

### Windows 10 Sample

- The [Writing print workflow apps and migrating WSDAs to UWP](https://github.com/microsoft/print-oem-samples) sample shows OEM print partners how to use the Print Workflow feature and migrate their existing Windows Store Device Apps (WSDAs) code to the Universal Windows Platform.

## Related topics

[Developing v4 print drivers](../print/v4-printer-driver.md)

[Printer Extension Interfaces (v4 Print Driver)](/windows-hardware/drivers/ddi/_print/)

[Bidirectional Communications](../print/bidirectional-communication.md)

[Getting started with UWP apps](getting-started.md)

[Create a UWP device app (step-by-step guide)](step-1--create-a-uwp-device-app.md)

[Create device metadata for a UWP device app (step-by-step guide)](step-2--create-device-metadata.md)
