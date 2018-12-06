---
title: Introduction to Windows Filtering Platform Callout Drivers
description: Introduction to Windows Filtering Platform Callout Drivers
ms.assetid: d075da82-8dbc-41a5-a081-dd0e2b292371
keywords:
- Windows Filtering Platform callout drivers WDK , about callout drivers
- callout drivers WDK Windows Filtering Platform , about callout drivers
- callouts WDK Windows Filtering Platform
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to Windows Filtering Platform Callout Drivers


This section introduces Windows Filtering Platform [callout drivers](callout-driver.md). For a more information about the Windows Filtering Platform, see the [Windows Filtering Platform](http://go.microsoft.com/fwlink/p/?linkid=90220) documentation in the Microsoft Windows SDK.

### Purpose of Callout Drivers

A callout driver implements one or more [callouts](callout.md). Callouts extend the capabilities of the Windows Filtering Platform by processing TCP/IP-based network data in ways that are beyond the scope of the simple filtering functionality. Callouts are typically used to do the following tasks:

<a href="" id="deep-inspection-------"></a>**Deep Inspection**   
Perform complex inspection of the network data to determine which data should be blocked, which data should be permitted, and which data should be passed to another filter. An antivirus product, for example, could look for virus signatures.

<a href="" id="packet-modification-------"></a>**Packet Modification**   
Perform modification and reinjection of the network packet headers or data, or both. A network address translation (NAT) product, for example, could modify the headers on IPv4 packets.

<a href="" id="stream-modification-------"></a>**Stream Modification**   
Perform modification and reinjection of the network data in a stream. A parental control product, for example, could remove or replace specific words or phrases in a data stream.

<a href="" id="data-logging-------"></a>**Data Logging**   
Log of network traffic data. A network monitoring product, for example, could count the number of data packets that are discarded for a specific reason.

In addition to processing network data, callout drivers can perform other Windows Filtering Platform management tasks, such as adding filters to the base filtering engine. For more information about other tasks that a callout driver can perform, see [Calling Other Windows Filtering Platform Functions](calling-other-windows-filtering-platform-functions.md).

 

 





