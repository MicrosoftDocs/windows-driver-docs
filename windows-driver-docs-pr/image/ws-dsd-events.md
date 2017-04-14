---
title: WS-DSD Events
author: windows-driver-content
description: WS-DSD Events
ms.assetid: f690cb96-5b51-4909-b50e-77313d00a8de
---

# WS-DSD Events


The following events are defined to inform a control point when the configuration has changed in the DSM Device, and the status of active and finished scan jobs. The basic event model is based on web service eventing. The DSM Device will only send events to subscribed clients as specified in WS-Eventing specification at [Web Services Eventing](http://go.microsoft.com/fwlink/p/?linkid=154074).

The following events must be produced by the DSM Device:

**JobEndStateEvent** - sent by the DSM Device to the control point when a scan job has finished processing.

**JobStatusEvent** - sent by the DSM Device to the control point when a scan job's status has changed.

**ScannerElementsChangedEvent** - sent by the DSM Device to the control point when something has changed in the **ScannerDescription** element, the **ScannerConfiguration** element, the **DefaultScanTicket** element, or an IHV extension element.

**ScannerStatusConditionClearedEvent** - sent by the DSM Device to the control point when a previously reported status condition has been cleared.

**ScannerStatusConditionEvent** - sent by the DSM Device to provide the control point with detailed information about a status change in the device.

**ScannerStatusSummaryEvent** - sent by the DSM Device to the control point when the device status has changed.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WS-DSD%20Events%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


