---
title: Power-down sequence for a NetAdapterCx client driver
description: Power-down sequence for a NetAdapterCx client driver
ms.assetid: 9E16172C-9E45-4ED7-B6D2-7539DF4718B5
keywords:
- Power-down sequence for a NetAdapterCx client driver
ms.author: windowsdriverdev
ms.date: 06/05/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Power-down sequence for a NetAdapterCx client driver

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The following figure shows the order in which NetAdapterCx calls a client driver's event callback functions when powering down and removing the device. The sequence starts at the top of the figure with an operational device that is in the working power state (D0):

<img src="images/powerdown.png" alt="Device enumeration and power-down sequence for NetAdapterCx client driver" title="Device enumeration and power-down sequence for NetAdapterCx client driver" style="width: 600px;"/>

The broad horizontal lines mark the steps that are involved in powering down a device. The column on the left side of the figure describes the step, and the column on the right lists the event callbacks that accomplish it. Steps marked with blue text and a bold outline are specific to NetAdapterCx, while other steps are common to all WDF-based drivers.

As the figure shows, the power-down and removal sequence involves calling the corresponding "undo" callbacks in the reverse order in which the framework called the functions that are involved in making the device operational. The framework deletes the device object after it deletes the device object context area.
