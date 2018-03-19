---
title: Unidrv/PScript5 driver PT/PC provider implementation behavior
author: windows-driver-content
description: Unidrv and PScript5 driver PrintTicket or print provider (PT/PC) implementation behavior changes
ms.assetid: ff401ae8-b0c5-4f20-88dd-055a14e1d065
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Unidrv/PScript5 driver PT/PC provider implementation behavior changes


When running in XPSDrv mode, a Unidrv or PScript5 driver's PrintTicket or print provider (PT/PC) implementation must also disable any Unidrv/PScript5 hard-coded features. That is, the PrintCapabilities XML should not contain any hard-coded capabiity, and the default PrintTicket or validated PrintTicket should not contain any hardcoded features.

 

 


