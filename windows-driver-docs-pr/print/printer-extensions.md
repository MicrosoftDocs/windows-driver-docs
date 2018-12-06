---
title: Printer Extensions
description: Printer extension apps support print preferences and printer notifications when users run existing applications on the Windows desktop.
ms.assetid: D617A897-D93E-4006-B42D-923CA7F29D7E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Printer Extensions

Printer extension apps support print preferences and printer notifications when users run existing applications on the Windows desktop.

## Introduction

Printer extensions can be built in any COM-capable language, but are optimized to be built using Microsoft .NET Framework 4. Printer extensions may be distributed with a print driver package, if they are XCopy-capable and have no dependencies on external runtimes other than those included with the operating system, like for example, .NET. If the printer extension app doesn't meet these criteria, it could be distributed in a setup.exe or an MSI package, and advertised in the printer's Device Stage experience by using the PrinterExtensionUrl directive specified in the v4 manifest. When a printer extension app is distributed via an MSI package, you have the option of adding the print driver to the package or leaving it out and distributing the driver separately. The PrinterExtensionUrl is shown on the printer preferences experience.

IT administrators have a few options for managing the distribution of printer extensions. If the application is packaged in a setup.exe or MSI, then IT administrators can use standard software distribution tools such as System Center Configuration Manager (SCCM), or they can include the applications in their standard OS image. IT administrators can also override the PrinterExtensionUrl specified in the v4 manifest, if they edit HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Print\\Printers\\&lt;print queue name&gt;\\PrinterDriverData\\PrinterExtensionUrl.

And if an enterprise chooses to block printer extensions altogether, this can be done via a group policy called "Computer Configuration\\Administrative Templates\\Printers\\Do not allow v4 printer drivers to show printer extension applications".

## Building a printer extension

