---
title: WIA\_DPS\_DEVICE\_ID
description: The WIA\_DPS\_DEVICE\_ID property contains a unique Function Instance identifier for a web services scanner device.
ms.assetid: 48c45b94-86b1-41b5-89bc-e3270ad56d7e
keywords: ["WIA_DPS_DEVICE_ID Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_DEVICE_ID
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA\_DPS\_DEVICE\_ID


The WIA\_DPS\_DEVICE\_ID property contains a unique Function Instance identifier for a web services scanner device. This identifier represents the web service on the scanner device with which the WIA minidriver is communicating. No assumptions about the form of this identifier should be made. The WIA minidriver creates and maintains this property.

WIA applications can use the value of WIA\_DPS\_DEVICE\_ID to find, using the Function Discovery API, the Function Instance object that represents the web services scanner device used in the current WIA session.

Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The WIA minidriver initializes this property at run time by reading the PKEY\_PNPX\_ID device property from the Function Instance object.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**WIA\_DPS\_GLOBAL\_IDENTITY**](wia-dps-global-identity.md)

[**WIA\_DPS\_SERVICE\_ID**](wia-dps-service-id.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DPS_DEVICE_ID%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





