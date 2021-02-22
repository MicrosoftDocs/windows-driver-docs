---
title: Obtaining Information About a General I/O Target in UMDF
description: Obtaining Information About a General I/O Target in UMDF
keywords:
- general I/O targets WDK UMDF , information about
- status information WDK I/O targets
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Obtaining Information About a General I/O Target in UMDF


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

To obtain information about an I/O target, a UMDF driver can call the following methods that the I/O target object defines:

<a href="" id="iwdfiotarget--gettargetfile"></a>[**IWDFIoTarget::GetTargetFile**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotarget-gettargetfile)  
Returns the framework file object that is associated with the I/O target.

<a href="" id="iwdfiotargetstatemanagement--getstate"></a>[**IWDFIoTargetStateManagement::GetState**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotargetstatemanagement-getstate)  
Returns state information for a local I/O target.

<a href="" id="iwdfremotetarget--getstate"></a>[**IWDFRemoteTarget::GetState**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfremotetarget-getstate)  
Returns state information for a remote I/O target.

 

