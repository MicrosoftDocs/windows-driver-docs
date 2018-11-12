---
title: Delivering Received Data From an Offload Target
description: Delivering Received Data From an Offload Target
ms.assetid: b4f8cb27-f0d8-401c-98ef-f1dfc62648a8
keywords:
- data I/O WDK TCP chimney offload , delivering data
- I/O WDK TCP chimney offload , delivering data
- delivering received data WDK TCP chimney offload
- received data processing WDK TCP chimney offload , delivering data
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Delivering Received Data From an Offload Target


\[The TCP chimney offload feature is deprecated and should not be used.\]

An offload target can deliver received data through the TCP chimney in either of the following ways:

-   By [completing a receive request](posting-and-completing-receive-requests.md)(a receive buffer) that has been preposted by an application.

-   By [indicating the received data](indicating-received-data-from-an-offload-target.md). An offload target can [use the receive indication size](using-the-specified-receive-indication-size.md) to optimize the delivery of received data.

The [delivery algorithm](delivery-algorithm.md) specifies the conditions under which an offload target must use a preposted receive request or make an receive indication.

 

 





