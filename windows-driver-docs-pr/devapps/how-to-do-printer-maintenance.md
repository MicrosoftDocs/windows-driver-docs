---
title: How to do printer maintenance in a UWP device app
description: In Windows 8.1, UWP device apps can perform printer maintenance, such as aligning print heads and cleaning nozzles.
ms.assetid: 52141F66-872A-4381-92C8-B04ABDABA7AD
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to do printer maintenance in a UWP device app


In Windows 8.1, UWP device apps can perform printer maintenance, such as aligning print heads and cleaning nozzles. This topic uses the C# version of the [Print job management and printer maintenance](http://go.microsoft.com/fwlink/p/?LinkID=299829) sample to demonstrate how bidirectional communication (Bidi) can be used to perform such device maintenance. To learn more about UWP device apps in general, see [Meet UWP device apps](meet-uwp-device-apps.md).

The C# version of the [Print job management and printer maintenance](http://go.microsoft.com/fwlink/p/?LinkID=299829) sample demonstrates printer maintenance with the **DeviceMaintenance.xaml.cs** file in the **DeviceAppForPrinters2** project. To work with Bidi, the sample uses the printer extension library in the **PrinterExtensionLibrary** project. The printer extension library provides a convenient way to access the printer extension interfaces of the v4 print driver. For more info, see the [Printer extension library overview](printer-extension-library-overview.md).

**Note**  The code examples shown in this topic are based on the C# version of the [Print job management and printer maintenance](http://go.microsoft.com/fwlink/p/?LinkID=299829) sample. This sample is also available in JavaScript and C++. Note that because C++ can access COM directly, the C++ version of the sample does not include code library projects. Download the samples to see the latest versions of the code.

 

## <span id="Printer_maintenance"></span><span id="printer_maintenance"></span><span id="PRINTER_MAINTENANCE"></span>Printer maintenance


