---
title: Windows Store device apps for printers
description: This section introduces Windows Store device apps for printers.
ms.assetid: 3325B492-2A70-4EB7-99B0-3FE3E24CE398
---

# Windows Store device apps for printers


This section introduces Windows Store device apps for printers. Windows Store device apps can highlight the special features of printers through customized print settings flyouts and notifications support. Windows Store device apps can also display printer status, manage print jobs, and perform printer maintenance tasks. To learn more about Windows Store device apps in general, see [Meet Windows Store device apps](meet-windows-store-device-apps.md).

**Important**  To use Windows Store device app features, your printer must support the v4 print driver model. For more info, see [Developing v4 print drivers](http://go.microsoft.com/fwlink/p/?LinkId=314231).

 

## <span id="in_this_section"></span>In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[How to display printer status](how-to-display-printer-status.md)</p></td>
<td align="left"><p>This topic uses the C# version of the [Print settings and print notifications](http://go.microsoft.com/fwlink/p/?LinkID=242862) sample to demonstrate how to query the printer status and display it.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[How to customize print settings](how-to-customize-print-settings.md)</p></td>
<td align="left"><p>This topic introduces the advanced print settings flyout, and shows how the C# version of the [Print settings and print notifications](http://go.microsoft.com/fwlink/p/?LinkID=242862) sample replaces the default flyout with a custom flyout.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Working with print notifications](working-with-print-notifications.md)</p></td>
<td align="left"><p>This topic introduces print notifications, and shows how the C# version of the [Print settings and print notifications](http://go.microsoft.com/fwlink/p/?LinkID=242862) sample uses a background task to respond to print notification. The background task demonstrates how to save notification details in the local app data store, send toasts, and update a tile and badge.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[How to manage print jobs](how-to-manage-print-jobs.md)</p></td>
<td align="left"><p>In Windows 8.1, Windows Store device apps for printers can manage print jobs. This topic uses the C# version of the [Print job management and printer maintenance](http://go.microsoft.com/fwlink/p/?LinkID=299829) sample to demonstrate how to create a view of print jobs, monitor those jobs, and if necessary, cancel a job.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[How to do printer maintenance](how-to-do-printer-maintenance.md)</p></td>
<td align="left"><p>In Windows 8.1, Windows Store device apps can perform printer maintenance, such as aligning print heads and cleaning nozzles. This topic uses the C# version of the [Print job management and printer maintenance](http://go.microsoft.com/fwlink/p/?LinkID=299829) sample to demonstrate how bidirectional communication (Bidi) can be used to perform such device maintenance.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Printer extension library overview](printer-extension-library-overview.md)</p></td>
<td align="left"><p>This topic introduces the printer extension library, a library that helps device manufacturers write Windows Store device apps for their printer.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Should_I_create_a_Windows_Store_device_app_for_my_printer_"></span><span id="should_i_create_a_windows_store_device_app_for_my_printer_"></span><span id="SHOULD_I_CREATE_A_WINDOWS_STORE_DEVICE_APP_FOR_MY_PRINTER_"></span>Should I create a Windows Store device app for my printer?


Use a Windows Store device app for a printer if you'd like to:

-   Highlight advanced device capabilities, such as printing multiple photos per page.
-   Make device-specific recommendations. For example, you could use your device app to present image management options or provide methods for setting and saving printer-specific defaults.

## <span id="General_recommendations"></span><span id="general_recommendations"></span><span id="GENERAL_RECOMMENDATIONS"></span>General recommendations


-   After you call window.print(), check for and handle error messages from within the onClick event handler for your app's Print button. This allows your app to abort a print request if, for example, no printer is available.
-   Notify the user if printing fails and, if possible, explain the reason for the failure.
-   If you plan to customize the print experience, separate this code into a print companion app. This allows you to componentize your code and eases the test and debugging process.
-   Don't try to customize your print experience to use the V3 print driver.
-   Don't advertise accessories for the print device in your customized print UI.
-   Don't show items for sale that aren't related to the reason the Windows Store device app was invoked. For example, it's relevant to show print cartridges for purchase after a user clicks a notification alerting them that ink is low. However, it's not appropriate to also try to sell print cords or photo printing kits in this same scenario.
-   Don't redirect the user to your company’s website for more product sales.
-   Don't present information that isn't relevant to the task of setting printing preferences. For example, don't provide info about how to clean the print heads or how to align and test the print nozzles.

## <span id="Samples"></span><span id="samples"></span><span id="SAMPLES"></span>Samples


The Windows Store device app samples for printers demonstrate the printer-related features that you can implement in your own Windows Store device app. Each sample also includes the `PrinterExtensionLibrary` project, that you can reuse in your own app to help with printer extensions. The printer extension library wraps the COM implementation of the [printer extension interfaces](http://go.microsoft.com/fwlink/p/?LinkID=299887) from the v4 print driver.

-   The [Print job management and printer maintenance](http://go.microsoft.com/fwlink/p/?LinkID=299829) sample demonstrates how to manage print jobs and perform printer maintenance tasks using bidirectional communications (Bidi).

-   The [Print settings and print notifications](http://go.microsoft.com/fwlink/p/?LinkID=242862) sample shows how to create a Windows Store device app that provides a customized flyout for advanced print settings, can display printer status, and can display printer notifications in tiles or toasts.

## <span id="related_topics"></span>Related topics


[Developing v4 print drivers](http://go.microsoft.com/fwlink/p/?LinkId=314231)

[Printer Extension Interfaces (v4 Print Driver)](http://go.microsoft.com/fwlink/p/?LinkID=299887)

[Bidirectional Communications](http://go.microsoft.com/fwlink/p/?LinkId=317192)

[Getting started with Windows Store apps](getting-started.md)

[Create a Windows Store device app (step-by-step guide)](step-1--create-a-windows-store-device-app.md)

[Create device metadata for a Windows Store device app (step-by-step guide)](step-2--create-device-metadata.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devapps\devapps]:%20Windows%20Store%20device%20apps%20for%20printers%20%20RELEASE:%20%281/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





