---
title: How to Manage Print Jobs in a UWP Device App
description: In Windows 8.1, UWP device apps for printers can manage print jobs.
ms.date: 03/17/2023
---

# How to manage print jobs in a UWP device app

In Windows 8.1, UWP device apps for printers can manage print jobs. This topic uses the C# version of the [Print job management and printer maintenance](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Print%20job%20management%20and%20printer%20maintenance) sample to demonstrate how to create a view of print jobs, monitor those jobs, and if necessary, cancel a job. To learn more about UWP device apps in general, see [Meet UWP device apps](meet-uwp-device-apps.md).

The C# version of the [Print job management and printer maintenance](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Print%20job%20management%20and%20printer%20maintenance) sample demonstrates printer maintenance with the **DeviceMaintenance.xaml.cs** file in the **DeviceAppForPrinters2** project. To work with Bidi, the sample uses the printer extension library in the **PrinterExtensionLibrary** project. The printer extension library provides a convenient way to access the printer extension interfaces of the v4 print driver. For more info, see the [Printer extension library overview](printer-extension-library-overview.md).

The code examples shown in this topic are based on the C# version of the [Print job management and printer maintenance](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Print%20job%20management%20and%20printer%20maintenance) sample. This sample is also available in JavaScript and C++. Note that because C++ can access COM directly, the C++ version of the sample does not include code library projects. Download the samples to see the latest versions of the code.

## Managing print jobs

Windows 8.1 introduces new printer extension interfaces in the v4 printer driver that you can use for managing print jobs: [**IPrinterQueue2**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterqueue2), [**IPrinterQueueView**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterqueueview), [**IPrinterQueueViewEvent**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterqueueviewevent), [**IPrintJob**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintjob), and [**IPrintJobCollection**](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintjobcollection). These interfaces make it possible to monitor and cancel print jobs. For more info, see [Print job management (v4 Printer Driver)](../print/job-management.md).

C# and JavaScript apps can't work with COM APIs directly. If you're writing a C# or JavaScript UWP device app, use the printer extension library to access these interfaces (as shown in this topic).

## Prerequisites

Before you get started:

1. Make sure your printer is installed using a v4 print driver. For more info, see [Developing v4 print drivers](../print/v4-printer-driver.md).

1. Get your development PC set up. See [Getting started](getting-started.md) for info about downloading the tools and creating a developer account.

1. Associate your app with the store. See [Create a UWP device app](step-1--create-a-uwp-device-app.md) for info about that.

1. Create device metadata for your printer that associates it with your app. See [Create device metadata](step-2--create-device-metadata.md) for more about that.

1. Build the UI for the main page of your app. All UWP device apps can be launched from Start, where they'll be displayed full-screen. Use the Start experience to highlight your product or services in a way that matches the specific branding and features of your devices. There are no special restrictions on the type of UI controls it can use. To get started with the design of the full-screen experience, see the [Microsoft Store design principles](/windows/uwp/design/).

1. If you're writing you're writing your app with C# or JavaScript, add the **PrinterExtensionLibrary** project to your UWP device app solution. You can find this project in the [Print job management and printer maintenance](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Print%20job%20management%20and%20printer%20maintenance) sample.

Because C++ can access COM directly, C++ apps do not require a separate library to work with the COM-based printer device context.

## Step 1: Find printer

Before your app can manage print jobs, it must first locate the printer having the print jobs. To do this, the [Print job management and printer maintenance](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Print%20job%20management%20and%20printer%20maintenance) sample includes a handy class named `PrinterEnumeration` (in the **PrinterEnumeration.cs** file). This class finds all the printers that are associated with your app via device metadata, and returns a list of `PrinterInfo` objects, which contains the names and device IDs for each printer.

This example shows the `EnumeratePrinters_Click` method in the **PrintJobManagement.xaml.cs** file. It shows how the sample uses the `PrinterEnumeration` class to get a list of associated printers.

```csharp
private async void EnumeratePrinters_Click(object sender, RoutedEventArgs e)
{
    try
    {
        rootPage.NotifyUser("Enumerating printers. Please wait", NotifyType.StatusMessage);

        // Retrieve the running app's package family name, and enumerate associated printers.
        string currentPackageFamilyName = Windows.ApplicationModel.Package.Current.Id.FamilyName;

        // Enumerate associated printers.
        PrinterEnumeration pe = new PrinterEnumeration(currentPackageFamilyName);
        List<PrinterInfo> associatedPrinters = await pe.EnumeratePrintersAsync();

        // Update the data binding source on the combo box that displays the list of printers.
        PrinterComboBox.ItemsSource = associatedPrinters;
        if (associatedPrinters.Count > 0)
        {
            PrinterComboBox.SelectedIndex = 0;
            rootPage.NotifyUser(associatedPrinters.Count + " printers enumerated", NotifyType.StatusMessage);
        }
        else
        {
            rootPage.NotifyUser(DisplayStrings.NoPrintersEnumerated, NotifyType.ErrorMessage);
        }
    }
    catch (Exception exception)
    {
        rootPage.NotifyUser("Caught an exception: " + exception.Message, NotifyType.ErrorMessage);
    }
}
```

