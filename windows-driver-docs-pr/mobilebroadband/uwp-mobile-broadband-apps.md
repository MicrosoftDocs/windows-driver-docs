---
title: UWP mobile broadband apps overview
description: UWP mobile broadband apps overview
ms.date: 07/05/2019
---

# UWP mobile broadband apps overview

The following sections are available in this topic:

- [UWP apps](#uwp-apps)
- [UWP mobile broadband apps](#uwp-mobile-broadband-apps)
- [UWP mobile broadband apps and MBAE apps](#uwp-mobile-broadband-apps-and-mbae)

## UWP apps

UWP apps are full-screen or windowed apps that are tailored for the following:

-   Your users’ needs

-   The devices that they run

-   Touch interaction

-   The Windows user interface

UWP apps are optimized for touch, are aware of the user's location and identity, and are hosted in the Microsoft Store. UWP apps are always on and available for instant use, and always connected with the latest content from the web. Users can discover and purchase these apps in the Microsoft Store: the apps can be installed quickly and uninstalled cleanly.

All UWP apps share the following features and benefits:

-   **Development platforms** UWP apps are built by using the Windows Software Development Kit for Windows 10 and the Windows Runtime APIs.

-   **Programming languages** You can build UWP apps by using JavaScript with an HTML and cascading style sheets (CSS) presentation layer, or by using C++ or C# with an Extensible Application Markup Language (XAML) presentation layer.

-   **Touch optimization** Touch interaction support is built-in. You can design your mobile broadband app for touch, and Windows gives you keyboard, mouse, and graphical scaling support.

For more info about UWP apps, see [Getting started with Windows 10 apps](/windows/uwp/get-started/).

## UWP mobile broadband apps


A UWP mobile broadband app is a UWP app that is authored by mobile operators and is associated with a mobile broadband connection. In addition to the benefits of being a UWP app, this app has special access to privileged mobile broadband APIs.

A mobile broadband app provides the following benefits:

-   **Increased customer connection** Users can easily discover the operator’s brand and services from the Windows **Start** screen and from the network list.

-   **Ongoing control over the experience** You can use the app to change subscribers’ account experiences.

-   **Reduced deployment and maintenance burden** The app is automatically deployed on the customer device either by using the Internet, or preinstalled by the original equipment manufacturer. When a user first attaches the mobile broadband hardware, Windows automatically searches the Microsoft Store for a mobile broadband app that has been associated with the device by using service metadata, and automatically installs the appropriate app for the mobile broadband connection. This makes it easier for users to discover and use a mobile broadband device and services that are associated with that device.

This app does not provide connection management functionality, but instead provides account experience and branding for your service.

> [!IMPORTANT]
> Your app must optimize for touch input and follow Windows 10 UI design principles. For more info about how to design the user experience for mobile broadband apps, see [Designing the user experience of a mobile broadband app](designing-the-user-experience-of-a-mobile-broadband-app.md).

## UWP mobile broadband apps and MBAE

Mobile broadband app experience apps, or MBAE apps, are replaced in Windows 10, version 1803 and later by MO UWP apps. MO UWP apps are now part of COSA and don't require creating service metadata on the Windows Dev Center Hardware dashboard (Sysdev). Windows 8, Windows 8.1, and versions of Windows 10 before 1803 continue to use MBAE apps via service metadata published on Sysdev. 

In Windows 10, version 1803, MBAE apps work without having to migrate to COSA. However, we strongly recommend that mobile operators migrate to an MO UWP app and COSA. For details about COSA, see [COSA overview](cosa-overview.md). For more information about COSA settings, see [Desktop COSA/APN database settings](desktop-cosa-apn-database-settings.md).

If the **AppID** setting is filled out in COSA, Windows will not check for a matching Sysdev metadata package to download your app. If **AppID** is not filled out, then Windows will check for a matching Sysdev metadata package to download your app.

The following table provides information about the differences between MBAE and MO UWP apps.

|  App type | Target platform | Delivery mechanism | Icon retrieval |
| --- | --- | --- | --- |
| MBAE | Windows 8, Windows 8.1, or Windows 10 | Sysdev metadata | Sysdev metadata or COSA if declared as part of the profile | 
| MO UWP app | Windows 10 (preferably version 1803 and later with the same SDK version) | COSA database | COSA database |

UI source code between MBAE and an MO UWP app might differ due to changes between Windows 8/Windows 8.1 and Windows 10 UI principles. Most business logic source code, however, should not require much change. For example, the code for accessing the back end and accessing mobile broadband information might be the same. However, MOs should validate each of the [Mobile broadband app scenarios](./account-management.md) accordingly.
