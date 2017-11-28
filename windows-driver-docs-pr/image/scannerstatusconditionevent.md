---
title: ScannerStatusConditionEvent element
description: The required ScannerStatusConditionEvent element provides the client with detailed information about a single status change in the scan device.
ms.assetid: 0a61fe67-ea1e-4143-afb8-edcdf50ee7c4
keywords: ["ScannerStatusConditionEvent element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScannerStatusConditionEvent
api_type:
- Schema
---

# ScannerStatusConditionEvent element


The required **ScannerStatusConditionEvent** element provides the client with detailed information about a single status change in the scan device.

Usage
-----

``` syntax
<wscn:ScannerStatusConditionEvent>
  child elements
</wscn:ScannerStatusConditionEvent>
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
<td><p>[<strong>DeviceCondition</strong>](devicecondition.md)</p></td>
</tr>
</tbody>
</table>

## Parent elements


There are no parent elements.

Remarks
-------

The WSD Scan Service sends a **ScannerStatusConditionEvent** element to a client when a [**DeviceCondition**](devicecondition.md) element is added or changed in the [**ActiveConditions**](activeconditions.md) element table. The body of **ScannerStatusConditionEvent** contains the new or changed **DeviceCondition** element.

The WSD Scan Service should send a [**ScannerStatusConditionClearedEvent**](scannerstatusconditionclearedevent.md) element to the client when the reported **DeviceCondition** has been cleared.

Examples
--------

The following code example shows how the scan device notifies the client about a scan lamp failure.

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
      http://schemas.microsoft.com/windows/2006/01/wdp/scan/ScannerStatusConditionEvent
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>

  <soap:Body>
    <wscn:ScannerStatusConditionEvent>
      <wscn:DeviceCondition wscn:Id="1543">
        <wscn:Time>2006-01-21T17:22:27.5242689Z</wscn:Time>
        <wscn:Name>LampError</wscn:Name>
        <wscn:Component>Platen</wscn:Component>
        <wscn:Severity>Critical</wscn:Severity>
      </wscn:DeviceCondition>
    </wscn:ScannerStatusConditionEvent>
  </soap:Body
</soap:Envelope>
```

## <span id="see_also"></span>See also


[**ActiveConditions**](activeconditions.md)

[**DeviceCondition**](devicecondition.md)

[**ScannerStatusConditionClearedEvent**](scannerstatusconditionclearedevent.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ScannerStatusConditionEvent%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





