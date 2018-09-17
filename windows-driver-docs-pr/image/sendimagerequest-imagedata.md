---
title: SendImageRequest.ImageData
description: SendImageRequest.ImageData
ms.assetid: b14dc6a4-b237-46f0-b40f-dec0545f1a16
keywords: ["SendImageRequest.ImageData"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# SendImageRequest.ImageData


The **ImageData** element contains the image data that is attached to a **SendImageRequest** message.

A WS-DSP client running on a DSM scan device uses the W3C Message Transmission Optimization Mechanism (MTOM) to attach an image file to a **SendImageRequest** message. MTOM uses XML-Binary Optimized Packaging (XOP) to encode binary data for transmission as part of a SOAP message.

An XML-Binary Optimized Packaging (XOP) **Include** element that identifies the location of the image data that is attached to the **SendImageRequest** message

 

 





