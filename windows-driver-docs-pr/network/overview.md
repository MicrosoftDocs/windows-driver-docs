---
title: USB Remote NDIS overview
description: USB Remote NDIS overview
ms.assetid: 05714f49-38bc-4a36-83db-2eeb16c6add6
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# USB Remote NDIS overview

## <a href="" id="ddk-overview-ng"></a>


A USB Remote NDIS device is implemented as a USB Communication Device Class (CDC) device with two interfaces. A Communication Class interface, of type Abstract Control, and a Data Class interface combine to form a single functional unit representing the USB Remote NDIS device. The Communication Class interface includes a single endpoint for event notification and uses the shared bidirectional Control endpoint for control messages. The Data Class interface includes two bulk endpoints for data traffic.

>[!NOTE]
> An understanding of the Universal Serial Bus (USB) Specification versions 1.1 and 2.0 is required. The USB Communication Device Class (CDC) Specifications are suggested as references. These documents can be found at http://www.usb.org.

 

 

 





