---
title: How to display printer status in a UWP device app
description: This topic uses the C# version of the Print settings and print notifications sample to demonstrate how to query the printer status and display it.
ms.assetid: 91AD1B3B-0D0B-4FB6-8A0F-4943143D8FCE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to display printer status in a UWP device app


In Windows 8.1, users can check their printer status from the modern UI of a UWP device app. This topic uses the C# version of the [Print settings and print notifications](http://go.microsoft.com/fwlink/p/?LinkID=242862) sample to demonstrate how to query the printer status and display it. To learn more about UWP device apps in general, see [Meet UWP device apps](meet-uwp-device-apps.md).

The C# version of the [Print settings and print notifications](http://go.microsoft.com/fwlink/p/?LinkID=242862) sample uses the **InkLevel.xaml** page to demonstrate how to get the printer status (in this case, the ink level) and display it. A print helper class is used to create a device context (IPrinterExtensionContext) and perform the device queries. The **PrinterHelperClass.cs** file is in the **DeviceAppForPrintersLibrary** project and uses APIs defined in the **PrinterExtensionLibrary** project. The printer extension library provides a convenient way to access the printer extension interfaces of the v4 print driver. For more info, see the [Printer extension library overview](printer-extension-library-overview.md).

**Note**  The code examples shown in this topic are based on the C# version of the [Print settings and print notifications](http://go.microsoft.com/fwlink/p/?LinkID=242862) sample. This sample is also available in JavaScript and C++. Note that because C++ can access COM directly, the C++ version of the sample does not include code library projects. Download the samples to see the latest versions of the code.

 

## <span id="Prerequisites"></span><span id="prerequisites"></span><span id="PREREQUISITES"></span>Prerequisites


Before you get started:

