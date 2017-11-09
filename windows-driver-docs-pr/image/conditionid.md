---
title: ConditionId element
description: The required ConditionId element uniquely identifies the device condition that was just cleared.
MS-HAID:
- 'wsdss\_events\_6b77a5ac-6e45-4535-a117-8f22b5f0b6b1.xml'
- 'image.conditionid'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4b154fb3-625e-478d-9bb4-92fd7cae0530
keywords: ["ConditionId element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ConditionId
api_type:
- Schema
---

# ConditionId element


The required **ConditionId** element uniquely identifies the device condition that was just cleared.

Usage
-----

``` syntax
<wscn:ConditionId>
  text
</wscn:ConditionId>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. An integer value that is equivalent to the Id attribute of a previously reported DeviceCondition element.

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
<td><p>[<strong>DeviceConditionCleared</strong>](deviceconditioncleared.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **ConditionId** element must be the **Id** attribute of a **DeviceCondition** element that the WSD Scan Service previously reported through [**ScannerStatusConditionEvent**](scannerstatusconditionevent.md).

## <span id="see_also"></span>See also


[**DeviceCondition**](devicecondition.md)

[**DeviceConditionCleared**](deviceconditioncleared.md)

[**ScannerStatusConditionEvent**](scannerstatusconditionevent.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ConditionId%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





