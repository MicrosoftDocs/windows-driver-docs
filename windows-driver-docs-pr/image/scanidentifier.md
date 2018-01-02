---
title: ScanIdentifier element
description: The required ScanIdentifier element contains a device-specific string that the scanner provides through a ScanAvailableEvent event.
ms.assetid: 77116871-63dc-4388-9b36-a553219ddcf7
keywords: ["ScanIdentifier element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScanIdentifier
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ScanIdentifier element


The required **ScanIdentifier** element contains a device-specific string that the scanner provides through a [**ScanAvailableEvent**](scanavailableevent.md) event.

Usage
-----

``` syntax
<wscn:ScanIdentifier>
  text
</wscn:ScanIdentifier>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. Any valid character string.

## Child elements


There are no child elements.

## Parent elements


<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>CreateScanJobRequest</strong>](createscanjobrequest.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ScanAvailableEvent</strong>](scanavailableevent.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The client can send the **ScanIdentifier** element to the WSD Scan Service in a [**CreateScanJobRequest**](createscanjobrequest.md) operation element. The WSD Scan Service can use **ScanIdentifier** to ensure that the correct client is requesting the scan after a user has selected the destination.

The **ScanIdentifier** value must be unique for every [**ScanAvailableEvent**](scanavailableevent.md) instance.

## <span id="see_also"></span>See also


[**CreateScanJobRequest**](createscanjobrequest.md)

[**ScanAvailableEvent**](scanavailableevent.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ScanIdentifier%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





