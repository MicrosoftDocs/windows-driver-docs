---
title: DeviceConditionCleared element
description: The required DeviceConditionCleared element contains information about a previously reported DeviceCondition condition that has been cleared.
MS-HAID:
- 'wsdss\_events\_7a8940da-7efc-4651-86d6-a98b5fcbe5c7.xml'
- 'image.deviceconditioncleared'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f4ed3d25-cee0-4532-84aa-d1cdd144ce2a
keywords: ["DeviceConditionCleared element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn DeviceConditionCleared
api_type:
- Schema
---

# DeviceConditionCleared element


The required **DeviceConditionCleared** element contains information about a previously reported [**DeviceCondition**](devicecondition.md) condition that has been cleared.

Usage
-----

``` syntax
<wscn:DeviceConditionCleared>
  child elements
</wscn:DeviceConditionCleared>
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
<td><p>[<strong>ConditionClearTime</strong>](conditioncleartime.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ConditionId</strong>](conditionid.md)</p></td>
</tr>
</tbody>
</table>

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
<td><p>[<strong>ScannerStatusConditionEvent</strong>](scannerstatusconditionevent.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **DeviceConditionCleared** element contains the [**ConditionId**](conditionid.md) and [**ConditionClearTime**](conditioncleartime.md) elements, which specify the condition identifier and time at which the condition was cleared, respectively. The WSD Scan Service sends the **DeviceConditionCleared** element to a client in a [**ScannerStatusConditionClearedEvent**](scannerstatusconditionclearedevent.md) event element.

## <span id="see_also"></span>See also


[**ConditionClearTime**](conditioncleartime.md)

[**ConditionId**](conditionid.md)

[**DeviceCondition**](devicecondition.md)

[**DeviceConditionCleared**](deviceconditioncleared.md)

[**ScannerStatusConditionClearedEvent**](scannerstatusconditionclearedevent.md)

[**ScannerStatusConditionEvent**](scannerstatusconditionevent.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20DeviceConditionCleared%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





