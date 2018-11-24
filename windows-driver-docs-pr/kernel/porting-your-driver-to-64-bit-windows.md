---
title: Porting Your Driver to 64-Bit Windows
description: Porting Your Driver to 64-Bit Windows
ms.assetid: f06e6aae-fc44-481c-a277-1c266d6e6d7b
keywords: ["64-bit WDK kernel , porting drivers to", "porting drivers to 64-bit Windows", "thunking WDK", "WOW64 thunking layer WDK", "converting parameters to fixed-precision types"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Porting Your Driver to 64-Bit Windows





The 64-bit version of Windows is designed to make it possible for developers to use a single source-code base for their 32-bit and 64-bit Windows applications. To a large extent, this is also true for 32-bit and 64-bit Windows drivers.

For user-mode applications, 64-bit Windows includes a Windows on Windows (WOW64) *thunking layer* that enables 32-bit applications to execute (with some performance degradation) on 64-bit versions of Windows. It does this by intercepting 32-bit function calls and converting pointer-precision parameter types to fixed-precision types as appropriate before making the transition to the 64-bit kernel. This conversion process is called *thunking*.

**Note**  This thunking is only done for 32-bit *applications*; 32-bit *drivers* are not supported on 64-bit versions of Windows.

 

 

 




