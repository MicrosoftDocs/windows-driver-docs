---
title: Ndi Values and Keys Not Used in Windows 2000 and Later Versions
description: Ndi Values and Keys Not Used in Windows 2000 and Later Versions
ms.assetid: 932e1c83-feb6-47a8-bed3-847ee4094b9e
keywords:
- add-registry-sections WDK networking , Ndi values and keys
- Ndi key WDK networking
- Ndi value WDK networking
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Ndi Values and Keys Not Used in Windows 2000 and Later Versions


## <a href="" id="ddk-ndi-values-and-keys-not-used-in-windows-2000-and-later-versions-ng"></a>


**Important**  The following **Ndi** registry keys and values are available in Windows 95/98/Me but are not used in Windows 2000 and later versions of the operating system. This information is provided to aid developers who are migrating network drivers from Windows 95/98/Me to Windows 2000 and later versions of the operating system.

 

**DeviceVxD**

**DevLoader**

**DriverDesc**

**InfFile**

**InfSelection**

**Ndi\\CardType**

**Ndi\\Compability**

**Ndi\\DeviceID**

**Ndi\\***filename*\\...

**Ndi\\Install**

**Ndi\\InstallInf**

**Ndi\\Interfaces\\DefLower**

**Ndi\\Interfaces\\DefUpper**

**Ndi\\Interfaces\\ExcludeAny**

**Ndi\\Interfaces\\RequireAny**

**Ndi\\NdiInstaller**

**Ndi\\***param-key-name***\\resc**

**Ndi\\Params\\***param-key-name***\\flag**

**Ndi\\Params\\***param-key-name***\\location**

**Ndi\\Remove**

**NDIS**\\...

**StaticVxD**

In particular, Windows 2000 does not support **Ndi\\***param-key-name***\\resc** and **Ndi\\Params\\***param-key-name***\\flag** values. This means that a user cannot specify adapter resources through the **Advanced** properties page.

 

 





