---
title: Working with Print Notifications in a UWP Device App
description: This topic introduces print notifications, and shows how the C# version of the Print settings and print notifications sample uses a background task to respond to print notification.
ms.date: 03/17/2023
---

# Working with print notifications in a UWP device app

In Windows 8.1, UWP device apps can respond to bidirectional communication (Bidi) events that are sent from a v4 print driver. This topic introduces print notifications, and shows how the C# version of the [Print settings and print notifications](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Print%20settings%20and%20print%20notifications) sample uses a background task to respond to print notification. The background task demonstrates how to save notification details in the local app data store, send toasts, and update a tile and badge. To learn more about UWP device apps in general, see [Meet UWP device apps](meet-uwp-device-apps.md).

The C# version of the [Print settings and print notifications](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Print%20settings%20and%20print%20notifications) sample demonstrates the background portion of the app (*the background task*) in the **BackgroundTask** project. The code for the background task is in the **PrintBackgroundTask.cs** file. The *foreground app*, the full-screen app that can be launched from Start, is in the **DeviceAppForPrinters** project. The **InkLevel.xaml.cs** file shows one way that notification details can be accessed from the foreground app. To work with print notifications, the sample uses the printer extension library in the **PrinterExtensionLibrary** project. The printer extension library provides a convenient way to access the printer extension interfaces of the v4 print driver. For more info, see the [Printer extension library overview](printer-extension-library-overview.md).

The code examples shown in this topic are based on the C# version of the [Print settings and print notifications](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Print%20settings%20and%20print%20notifications) sample. This sample is also available in JavaScript and C++. Note that because C++ can access COM directly, the C++ version of the sample does not include code library projects. Download the samples to see the latest versions of the code.

## Print notifications

Print notifications let your UWP device app inform the user of important printer events while printing, such as a paper jam, open printer door, low ink levels, or printer out-of-paper errors. When a printer triggers a notification, the system event broker runs the background task of your app. From there, the background task can save the notification details, send a toast, update a tile, update a badge, or do nothing. By saving notification details, your app can provide an experience that helps users understand and fix their printer problems.

Printer manufacturers must implement Bidi and the DriverEvent XML file in their v4 print driver to use print notifications with their UWP device apps. For more info, see [Bidirectional Communications](../print/bidirectional-communication.md).

When a DriverEvent occurs, and the background task of a UWP device app is started, the app has several options as to how it can proceed. For more details about the flow that leads to the launch of the task, see [Driver Support for Customized UI](../print/driver-support-for-customized-ui.md).

The background task can choose to:

- Do nothing

- Save the notification details in [local app data store](/previous-versions/windows/apps/hh700361(v=win.10))

- Update a [UWP app tile notification](/previous-versions/windows/apps/hh779724(v=win.10))

- Update a [UWP app notification badge](/previous-versions/windows/apps/hh779719(v=win.10))

- Send a [UWP app toast notification](/previous-versions/windows/apps/hh779727(v=win.10))

The tile notification or toast notification can let the user conveniently launch your foreground app. When the foreground app is launched, it can use the `OnLaunched` method in **App.xaml.cs** to check if it was launched by a tile or toast. If it was, the foreground app can access any print notification details in the [local app data store](/previous-versions/windows/apps/hh700361(v=win.10)).

## Prerequisites

Before you get started:

1. Make sure your printer is installed using a v4 print driver. For more info, see [Developing v4 print drivers](../print/v4-printer-driver.md).

1. Get your development PC set up. See [Getting started](getting-started.md) for info about downloading the tools and creating a developer account.

1. Associate your app with the store. See [Create a UWP device app](step-1--create-a-uwp-device-app.md) for info about that.

1. Create device metadata for your printer that associates it with your app. See [Create device metadata](step-2--create-device-metadata.md) for more about that.

1. Build the UI for the main page of your app. All UWP device apps can be launched from Start, where they'll be displayed full-screen. Use the Start experience to highlight your product or services in a way that matches the specific branding and features of your devices. There are no special restrictions on the type of UI controls it can use. To get started with the design of the full-screen experience, see the [Microsoft Store design principles](/windows/uwp/design/).