For more info about the `PrinterEnumeration` and `PrinterInfo` classes, see the **PrinterEnumeration.cs** file.

## Step 2: Get printer queue

Once you've identified the printer having the print jobs that you want to manage, create a *view* of the print jobs, with object based on the `IPrinterQueueView` interface (defined in the **PrinterExtensionTypes.cs** file of the **PrinterExtensionLibrary** project). In the [Print job management and printer maintenance](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Print%20job%20management%20and%20printer%20maintenance) sample, this object is named `currentPrinterQueueView` and is re-created each time the printer selection changes.

In the `Printer_SelectionChanged` method, the sample first uses a `PrinterInfo` object to create a printer extension context object named `context`. Then it uses the `GetPrinterQueueView` method on the `context` to create the `currentPrinterQueueView` object. Finally, an event handler is added to handle the `currentPrinterQueueView`'s `OnChanged` event.

This example shows the `Printer_SelectionChanged` method in the **PrintJobManagement.xaml.cs** file. It shows how to create a printer queue view object based on `IPrinterQueueView`.

```csharp
private void Printer_SelectionChanged(object sender, SelectionChangedEventArgs e)
{
    try
    {
        // Remove the current printer queue view (if any) before displaying the new view.
        if (currentPrinterQueueView != null)
        {
            currentPrinterQueueView.OnChanged -= OnPrinterQueueViewChanged;
            currentPrinterQueueView = null;
        }

        // Retrieve a COM IPrinterExtensionContext object, using the static WinRT factory.
        // Then instantiate one "PrinterExtensionContext" object that allows operations on the COM object.
        PrinterInfo queue = (PrinterInfo)PrinterComboBox.SelectedItem;
        Object comContext = Windows.Devices.Printers.Extensions.PrintExtensionContext.FromDeviceId(queue.DeviceId);
        PrinterExtensionContext context = new PrinterExtensionContext(comContext);

        // Display the printer queue view.
        const int FirstPrintJobEnumerated = 0;
        const int LastPrintJobEnumerated = 10;

        currentPrinterQueueView = context.Queue.GetPrinterQueueView(FirstPrintJobEnumerated, LastPrintJobEnumerated);
        currentPrinterQueueView.OnChanged += OnPrinterQueueViewChanged;
    }
    catch (Exception exception)
    {
        rootPage.NotifyUser("Caught an exception: " + exception.Message, NotifyType.ErrorMessage);
    }
}
```

Also, whenever there is a change to the view of the print jobs, an event handler calls the `OnPrinterQueueViewChanged` method. This method is responsible for re-binding the `PrintJobListBox` with an IEnumerable collection of `IPrintJob` objects. The collection is passed to the method via the `PrinterQueueViewEventArgs` object, which is defined in the **PrinterExtensionTypes.cs** file.

This example shows the `OnPrinterQueueViewChanged` method in the **PrintJobManagement.xaml.cs** file.

```csharp
private async void OnPrinterQueueViewChanged(object sender, PrinterQueueViewEventArgs e)
{
    await Dispatcher.RunAsync(Windows.UI.Core.CoreDispatcherPriority.Normal, () =>
    {
        // Update the data binding on the ListBox that displays print jobs.
        PrintJobListBox.ItemsSource = e.Collection;
        if (PrintJobListBox.Items.Count > 0)
        {
            // If there are print jobs in the current view, mark the first job as selected.
            PrintJobListBox.SelectedIndex = 0;
        }
    });
}
```

## Step 3: Display print job status

Because the `PrintJobListBox` is bound to a collection of `IPrintJob` objects, displaying the status of a job is fairly straightforward. The selected print job is cast as an `IPrintJob` object, and then the properties of that object are used to fill the `PrintJobDetails` TextBox.

In the [Print job management and printer maintenance](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Print%20job%20management%20and%20printer%20maintenance) sample, the print job status is displayed each time a different print job is selected. This update is taken care of by the `PrintJob_SelectionChanged` method.

This example shows the `PrintJob_SelectionChanged` method in the **PrintJobManagement.xaml.cs** file. It shows how to display the status of a print job, based on an `IPrintJob` object.

```csharp
private void PrintJob_SelectionChanged(object sender, SelectionChangedEventArgs e)
{
    try
    {
        // Display details of the selected print job.
        IPrintJob job = (IPrintJob)PrintJobListBox.SelectedItem;
        if (job != null)
        {
            PrintJobDetails.Text =
                "Details of print job: " + job.Name + "\r\n" +
                "Pages printed: " + job.PrintedPages + "/" + job.TotalPages + "\r\n" +
                "Submission time: " + job.SubmissionTime + "\r\n" +
                "Job status: " + DisplayablePrintJobStatus.ToString(job.Status);
        }
        else
        {
            PrintJobDetails.Text = "Please select a print job";
        }
    }
    catch (Exception exception)
    {
        rootPage.NotifyUser("Caught an exception: " + exception.Message, NotifyType.ErrorMessage);
    }
}
```

