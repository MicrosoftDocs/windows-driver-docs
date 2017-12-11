---
title: ScannerStatusConditionClearedEvent element
description: The required ScannerStatusConditionClearedEvent element informs the client that a previously reported DeviceCondition condition has been cleared at the scanner.
ms.assetid: c849caba-d77b-441b-a5e1-94f9285cef3f
keywords: ["ScannerStatusConditionClearedEvent element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScannerStatusConditionClearedEvent
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ScannerStatusConditionClearedEvent element


The required **ScannerStatusConditionClearedEvent** element informs the client that a previously reported [**DeviceCondition**](devicecondition.md) condition has been cleared at the scanner.

Usage
-----

``` syntax
<wscn:ScannerStatusConditionClearedEvent>
  child elements
</wscn:ScannerStatusConditionClearedEvent>
```

Attributes
----------

There are no attributes.

## Child elements


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
<td><p>[<strong>DeviceConditionCleared</strong>](deviceconditioncleared.md)</p></td>
</tr>
</tbody>
</table>

## Parent elements


There are no parent elements.

Remarks
-------

The WSD Scan Service sends a **ScannerStatusConditionClearedEvent** element when a device condition that is identified in [**ScannerStatusConditionEvent**](scannerstatusconditionevent.md) has been cleared. **ScannerStatusConditionClearedEvent** contains a [**DeviceConditionCleared**](deviceconditioncleared.md) element that contains the cleared condition and the time at which it was cleared.

Examples
--------

The following code example shows how the device notifies a client that the previous condition that ConditionId 1543 identified has cleared:

```
<soap:Envelope
  xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
  xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing"
  xmlns:wse="http://schemas.xmlsoap.org/ws/2004/08/eventing"
  xmlns:wscn="http://schemas.microsoft.com/windows/2006/01/wdp/scan"
  soap:encodingStyle=&#39;http://www.w3.org/2002/12/soap-encoding&#39;>

  <soap:Header>
    <wsa:To>AddressofEventSink</wsa:To>
    <wsa:Action>
      http://schemas.microsoft.com/windows/2006/01/wdp/scan/ScannerStatusConditionClearedEvent
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>

  <soap:Body>
    <wscn:ScannerStatusConditionClearedEvent>
      <wscn:DeviceConditionCleared>
        <wscn:ConditionId>1543</wscn:ConditionId>
        <wscn:ConditionClearTime>
          2006-01-21T17:22:35.8345Z
        </wscn:ConditionClearTime>
      </wscn:DeviceConditionCleared>
    </wscn:ScannerStatusConditionClearedEvent>
  </soap:Body
</soap:Envelope>
```

## <span id="see_also"></span>See also


[**ConditionId**](conditionid.md)

[**DeviceCondition**](devicecondition.md)

[**DeviceConditionCleared**](deviceconditioncleared.md)

[**ScannerStatusConditionEvent**](scannerstatusconditionevent.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ScannerStatusConditionClearedEvent%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





