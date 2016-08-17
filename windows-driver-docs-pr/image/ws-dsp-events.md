---
title: WS-DSP Events
description: WS-DSP Events
MS-HAID:
- 'dsm\_des\_theory\_859fe6ae-28fa-4173-83fc-20e50c4cd9d8.xml'
- 'image.ws\_dsp\_events'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 660d3110-c695-405e-8bab-c0a9c65fcc8f
---

# WS-DSP Events


Events are defined to inform the DSM Device of the status of active and finished post-scan jobs. The basic event model is based on Web Service Eventing. The DSM Device will only send events to subscribed clients as specified in WS-Eventing specification at [Web Services Eventing](http://go.microsoft.com/fwlink/p/?linkid=154074).

The following events must be produced by the DSM Scan Server and supported by the DSM Device:

**PostScanJobEndStateEvent** - sent by the DSM Scan Server to the DSM Device when a post-scan job has finished processing.

**PostScanJobStatusEvent** - sent by the DSM Scan Server to the DSM Device when a post-scan job's status has changed.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WS-DSP%20Events%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




