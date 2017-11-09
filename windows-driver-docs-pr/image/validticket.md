---
title: ValidTicket element
description: The required ValidTicket element indicates whether a client's ScanTicket was valid.
MS-HAID:
- 'wsdss\_ops\_82219030-c722-4b9d-a2f6-6246c80383ad.xml'
- 'image.validticket'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8c2f35b5-1b1e-49a4-8aab-4d57ff9f1803
keywords: ["ValidTicket element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ValidTicket
api_type:
- Schema
---

# ValidTicket element


The required **ValidTicket** element indicates whether a client's [**ScanTicket**](scanticket.md) was valid.

Usage
-----

``` syntax
<wscn:ValidTicket>
  text
</wscn:ValidTicket>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. A Boolean value that must be 0, false, 1, or true.

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
<td><p>[<strong>ValidationInfo</strong>](validationinfo.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

A client submits a [**ScanTicket**](scanticket.md) for validation through the [**ValidateScanTicketRequest**](validatescanticketrequest.md) operation. The WSD Scan Service returns validation information, which includes **ValidTicket**, in [**ValidateScanTicketResponse**](validatescanticketresponse.md).

## <span id="see_also"></span>See also


[**ScanTicket**](scanticket.md)

[**ValidateScanTicketRequest**](validatescanticketrequest.md)

[**ValidateScanTicketResponse**](validatescanticketresponse.md)

[**ValidationInfo**](validationinfo.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ValidTicket%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





