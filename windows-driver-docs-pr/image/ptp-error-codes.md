---
title: PTP Error Codes
author: windows-driver-content
description: PTP Error Codes
MS-HAID:
- 'WIA\_drv\_cam\_4f63c523-5cc6-41bb-9f12-ab91c5e96822.xml'
- 'image.ptp\_error\_codes'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4d7ad081-fc0b-4a9e-8f17-a0c98fa4fa50
---

# PTP Error Codes


## <a href="" id="ddk-ptp-error-codes-si"></a>


When the Microsoft PTP WIA minidriver detects an error, it passes the response code to WIA. If the PTP camera returns a response other than 0x2001 (OK), the WIA minidriver returns the response code wrapped as an HRESULT error code. The format of the error code is 0x8004XXXX, where XXXX represents the four hexadecimal digits of the response code. This is very useful for WIA applications that are designed to work with specific PTP cameras. The error/status information is preserved for rich status to be reported to the end user.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20PTP%20Error%20Codes%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


