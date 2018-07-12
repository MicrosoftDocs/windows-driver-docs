---
title: Security Issues for Still Image Drivers
author: windows-driver-content
description: Security Issues for Still Image Drivers
ms.assetid: ad795cf0-8bff-4b9b-ac43-94c74cc19d60
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Security Issues for Still Image Drivers





It is important to remember that a user-mode minidriver can be called either from an application (through an image acquisition API), or from the still image event monitor (which is implemented as a Windows 2000 service). There are security implications associated with these multiple calling sources. For example, if a user-mode minidriver creates a mutex using the default security descriptor (by specifying a **NULL** security descriptor), one mutex cannot be shared between an instance of the minidriver called from the event monitor and one called from an image acquisition API.

 

 




