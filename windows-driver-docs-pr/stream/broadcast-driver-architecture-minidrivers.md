---
title: Broadcast Driver Architecture Minidrivers
description: Broadcast Driver Architecture Minidrivers
ms.assetid: 0ad56dbd-6f79-439f-8dfc-8d118d114ddd
keywords:
- Broadcast Driver Architecture WDK AVStream , minidrivers
- BDA WDK AVStream , minidrivers
- minidrivers WDK BDA
- BDA minidrivers WDK AVStream
- BDA minidrivers WDK AVStream , about BDA minidrivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Broadcast Driver Architecture Minidrivers





Broadcast Driver Architecture (BDA) minidrivers control hardware that performs the following operations:

-   Tuning a digital broadcast signal

-   Demodulating the digital signal

-   Capturing frames of the digital signal

-   Demultiplexing the signal into video, audio, and data streams

BDA minidrivers are AVStream minidrivers that run under the [AVStream module](avstream-overview.md) in the kernel-streaming driver *ks.sys*. AVStream is a class driver that provides a unified kernel streaming class model for both audio and video minidrivers, and that supports use of COM objects without altering existing minidriver binaries. The AVStream class driver provides much of the default behavior required to make a minidriver's filter work as a WDM kernel streaming compliant filter. To simplify the task of writing BDA minidrivers, you can use the BDA support library (*Bdasup.lib*) of functions that is included in the Microsoft Windows Driver Kit (WDK). This library provides extensive default handling for the BDA minidriver's property and method sets.

Typically, driver writers only have to code the appropriate static template structures, register them with the BDA support library, and then let the library provide default handling for all the properties and methods. In some instances, a BDA minidriver must intercept a property or method request and perform appropriate operations.

The following figure shows an architectural overview for BDA minidrivers:

![diagram overview of bda minidriver architecture](images/bdaarch.png)

The following sections describe implementation details for a BDA minidriver, discuss details of some property and method sets, and contain sample code that shows how to intercept certain properties and methods:

[Initializing a BDA Minidriver](initializing-a-bda-minidriver.md)

[Starting a BDA Minidriver](starting-a-bda-minidriver.md)

[Creating Dispatch Tables](creating-dispatch-tables.md)

[Defining Automation Tables](defining-automation-tables.md)

[Initializing a BDA Filter](initializing-a-bda-filter.md)

[Using BDA Property and Method Sets](using-bda-property-and-method-sets.md)

[Caching Pin Information for DirectShow](caching-pin-information-for-directshow.md)

[Securing a BDA Minidriver](securing-a-bda-minidriver.md)

[Connecting Between Pins of Filters for BDA Minidrivers](connecting-between-pins-of-filters-for-bda-minidrivers.md)

 

 




