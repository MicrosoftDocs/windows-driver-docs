---
title: Hardware access for Universal Windows Platform apps
author: windows-driver-content
description: Writing apps with custom capabilities
keywords:
- Custom , Capabilities
- UWP Apps
- Custom Capabilities
- UWP
- Hardware
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Hardware access for Universal Windows Platform apps

## Overview
The extensibility of the Windows platform has led to the creation of a
diverse ecosystem of device builders where innovative differentiation is
key to success for these device manufacturers, which enables unique
hardware and software experiences. [Universal Windows Platform
(UWP)](https://docs.microsoft.com/en-us/windows/uwp/get-started/universal-application-platform-guide)
applications create a broad range of scenarios such as to control
hardware device settings and provide a diverse app platform available on
any device running Windows 10.

Device and System vendors often provide their users with applications
that allow them to have some control over the functionality of their
hardware; previously apps with such functionality were not made as UWP
apps as they were unable to get access to system software from the app
container. They would come pre-installed or become installed with a
driver by a Windows Update or as an installation downloaded from the
internet. A problem would be that these applications couldn’t update
outside of an updater app, often required a co-installer, and could very
easily get out of sync.

For more information about developing specific types of UWP apps, see
[Develop UWP
apps](https://developer.microsoft.com/en-us/windows/apps/develop)**.**

## In this Section
|Topic|Description|
|-----|-----------|
|[Custom Capabilities for Universal Windows Platform Apps](custom-capabilities-for-universal-windows-platform-apps.md)| This section goes over what Custom Capabilities are and how they can be used in UWP Apps.|
|[Developing a Universal Windows Platform app with Custom Capabilities](developing-a-universal-windows-platform-app-with-custom-capabilities.md)| This section goes over how to use Custom Capabilities in developing UWP Apps.|
|[FAQ on custom capabilities](FAQ-on-custom-capabilities.md)| This Section goes over some of the frequently asked question about custom capabilities.|

## See Also

-   [App capabilities](https://docs.microsoft.com/en-us/windows/uwp/packaging/app-capability-declarations)

-   [Develop Windows Store apps using Visual Studio](https://developer.microsoft.com/en-us/windows/apps/develop)

-   [Develop UWP apps](https://developer.microsoft.com/en-us/windows/apps/develop)

-   [Custom Capability Sample App](http://go.microsoft.com/fwlink/p/?LinkId=846904)

-   [Sideload apps in Windows 10](https://technet.microsoft.com/library/mt269549.aspx)

-   [FAQ on custom capabilities](FAQ-on-custom-capabilities.md)
