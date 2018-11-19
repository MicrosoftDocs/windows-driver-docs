---
title: Specify applications in the Device Metadata Authoring Wizard
description: Specify applications in the Device Metadata Authoring Wizard
ms.assetid: B3ECEBF3-FBC6-45E7-9FF5-439F1CDF351F
keywords:
- Specify applications in the Device Metadata Authoring Wizard
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specify applications in the Device Metadata Authoring Wizard


You can specify various applications for your device, including the Microsoft Store device app and privileged applications.

The UWP device app is downloaded and installed when a user first connects a device. Privileged applications have special access to the device. You can specify only one of each.

For more information about UWP device apps and privileged applications, see [Windows 8 Device Experience](http://go.microsoft.com/fwlink/p/?LinkId=227312).

## <span id="To_specify_the_Windows_Store_device_app"></span><span id="to_specify_the_windows_store_device_app"></span><span id="TO_SPECIFY_THE_WINDOWS_STORE_DEVICE_APP"></span>To specify the Microsoft Store device app


1.  Click the **Applications** tab.
2.  Fill out the following fields:
    -   **Package Name**. Enter the value of the Name attribute in the Identity element in the Package element of the Application Manifest. The package name should be obtained after an app submission to the Microsoft Store is created, because the Package Name is changed by the Microsoft Store submission process. See [UWP device app lifecycle](http://go.microsoft.com/fwlink/p/?linkid=246571) for more info on how to associate the app with the Microsoft Store and copy updated values into the app manifest.
    -   **Publisher**. Enter the value of the Publisher attribute in the Identity element in the Package element of the Application Manifest. The Publisher Name should be the same as the one on the developer certificate used to sign the package and the metadata.
    -   **App ID**. Enter the value of the ID attribute in the Application element of the Application Manifest.
    -   **Notification Handlers**. For information about Notification Handlers, see [Device Metadata Package Schema Reference for Windows 8](http://go.microsoft.com/fwlink/p/?LinkId=226753).

The **Package Name**, **Publisher**, and **App ID** must match the information in the app package .appxmanifest.

The following is an example of the Application Manifest:

```
<?xml version="1.0" encoding="utf-8" ?> 
   <Package xmlns="http://schemas.microsoft.com/appx/2010/manifest">
      <Identity Name="Microsoft.SDKSamples.MoFx2App" Version="1.0.0.0" Publisher="CN=Microsoft\O=Microsoft Corp\L=Redmond\S=WA\C=US" ResourceId="NorthAmerica" /> 
   <Properties>
     <DisplayName>MoFx2App SDK Sample</DisplayName> 
     <Description>MoFx2App SDK Sample</Description> 
     <Logo>images\tile-sdk.png</Logo> 
   </Properties>
<Resources>
  <Resource Language="en-us" /> 
</Resources>
<Applications>
  <Application Id="Microsoft.SDKSamples.MoFx2App" DisplayName="MoFx2App" Logo="images\tile-sdk.png" SmallLogo="images\tile-sdk.png" EntryPointType="startPage" EntryPoint="default.html">
```

## <span id="To_see_the_Package_name_and_Publisher_"></span><span id="to_see_the_package_name_and_publisher_"></span><span id="TO_SEE_THE_PACKAGE_NAME_AND_PUBLISHER_"></span>To see the Package name and Publisher


1.  Open the app solution in Visual Studio.
2.  Click the app manifest in Solution Explorer.
3.  Double-click Package.appxmanifest.
4.  On the **Packaging** tab, review the **Package name** and **Publisher** fields.

## <span id="To_see_the_App_ID_"></span><span id="to_see_the_app_id_"></span><span id="TO_SEE_THE_APP_ID_"></span>To see the App ID


1.  Open the app solution in Visual Studio.
2.  Click the app manifest in Solution Explorer.
3.  Right-click Package.appxmanifest.
4.  Select **View Code**.

## <span id="Privileged_applications"></span><span id="privileged_applications"></span><span id="PRIVILEGED_APPLICATIONS"></span>Privileged applications


For the Microsoft Store device app to have access to privileged device interfaces, the app must be specified under **Privileged Applications**.

To specify the privileged applications, fill out the following fields under **Privileged Application**:

**Note**  
For more information about the Privileged Device Interface Property Key, see [DEVPKEY\_DeviceInterface\_Restricted](http://go.microsoft.com/fwlink/p/?linkid=256362).



-   **Package Name**. Enter the value of the Name attribute in the Identity element in the Package element of the Application Manifest.
-   **Publisher**. Enter the value of the Publisher attribute in the Identity element in the Package element of the Application Manifest.
-   If the privileged application accesses a custom driver, select **AccessCustomDriver**.

The following is an example of an Application Manifest, showing the Identity Name, Publisher, and Application Id fields that are entered into the Device Metadata Authoring Wizard:

```XML
<?xml version="1.0" encoding="utf-8"?>
<Package xmlns="http://schemas.microsoft.com/appx/2010/manifest">
  <Identity Name="64022FABRIKAM.FabrikamDeviceApp" Publisher="CN=05558413-FFF6-4AA5-8176-AD43036533FA" Version="1.0.0.0" />
  <Properties>
    <DisplayName>Fabrikam Device App</DisplayName>
    <PublisherDisplayName>Fabrikam</PublisherDisplayName>
    <Logo>Assets\storeLogo-sdk.png</Logo>
  </Properties>
  <Prerequisites>
    <OSMinVersion>6.2</OSMinVersion>
    <OSMaxVersionTested>6.2</OSMaxVersionTested>
  </Prerequisites>
  <Resources>
    <Resource Language="x-generate" />
  </Resources>
  <Applications>
    <Application Id="DeviceAppForPrinters" Executable="$targetnametoken$.exe" 
        EntryPoint="DeviceAppForPrinters.App">
      <VisualElements DisplayName="Fabrikam Device App" Logo="Assets\squareTile-sdk.png" 
         SmallLogo="Assets\smallTile-sdk.png" Description="DeviceAppForPrinters" ForegroundText="light" BackgroundColor="#00b2f0" ToastCapable="true">
        <DefaultTile ShowName="allLogos" ShortName="App4PrinterCS" WideLogo="Assets\tile-sdk.png" />
        <SplashScreen Image="Assets\splash-sdk.png" BackgroundColor="#00b2f0" />
      </VisualElements>
      <Extensions>
          <Extension Category="windows.backgroundTasks" 
             EntryPoint="Fabrikam.Printing.PrintApp.PrintNotificationHandler">
               <BackgroundTasks>
                 <Task Type="systemEvent" />
               </BackgroundTasks>
          </Extension>
          <Extension Category="windows.printTaskSettings" 
             Executable="$targetnametoken$.exe" EntryPoint="DeviceAppForPrinters.App" />
      </Extensions>
    </Application>
  </Applications>
</Package>
```

The following is an example of the elements in the XML generated by the Device Metadata Authoring Wizard that correspond to the Application Manifest fields:

```XML
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<SoftwareInfo xmlns="http://schemas.microsoft.com/windows/2010/08/DeviceMetadata/SoftwareInfo">

  <DeviceCompanionApplications>
       <Package>
         <Identity Name="64022FABRIKAM.FabrikamDeviceApp" 
          Publisher="CN=05558413-FFF6-4AA5-8176-AD43036533FA" />
         <Applications>
          <Application Id="DeviceAppForPrinters">
           <DeviceNotificationHandlers>
                   <DeviceNotificationHandler
                      EventID="PrintNotificationHandler"
            EventAsset="Fabrikam.Printing.PrintApp.PrintNotificationHandler" />
                </DeviceNotificationHandlers>
         </Application>
          </Applications>
       </Package>
  </DeviceCompanionApplications>

  <PrivilegedApplications>
    <Package>
         <Identity Name="64022FABRIKAM.FabrikamDeviceApp" 
              Publisher="CN=05558413-FFF6-4AA5-8176-AD43036533FA"
              AccessCustomDriver="false" />  
    </Package>
  </PrivilegedApplications>
</SoftwareInfo>
```

## <span id="related_topics"></span>Related topics


[Device Metadata Schema Reference](https://msdn.microsoft.com/library/windows/hardware/br259102)










