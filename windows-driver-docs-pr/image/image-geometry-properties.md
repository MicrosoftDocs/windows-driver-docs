---
title: Image Geometry Properties
description: Image Geometry Properties
ms.assetid: d1343ad4-3a54-414c-bc08-e07e0fb079cd
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Image Geometry Properties





The ImgPixHeight and ImgPixWidth image geometry properties (see the PIMA 15740 standard) are optional in PTP. For cameras that do not implement these properties, the Microsoft PTP minidriver downloads the entire image and calculates the correct values for these properties. You can prevent this from occurring by implementing these optional PTP properties.

 

 




