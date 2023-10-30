---
title: Battery devices design guide
description: Learn about battery device drivers, including writing battery miniclass drivers and UPS minidrivers.
ms.assetid: d8eecfcb-6c06-40d1-8c78-b8c88eb890f2
ms.date: 10/04/2023
ms.topic: article
---

# Battery devices design guide

A battery typically has a pair of drivers: the generic battery class driver provided by Microsoft, and a miniclass driver written specifically for that individual type of battery. The class driver defines the overall functionality of the batteries in the system and interacts with the power manager.

This design guide focuses on:

## Writing battery miniclass drivers

Learn how to write battery miniclass drivers by referring to the [Writing Battery Miniclass Drivers](writing-battery-miniclass-drivers.md) guide.

## Writing UPS minidrivers

Find information on writing UPS minidrivers, which were used with older versions of Windows, in the [Writing UPS Minidrivers](writing-ups-minidrivers.md) guide.
