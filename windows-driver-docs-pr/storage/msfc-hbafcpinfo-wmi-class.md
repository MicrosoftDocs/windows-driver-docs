---
title: MSFC\_HBAFCPInfo WMI Class
description: MSFC\_HBAFCPInfo WMI Class
ms.assetid: db11c2f8-3d68-47f0-ae77-42cd20812673
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSFC\_HBAFCPInfo WMI Class


## <span id="ddk_msfc_hbafcpinfo_wmi_class_kr"></span><span id="DDK_MSFC_HBAFCPINFO_WMI_CLASS_KR"></span>


A WMI client uses the MSFC\_HBAFCPInfo class to query an HBA miniport driver for fibre channel protocol (FCP) information as defined in the section on FCP Information Functions in the T11 committee's *Fibre Channel HBA API* specification.

This WMI class has no data blocks, and therefore the WMI tool suite generates structures that hold parameter data for the methods that belong to the class, but it does not generate a structure corresponding to the class itself.

The MOF syntax for each method that belongs to this class is described in the reference page for the method. The following sections describe these methods and their accompanying structures:

[**GetBindingCapability**](getbindingcapability.md)

[**GetBindingSupport**](getbindingsupport.md)

[**GetFcpTargetMapping**](getfcptargetmapping.md)

[**GetFcpPersistentBinding**](getfcppersistentbinding.md)

[**GetPersistentBinding2**](getpersistentbinding2.md)

[**RemovePersistentEntry**](removepersistententry.md)

[**SetBindingSupport**](setbindingsupport.md)

[**SetPersistentEntry**](setpersistententry.md)

 

 