The [Printer Extension Sample](http://go.microsoft.com/fwlink/p/?LinkId=617945) on GitHub shows how to build a printer extension using C#. In order to allow code sharing between UWP device apps and printer extensions, this sample uses two projects: PrinterExtensionLibrary (a C) and ExtensionSample (a printer extension that is dependent on the PrinterExtensionLibrary).

The code snippets shown in this topic are all taken from the PrinterExtensionSample solution. If you are building a printer extension in C, C++ or some other COM-based language, the concepts are similar but the APIs must instead match those specified in *PrinterExtension.IDL*, which is included in the Windows Driver Kit. The code comments in the PrinterExtensionLibrary from the sample document also include code comments that indicate the underlying COM interface that a particular object corresponds to.

When you are developing a printer extension, there are six main areas of focus that you must be aware of. These focus areas are shown in the following list.

- Registration

- Enabling Events

- OnDriverEvent Handler

- Print Preferences

- Printer Notifications

- Managing Printers

### Registration

Printer extensions are registered with the print system by specifying a set of registry keys or by specifying the application information in the PrinterExtensions section of the v4 manifest file.

There are specified GUIDs that support each of the different entry points for printer extensions. You do not have to use these GUIDs in the v4 manifest file, but you must know the GUID values to use the registry format for v4 driver installation. The following table shows the GUID values for the two entry points.

| Entry Point           | GUID                                   |
|-----------------------|----------------------------------------|
| Print Preferences     | {EC8F261F-267C-469F-B5D6-3933023C29CC} |
| Printer Notifications | {23BB1328-63DE-4293-915B-A6A23D929ACB} |

Printer extensions that are installed outside of the printer driver need to be registered using the registry. This ensures that printer extensions can be installed regardless of the status of the spooler, or the v4 configuration module on the client machine.

Once the PrintNotify service starts, it will check for registry keys under the \[OfflineRoot\] path and process any pending registrations or unregistrations. Once any pending registrations or unregistrations are completed, the registry keys are deleted in real time. Note that if you are using a script or iterative process to place registry keys, you may need to recreate the \\\[PrinterExtensionID\] key every time you specify a \\\[PrinterDriverId\] key. Incomplete or malformed keys are not deleted.

This registration is only necessary on first install. The following example shows the correct registry key format used for registering printer extensions.

> [!NOTE]
> **\[OfflineRoot\]** is used as shorthand for HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Print\\OfflinePrinterExtensions.

```Registry
[OfflineRoot]
    \[PrinterExtensionId] {GUID}
           AppPath=[PrinterExtensionAppPath] {String}
           \[PrinterDriverId] {GUID}
                  \[PrinterExtensionReasonGuid]
(default) = ["0"|"1"] {REG_SZ 0:Unregister, 1:Register}
                  \…
                  \[PrinterExtensionReasonGuidN]
           \[PrinterDriverId2]
                  \[PrinterExtensionReasonGuid2.1]
                  \…
                  \[PrinterExtensionReasonGuid2.Z]
           …
           \[PrinterDriverIdM]
    \[PrinterExtensionId2]
    …
    \[PrinterExtensionIdT]
```

For example, the following set of keys would register a printer extension with the {*PrinterExtensionIDGuid*} PrinterExtensionID and a fully-qualified path to the "C:\\Program Files\\Fabrikam\\pe.exe" executable for the {*PrinterDriverID1Guid*} and {*PrinterDriverID2Guid*} PrinterDriverIDs, with the printer preferences and printer notifications reasons.

```Registry
[OfflineRoot]
    \{PrinterExtensionIDGuid}
           AppPath="C:\Program Files\Fabrikam\pe.exe"
           \{PrinterDriverID1Guid}
                 \{EC8F261F-267C-469F-B5D6-3933023C29CC}
            (default) = "1"
                 \{23BB1328-63DE-4293-915B-A6A23D929ACB}
            (default) = "1"
           \{PrinterDriverID1Guid}
                 \{EC8F261F-267C-469F-B5D6-3933023C29CC}
            (default) = "1"
                 \{23BB1328-63DE-4293-915B-A6A23D929ACB}
            (default) = "1"
```

To uninstall the same printer extension, the following set of keys should be specified.

```Registry
[OfflineRoot]
    \{PrinterExtensionIDGuid}
           AppPath="C:\Program Files\Fabrikam\pe.exe"
           \{PrinterDriverID1Guid}
                 \{EC8F261F-267C-469F-B5D6-3933023C29CC}
            (default) = "0"
                 \{23BB1328-63DE-4293-915B-A6A23D929ACB}
            (default) = "0"
           \{PrinterDriverID1Guid}
                 \{EC8F261F-267C-469F-B5D6-3933023C29CC}
            (default) = "0"
                 \{23BB1328-63DE-4293-915B-A6A23D929ACB}
            (default) = "0"
```

Since printer extensions can run in both a user-launched context and an event-launched context, it is useful to be able to determine the context in which your printer extension is operating. This can allow an app to, for example, not enumerate the status on all queues if it has been launched for a notification or print preferences. Microsoft recommends that printer extensions which are installed separately from the driver (e.g. with an MSI or setup.exe) should use command line switches either on the Start menu shortcuts, or the in the AppPath entry that was populated in the registry during registration. Since printer extensions that are installed with the driver are installed to the DriverStore, these will not be launched outside the print preferences or printer notifications events. Therefore specifying command line switches is unsupported in this case.

When the printer extension registers for the current PrinterDriverID, it must include the PrinterDriverID in the AppPath. For example, for a printer extension app with the name *printerextension.exe*, and a PrinterDriverID value of *{GUID}*, the \[PrinterExtensionAppPath\] would look like the following:

```console
"C:\program files\fabrikam\printerextension.exe {GUID}"
```

### Enabling events

At runtime, printer extensions must enable event triggering for the current PrinterDriverID. This is the PrinterDriverID that was passed to the app via the args\[\] array, and it allows the print system to provide an appropriate event context for handling reasons like print preferences or printer notifications.

So the application should create a new PrinterExtensionManager for the current PrinterDriverID, register a delegate to handle the OnDriverEvent event, and call the EnableEvents method with the PrinterDriverID. The following code snippet illustrates this approach.

```csharp
PrinterExtensionManager mgr = new PrinterExtensionManager();
mgr.OnDriverEvent += OnDriverEvent;
mgr.EnableEvents(new Guid(PrinterDriverID1));
```

If an app does not call EnableEvents within 5 seconds, Windows will timeout and launch a standard UI. In order to mitigate this, printer extensions should follow the latest performance best practices, including the following:

- Delay as much of the app initialization as possible, until after you call EnableEvents. After this, prioritize UI responsiveness by using asynchronous methods and not blocking the UI thread during initialization.

- Use ngen to generate a native image during installation. For more information, see [Native Image Generator](https://msdn.microsoft.com/library/6t9t5wcf.aspx).

- Use performance measurement tools to find performance issues on loading. For more information, see [Windows Performance Analysis Tools](https://msdn.microsoft.com/performance/cc825801.aspx).

### DriverEvent handler

After an OnDriverEvent handler is registered and events are enabled, if the printer extension was launched to handle print preferences or printer notifications, then the handler will be invoked. In the preceding code snippet, a method called OnDriverEvent was registered as the event handler. In the following code snippet, the *PrinterExtensionEventArgs* parameter is the object that enables the print preferences and printer notifications scenarios to be constructed. *PrinterExtensionEventArgs* is a wrapper for [**IPrinterExtensionEventArgs**](https://msdn.microsoft.com/library/windows/hardware/hh973207).

```csharp
static void OnDriverEvent(object sender, PrinterExtensionEventArgs eventArgs)
{
    //
    // Display the print preferences window.
    //

    if (eventArgs.ReasonId.Equals(PrinterExtensionReason.PrintPreferences))
    {
        PrintPreferenceWindow printPreferenceWindow = new PrintPreferenceWindow();
        printPreferenceWindow.Initialize(eventArgs);

        //
        // Set the caller application's window as parent/owner of the newly created printing preferences window.
        //

        WindowInteropHelper wih = new WindowInteropHelper(printPreferenceWindow);
        wih.Owner = eventArgs.WindowParent;

        //
        // Display a modal/non-modal window based on the 'WindowModal' parameter.
        //

        if (eventArgs.WindowModal)
        {
            printPreferenceWindow.ShowDialog();
        }
        else
        {
            printPreferenceWindow.Show();
        }
    }

    //
    // Handle driver events.
    //

    else if (eventArgs.ReasonId.Equals(PrinterExtensionReason.DriverEvent))
    {
        // Handle driver events here.
    }
}
```

In order to prevent a bad user experience associated with crashing or slow printer extensions, Windows implements a timeout if EnableEvents is not called within a short amount of time after the app is launched. To enable debugging, this timeout is disabled if there is a debugger attached to the PrintNotify service.

In most cases, however, all the app-related code in which we're interested, runs during or after the OnDriverEvent callback. During development, it may also be useful to show a MessageBox prior to starting either a print preferences or printer notifications experience from the OnDriverEvent callback. When the MessageBox appears, go back to Visual Studio and click **Debug** &gt; **Attach to Process** and choose the name of your process. Finally, go back to your MessageBox and click OK to resume. This will ensure that you see exceptions and hit any breakpoints from that point onward.

New ReasonIds may be supported in the future. As a result, printer extensions must explicitly check the ReasonID and must not use an "else" statement to detect the last known ReasonID. If a ReasonID is received and unknown, the app should exit gracefully.

### Print preferences

Print preferences is driven by the PrintSchemaEventArgs.Ticket object. This object encapsulates both the PrintTicket and PrintCapabilities documents that describe the features and options for a device. While the underlying XML is also available, the object model makes working with these formats easier.

Inside each [**IPrintSchemaTicket**](https://msdn.microsoft.com/library/windows/hardware/hh451398) or [**IPrintSchemaCapabilities**](https://msdn.microsoft.com/library/windows/hardware/hh451256) object there are features ([**IPrintSchemaFeature**](https://msdn.microsoft.com/library/windows/hardware/hh451284)) and options ([**IPrintSchemaOption**](https://msdn.microsoft.com/library/windows/hardware/hh451335)). While the interfaces used for features and options are the same regardless of the origin, the behavior varies slightly as a result of the underlying XML. For example, PrintCapabilities documents specify many options per feature, while PrintTicket documents specify only the selected (or default) option. Similarly, PrintCapabilities documents specify localized display strings, whereas PrintTicket documents do not.

The [PrinterExtensionSample](http://go.microsoft.com/fwlink/p/?LinkId=617945) uses data binding to create ComboBox controls for printer preferences. Microsoft recommends using data binding as it makes the code much easier to maintain by reducing scattering. For more information on data binding in WPF, see [Data Binding Overview](https://msdn.microsoft.com/library/ms752347.aspx).

In order to maximize performance, Microsoft recommends that calls to GetPrintCapabilities should only be done when it is necessary to update the PrintCapabilities document.

As a user makes choices using the data bound ComboBox controls, the PrintTicket object is automatically updated. When the user finally clicks **OK**, a chain of asynchronous validation and completion begins. This asynchronous pattern is used extensively in order to prevent long running tasks from occurring on UI threads and causing hangs in either the print preferences UI or the app that is printing. The following is a list of the steps used for processing the PrintTicket changes after the user clicks **OK**.

1. The PrintSchemaTicket is validated asynchrously using the [**IPrintSchemaTicket::ValidateAsync**](https://msdn.microsoft.com/library/windows/hardware/hh451448) method.

1. When the asynchronous validation completes, the Common Language Runtime (CLR) invokes the PrintTicketValidateCompleted method.

    1. If validation was successful, it calls the CommitPrintTicketAsync method, and CommitPrintTicketAsync calls the [**IPrintSchemaTicket::CommitAsync**](https://msdn.microsoft.com/library/windows/hardware/hh451382) method. And when update PrintTicket is successfully completed, this invokes the PrintTicketCommitCompleted method, which calls a convenience method that calls the PrinterExtensionEventArgs.Request.Complete method to indicate that print preferences are complete, and then it closes the app.

    1. Otherwise, it presents UI to the user to handle the constraint situation.

If the user clicked cancel or closed the print preferences window directly, the printer extension calls IPrinterExtensionEventArgs.Request.Cancel with an appropriate HRESULT value and message for the error log.

If the process for the printer extension has closed and not called the Complete or Cancel methods as described in the preceding paragraphs, then the print system will automatically fall back to using Microsoft-provided UI.

In order to retrieve device status information, printer extensions can use Bidi to query the print device. For example, to show ink status or other kinds of status about the device, printer extensions can use the IPrinterExtensionEventArgs.PrinterQueue.SendBidiQuery method to issue Bidi queries to the device. Getting the latest Bidi status is a two-step process involving setting up an event handler for the OnBidiResponseReceived event, and calling the SendBidiQuery method with a valid Bidi query. The following code snippet shows this two-step process.

```csharp
PrinterQueue.OnBidiResponseReceived += new
EventHandler<PrinterQueueEventArgs>(OnBidiResponseReceived);
PrinterQueue.SendBidiQuery("\\Printer.consumables");
```

When the Bidi response is received, the following event handler is invoked. Note that this event handler also has a mocked ink status implementation, which may be useful for development when a device is unavailable. The PrinterQueueEventArgs object includes both an HRESULT and a Bidi XML response. For more information on Bidi XML responses, see [Bidi Request and Response Schemas](https://msdn.microsoft.com/library/windows/desktop/dd183368.aspx).

```csharp
private void OnBidiResponseReceived(object sender, PrinterQueueEventArgs e)
{
    if (e.StatusHResult != (int)HRESULT.S_OK)
    {
        MockInkStatus();
        return;
    }

    //
    // Display the ink levels from the data.
    //

    BidiHelperSource = new BidiHelper(e.Response);
    if (PropertyChanged != null)
    {
        PropertyChanged(this, new PropertyChangedEventArgs("BidiHelperSource"));
    }
    InkStatusTitle = "Ink status (Live data)";
}
```

### Printer notifications

Printer notifications are invoked in precisely the same way as print preferences. In the OnDriverEvent handler, if IPrinterExtensionEventArgs indicates that a ReasonID matches the DriverEvents GUID, then we can build an experience to handle this event.

The [PrinterExtensionSample](http://go.microsoft.com/fwlink/p/?LinkId=617945) project does not demonstrate a functional printer notifications experience, but the following variables are most helpful in handling this.

- PrinterExtensionEventArgs.BidiNotification – This carries the Bidi XML that caused the event to be triggered.

- PrinterExtensionEventArgs.DetailedReasonId – This contains the eventID GUID from the driver event xml file.

The most important attribute from the IPrinterExtensionEventArgs object for notifications is the BidiNotification property. This carries the Bidi XML that caused the event to be triggered. For more information on Bidi XML responses, see [Bidi Request and Response Schemas](https://msdn.microsoft.com/library/windows/desktop/dd183368.aspx).

### Managing printers

In order to support the role of a printer extension as an app that can be used as a hub for managing/maintaining printers, it is possible to enumerate the print queues for which the current printer extension is registered, and get the status for each queue. This is not demonstrated in the PrinterExtensionSample project, but the following code snippet could be added into the Main method of App.xaml.cs to register an event handler.

```csharp
mgr.OnPrinterQueuesEnumerated += new EventHandler<PrinterQueuesEnumeratedEventArgs>(mgr_OnPrinterQueuesEnumerated);
```

Once the queues are enumerated, the event handler is called and status operations can take place. This event fires periodically during the lifetime of the app in order to ensure that the list of enumerated print queues is current, even if the user has installed more queues since it was opened. As a result, it is important that the event handler does not create a new window each time it is executed, and this is shown in the following code snippet.

```csharp
static void mgr_OnPrinterQueuesEnumerated(object sender, PrinterQueuesEnumeratedEventArgs e)
{
    foreach (IPrinterExtensionContext pContext in e)
    {
        // show status
    }
}
```

In order to perform maintenance tasks using a printer extension, Microsoft recommends that the legacy WritePrinter API is used as outlined by the following pseudo code.

```Pseudocode
OpenPrinter
    StartDocPrinter
        StartPagePrinter
          WritePrinter
        EndPagePrinter
    EndDocPrinter
ClosePrinter
```

For more information on how to marshal these legacy APIs into .NET, see [How to send raw data to a printer by using Visual C# .NET](http://support.microsoft.com/?kbid=322091) or [How to send raw data to a printer by using Visual Basic .NET](http://support.microsoft.com/?kbid=322090).

## Printer extension performance best practices

In order to ensure the best user experience, printer extensions should be designed to load as fast as possible. The Printer Extension Sample project is a .NET application, which means that it gets built into an intermediate language (IL) that must be compiled at runtime into the appropriate format for the native processor architecture. During installation, Microsoft recommends that printer extensions are installed according to best practices, to ensure that the app has been compiled for the native system architecture. For more information about code compilation and installation best practices, see [Improving Launch Performance for Your Desktop Applications](http://blogs.msdn.com/b/dotnet/archive/2012/03/20/improving-launch-performance-for-your-desktop-applications.aspx).

Microsoft also recommends that printer extensions postpone initialization tasks such as loading resources until after the EnableEvents method has been called. This minimizes the likelihood of the app calling EnableEvents prior to the 5 second timeout for printer extensions.

After the OnDriverEvent call, printer extensions should initialize their UI and draw as quickly as possible, making use of asynchronous methods where possible to ensure responsiveness. Printer extensions should have no dependency on network calls or Bidi in order to create the initial window state for print preferences or printer notifications.

As the user makes choices using the on screen UI that affect the PrintTicket, the printer extension should make use of the IPrintSchemaTicket::ValidateAsync method in order to validate changes as early as possible. Finally, the printer extension should use the [**IPrintSchemaTicket::CommitAsync**](https://msdn.microsoft.com/library/windows/hardware/hh451382) method in order to commit the PrintTicket changes.

Printer extensions are always executed out of process from the process invoked them. So you must keep window behavior in mind when you're developing a printer extension:

- The **WindowParent** property from [**IPrinterExtensionEventArgs**](https://msdn.microsoft.com/library/windows/hardware/hh973207) specifies the handle to the window that invoked the app.
- The **WindowModal** property from [**IPrinterExtensionEventArgs**](https://msdn.microsoft.com/library/windows/hardware/hh973207) specifies whether a printer extension (in print preferences mode) should be run modally.

The Printer Extension Sample demonstrates how to create a UI that is generally launched as the topmost window. But in some cases, the UI will not be shown in the foreground, such as when the process that caused the UI to be invoked is running at a different integrity level, or when the process is compiled for a different processor architecture. In this case, the printer extension should call FlashWindowEx to request user permission to come to the foreground by flashing the icon in the taskbar.

## Related topics

[Bidi Request and Response Schemas](https://msdn.microsoft.com/library/windows/desktop/dd183368.aspx)

[Data Binding Overview](https://msdn.microsoft.com/library/ms752347.aspx)

[How to send raw data to a printer by using Visual Basic .NET](http://support.microsoft.com/?kbid=322090)

[How to send raw data to a printer by using Visual C# .NET](http://support.microsoft.com/?kbid=322091)

[Improving Launch Performance for Your Desktop Applications](http://blogs.msdn.com/b/dotnet/archive/2012/03/20/improving-launch-performance-for-your-desktop-applications.aspx)

[Native Image Generator](https://msdn.microsoft.com/library/6t9t5wcf.aspx)

[Print Schema Interfaces](https://msdn.microsoft.com/library/windows/hardware/hh464019)

[Printer Extension Sample](http://go.microsoft.com/fwlink/p/?LinkId=617945)

[Windows Performance Analysis Tools](https://msdn.microsoft.com/performance/cc825801.aspx)