To help display the print job status description, the `PrintJob_SelectionChanged` method uses a static dictionary, named `printJobStatusDisplayNames`, to help display job status descriptions that are in a user-friendly text format.

This example shows the `DisplayablePrintJobStatus` class in the **PrintJobManagement.xaml.cs** file. This class contains the static members used by the `PrintJob_SelectionChanged`.

```csharp
internal class DisplayablePrintJobStatus
{
    /// <summary>
    /// Converts the PrintJobStatus bit fields to a display string.
    /// </summary>
    internal static string ToString(PrintJobStatus printJobStatus)
    {
        StringBuilder statusString = new StringBuilder();

        // Iterate through each of the PrintJobStatus bits that are set and convert it to a display string.
        foreach (var printJobStatusDisplayName in printJobStatusDisplayNames)
        {
            if ((printJobStatusDisplayName.Key & printJobStatus) != 0)
            {
                statusString.Append(printJobStatusDisplayName.Value);
            }
        }

        int stringlen = statusString.Length;
        if (stringlen > 0)
        {
            // Trim the trailing comma from the string.
            return statusString.ToString(0, stringlen - 1);
        }
        else
        {
            // If no print job status field was set, display "Not available".
            return "Not available";
        }
    }

    /// <summary>
    /// Static constructor that initializes the display name for the PrintJobStatus field.
    /// </summary>
    static DisplayablePrintJobStatus()
    {
        printJobStatusDisplayNames = new Dictionary<PrintJobStatus, string>();

        printJobStatusDisplayNames.Add(PrintJobStatus.Paused, "Paused,");
        printJobStatusDisplayNames.Add(PrintJobStatus.Error, "Error,");
        printJobStatusDisplayNames.Add(PrintJobStatus.Deleting, "Deleting,");
        printJobStatusDisplayNames.Add(PrintJobStatus.Spooling, "Spooling,");
        printJobStatusDisplayNames.Add(PrintJobStatus.Printing, "Printing,");
        printJobStatusDisplayNames.Add(PrintJobStatus.Offline, "Offline,");
        printJobStatusDisplayNames.Add(PrintJobStatus.PaperOut, "Out of paper,");
        printJobStatusDisplayNames.Add(PrintJobStatus.Printed, "Printed,");
        printJobStatusDisplayNames.Add(PrintJobStatus.Deleted, "Deleted,");
        printJobStatusDisplayNames.Add(PrintJobStatus.BlockedDeviceQueue, "Blocked device queue,");
        printJobStatusDisplayNames.Add(PrintJobStatus.UserIntervention, "User intervention required,");
        printJobStatusDisplayNames.Add(PrintJobStatus.Restarted, "Restarted,");
        printJobStatusDisplayNames.Add(PrintJobStatus.Complete, "Complete,");
        printJobStatusDisplayNames.Add(PrintJobStatus.Retained, "Retained,");
    }
    
    /// <summary>
    /// Private constructor to prevent default instantiation.
    /// </summary>
    private DisplayablePrintJobStatus() { }

    /// <summary>
    /// Contains the mapping between PrintJobStatus fields and display strings.
    /// </summary>
    private static Dictionary<PrintJobStatus, string> printJobStatusDisplayNames;
}
```

## Step 4: Cancel print job

Similar to displaying print job status, cancelling a print job is fairly straightforward when you have an `IPrintJob` object. The `IPrintJob` class provides a `RequestCancel` method that initiates the cancellation of the corresponding print job. This is demonstrated in the sample's `CancelPrintJob_Click` method.

This example shows the `CancelPrintJob_Click` method in the **PrintJobManagement.xaml.cs** file.

```csharp
private void CancelPrintJob_Click(object sender, RoutedEventArgs e)
{
    try
    {
        IPrintJob job = (IPrintJob)PrintJobListBox.SelectedItem;
        job.RequestCancel();
    }
    catch (Exception exception)
    {
        rootPage.NotifyUser("Caught an exception: " + exception.Message, NotifyType.ErrorMessage);
    }
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

## Related topics

[Job Management (v4 Printer Driver)](../print/job-management.md)

[Developing v4 print drivers](../print/v4-printer-driver.md)

[Bidirectional Communications](../print/bidirectional-communication.md)

[Getting started with UWP apps](getting-started.md)

[Create a UWP device app (step-by-step guide)](step-1--create-a-uwp-device-app.md)

[Create device metadata for a UWP device app (step-by-step guide)](step-2--create-device-metadata.md)
