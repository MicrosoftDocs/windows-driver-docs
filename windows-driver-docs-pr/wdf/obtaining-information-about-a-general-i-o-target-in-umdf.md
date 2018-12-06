---
title: Obtaining Information About a General I/O Target in UMDF
description: Obtaining Information About a General I/O Target in UMDF
ms.assetid: 306a7f46-423a-4647-846d-76f917ca0f7c
keywords:
- general I/O targets WDK UMDF , information about
- status information WDK I/O targets
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Obtaining Information About a General I/O Target in UMDF


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

To obtain information about an I/O target, a UMDF driver can call the following methods that the I/O target object defines:

<a href="" id="iwdfiotarget--gettargetfile"></a>[**IWDFIoTarget::GetTargetFile**](https://msdn.microsoft.com/library/windows/hardware/ff559243)  
Returns the framework file object that is associated with the I/O target.

<a href="" id="iwdfiotargetstatemanagement--getstate"></a>[**IWDFIoTargetStateManagement::GetState**](https://msdn.microsoft.com/library/windows/hardware/ff559202)  
Returns state information for a local I/O target.

<a href="" id="iwdfremotetarget--getstate"></a>[**IWDFRemoteTarget::GetState**](https://msdn.microsoft.com/library/windows/hardware/ff560265)  
Returns state information for a remote I/O target.

 

 