1. If you're writing you're writing your app with C# or JavaScript, add the **PrinterExtensionLibrary** and **DeviceAppForPrintersLibrary** projects to your UWP device app solution. You can find each of these projects in the [Print settings and print notifications](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Print%20settings%20and%20print%20notifications) sample.

Because C++ can access COM directly, C++ apps do not require a separate library to work with the COM-based printer device context.

## Step 1: Register background task

In order for Windows to recognize that the app can handle print notifications, it must register a background tasks extension for print notifications. This extension is declared in an `Extension` element, with a `Category` attribute set to `windows.backgroundTasks` and an `EntryPoint` attribute set to `BackgroundTask.PrintBackgroundTask`. The extension also includes a `Task` element to indicate that it supports `systemEvent` task types.

You can add the print background task extension on the **Declarations** tab of the Manifest Designer in Microsoft Visual Studio. You can also edit the app package manifest XML manually, using the XML (Text) Editor. Right-click the **Package.appxmanifest** file in **Solution Explorer** for editing options.

This example shows the background task extension in the `Extension` element, as it appears in the app package manifest file, **Package.appxmanifest**.

```xml
<?xml version="1.0" encoding="utf-8"?>
<Package xmlns="http://schemas.microsoft.com/appx/2010/manifest">
  <Identity Name="Microsoft.SDKSamples.DeviceAppForPrinters.CS" Publisher="CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US" Version="1.0.0.0" />
  <Properties>
    <DisplayName>Device App For Printers C# sample</DisplayName>
    <PublisherDisplayName>Microsoft Corporation</PublisherDisplayName>
    <Logo>Assets\storeLogo-sdk.png</Logo>
  </Properties>
  <Prerequisites>
    <OSMinVersion>6.3.0</OSMinVersion>
    <OSMaxVersionTested>6.3.0</OSMaxVersionTested>
  </Prerequisites>
  <Resources>
    <Resource Language="x-generate" />
  </Resources>
  <Applications>
    <Application Id="DeviceAppForPrinters" Executable="$targetnametoken$.exe" EntryPoint="DeviceAppForPrinters.App">
      <VisualElements DisplayName="Device App For Printers C# sample" Logo="Assets\squareTile-sdk.png"
                      SmallLogo="Assets\smallTile-sdk.png" Description="DeviceAppForPrinters C# sample"
                      ForegroundText="light" BackgroundColor="#00b2f0" ToastCapable="true">
        <DefaultTile ShowName="allLogos" ShortName="App4PrinterCS" WideLogo="Assets\tile-sdk.png" />
        <SplashScreen Image="Assets\splash-sdk.png" BackgroundColor="#00b2f0" />
      </VisualElements>
      <Extensions>
        <Extension Category="windows.backgroundTasks" EntryPoint="BackgroundTask.PrintBackgroundTask">
          <BackgroundTasks>
            <Task Type="systemEvent" />
          </BackgroundTasks>
        </Extension>
        <Extension Category="windows.printTaskSettings" Executable="$targetnametoken$.exe" EntryPoint="DeviceAppForPrinters.App" />
      </Extensions>
    </Application>
  </Applications>
</Package>
```

## Step 2: Configure device metadata

When you're using the **Device Metadata Authoring Wizard** to associate your app with your device, be sure complete the **Notification handlers** box on the **Specify UWP device app information** page. This helps ensure that your app's background task is called during a print notification.

