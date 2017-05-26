---
title: Kiosk apps for assigned access Best practices
description: Kiosk apps for assigned access Best practices
ms.assetid: 2405B5BB-2214-4B40-B3A1-C47073390B21
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Kiosk apps for assigned access: Best practices


In Windows 10, you use the Lock framework and assigned access to create a kiosk app that enables users to interact with a single app on a device. This document describes how to implement a kiosk app and describes best practices. All sample code is written in C# but should be easily translatable to the language of your choice, because the underlying framework is Windows RT. This document is written for OEMs and ISVs who want to write kiosk apps for their customers.

## <span id="Terms"></span><span id="terms"></span><span id="TERMS"></span>Terms


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><span id="assigned_access"></span><span id="ASSIGNED_ACCESS"></span>assigned access</p></td>
<td><p>A feature that allows a system administrator to manage the user’s experience by limiting application entry points exposed to the user of the device. For example, you can restrict customers at your business to using one app so your PC acts like a kiosk. Whenever someone signs in with the specified account, they'll only be able to use that one app. They won't be able to switch apps or close the app using touch gestures, a mouse, the keyboard, or hardware buttons. They also won't see any app notifications.</p></td>
</tr>
<tr class="even">
<td><p><span id="lock_screen_app__or_lock_app_"></span><span id="LOCK_SCREEN_APP__OR_LOCK_APP_"></span>lock screen app (or lock app)</p></td>
<td><p>An application that either takes advantage of the ability to set a dynamic wallpaper or that takes advantage of the new lock extensibility framework.</p></td>
</tr>
<tr class="odd">
<td><p><span id="above_lock_screen_app__or_above_lock_app_"></span><span id="ABOVE_LOCK_SCREEN_APP__OR_ABOVE_LOCK_APP_"></span>above lock screen app (or above lock app)</p></td>
<td><p>An application that launches above the lock screen while lock screen app is running (for example, when the desktop is locked).</p></td>
</tr>
<tr class="even">
<td><p><span id="under_lock_app"></span><span id="UNDER_LOCK_APP"></span>under lock app</p></td>
<td><p>An application that runs normally, in an unlocked Windows context.</p></td>
</tr>
<tr class="odd">
<td><p><span id="LockApplicationHost"></span><span id="lockapplicationhost"></span><span id="LOCKAPPLICATIONHOST"></span>[LockApplicationHost](http://go.microsoft.com/fwlink/?LinkId=691219)</p></td>
<td><p>A WinRT class that allows above lock screen apps to request that the device unlocks, and allows the app to register to be notified when the device begins to unlock.</p></td>
</tr>
<tr class="even">
<td><p><span id="View_or_Application_View"></span><span id="view_or_application_view"></span><span id="VIEW_OR_APPLICATION_VIEW"></span>View or Application View</p></td>
<td><p>Each view is a separate window into the app. An app can have a main view, and create multiple and secondary views on demand. See [ApplicationView]( http://go.microsoft.com/fwlink/?LinkId=691220) for more information.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Under_the_hood"></span><span id="under_the_hood"></span><span id="UNDER_THE_HOOD"></span>Under the hood


Assigned access in Windows 10 leverages the new lock framework. When an assigned access user logs in, a background task locks the desktop and a lock screen app launches, which then runs the kiosk app above lock. The kiosk app is actually running as an above lock screen app.

When the lock framework launches the kiosk app above the lock and the app has the **windows.aboveLockScreen** extension, the lock framework automatically creates a new secondary view for the kiosk app and all content of the main view is rendered in the new secondary view. If the app does not have the **windows.aboveLockScreen** extension, no secondary view is created and the app launches as if it’s running normally.

Starting in Windows 10, version 1607, there is no longer a restriction on the Universal Windows Platform (UWP) extension, so most apps can be shown in **Settings** when user configures assigned access. However, there still are benefits of using the extension, detailed below .

## <span id="Best_practices"></span><span id="best_practices"></span><span id="BEST_PRACTICES"></span>Best practices


**Note**  This section applies to a Kiosk application that uses a **windows.aboveLockScreen** extension.

 

### <span id="Secure_your_information"></span><span id="secure_your_information"></span><span id="SECURE_YOUR_INFORMATION"></span>Secure your information

If the kiosk app is meant to run both above lock in assigned access and also in the unlocked Windows context, you may want to create a different page to render above lock, and another page for under the lock. This will allow you to avoid showing sensitive information in kiosk mode, since kiosk mode usually means anonymous access. Here are the steps you'd follow to use two different pages, one for under the lock and one for above the lock:

1.  Inside the override of the **OnLaunched** function in App.xaml.cs, try to obtain an instance of the [LockApplicationHost](http://go.microsoft.com/fwlink/?LinkId=691219) class before rootFrame navigation.
2.  If the call fails, the kiosk app should launch normally, under the lock.
3.  If the call succeeds, the kiosk app should launch above the lock running in assigned access mode. You may want this version of the kiosk app to have a different main page to hide sensitive information.

The following sample demonstrates how to do this. AssignedAccessPage.xaml is predefined, and the app navigates to AssignedAccessPage.xaml once it detects that is running in above lock mode. As a result, the normal page would display only in the under lock scenario.

You can use this method to determine if the app is running above lock screen anytime in the app lifecycle and react accordingly.

```
using Windows.ApplicationModel.LockScreen;

// inside the override OnLaunched function in App.xaml.cs

if (rootFrame.Content == null)
{
    LockApplicationHost host = LockApplicationHost.GetForCurrentView();
    if (host == null)
    {
        // if call to LockApplicationHost is null, this app is running under lock
        // render MainPage normally
        rootFrame.Navigate(typeof(MainPage), e.Arguments);
    }
    else
    {
        // If LockApplicationHost was successfully obtained
        // this app is running as a lock screen app, or above lock screen app
        // render a different page for assigned access use
        // to avoid showing regular main page to keep secure information safe
        rootFrame.Navigate(typeof(AssignedAccessPage), e.Arguments);
    }
}
```

### <span id="Multiple_views__windows__and_threads"></span><span id="multiple_views__windows__and_threads"></span><span id="MULTIPLE_VIEWS__WINDOWS__AND_THREADS"></span>Multiple views, windows, and threads

Only the main view or window gets rendered in assigned access mode, but in a new secondary view. *Any other views you've created in the app will not be rendered.* Make sure everything you want the user to see or access is in the main window because the user will not see the other views.

The lock framework renders the kiosk app’s main view in a new secondary view- it’s transparent to the app. You do not have to manually create the secondary view for above lock mode because the lock framework creates one for you. This means that there are actually two views to your app when it's running in above lock mode. Run the following code in your main window with your app in assigned access mode to see the view count and value for whether the current window is the main window.

```
using Windows.ApplicationModel.Core;

CoreApplication.GetCurrentView().IsMain //false
CoreApplication.Views.Count //2
```

Here’s a sample layout.

![z-order for views when the app is running in lock mode](images/assignedaccesssamplelayout.png)

### <span id="Dispatcher"></span><span id="dispatcher"></span><span id="DISPATCHER"></span>Dispatcher

Each view or window has its own dispatcher. In assigned access mode, you should not use the **MainView** dispatcher, instead you should use the **CurrentView** dispatcher.

For example, in the following code sample there is a Button and a **TextBlock** on the .xaml page. A click event handler is added to the button. The handler does some background work and then updates the text of **TextBlock**. The usage of **CoreApplication.MainView.Dispatcher** would cause the app crash in this example because in assigned access mode, the main window is not **MainView** but rendered in a secondary view. It is recommended you use **CoreApplication.GetCurrentView.Dispatcher**.

```
using Windows.ApplicationModel.Core;

private async void Button_Click(object sender, RoutedEventArgs e)
{
    button.IsEnabled = false;

    // start a background task and update UI periodically (every 1 second)
    // using MainView dispatcher in below code will end up with app crash
    // in assigned access mode, use GetCurrentView().Dispatcher instead
    await CoreApplication.GetCurrentView().Dispatcher.RunAsync(
        CoreDispatcherPriority.Normal,
        async () =>
        {
            for (int i = 0; i < 60; ++i)
            {
                // do some background work, here we use Task.Delay to sleep
                await Task.Delay(1000);
                // update UI
                textBlock1.Text = "   " + i.ToString();
            }
            button.IsEnabled = true;
        });
}

```

### <span id="Add_a_way_out_of_assigned_access"></span><span id="add_a_way_out_of_assigned_access"></span><span id="ADD_A_WAY_OUT_OF_ASSIGNED_ACCESS"></span>Add a way out of assigned access

In some situations, the power button, escape button, or other buttons used to stop an application may not be enabled or available on the keyboard. In these situations, provide a way to stop assigned access, for instance a software key. The following event handler shows how to stop assigned access mode by responding to button click event that could be triggered by a software key.

```
LockApplicationHost^ lockHost = LockApplicationHost::GetForCurrentView();
    if (lockHost != nullptr)
    {
        lockHost->RequestUnlock();
    }
```

### <span id="Lifecycle_management"></span><span id="lifecycle_management"></span><span id="LIFECYCLE_MANAGEMENT"></span>Lifecycle management

If the kiosk app ends unexpectedly, the assigned access framework tries to relaunch it. If a user has physical access to the keyboard and presses Ctrl+Alt+Del to bring up the login screen, an Unlocking event is triggered. The assigned access framework is listening to this event and will try to terminate the kiosk app. Your kiosk app can also register a handler to this event and exit. See the code below for an example of how to do this.

```
using Windows.ApplicationModel.LockScreen;

public AssignedAccessPage()
{
    this.InitializeComponent();

    LockApplicationHost lockHost = LockApplicationHost.GetForCurrentView();
    if (lockHost != null)
    {
        lockHost.Unlocking += LockHost_Unlocking;
}
}

private void LockHost_Unlocking(LockApplicationHost sender, LockScreenUnlockingEventArgs args)
{
    // save any unsaved work and gracefully exit the app
    App.Current.Exit();
}
```

After the user presses Ctrl+Alt+Del and a login screen is shown, two things could happen:

1.  The user knows the assigned access account password and unlocks the desktop. The assigned access framework starts, locks the desktop, and the lock screen app launches which in turn launches the kiosk app.
2.  The user doesn’t know the password or doesn’t take any further action. The login screen timeouts and the desktop relocks; the lock screen app launches which in turn launches the kiosk app.

### <span id="Don_t_create_new_windows_or_views_in_assigned_access_mode"></span><span id="don_t_create_new_windows_or_views_in_assigned_access_mode"></span><span id="DON_T_CREATE_NEW_WINDOWS_OR_VIEWS_IN_ASSIGNED_ACCESS_MODE"></span>Don't create new windows or views in assigned access mode

The following function call will end up with a runtime exception if it’s invoked in assigned access mode. If the same app, when used under lock, calls the function, it does not cause a runtime exception. It’s helpful to use [LockApplicationHost](http://go.microsoft.com/fwlink/?LinkId=691219) to determine the app's assigned access mode, and code your app accordingly, such as not creating new views if the app is in assigned access mode.

```
Windows.ApplicationModel.Core.CoreApplication.CreateNewView(); //causes exception

```

## <span id="Appendix_1__UWP_extension"></span><span id="appendix_1__uwp_extension"></span><span id="APPENDIX_1__UWP_EXTENSION"></span>Appendix 1: UWP extension


The following sample application manifest uses the **windows.aboveLockScreen**UWP extension. You must use this extension in your Windows 10 Universal Windows Platform (UWP) app in order for it to display in the Assigned Access app list in **Settings.**

```
<Package xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10" xmlns:mp="http://schemas.microsoft.com/appx/2014/phone/manifest" xmlns:uap="http://schemas.microsoft.com/appx/manifest/uap/windows10" IgnorableNamespaces="uap mp">
  <Identity Name="bd4df68b-dc18-4748-a14e-bc21dac13736" Publisher="Contoso" Version="1.0.0.0" />
  <mp:PhoneIdentity PhoneProductId="bd4df68b-dc18-4748-a14e-bc21dac13736" PhonePublisherId="00000000-0000-0000-0000-000000000000" />
  <Properties>
    <DisplayName>AboveLock</DisplayName>
    <PublisherDisplayName>Contoso</PublisherDisplayName>
    <Logo>Assets\StoreLogo.png</Logo>
  </Properties>
  <Dependencies>
    <TargetDeviceFamily Name="Windows.Universal" MinVersion="10.0.0.0" MaxVersionTested="10.0.0.0" />
  </Dependencies>
  <Resources>
    <Resource Language="x-generate" />
  </Resources>
  <Applications>
    <Application Id="App" Executable="$targetnametoken$.exe" EntryPoint="AboveLock.App">
      <uap:VisualElements DisplayName="AboveLock" Square150x150Logo="Assets\Square150x150Logo.png" Square44x44Logo="Assets\Square44x44Logo.png" Description="AboveLock" BackgroundColor="transparent">
        <uap:DefaultTile Wide310x150Logo="Assets\Wide310x150Logo.png">
        </uap:DefaultTile>
        <uap:SplashScreen Image="Assets\SplashScreen.png" />
      </uap:VisualElements>
      <Extensions>
        <uap:Extension Category="windows.lockScreenCall" />
        <uap:Extension Category="windows.aboveLockScreen" />
      </Extensions>
    </Application>
  </Applications>
  <Capabilities>
    <Capability Name="internetClient" />
  </Capabilities>
</Package>

```

## <span id="Appendix_2__troubleshooting"></span><span id="appendix_2__troubleshooting"></span><span id="APPENDIX_2__TROUBLESHOOTING"></span>Appendix 2: troubleshooting


Normally, if a Kiosk app fails to activate above the lock screen app, you can find the activation error code in the lockdown screen. Use the error code to discover the issue by looking up Windows [System Error Codes](https://msdn.microsoft.com/library/windows/desktop/ms681381). In addition Event Viewer contains more information about activation failures. To do so:

1.  Open **Event Viewer**. There are two likely places to find activation errors.
2.  In the **Event Viewer (Local)** pane, expand **Windows Logs**, and then click **Application**.
3.  Also, in **Event Viewer (local)**, expand **Applications and Services Logs**, expand **Windows**, expand **Apps**, and then click **Microsoft-Windows-TWinUI/Operational**.

Note that because kiosk apps with assigned access do not run in full-screen mode, **ApplicationView.GetForCurrentView().IsFullScreenMode** will return false.

## <span id="related_topics"></span>Related topics


[Assigned access](https://msdn.microsoft.com/library/windows/hardware/mt620040)

[Show multiple views for an app]( http://go.microsoft.com/fwlink/?LinkId=708251)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_phPartAppDev\p_phPartAppDev%5D:%20Kiosk%20apps%20for%20assigned%20access:%20Best%20practices%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")
