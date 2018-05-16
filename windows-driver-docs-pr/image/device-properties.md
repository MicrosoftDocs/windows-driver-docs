---
title: Device Properties
author: windows-driver-content
description: Device Properties
ms.assetid: f41040c5-0eac-450d-b532-9165c543cc1a
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Device Properties


## <a href="" id="ddk-device-properties-si"></a>


All still image devices have specific characteristics that describe that device. For example, two characteristics of a flatbed scanner are its horizontal and vertical bed sizes. A possible characteristic of a digital still camera is its battery status, which indicates remaining battery life.

Similarly, data that the device produces or stores can also be described with characteristics. For example, the data produced by a scanner can be described by the number of pixels on a line and the number of bits per pixel.

In WIA, characteristics that describe both devices and data are referred to as *properties*. Properties exist in sets; the WIA minidriver maintains them in a WIA driver item.

 

 




