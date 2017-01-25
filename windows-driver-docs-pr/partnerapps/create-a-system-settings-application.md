---
title: Create a partner settings app
description: Create a partner settings app
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3b549c11-f8b2-46e8-9d22-4edc787743ee
---

# Create a partner settings app


OEMs and mobile operators can expose custom settings for hardware components that they add to a device to differentiate it from other devices, such as speakers, sensors, or microphones. These settings appear in the **Extras** page of the **Settings** application, along with other system settings provided by the operating system. To add custom settings, partners create an partner settings app.

## <span id="Characteristics_of_partner_settings_app"></span><span id="characteristics_of_partner_settings_app"></span><span id="CHARACTERISTICS_OF_PARTNER_SETTINGS_APP"></span>Characteristics of partner settings app


Partner settings apps have the following characteristics:

-   They are Universal Windows Platform (UWP) apps, or, in the case of Windows Phone, they can also be Microsoft Silverlight apps on Windows Phone .

-   Users can uninstall them directly just like any other application. They can be upgraded by updating the settings application in the Store like any other Windows app.

-   They are preinstalled applications. Like any other preinstalled application, partners must submit a system settings application to Windows Dev Center in order to certify the application and obtain the signed .appx file and license file needed to include the application in a device image. They are installed at first boot.

-   They are published to a hidden location in the Store that users cannot browse to or find by using search.

-   They can have their own tile but cannot be pinned to the Start menu.

## <span id="Creating_system_settings_applications"></span><span id="creating_system_settings_applications"></span><span id="CREATING_SYSTEM_SETTINGS_APPLICATIONS"></span>Creating system settings applications


Settings applications are Windows apps and should therefore conform to all programming guidelines for Windows apps (see [Guidelines for Windows Runtime apps)](https://msdn.microsoft.com/library/windows/apps/hh465424.aspx):

1.  Use the Windows Software Development Kit (SDK) to create a Windows app. For more information on creating a Windows app, see [Build a Universal Windows app](https://msdn.microsoft.com/library/windows/apps/xaml/dn609832.aspx). This application will be the system settings application. If you're writing a settings app targeting the phone, you can also create a Silverlight app on Windows Phone .
2.  Declare the settings app capability in the application manifest, as in this xml: `    xmlns:rescap=http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities`
3.  Add the extension to the application manifest, as in the following xml. Note that the rescap declaration needs to be part of the Package node.

    ```
    <Package
      xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10"
      xmlns:mp="http://schemas.microsoft.com/appx/2014/phone/manifest"
      xmlns:uap="http://schemas.microsoft.com/appx/manifest/uap/windows10"
      xmlns:rescap="http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities"
      IgnorableNamespaces="uap mp rescap">
    ```

    Add the following extension element to you application manifest:

    ```
    <Extensions>
         <rescap:Extension Category="windows.settingsApp">
         <rescap:SettingsApp Category="extras"/>
         </rescap:Extension>
    </Extensions>
    ```

    The extension element needs to be added inside of the application node, as in the following example.

    ```
    <Applications>
        <Application Id="App"
          Executable="$targetnametoken$.exe"
          EntryPoint="PhoneNumber.App">
          <uap:VisualElements
            DisplayName="PhoneNumber"
            Square150x150Logo="Assets\Square150x150Logo.png"
            Square44x44Logo="Assets\Square44x44Logo.png"
            Description="PhoneNumber"
            BackgroundColor="transparent">
            <uap:DefaultTile Wide310x150Logo="Assets\Wide310x150Logo.png"/>
            <uap:SplashScreen Image="Assets\SplashScreen.png" />
          </uap:VisualElements>
         <Extensions>
            <rescap:Extension Category="windows.settingsApp">
              <rescap:SettingsApp Category="extras"/>
            </rescap:Extension>
          </Extensions>
        </Application>
      </Applications>
    ```

    **Note**  If a settings application is detected by the operating system when the system boots up, a custom settings category called **Extras** is created at the bottom of the settings page. This category name cannot be changed, and all settings apps not created by Microsoft will populate this same category.

     

4.  Configure the system settings application as a preinstalled application by submitting the application to Windows Dev Center to sign the .appx and obtain a license file, and then include the application in a device image using Windows Imaging and Configuration Designer (ICD). For more information about creating a preinstalled application, see [Preinstalled apps](https://msdn.microsoft.com/library/windows/hardware/mt269740). For more information about Windows ICD, including how to download and install it, see [Getting started with Windows ICD](https://msdn.microsoft.com/library/windows/hardware/dn916112.aspx). To learn how to add an application to the an image using Windows ICD, see the **To add an app** section of the [Configure customizations using Windows ICD](https://msdn.microsoft.com/library/windows/hardware/dn916109.aspx) topic.

## <span id="Updated_system_settings_applications"></span><span id="updated_system_settings_applications"></span><span id="UPDATED_SYSTEM_SETTINGS_APPLICATIONS"></span>Updated system settings applications


Settings applications follow the typical process for any Windows app. Partners can submit updates to system settings applications to the Store. After an update is submitted, customers who have the system settings application installed are notified of the update and can install the update through the Store.

Because a system settings application does not appear in the application list on devices, users might be confused when they are notified of an update for the application on the Store. To help avoid confusion, Microsoft recommends providing some context for users by specifying in the Store description for the application that it provides system-level settings that appear in **Settings** on the device.

## <span id="What_happens_to_legacy_Control_Panel_or_system_settings_apps_when_the_OS_upgrades_to_Windows_10_"></span><span id="what_happens_to_legacy_control_panel_or_system_settings_apps_when_the_os_upgrades_to_windows_10_"></span><span id="WHAT_HAPPENS_TO_LEGACY_CONTROL_PANEL_OR_SYSTEM_SETTINGS_APPS_WHEN_THE_OS_UPGRADES_TO_WINDOWS_10_"></span>What happens to legacy Control Panel or system settings apps when the OS upgrades to Windows 10?


If your Control Panel application was written for Windows 7, Windows 8, or Windows 8.1, it will continue to work in the legacy Control Panel, but it will not support any of the features of the Windows 10 system settings app. Likewise, if your legacy system settings app was written for Windows 8 or Windows 8.1, it will continue to work but it will not support any of the features of the Windows 10 system settings app. Legacy apps cannot display in the Windows 10 system settings app.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_phPartAppDev\p_phPartAppDev%5D:%20Create%20a%20partner%20settings%20app%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




