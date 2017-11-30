---
title: UWP mobile broadband apps
description: UWP mobile broadband apps
ms.assetid: bb02397b-0da5-4e09-be1c-8812abec6fd5
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# UWP mobile broadband apps


The following sections are available in this topic:

-   [UWP apps](#wsa)

-   [UWP mobile broadband apps](#mb)

## <span id="wsa"></span><span id="WSA"></span>UWP apps


UWP apps are full-screen apps that are tailored for the following:

-   Your users’ needs

-   The devices that they run

-   Touch interaction

-   The Windows user interface

UWP apps are optimized for touch, are aware of the user's location and identity, and are hosted in the Microsoft Store. UWP apps are always on and available for instant use, and always connected with the latest content from the web. Users can discover and purchase these apps in the Microsoft Store: the apps can be installed quickly and uninstalled cleanly.

All UWP apps share the following features and benefits:

-   **Development platforms** UWP apps are built by using the Windows Software Development Kit for Windows 8 and the Windows Runtime APIs.

-   **Programming languages** You can build UWP apps by using JavaScript with an HTML and cascading style sheets (CSS) presentation layer, or by using C++ or C# with an Extensible Application Markup Language (XAML) presentation layer.

-   **Touch optimization** Touch interaction support is built-in. You can design your mobile broadband app for touch, and Windows gives you keyboard, mouse, and graphical scaling support.

For more info about UWP apps, see [Make great UWP apps](https://msdn.microsoft.com/library/windows/apps/hh464920).

## <span id="mb"></span><span id="MB"></span>UWP mobile broadband apps


A UWP mobile broadband app is a UWP app that is authored by mobile operators and is associated with a mobile broadband connection. In addition to the benefits of being a UWP app, this app has special access to privileged mobile broadband APIs.

A mobile broadband app provides the following benefits:

-   **Increased customer connection** Users can easily discover the operator’s brand and services from the Windows **Start** screen and from the network list.

-   **Ongoing control over the experience** You can use the app to change subscribers’ account experiences.

-   **Reduced deployment and maintenance burden** The app is automatically deployed on the customer device either by using the Internet, or preinstalled by the original equipment manufacturer. When a user first attaches the mobile broadband hardware, Windows automatically searches the Microsoft Store for a mobile broadband app that has been associated with the device by using service metadata, and automatically installs the appropriate app for the mobile broadband connection. This makes it easier for users to discover and use a mobile broadband device and services that are associated with that device.

This app does not provide connection management functionality, but instead provides account experience and branding for your service.

**Important**  
Your app must optimize for touch input and follow Windows 8 or Windows 8.1 UI design principles. For more info about how to design the user experience for mobile broadband apps, see [Designing the user experience of a mobile broadband app](designing-the-user-experience-of-a-mobile-broadband-app.md).

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Windows%20Store%20mobile%20broadband%20apps%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




