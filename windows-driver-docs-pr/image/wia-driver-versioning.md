---
title: WIA Driver Versioning
description: WIA Driver Versioning
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Driver Versioning


A driver reports the version of WIA (or STI for legacy drivers) that it supports in the version field that is returned from [**IStiUSD::GetCapabilities**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-getcapabilities). Drivers typically set this field to STI\_VERSION, which is defined in *Sti.h*.

In the Windows Driver Kit (WDK) for Windows Vista, the value of STI\_VERSION is greater than the value of STI\_VERSION in previous operating systems. If a driver has the Windows Vista value for its driver version, it must support Windows Vista [IStream data transfers](istream-data-transfers.md).

A Windows Vista driver that adheres to the new Windows Vista WIA model must return STI\_VERSION\_3 in the version field that is returned from **IStiUSD::GetCapabilities**.

 