For step-by-step instructions on how to edit your device metadata, see the [Testing](#testing) section.

## Step 3: Build the UI

Before building your app, you should work with your designers and your marketing team to design the user experience. The user experience should project the branding aspects of your company and help you build a connection with your users.

### Design guidelines

It's important to review the Microsoft Store app guidelines before designing your tile and badge experience. The guidelines help ensure that your app provides an intuitive experience that is consistent with other UWP apps.

- [Guidelines for tiles and badges](/windows/uwp/design/shell/tiles-and-notifications/creating-tiles)

- [Guidelines for toast notifications](/windows/uwp/design/shell/tiles-and-notifications/)

For the main page of your app, keep in mind that Windows 8.1 can display multiple apps in various sizes on a single monitor. See the following guidelines to learn more about how your app can reflow gracefully between screen sizes, window sizes, and orientations.

- [Guidelines for window sizes and scaling to screens](/windows/apps/design/layout/screen-sizes-and-breakpoints-for-responsive-design)

- [Guidelines for resizing windows to tall and narrow layouts](/previous-versions/windows/hh465371(v=win.10))

### Best practices

- **Don't include action words on notifications.** On the notification message, don't use text that tells users to push, press, or click notification. Users already understand that they can press a toast to find out more information. For example just write "Your printer is low on ink" instead of "Your printer is low on ink. Press to troubleshoot".

- **Keep interactions simple.** Everything shown on the notifications experience should be related to the notification. For example a notification page about a paper jam should only contain links and information about resolving that issue. It should not contain links to unrelated experiences such purchasing ink or other support information.

- **Use multimedia.** Use actual photos, videos, or illustrations of the device to help users quickly resolve an issue with their device.

- **Keep users within the context of your app.** When providing information about an issue, do not link to online or other support materials. Keep the user in the context of the app.

## Step 4: Create background task

If your app registers a background task for print notifications, it must supply a handler for the background task activation. In the [Print settings and print notifications](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Print%20settings%20and%20print%20notifications) sample, the `PrintBackgroundTask` class handles the print notifications.

If your printer status doesn't require immediate user intervention, update a tile rather than show a toast. For example, for a low ink condition, a tile update is sufficient. But if the printer is completely out of ink, the app may show a toast notification.

### Saving notification details

The background task cannot launch the foreground app directly, only the user can: from a tile, toast, or Start. So, to ensure that the foreground app can access the print notification details, the background task saves them to local storage. For more info about using local storage, see [Quickstart: local app data](/previous-versions/windows/apps/hh700361(v=win.10)).

When a print notification is triggered, Windows runs the background task by calling its `Run` method. The notification data is passed to the background task through a method parameter that must be cast to type Windows.Devices.Printers.Extensions.PrintNotificationEventDetails. The `PrinterName` and `EventData` properties of that object carry the printer name and Bidi message, respectively.

This example shows the background task's `Run` method, in the **PrintBackgroundTask.cs** file, where the print notification details are saved to app settings before the toast, tile, and badge methods are called.

```csharp
public void Run(Windows.ApplicationModel.Background.IBackgroundTaskInstance taskInstance)
{
    // Save notification details to local storage
    PrintNotificationEventDetails details = (PrintNotificationEventDetails)taskInstance.TriggerDetails;
    settings.Values[keyPrinterName] = details.PrinterName;
    settings.Values[keyAsyncUIXML] = details.EventData;

    // Demonstrate possible actions
    ShowToast(details.PrinterName, details.EventData);
    UpdateTile(details.PrinterName, details.EventData);
    UpdateBadge();
}
```

### Updating a tile

When the print notification details are sent to the `UpdateTile` method, the sample's background task demonstrates how to display them on a tile. For more info about tiles, see [Tile and tile notification overview](/previous-versions/windows/apps/hh779724(v=win.10)).

This example shows the background task's `UpdateTile` method, in the **PrintBackgroundTask.cs** file.

```csharp
void UpdateTile(string printerName, string bidiMessage)
{
    TileUpdater tileUpdater = TileUpdateManager.CreateTileUpdaterForApplication();
    tileUpdater.Clear();

    XmlDocument tileXml = TileUpdateManager.GetTemplateContent(TileTemplateType.TileWide310x150Text09);
    XmlNodeList tileTextAttributes = tileXml.GetElementsByTagName("text");
    tileTextAttributes[0].InnerText = printerName;
    tileTextAttributes[1].InnerText = bidiMessage;

    TileNotification tileNotification = new TileNotification(tileXml);
    tileNotification.Tag = "tag01";
    tileUpdater.Update(tileNotification);
}
```

### Updating a badge

The `UpdateBadge` method shows how to use the BadgeNotification class to update a badge. For more info about tiles, see [Badge overview](/previous-versions/windows/apps/hh779719(v=win.10)).

This example shows the background task's `UpdateBadge` method, in the **PrintBackgroundTask.cs** file.

```csharp
void UpdateBadge()
{
    XmlDocument badgeXml = BadgeUpdateManager.GetTemplateContent(BadgeTemplateType.BadgeGlyph);
    XmlElement badgeElement = (XmlElement)badgeXml.SelectSingleNode("/badge");
    badgeElement.SetAttribute("value", "error");

    var badgeNotification = new BadgeNotification(badgeXml);
    BadgeUpdateManager.CreateBadgeUpdaterForApplication().Update(badgeNotification);
}
```

### Raising a toast

A toast notification is a transient message to the user that contains relevant, time-sensitive information and provides quick access to related content in an app. Toast notifications should be viewed to users as an invitation to return to your app to follow up on something of interest. For more info, see [Toast notification overview](/previous-versions/windows/apps/hh779727(v=win.10)).

To enable toast notifications, the app needs to register that it is toast-capable in the app package manifest. In the `VisualElements` element, set the `ToastCapable` attribute to true.

> [!IMPORTANT]
> We do not recommended always showing a toast, especially for non-actionable events. This may become annoying for users and cause them to turn off all toasts from an app. For events that do not require user's immediate attention, we recommended updating only the tile and badge, and not showing a toast.

This example shows the `ToastCapable` attribute in the `VisualElements` element, as it appears in the app package manifest file, **Package.appxmanifest**.

```xml
<VisualElements DisplayName="Device App For Printers C# sample" Logo="Assets\squareTile-sdk.png"
                SmallLogo="Assets\smallTile-sdk.png" Description="DeviceAppForPrinters C# sample"
                ForegroundText="light" BackgroundColor="#00b2f0" ToastCapable="true">
  <DefaultTile ShowName="allLogos" ShortName="App4PrinterCS" WideLogo="Assets\tile-sdk.png" />
  <SplashScreen Image="Assets\splash-sdk.png" BackgroundColor="#00b2f0" />
</VisualElements>
```

This example is from the `ShowToast` method of the **PrintBackgroundTask.cs** file. It shows how to raise a toast based on two strings, named `title` and `body`.

```csharp
void ShowToast(string title, string body)
{
    //
    // Get Toast template
    //
    XmlDocument toastXml = ToastNotificationManager.GetTemplateContent(ToastTemplateType.ToastText02);

    //
    // Pass to app as eventArgs.detail.arguments
    //
    ((XmlElement)toastXml.SelectSingleNode("/toast")).SetAttribute("launch", title);

    //
    // The ToastText02 template has 2 text nodes (a header and a body)
    // Assign title to the first one, and body to the second one
    //
    XmlNodeList textList = toastXml.GetElementsByTagName("text");
    textList[0].AppendChild(toastXml.CreateTextNode(title));
    textList[1].AppendChild(toastXml.CreateTextNode(body));

    //
    // Show the Toast
    //
    ToastNotification toast = new ToastNotification(toastXml);
    ToastNotificationManager.CreateToastNotifier().Show(toast);
}
```

## Step 5: Handle activation

After a print notification triggers the background task, the app can be launched by tapping a toast notification or a tile. If your app is activated from either, a parameter will be passed to the app through `LaunchActivatedEventArgs.arguments` property. For more info about activation and the Microsoft Store app lifecycle, see [Application lifecycle](/previous-versions/windows/apps/hh464925(v=win.10)).

To determine if your app was activated in one these cases, handle the `OnLaunched` event, and examine the event arguments that are passed to the event handler. If the event arguments are null, the app was activated by the user from Start. If the event arguments are not null, the app was launched from a toast or tile.

This example is from the `OnLaunched` method of the **App.xaml.cs** file. It shows how to handle the activation from toast or tiles.

```csharp
protected override async void OnLaunched(LaunchActivatedEventArgs args)
{
    Frame rootFrame = Window.Current.Content as Frame;

    // Do not repeat app initialization when the Window already has content,
    // just ensure that the window is active

    if (rootFrame == null)
    {
        // Create a Frame to act as the navigation context and navigate to the first page
        rootFrame = new Frame();
        // Associate the frame with a SuspensionManager key
        SuspensionManager.RegisterFrame(rootFrame, "AppFrame");

        if (args.PreviousExecutionState == ApplicationExecutionState.Terminated)
        {
            // Restore the saved session state only when appropriate
            try
            {
                await SuspensionManager.RestoreAsync();
            }
            catch (SuspensionManagerException)
            {
                //Something went wrong restoring state.
                //Assume there is no state and continue
            }
        }

        // Place the frame in the current Window
        Window.Current.Content = rootFrame;
    }
    if (rootFrame.Content == null || !String.IsNullOrEmpty(args.Arguments))
    {
        // When the navigation stack isn't restored or there are launch arguments
        // indicating an alternate launch (e.g.: via toast or secondary tile),
        // navigate to the appropriate page, configuring the new page by passing required
        // information as a navigation parameter
        if (!rootFrame.Navigate(typeof(MainPage), args.Arguments))
        {
            throw new Exception("Failed to create initial page");
        }
    }
    // Ensure the current window is active
    Window.Current.Activate();
}
```

## Step 6: Access notification details

Because the background task can't directly launch the foreground app, the print notification details need to be saved to the app's settings so that the foreground app can access them. For more info about using local storage, see [Quickstart: local app data](/previous-versions/windows/apps/hh700361(v=win.10)).

This example shows how the printer name and Bidi message are be retrieved from app settings in the [Print settings and print notifications](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Print%20settings%20and%20print%20notifications) sample. The code is from the `DisplayBackgroundTaskTriggerDetails` method of the **InkLevel.xaml.cs** file. Note that the key index values, `keyPrinterName` and `keyAsyncUIXML`, are the same string constants that are used in the background task, **PrintBackgroundTask.cs**.

```csharp
void DisplayBackgroundTaskTriggerDetails()
{
    String outputText = "\r\n";

    try
    {
        string printerName = settings.Values[keyPrinterName].ToString();
        outputText += ("Printer name from background task triggerDetails: " + printerName);
    }
    catch (Exception)
    {
        outputText += ("No printer name retrieved from background task triggerDetails ");
    }

    outputText += "\r\n";
    try
    {
        string asyncUIXML = settings.Values[keyAsyncUIXML].ToString();
        outputText += ("AsyncUI xml from background task triggerDetails: " + asyncUIXML);
    }
    catch (Exception)
    {
        outputText += ("No asyncUI xml retrieved from background task triggerDetails ");
    }

    ToastOutput.Text += outputText;
}
```

## Testing

Before you can test your UWP device app, it must be linked to your printer using device metadata.

You need a copy of the device metadata package for your printer, to add the device app info to it. If you don't have device metadata, you can build it using the **Device Metadata Authoring Wizard** as described in the topic [Create device metadata for your UWP device app](./step-2--create-device-metadata.md).

To use the **Device Metadata Authoring Wizard**, you must install Microsoft Visual Studio Professional, Microsoft Visual Studio Ultimate, or the [standalone SDK for Windows 8.1](https://developer.microsoft.com/windows/hardware/), before completing the steps in this topic. Installing Microsoft Visual Studio Express for Windows installs a version of the SDK that doesn't include the wizard.

The following steps build your app and install the device metadata.

1. Enable test signing.

    1. Start the **Device Metadata Authoring Wizard** from *%ProgramFiles(x86)%*\\Windows Kits\\8.1\\bin\\x86, by double-clicking **DeviceMetadataWizard.exe**

    1. From the **Tools** menu, select **Enable Test Signing**.

1. Reboot the computer

1. Build the solution by opening the solution (.sln) file. Press F7 or go to **Build-&gt;Build Solution** from the top menu after the sample has loaded.

1. Disconnect and uninstall the printer. This step is required so that Windows will read the updated device metadata the next time the device is detected.

1. Edit and save device metadata. To link the device app to your device, you must associate the device app with your device.

    If you haven't created your device metadata yet, see [Create device metadata for your UWP device app](./step-2--create-device-metadata.md).

    1. If the **Device Metadata Authoring Wizard** is not open yet, start it from *%ProgramFiles(x86)%*\\Windows Kits\\8.1\\bin\\x86, by double-clicking **DeviceMetadataWizard.exe**.

    1. Click **Edit Device Metadata**. This will let you edit your existing device metadata package.

    1. In the **Open** dialog box, locate the device metadata package associated with your UWP device app. (It has a **devicemetadata-ms** file extension.)

    1. On the **Specify UWP device app information** page, enter the Microsoft Store app info in the **UWP device app** box. Click on **Import UWP app manifest file** to automatically enter the **Package name**, **Publisher name**, and **UWP app ID**.

    1. If your app is registering for printer notifications, fill out the **Notification handlers** box. In **Event ID**, enter the name of the print event handler. In **Event Asset**, enter the name of the file where that code resides.

    1. When you're done, click **Next** until you get to the **Finish** page.

    1. On the **Review the device metadata package** page, make sure that all of the settings are correct and select the **Copy the device metadata package to the metadata store on the local computer** check box. Then click **Save**.

1. Reconnect your printer so that Windows reads the updated device metadata when the device is connected.

## Troubleshooting

### Issue: No default toast notification appears

If no default print notification appears when expected...

- **Possible cause:** Test signing is not turned on. See the Debugging section in this topic for info about turning it on.

- **Possible cause:** Domain policies have disabled toast notifications. Leave the domain and try again.

- **Possible cause:** The printer has not implemented DriverEvents. Check that your v4 driver supports Bidi and DriverEvents. For more info, see [Driver Support for Customized UI](../print/driver-support-for-customized-ui.md).

- **Possible cause:** The machine has no recent job in the printer queue. Make sure the printer icon is shown in the lower right hand corner of your screen. If not, send another print job.

- **Possible cause:** Your entry point for the background task (`IBackgroundTask`) is within the same project as your foreground app. This is not allowed. Separate out an entirely new class for your background task handler.

- **Possible cause:** The class that is the entry point for notifications in your app is incorrectly given in your manifest or device metadata, causing the app to crash within the backgroundhost and not showing any toast. Check the following:

  - Make sure the entry point is given correctly in the **Declarations** tab of the Manifest Designer. It should be in the form of Namespace.ClassName for C# and C++. For JavaScript, it should be the relative directory path to the .js file.

  - A JavaScript app should call close() after it is finished.

  - The C# class has to implement Windows.ApplicationModel.Background.IBackgroundTask and has to have a public void `Run(Windows.ApplicationModel.Background.IBackgroundTaskInstance taskInstance)` method.
  
  - The C++ class has to implement Windows::ApplicationModel::Background::IBackgroundTask and has to have a `virtual void Run(Windows::ApplicationModel::Background::IBackgroundTaskInstance^ taskInstance)` method.

## Related topics

[Badge overview (UWP apps)](/previous-versions/windows/apps/hh779719(v=win.10))

[Tile and tile notification overview (UWP apps)](/previous-versions/windows/apps/hh779724(v=win.10))

[Guidelines and checklist for tiles and badges (UWP apps)](/windows/uwp/design/shell/tiles-and-notifications/creating-tiles)

[Toast notification overview (UWP apps)](/previous-versions/windows/apps/hh779727(v=win.10))

[Guidelines and checklist for toast notifications (UWP apps)](/windows/uwp/design/shell/tiles-and-notifications/)

[Driver Support for Customized UI](../print/driver-support-for-customized-ui.md)

[Developing v4 print drivers](../print/v4-printer-driver.md)

[Printer Extension Interfaces (v4 Print Driver)](/windows-hardware/drivers/ddi/_print/)

[Bidirectional Communications](../print/bidirectional-communication.md)

[Getting started with UWP apps](getting-started.md)

[Create a UWP device app (step-by-step guide)](step-1--create-a-uwp-device-app.md)

[Create device metadata for a UWP device app (step-by-step guide)](step-2--create-device-metadata.md)