Windows 8.1 introduces new printer extension interfaces in the v4 printer driver that you can use for implementing device maintenance: [**IPrinterBidiSetRequestCallback**](https://msdn.microsoft.com/library/windows/hardware/dn265385), [**IPrinterExtensionAsyncOperation**](https://msdn.microsoft.com/library/windows/hardware/dn265387) , and [**IPrinterQueue2**](https://msdn.microsoft.com/library/windows/hardware/dn265389). These interfaces make it possible to asynchronously send Bidi requests to the port monitor so that they can be translated into device and protocol-specific commands, and then sent to the printer. For more info, see [Device Maintenance (v4 Printer Driver)](https://msdn.microsoft.com/library/windows/hardware/dn265274).

**Tip**  C# and JavaScript apps can't work with COM APIs directly. If you're writing a C# or JavaScript UWP device app, use the printer extension library to access these interfaces (as shown in this topic).

 

## <span id="Prerequisites"></span><span id="prerequisites"></span><span id="PREREQUISITES"></span>Prerequisites


Before you get started:

1.  Make sure your printer is installed using a v4 print driver. For more info, see [Developing v4 print drivers](http://go.microsoft.com/fwlink/p/?LinkId=314231).
2.  Get your development PC set up. See [Getting started](getting-started.md) for info about downloading the tools and creating a developer account.
3.  Associate your app with the store. See [Create a UWP device app](step-1--create-a-uwp-device-app.md) for info about that.
4.  Create device metadata for your printer that associates it with your app. See [Create device metadata](step-2--create-device-metadata.md) for more about that.
5.  Build the UI for the main page of your app. All UWP device apps can be launched from Start, where they'll be displayed full-screen. Use the Start experience to highlight your product or services in a way that matches the specific branding and features of your devices. There are no special restrictions on the type of UI controls it can use. To get started with the design of the full-screen experience, see the [Microsoft Store design principles](http://go.microsoft.com/fwlink/p/?LinkID=299845).
6.  If you're writing you're writing your app with C# or JavaScript, add the **PrinterExtensionLibrary** project to your UWP device app solution. You can find this project in the [Print job management and printer maintenance](http://go.microsoft.com/fwlink/p/?LinkID=299829) sample.
    **Note**  Because C++ can access COM directly, C++ apps do not require a separate library to work with the COM-based printer device context.

     

## <span id="Step_1__Prepare_Bidi_request"></span><span id="step_1__prepare_bidi_request"></span><span id="STEP_1__PREPARE_BIDI_REQUEST"></span>Step 1: Prepare Bidi request


The device maintenance interfaces require that your Bidi requests are XML data in the form of a string. You can construct your Bidi requests wherever it makes sense in your app. For example, you could save the Bidi requests as string constants or dynamically create them based on user input. The [Print job management and printer maintenance](http://go.microsoft.com/fwlink/p/?LinkID=299829) sample happens to construct a default request in `OnNavigatedTo` method. For more info about Bidi, see [Bidirectional Communications](http://go.microsoft.com/fwlink/p/?LinkId=317192).

This example is from the `OnNavigatedTo` method of the **DeviceMaintenance.xaml.cs** file.

```CSharp
string defaultBidiQuery =
    "<bidi:Set xmlns:bidi=\"http://schemas.microsoft.com/windows/2005/03/printing/bidi\">\r\n" +
    "    <Query schema=&#39;\\Printer.Maintenance:CleanHead&#39;>\r\n" +
    "        <BIDI_BOOL>false</BIDI_BOOL>\r\n" +
    "    </Query>\r\n" +
    "</bidi:Set>";
```

## <span id="Step_2__Find_printer"></span><span id="step_2__find_printer"></span><span id="STEP_2__FIND_PRINTER"></span>Step 2: Find printer


Before your app can send commands to the printer, it must first locate the printer. To do this, the [Print job management and printer maintenance](http://go.microsoft.com/fwlink/p/?LinkID=299829) sample includes a handy class named `PrinterEnumeration` (in the **PrinterEnumeration.cs** file). This class finds all the printers that are associated with your app via device metadata, and returns a list of `PrinterInfo` objects, which contains the names and device IDs for each printer.

This example is from the `EnumeratePrinters_Click` method of the **DeviceMaintenance.xaml.cs** file. It shows how the sample uses the `PrinterEnumeration` class to get a list of associated printers.

```CSharp
private async void EnumeratePrinters_Click(object sender, RoutedEventArgs e)
{
    try
    {
        rootPage.NotifyUser("Enumerating printers. Please wait", NotifyType.StatusMessage);

        // Retrieve the running app&#39;s package family name, and enumerate associated printers.
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

**Tip**  For more info about the `PrinterEnumeration` and `PrinterInfo` classes, see the **PrinterEnumeration.cs** file.

 

## <span id="Step_3__Send_Bidi_request"></span><span id="step_3__send_bidi_request"></span><span id="STEP_3__SEND_BIDI_REQUEST"></span>Step 3: Send Bidi request


To send the Bidi request, the device maintenance interfaces require a Bidi string and a callback. In the `SendBidiRequest_Click` method, the sample first uses a `PrinterInfo` object to create a printer extension context object named `context`. Then a `PrinterBidiSetRequestCallback` object is created, and an event handler is added to handle the callback's `OnBidiResponseReceived` event. Finally, the printer extension context's `SendBidiSetRequestAsync` method is used to send the Bidi string and callback.

This example is from the `SendBidiRequest_Click` method of the **DeviceMaintenance.xaml.cs** file.

```CSharp
private void SendBidiRequest_Click(object sender, RoutedEventArgs e)
{
    try
    {
        PrinterInfo queue = (PrinterInfo)PrinterComboBox.SelectedItem;

        // Retrieve a COM IPrinterExtensionContext object, using the static WinRT factory.
        // Then instantiate one "PrinterExtensionContext" object that allows operations on the COM object.
        Object comComtext = Windows.Devices.Printers.Extensions.PrintExtensionContext.FromDeviceId(queue.DeviceId);
        PrinterExtensionContext context = new PrinterExtensionContext(comComtext);

        // Create an instance of the callback object, and perform an asynchronous &#39;bidi set&#39; operation.
        PrinterBidiSetRequestCallback callback = new PrinterBidiSetRequestCallback();

        // Add an event handler to the callback object&#39;s OnBidiResponseReceived event.
        // The event handler will be invoked once the Bidi response is received.
        callback.OnBidiResponseReceived += OnBidiResponseReceived;

        // Send the Bidi "Set" query asynchronously.
        IPrinterExtensionAsyncOperation operationContext
            = context.Queue.SendBidiSetRequestAsync(BidiQueryInput.Text, callback);

        // Note: The &#39;operationContext&#39; object can be used to cancel the operation if required.
    }
    catch (Exception exception)
    {
        rootPage.NotifyUser("Caught an exception: " + exception.Message, NotifyType.ErrorMessage);
    }
}
```

## <span id="Step_4__Receive_Bidi_response"></span><span id="step_4__receive_bidi_response"></span><span id="STEP_4__RECEIVE_BIDI_RESPONSE"></span>Step 4: Receive Bidi response


When the Bidi "set" operation is completed, the callback object, of type `PrinterBidiSetRequestCallback`, is invoked. This callback takes care of the error handling from the HRESULT response and then triggers the `OnBidiResponseReceived` event, sending the Bidi response through the event parameters.

This example shows the `PrinterBidiSetRequestCallback` class definition in the **DeviceMaintenance.xaml.cs** file.

```CSharp
internal class PrinterBidiSetRequestCallback : IPrinterBidiSetRequestCallback
{
    /// <summary>
    /// This method is invoked when the asynchronous Bidi "Set" operation is completed.
    /// </summary>
    public void Completed(string response, int statusHResult)
    {
        string result;

        if (statusHResult == (int)HRESULT.S_OK)
        {
            result = "The response is \r\n" + response;
        }
        else
        {
            result = "The HRESULT received is: 0x" + statusHResult.ToString("X") + "\r\n" +
                     "No Bidi response was received";
        }

        // Invoke the event handlers when the Bidi response is received.
        OnBidiResponseReceived(null, result);
    }

    /// <summary>
    /// This event will be invoked when the Bidi &#39;set&#39; response is received.
    /// </summary>
    public event EventHandler<string> OnBidiResponseReceived;
}
```

The Bidi response is then sent to the `OnBidiResponseReceived` method, where the `Dispatcher` is used to display the results on the UI thread.

This example is from the `OnBidiResponseReceived` method of the **DeviceMaintenance.xaml.cs** file.

```CSharp
internal async void OnBidiResponseReceived(object sender, string bidiResponse)
{
    await Dispatcher.RunAsync(Windows.UI.Core.CoreDispatcherPriority.Normal, () =>
    {
        BidiResponseOutput.Text = bidiResponse;
    });
}
```

## <span id="testing"></span><span id="TESTING"></span>Testing


Before you can test your UWP device app, it must be linked to your printer using device metadata.

-   You need a copy of the device metadata package for your printer, to add the device app info to it. If you don’t have device metadata, you can build it using the **Device Metadata Authoring Wizard** as described in the topic [Create device metadata for your UWP device app](http://go.microsoft.com/fwlink/p/?LinkId=313644).

    **Note**  To use the **Device Metadata Authoring Wizard**, you must install Microsoft Visual Studio Professional, Microsoft Visual Studio Ultimate, or the [standalone SDK for Windows 8.1](http://go.microsoft.com/fwlink/p/?linkid=309209), before completing the steps in this topic. Installing Microsoft Visual Studio Express for Windows installs a version of the SDK that doesn't include the wizard.

     

The following steps build your app and install the device metadata.

1.  Enable test signing.
    1.  Start the **Device Metadata Authoring Wizard** from *%ProgramFiles(x86)%*\\Windows Kits\\8.1\\bin\\x86, by double-clicking **DeviceMetadataWizard.exe**
    2.  From the **Tools** menu, select **Enable Test Signing**.

2.  Reboot the computer
3.  Build the solution by opening the solution (.sln) file. Press F7 or go to **Build-&gt;Build Solution** from the top menu after the sample has loaded.

4.  Disconnect and uninstall the printer. This step is required so that Windows will read the updated device metadata the next time the device is detected.
5.  Edit and save device metadata. To link the device app to your device, you must associate the device app with your device.
    **Note**  If you haven't created your device metadata yet, see [Create device metadata for your UWP device app](http://go.microsoft.com/fwlink/p/?LinkId=313644).

     

    1.  If the **Device Metadata Authoring Wizard** is not open yet, start it from *%ProgramFiles(x86)%*\\Windows Kits\\8.1\\bin\\x86, by double-clicking **DeviceMetadataWizard.exe**.
    2.  Click **Edit Device Metadata**. This will let you edit your existing device metadata package.
    3.  In the **Open** dialog box, locate the device metadata package associated with your UWP device app. (It has a **devicemetadata-ms** file extension.)
    4.  On the **Specify UWP device app information** page, enter the Microsoft Store app info in the **UWP device app** box. Click on **Import UWP app manifest file** to automatically enter the **Package name**, **Publisher name**, and **UWP app ID**.
    5.  If your app is registering for printer notifications, fill out the **Notification handlers** box. In **Event ID**, enter the name of the print event handler. In **Event Asset**, enter the name of the file where that code resides.

    6.  When you're done, click **Next** until you get to the **Finish** page.
    7.  On the **Review the device metadata package** page, make sure that all of the settings are correct and select the **Copy the device metadata package to the metadata store on the local computer** check box. Then click **Save**.

6.  Reconnect your printer so that Windows reads the updated device metadata when the device is connected.

## <span id="related_topics"></span>Related topics


[Device Maintenance (v4 Printer Driver)](https://msdn.microsoft.com/library/windows/hardware/dn265274)

[Developing v4 print drivers](http://go.microsoft.com/fwlink/p/?LinkId=314231)

[Bidirectional Communications](http://go.microsoft.com/fwlink/p/?LinkId=317192)

[Getting started with UWP apps](getting-started.md)

[Create a UWP device app (step-by-step guide)](step-1--create-a-uwp-device-app.md)

[Create device metadata for a UWP device app (step-by-step guide)](step-2--create-device-metadata.md)

 

 






