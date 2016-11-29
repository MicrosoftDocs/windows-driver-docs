---
title: Specify applications in the Mobile Broadband Metadata Authoring Wizard
description: Specify applications in the Mobile Broadband Metadata Authoring Wizard
ms.assetid: 58E95326-94C4-444F-BFE2-0E7DC8112119
keywords: ["Specify applications in the Mobile Broadband Metadata Authoring Wizard"]
---

# Specify applications in the Mobile Broadband Metadata Authoring Wizard


To specify the various applications for your service, including the Windows Store device app and privileged applications, click the **Applications** tab.

The Windows Store device app is downloaded and installed when a user first connects a device. Privileged applications have special access to the device. You can specify only one of each.

For more information about Windows Store device app and privileged applications, see [Windows 8 Device Experience](http://go.microsoft.com/fwlink/p/?LinkId=227312).

## <span id="To_specify_the_Windows_Store_device_app"></span><span id="to_specify_the_windows_store_device_app"></span><span id="TO_SPECIFY_THE_WINDOWS_STORE_DEVICE_APP"></span>To specify the Windows Store device app


To specify the app, fill out the following fields:

-   **Package Name**. Enter the value of the Name attribute in the Identity element in the Package element of the Application Manifest.
-   **Publisher**. Enter the value of the Publisher attribute in the Identity element in the Package element of the Application Manifest. This value must match the publisher certificate installed on the PC.
-   **App ID**. Enter the value of the ID attribute in the Application element of the Application Manifest.

The **Package Name**, **Publisher**, and **App ID** all must match the information in the app package.appxmanifest.

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

## <span id="To_see_the_Package_name_and_Publisher"></span><span id="to_see_the_package_name_and_publisher"></span><span id="TO_SEE_THE_PACKAGE_NAME_AND_PUBLISHER"></span>To see the Package name and Publisher


1.  Open the app solution in Visual Studio.
2.  Click the app manifest in Solution Explorer.
3.  Double-click Package.appxmanifest.
4.  In the **Packaging** tab, review the **Package name** and **Publisher** fields.

## <span id="To_see_the_App_ID_"></span><span id="to_see_the_app_id_"></span><span id="TO_SEE_THE_APP_ID_"></span>To see the App ID


1.  Open the app solution in Visual Studio.
2.  Click the app manifest in Solution Explorer.
3.  Right-click Package.appxmanifest.
4.  Select **View Code**.

## <span id="Privileged_applications"></span><span id="privileged_applications"></span><span id="PRIVILEGED_APPLICATIONS"></span>Privileged applications


For the Windows Store device app to access privileged mobile broadband interfaces, it needs to be specified under **Privileged Applications**.

To specify the Privileged Applications, fill out the following fields under **Privileged Application**:

**Note**  For detailed information about the following fields, see [Windows 8 Device Experience](http://go.microsoft.com/fwlink/p/?LinkId=242009). For information about the Privileged Device Interface Property Key, see [DEVPKEY\_DeviceInterface\_Restricted](http://go.microsoft.com/fwlink/p/?linkid=256362).

 

-   **Package Name**. Enter the value of the Name attribute in the Identity element in the Package element of the Application Manifest.
-   **Publisher**. Enter the value of the Publisher attribute in the Identity element in the Package element of the Application Manifest.

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

## <span id="Device_Notification_Handler"></span><span id="device_notification_handler"></span><span id="DEVICE_NOTIFICATION_HANDLER"></span>Device Notification Handler


The mobile broadband platform provides enhanced functionality for receiving and displaying MNO administrative SMS or USSD notifications, such as approaching data usage cap, international roaming, and low balance. It also provides functionality for responding to data usage and connect, disconnect, or roaming background events in a Windows Store app for mobile network providers.

Windows provides broker facilities for Windows Store app to run some code in response to events even if the Windows Store app isn't running. For more information about implementing notification handlers, see [Enabling mobile operator notifications and system events](http://go.microsoft.com/fwlink/p/?linkid=242062).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\dma]:%20Specify%20applications%20in%20the%20Mobile%20Broadband%20Metadata%20Authoring%20Wizard%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




