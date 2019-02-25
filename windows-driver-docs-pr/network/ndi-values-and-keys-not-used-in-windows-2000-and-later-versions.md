---
title: Deprecated Ndi Values and Keys 
description: Ndi Values and Keys deprecated in Windows 2000 and Later Versions
ms.assetid: 932e1c83-feb6-47a8-bed3-847ee4094b9e
keywords:
- add-registry-sections WDK networking , Ndi values and keys
- Ndi key WDK networking
- Ndi value WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deprecated Ndi Values and Keys





**Important**  The following **Ndi** registry keys and values are no longer used in the Windows operating system. If you are migrating network drivers from Windows 95/98/Me to later versions of the operating system, do not use these values.

 

**DeviceVxD**

**DevLoader**

**DriverDesc**

**InfFile**

**InfSelection**

**Ndi\\CardType**

**Ndi\\Compability**

**Ndi\\DeviceID**

**Ndi\\**<em>filename</em>\\...

**Ndi\\Install**

**Ndi\\InstallInf**

**Ndi\\Interfaces\\DefLower**

**Ndi\\Interfaces\\DefUpper**

**Ndi\\Interfaces\\ExcludeAny**

**Ndi\\Interfaces\\RequireAny**

**Ndi\\NdiInstaller**

**Ndi\\**<em>param-key-name</em>**\\resc**

**Ndi\\Params\\**<em>param-key-name</em>**\\flag**

**Ndi\\Params\\**<em>param-key-name</em>**\\location**

**Ndi\\Remove**

**NDIS**\\...

**StaticVxD**

Because Windows does not support **Ndi\\**<em>param-key-name</em>**\\resc** and **Ndi\\Params\\**<em>param-key-name</em>**\\flag** values, a user cannot specify adapter resources through the **Advanced** properties page.

 

 