1.  Make sure your printer is installed using a v4 print driver. For more info, see [Developing v4 print drivers](http://go.microsoft.com/fwlink/p/?LinkId=314231).
2.  Get your development PC set up. See [Getting started](getting-started.md) for info about downloading the tools and creating a developer account.
3.  Associate your app with the store. See [Step 1: Create a UWP device app](step-1--create-a-uwp-device-app.md) for info about that.
4.  Create device metadata for your printer that associates it with your app. See [Step 2: Create device metadata](step-2--create-device-metadata.md) for more about that.
5.  If you're writing you're writing your app with C# or JavaScript, add the **PrinterExtensionLibrary** and **DeviceAppForPrintersLibrary** projects to your UWP device app solution. You can find each of these projects in the [Print settings and print notifications](http://go.microsoft.com/fwlink/p/?LinkID=242862) sample.
    **Note**  Because C++ can access COM directly, C++ apps do not require a separate library to work with the COM-based printer device context.

     

## <span id="Step_1__Find_the_printer"></span><span id="step_1__find_the_printer"></span><span id="STEP_1__FIND_THE_PRINTER"></span>Step 1: Find the printer


Before a device context can be created, the app needs to determine the device ID of the printer. To do this, the sample uses the `EnumerateAssociatedPrinters` method to search through all printers that are attached to the PC. Then it checks the container for each printer and looks for an association by comparing each container's PackageFamilyName property.

**Note**  The System.Devices.AppPackageFamilyName for devices that are associated with your app can be found under the **Packaging** tab on the Manifest Designer in Microsoft Visual Studio.

 

This example shows the `EnumerateAssociatedPrinters` method from the **InkLevel.xaml.cs** file:

```CSharp
async void EnumerateAssociatedPrinters(object sender, RoutedEventArgs e)
{
    // Reset output text and associated printer array.
    AssociatedPrinters.Items.Clear();
    BidiOutput.Text = "";

    // GUID string for printers.
    string printerInterfaceClass = "{0ecef634-6ef0-472a-8085-5ad023ecbccd}";
    string selector = "System.Devices.InterfaceClassGuid:=\"" + printerInterfaceClass + "\"";

    // By default, FindAllAsync does not return the containerId for the device it queries.
    // We have to add it as an additonal property to retrieve. 
    string containerIdField = "System.Devices.ContainerId";
    string[] propertiesToRetrieve = new string[] { containerIdField };

    // Asynchronously find all printer devices.
    DeviceInformationCollection deviceInfoCollection = await DeviceInformation.FindAllAsync(selector, propertiesToRetrieve);

    // For each printer device returned, check if it is associated with the current app.
    for (int i = 0; i < deviceInfoCollection.Count; i++)
    {
        DeviceInformation deviceInfo = deviceInfoCollection[i];
        FindAssociation(deviceInfo, deviceInfo.Properties[containerIdField].ToString());
    }
}
```

The `FindAssociation` method, called by `EnumerateAssociatedPrinters`, checks if a printer is associated with the current application. In other words, this method checks if the app is a UWP device app. This association exists when the app and printer are defined in device metadata on the local PC.

This example shows the `FindAssociation` method from the **InkLevel.xaml.cs** file:

```CSharp
async void FindAssociation(DeviceInformation deviceInfo, string containerId)
{

    // Specifically telling CreateFromIdAsync to retrieve the AppPackageFamilyName. 
    string packageFamilyName = "System.Devices.AppPackageFamilyName";
    string[] containerPropertiesToGet = new string[] { packageFamilyName };

    // CreateFromIdAsync needs braces on the containerId string.
    string containerIdwithBraces = "{" + containerId + "}";

    // Asynchoronously getting the container information of the printer.
    PnpObject containerInfo = await PnpObject.CreateFromIdAsync(PnpObjectType.DeviceContainer, containerIdwithBraces, containerPropertiesToGet);

    // Printers could be associated with other device apps, only the ones with package family name
    // matching this app&#39;s is associated with this app. The packageFamilyName for this app will be found in this app&#39;s packagemanifest
    string appPackageFamilyName = "Microsoft.SDKSamples.DeviceAppForPrinters.CS_8wekyb3d8bbwe";
    var prop = containerInfo.Properties;

    // If the packageFamilyName of the printer container matches the one for this app, the printer is associated with this app.
    string[] packageFamilyNameList = (string[])prop[packageFamilyName];
    if (packageFamilyNameList != null)
    {
        for (int j = 0; j < packageFamilyNameList.Length; j++)
        {
            if (packageFamilyNameList[j].Equals(appPackageFamilyName))
            {
                AddToList(deviceInfo);
            }
        }
    }
}
```

When an association is found, the `FindAssociation` method uses the `AddToList` method to add the device ID to a list of associated device IDs. These IDs are stored in a ComboBox named `AssociatedPrinters`.

This example shows the `AddToList` method from the **InkLevel.xaml.cs** file:

```CSharp
void AddToList(DeviceInformation deviceInfo)
{
    // Creating a new display item so the user sees the friendly name instead of the interfaceId.
    ComboBoxItem item = new ComboBoxItem();
    item.Content = deviceInfo.Properties["System.ItemNameDisplay"] as string;
    item.DataContext = deviceInfo.Id;
    AssociatedPrinters.Items.Add(item);

    // If this is the first printer to be added to the combo box, select it.
    if (AssociatedPrinters.Items.Count == 1)
    {
        AssociatedPrinters.SelectedIndex = 0;
    }
}
```

## <span id="Step_2__Display_the_status"></span><span id="step_2__display_the_status"></span><span id="STEP_2__DISPLAY_THE_STATUS"></span>Step 2: Display the status


The `GetInkStatus` method uses an asynchronous event-based pattern to request information from the printer. This method uses an associated device ID to get a device context that can be used to get device status. The call to the `printHelper.SendInkLevelQuery()` method initiates the device query. When the response returns, the `OnInkLevelReceived` method is called and the UI is updated.

**Note**   This C# example follows a different pattern than the JavaScript sample, because C# lets you send a dispatcher to the PrintHelperClass so that it can post the event messages back onto the UI thread.

 

This example shows the `GetInkStatus` and `OnInkLevelReceived` methods from the **InkLevel.xaml.cs** file:

```CSharp
void GetInkStatus(object sender, RoutedEventArgs e)
{
    if (AssociatedPrinters.Items.Count > 0)
    {
        // Get the printer that the user has selected to query.
        ComboBoxItem selectedItem = AssociatedPrinters.SelectedItem as ComboBoxItem;

        // The interfaceId is retrieved from the detail field.
        string interfaceId = selectedItem.DataContext as string;

        try
        {
            // Unsubscribe existing ink level event handler, if any.
            if (printHelper != null)
            {
                printHelper.OnInkLevelReceived -= OnInkLevelReceived;
                printHelper = null;
            }

            object context = Windows.Devices.Printers.Extensions.PrintExtensionContext.FromDeviceId(interfaceId);printHelper.SendInkLevelQuery()

            // Use the PrinterHelperClass to retrieve the bidi data and display it.
            printHelper = new PrintHelperClass(context);
            try
            {
                printHelper.OnInkLevelReceived += OnInkLevelReceived;
                printHelper.SendInkLevelQuery();

                rootPage.NotifyUser("Ink level query successful", NotifyType.StatusMessage);
            }
            catch (Exception)
            {
                rootPage.NotifyUser("Ink level query unsuccessful", NotifyType.ErrorMessage);
            }
        }
        catch (Exception)
        {
            rootPage.NotifyUser("Error retrieving PrinterExtensionContext from InterfaceId", NotifyType.ErrorMessage);
        }
    }
}

private void OnInkLevelReceived(object sender, string response)
{
    BidiOutput.Text = response;
}
```

The print helper class takes care of sending the Bidi query to the device and receiving the response.

This example shows the `SendInkLevelQuery` method, and others, from the **PrintHelperClass.cs** file. Note that only some of the print helper class methods are shown here. Download the [Print settings and print notifications](http://go.microsoft.com/fwlink/p/?LinkID=242862) sample to see the full code.

```CSharp
public void SendInkLevelQuery()
{
    printerQueue.OnBidiResponseReceived += OnBidiResponseReceived;

    // Send the query.
    string queryString = "\\Printer.Consumables";
    printerQueue.SendBidiQuery(queryString);
}

private void OnBidiResponseReceived(object sender, PrinterQueueEventArgs responseArguments)
{
    // Invoke the ink level event with appropriate data.
    dispatcher.RunAsync(
        Windows.UI.Core.CoreDispatcherPriority.Normal,
        () =>
        {
            OnInkLevelReceived(sender, ParseResponse(responseArguments));
        });
}

private string ParseResponse(PrinterQueueEventArgs responseArguments)
{
    if (responseArguments.StatusHResult == (int)HRESULT.S_OK)
        return responseArguments.Response;
    else
        return InvalidHResult(responseArguments.StatusHResult);
}

private string InvalidHResult(int result)
{
    switch (result)
    {
        case unchecked((int)HRESULT.E_INVALIDARG):
            return "Invalid Arguments";
        case unchecked((int)HRESULT.E_OUTOFMEMORY):
            return "Out of Memory";
        case unchecked((int)HRESULT.ERROR_NOT_FOUND):
            return "Not found";
        case (int)HRESULT.S_FALSE:
            return "False";
        case (int)HRESULT.S_PT_NO_CONFLICT:
            return "PT No Conflict";
        default:
            return "Undefined status: 0x" + result.ToString("X");
    }
}
```

## <span id="Testing"></span><span id="testing"></span><span id="TESTING"></span>Testing


Before you can test your UWP device app, it must be linked to your printer using device metadata.

-   You need a copy of the device metadata package for your printer, to add the device app info to it. If you don’t have device metadata, you can build it using the **Device Metadata Authoring Wizard** as described in the topic [Step 2: Create device metadata for your UWP device app](http://go.microsoft.com/fwlink/p/?LinkId=313644).

    **Note**  To use the **Device Metadata Authoring Wizard**, you must install Microsoft Visual Studio Professional, Microsoft Visual Studio Ultimate, or the [standalone SDK for Windows 8.1](http://go.microsoft.com/fwlink/p/?linkid=309209), before completing the steps in this topic. Installing Microsoft Visual Studio Express for Windows installs a version of the SDK that doesn't include the wizard.

     

The following steps build your app and install the device metadata.

1.  Enable test signing.
    1.  Start the **Device Metadata Authoring Wizard** from *%ProgramFiles(x86)%*\\Windows Kits\\8.1\\bin\\x86, by double-clicking **DeviceMetadataWizard.exe**
    2.  From the **Tools** menu, select **Enable Test Signing**.

2.  Reboot the computer
3.  Build the solution by opening the solution (.sln) file. Press F7 or go to **Build-&gt;Build Solution** from the top menu after the sample has loaded.

4.  Disconnect and uninstall the printer. This step is required so that Windows will read the updated device metadata the next time the device is detected.
5.  Edit and save device metadata. To link the device app to your device, you must associate the device app with your device.
    **Note**  If you haven't created your device metadata yet, see [Step 2: Create device metadata for your UWP device app](http://go.microsoft.com/fwlink/p/?LinkId=313644).

     

    1.  If the **Device Metadata Authoring Wizard** is not open yet, start it from *%ProgramFiles(x86)%*\\Windows Kits\\8.1\\bin\\x86, by double-clicking **DeviceMetadataWizard.exe**.
    2.  Click **Edit Device Metadata**. This will let you edit your existing device metadata package.
    3.  In the **Open** dialog box, locate the device metadata package associated with your UWP device app. (It has a **devicemetadata-ms** file extension.)
    4.  On the **Specify UWP device app information** page, enter the Microsoft Store app info in the **UWP device app** box. Click on **Import UWP app manifest file** to automatically enter the **Package name**, **Publisher name**, and **UWP app ID**.
    5.  If your app is registering for printer notifications, fill out the **Notification handlers** box. In **Event ID**, enter the name of the print event handler. In **Event Asset**, enter the name of the file where that code resides.

    6.  When you're done, click **Next** until you get to the **Finish** page.
    7.  On the **Review the device metadata package** page, make sure that all of the settings are correct and select the **Copy the device metadata package to the metadata store on the local computer** check box. Then click **Save**.

6.  Reconnect your printer so that Windows reads the updated device metadata when the device is connected.

## <span id="Troubleshooting"></span><span id="troubleshooting"></span><span id="TROUBLESHOOTING"></span>Troubleshooting


### <span id="Issue__Can_t_find_printer_when_enumerating_devices_associated_with_the_app"></span><span id="issue__can_t_find_printer_when_enumerating_devices_associated_with_the_app"></span><span id="ISSUE__CAN_T_FIND_PRINTER_WHEN_ENUMERATING_DEVICES_ASSOCIATED_WITH_THE_APP"></span>Issue: Can’t find printer when enumerating devices associated with the app

If your printer isn’t found when enumerating the associated printers...

-   **Possible cause:** Test signing is not turned on. See the Debugging section in this topic for info about turning it on.

-   **Possible cause:** The app is not querying for the right Package Family Name. Check the Package Family Name in your code. Open up **package.appxmanifest** in Microsoft Visual Studio and make sure that the package family name you are querying for matches the one in the **Packaging** tab, in the Package Family Name field.

-   **Possible cause:** The device metadata is not associated with the Package Family Name. Use the **Device Metadata Authoring Wizard** to open the device metadata and check the package family name. Start the wizard from *%ProgramFiles(x86)%*\\Windows Kits\\8.1\\bin\\x86, by double-clicking **DeviceMetadataWizard.exe**.

### <span id="Issue__Found_printer_associated_with_the_app__but_can_t_query_Bidi_info"></span><span id="issue__found_printer_associated_with_the_app__but_can_t_query_bidi_info"></span><span id="ISSUE__FOUND_PRINTER_ASSOCIATED_WITH_THE_APP__BUT_CAN_T_QUERY_BIDI_INFO"></span>Issue: Found printer associated with the app, but can’t query Bidi info

If your printer was found when enumerating the associated printers, but a Bidi query returns an error...

-   **Possible cause:** Wrong package family name. Check the Package Family Name in your code. Open up **package.appxmanifest** in Visual Studio and make sure that the package family name you are querying for matches the one in the **Packaging** tab, in the Package Family Name field.

-   **Possible cause:** Printer was installed using a v3 printer, rather than a v4 printer. To see which version is installed, open PowerShell and type the following command:

    ```PowerShell
    get-printer | Select Name, {(get-printerdriver -Name $_.DriverName).MajorVersion}
    ```

## <span id="related_topics"></span>Related topics


[Developing v4 print drivers](http://go.microsoft.com/fwlink/p/?LinkId=314231)

[Printer Extension Interfaces (v4 Print Driver)](http://go.microsoft.com/fwlink/p/?LinkID=299887)

[Bidirectional Communications](http://go.microsoft.com/fwlink/p/?LinkId=317192)

[Getting started with UWP apps](getting-started.md)

[Create a UWP device app (step-by-step guide)](step-1--create-a-uwp-device-app.md)

[Create device metadata for a UWP device app (step-by-step guide)](step-2--create-device-metadata.md)

 

 






