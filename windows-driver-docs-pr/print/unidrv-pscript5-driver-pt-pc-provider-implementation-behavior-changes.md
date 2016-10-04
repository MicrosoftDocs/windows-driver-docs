---
title: Unidrv/PScript5 Driver PT/PC Provider Implementation Behavior Changes
author: windows-driver-content
description: Unidrv/PScript5 Driver PT/PC Provider Implementation Behavior Changes
MS-HAID:
- 'xpsconfig\_65d56bba-8ee5-48f4-b7ac-238c96ec68aa.xml'
- 'print.unidrv\_pscript5\_driver\_pt\_pc\_provider\_implementation\_behavior\_changes'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ff401ae8-b0c5-4f20-88dd-055a14e1d065
---

# Unidrv/PScript5 Driver PT/PC Provider Implementation Behavior Changes


When running in XPSDrv mode, a Unidrv or PScript5 driver's PrintTicket or print provider (PT/PC) provider implementation must also disable any Unidrv/PScript5 hard-coded features. That is, the PrintCapabilities XML should not contain any hard-coded capabiity, and the default PrintTicket or validated PrintTicket should not contain any hardcoded features.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Unidrv/PScript5%20Driver%20PT/PC%20Provider%20Implementation%20Behavior%20Changes%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


