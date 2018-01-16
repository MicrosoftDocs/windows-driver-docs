---
title: MSFC\_HBAAdapterMethods WMI Class
description: MSFC\_HBAAdapterMethods WMI Class
ms.assetid: 2fb2b055-475e-47bf-bd36-3901120e8992
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSFC_HBAAdapterMethods%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




