---
title: One Cannot detect Environment type
description: One Cannot detect Environment type
ms.assetid: d71ed95d-f070-4787-bcac-ca544ba34aa9
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# One Cannot detect Environment type


SDV reports this error message when it cannot determine which build environment was used in the verification.

SDV runs on x86-based and x64-based computers and supports all x86 and x64 build environments. However, SDV can run only on a 32-bit operating system. On a computer with an x86-based processor or a computer with an x64-based processor running in 32-bit mode, SDV runs in native mode. On a computer with an x64-based processor running in long mode, SDV runs in a 32-bit subsystem (WOW).

Also, be sure that you run SDV commands only from within a build environment window.

 

 





