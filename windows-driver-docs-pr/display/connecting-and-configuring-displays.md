---
title: Implementing display connection and configuration
description: Describes API that user-mode display driver writers and OEMs can use to connect and configure displays.
keywords:
- connecting displays API , WDK , Windows
- configuring displays API, WDK , Windows
- connecting displays DDI , WDK , Windows
- configuring displays DDI, WDK , Windows
- connecting and configuring displays API, DDI , WDK , Windows
- CCD APIs, WDK , Windows
ms.date: 04/24/2025
ms.topic: concept-article
---

# Implementing display connection and configuration

Display driver developers and OEMs can use the Connecting and Configuring Displays (CCD) interface to provide greater control over desktop display setup. The CCD interface consists of:

* A set of [user-mode APIs](ccd-apis.md) that user-mode drivers (UMDs) and OEM applications can call. The display control panel, hot keys, and the Hot Plug Detection (HPD) manager can use the CCD APIs. OEMs can use the CCD APIs for their value-add applets instead of using private driver escapes.

* [Kernel-mode DDIs](ccd-ddis.md) that kernel-mode display miniport drivers (KMDs) can call.

The CCD APIs provide the following functionality:

* Enumerate the display paths that are possible from the currently connected displays.

* Set the topology (for example, clone and extend), layout information, resolution, orientation, and aspect ratio for all the connected displays in one function call. With only a single function call, the number of screen flashes is reduced.

* Add or update settings to the persistence database.

* Apply settings that are persisted in the database.

* Use best mode logic to apply optimum display settings.

* Use best topology logic to apply the optimum topology for the connected displays.

* Start or stop forced output.

* Allow OEM hot keys to use the operating system persistence database.

The CCD APIs can't handle the following tasks:

* Replace the API sets and private driver escapes that hardware vendors previously provided to control desktop display setup before Windows 7.

* Pass private data down to the KMD.

* Provide a set of monitor-control APIs.

* Query the monitor capabilities, which include EDID, DDCCI, and so on.

* Provide a context identifier to uniquely identify the settings that the CCD APIs retrieve from the persistence database.

Although the CCD API allows a caller to get and set the displays, it doesn't provide any functionality to enumerate the possible source modes in a given path. APIs that existed before Windows 7 already provide this functionality.
