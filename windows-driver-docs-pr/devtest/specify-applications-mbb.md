---
title: Specify Applications in the Mobile Broadband Metadata Authoring Wizard
description: Specify applications in the Mobile Broadband Metadata Authoring Wizard
keywords:
- Specify applications in the Mobile Broadband Metadata Authoring Wizard
ms.date: 04/20/2017
---

# Specify applications in the Mobile Broadband Metadata Authoring Wizard

To specify the various applications for your service, including the Microsoft Store device app and privileged applications, click the **Applications** tab.

The UWP device app is downloaded and installed when a user first connects a device. Privileged applications have special access to the device. You can specify only one of each.

## To specify the Microsoft Store device app

To specify the app, fill out the following fields:

- **Package Name**. Enter the value of the Name attribute in the Identity element in the Package element of the Application Manifest.
- **Publisher**. Enter the value of the Publisher attribute in the Identity element in the Package element of the Application Manifest. This value must match the publisher certificate installed on the PC.
- **App ID**. Enter the value of the ID attribute in the Application element of the Application Manifest.

The **Package Name**, **Publisher**, and **App ID** all must match the information in the app package.appxmanifest.

The following is an example of the Application Manifest:

```xml
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

## To see the Package name and Publisher

1. Open the app solution in Visual Studio.
2. Click the app manifest in Solution Explorer.
3. Double-click Package.appxmanifest.
4. In the **Packaging** tab, review the **Package name** and **Publisher** fields.

## To see the App ID

1. Open the app solution in Visual Studio.
2. Click the app manifest in Solution Explorer.
3. Right-click Package.appxmanifest.
4. Select **View Code**.

## Privileged applications

For the Microsoft Store device app to access privileged mobile broadband interfaces, it needs to be specified under **Privileged Applications**.

To specify the Privileged Applications, fill out the following fields under **Privileged Application**:

>[!NOTE]
>For information about the Privileged Device Interface Property Key, see [DEVPKEY\_DeviceInterface\_Restricted](../install/devpkey-deviceinterface-restricted.md).

- **Package Name**. Enter the value of the Name attribute in the Identity element in the Package element of the Application Manifest.
- **Publisher**. Enter the value of the Publisher attribute in the Identity element in the Package element of the Application Manifest.

The following is an example of the Application Manifest:

```xml
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

## Device Notification Handler

The mobile broadband platform provides enhanced functionality for receiving and displaying MNO administrative SMS or USSD notifications, such as approaching data usage cap, international roaming, and low balance. It also provides functionality for responding to data usage and connect, disconnect, or roaming background events in a UWP app for mobile network providers.

Windows provides broker facilities for UWP app to run some code in response to events even if the Microsoft Store app isn't running. For more information about implementing notification handlers, see [Introduction to enabling mobile operator notifications and system events](../mobilebroadband/enabling-mobile-operator-notifications-and-system-events.md).
