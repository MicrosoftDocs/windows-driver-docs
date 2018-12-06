---
title: MSFC\_HBAAdapterMethods WMI Class
description: MSFC\_HBAAdapterMethods WMI Class
ms.assetid: 2fb2b055-475e-47bf-bd36-3901120e8992
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MSFC\_HBAAdapterMethods WMI Class


## <span id="ddk_msfc_hbaadaptermethods_wmi_class_kr"></span><span id="DDK_MSFC_HBAADAPTERMETHODS_WMI_CLASS_KR"></span>


An HBA miniport driver that supports the T11 committee's *Fibre Channel HBA API* specification uses the MSFC\_HBAAdapterMethods class to provide Fibre Channel-style services to WMI clients. Fibre channel services are defined by the T11 committee's *Fibre Channel HBA API* specification.

This WMI class has no data blocks, and therefore the WMI tool suite generates structures that hold parameter data for the methods that belong to the class, but it does not generate a structure corresponding to the class itself.

The MOF syntax for each method that belongs to this class is described in the reference page for the method. The following sections describe these methods and their accompanying structures:

[**GetDiscoveredPortAttributes**](getdiscoveredportattributes.md)

[**GetEventBuffer**](geteventbuffer.md)

[**GetFC3MgmtInfo**](getfc3mgmtinfo.md)

[**GetFC4Statistics**](getfc4statistics.md)

[**GetFCPStatistics**](getfcpstatistics.md)

[**GetPortAttributesByWWN**](getportattributesbywwn.md)

[**RefreshInformation**](refreshinformation.md)

[**ScsiInquiry**](scsiinquiry.md)

[**ScsiReadCapacity**](scsireadcapacity.md)

[**ScsiReportLuns**](scsireportluns.md)

[**SendCTPassThru**](sendctpassthru.md)

[**SendLIRR**](sendlirr.md)

[**SendRLS**](sendrls.md)

[**SendRNID**](sendrnid.md)

[**SendRNIDV2**](sendrnidv2.md)

[**SendRPL**](sendrpl.md)

[**SendRPS**](sendrps.md)

[**SendSRL**](sendsrl.md)

[**SetFC3MgmtInfo**](setfc3mgmtinfo.md)

 

 





