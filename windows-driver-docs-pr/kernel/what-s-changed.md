---
title: What's Changed
description: What's Changed
ms.assetid: c7799406-d046-4261-8af7-7abbac18fa70
keywords: ["64-bit WDK kernel , porting drivers to", "porting drivers to 64-bit Windows", "64-bit pointers WDK kernel", "integer size WDK 64-bit", "data types WDK 64-bit", "64-bit WDK kernel , what's changed"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# What's Changed





On 32-bit Windows, the integer, long, and pointer data types are all the same size—32 bits. This convenient uniformity in data type sizes has been a boon to clever C programmers, many of whom have come to take it for granted.

On 64-bit Windows, however, this assumption of uniformity is no longer valid. Pointers are now 64 bits in length, but integer and long data types remain the same size as before—32 bits. This is because, while 64-bit pointers are needed to accommodate systems with as much as 16 TB of virtual memory, most data still fits comfortably into 32-bit integers. For most applications, changing the default integer size to 64 bits would only be a waste of space.

On 32-bit Windows platforms, the operating system automatically fixes kernel-mode memory alignment faults and makes them invisible to the application. It does this for the calling process and any descendant processes. This feature, which often dramatically reduces performance, has not been implemented in 64-bit Windows. Thus, if your 32-bit driver contains misalignment bugs, you will need to fix them when porting to 64-bit Windows.

 

 




