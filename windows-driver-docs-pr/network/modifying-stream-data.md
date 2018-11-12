---
title: Modifying Stream Data
description: Modifying Stream Data
ms.assetid: 8f591bc1-272c-4e53-8e49-3350c6a3a33e
keywords:
- classify callouts WDK Windows Filtering Platform , stream data changes
- stream data changes WDK Windows Filtering Platform
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Modifying Stream Data


When a callout processes data at the stream layer, its [*classifyFn*](https://msdn.microsoft.com/library/windows/hardware/ff544890) callout function can modify the data in the data stream. The callout's *classifyFn* callout function permits acceptable data in the stream to pass through unaltered, blocks data in the stream that is to be removed, and injects new or altered data into the stream when it is suitable.

A callout can replace data in the stream with other data by blocking the data that is to be replaced, and, at the same time, injecting the new data into the stream. In this situation, the new data is injected into the stream at the same point where the blocked data is removed from the stream.

For a callout driver to inject data into a data stream, it must first create an injection handle. This can be the same injection handle that is created for injecting modified packet data back into the network stack. See [Inspecting Packet and Stream Data](inspecting-packet-and-stream-data.md) for information about how to create an injection handle.

For information about how to modify stream data, see the "Windows Filtering Platform Stream Edit Sample" in the [Hardware Samples](http://go.microsoft.com/fwlink/p/?LinkId=618052) code gallery.

 

 





