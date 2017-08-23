---
title: WDF General Object Macros
author: windows-driver-content
description: This section documents macros that support WDF general objects.
ms.assetid: 76639254-8912-40DA-9141-304EAA196CA5
ms.author: windowsdriverdev
ms.date: 08/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WDF General Object Macros


This section documents macros that support WDF general objects.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>WDF_DECLARE_CONTEXT_TYPE</strong>](wdf-declare-context-type.md)</p></td>
<td><div class="alert">
<strong>Note</strong>  Applies to KMDF and UMDF
</div>
<div>
 
</div>
<p>The WDF_DECLARE_CONTEXT_TYPE macro creates a name and an accessor method for a driver's object-specific context space.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>WDF_DECLARE_CONTEXT_TYPE_WITH_NAME</strong>](wdf-declare-context-type-with-name.md)</p></td>
<td><div class="alert">
<strong>Note</strong>  Applies to KMDF and UMDF
</div>
<div>
 
</div>
<p>The WDF_DECLARE_CONTEXT_TYPE_WITH_NAME macro creates an accessor method with a specified name for a driver's object-specific context space.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>WDF_DECLARE_CUSTOM_TYPE</strong>](wdf-declare-custom-type.md)</p></td>
<td><div class="alert">
<strong>Note</strong>  Applies to KMDF and UMDF
</div>
<div>
 
</div>
<p>The [<strong>WDF_DECLARE_CUSTOM_TYPE</strong>](wdf-declare-custom-type.md) macro creates a name and an accessor method for a driver's custom type.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE</strong>](wdf-object-attributes-init-context-type.md)</p></td>
<td><p>The [<strong>WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE</strong>](wdf-object-attributes-init-context-type.md) macro initializes a driver's [<strong>WDF_OBJECT_ATTRIBUTES</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure and inserts an object's driver-defined context information into the structure.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE</strong>](wdf-object-attributes-set-context-type.md)</p></td>
<td><div class="alert">
<strong>Note</strong>  Applies to KMDF and UMDF
</div>
<div>
 
</div>
<p>The WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE macro inserts an object's driver-defined context information into the object's [<strong>WDF_OBJECT_ATTRIBUTES</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>WDF_PTR_ADD_OFFSET</strong>](wdf-ptr-add-offset.md)</p></td>
<td><p>The [<strong>WDF_PTR_ADD_OFFSET</strong>](wdf-ptr-add-offset.md) macro adds an offset value to an address and returns the resulting address.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>WDF_PTR_ADD_OFFSET_TYPE</strong>](wdf-ptr-add-offset-type.md)</p></td>
<td><p>The [<strong>WDF_PTR_ADD_OFFSET_TYPE</strong>](wdf-ptr-add-offset-type.md) macro adds an offset value to an address and returns the resulting address cast to the specified type.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>WDF_PTR_GET_OFFSET</strong>](wdf-ptr-get-offset.md)</p></td>
<td><p>The [<strong>WDF_PTR_GET_OFFSET</strong>](wdf-ptr-get-offset.md) macro subtracts an address from another address and returns the resulting offset value.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>WdfObjectAddCustomType</strong>](wdfobjectaddcustomtype.md)</p></td>
<td><div class="alert">
<strong>Note</strong>  Applies to KMDF and UMDF
</div>
<div>
 
</div>
<p>The [<strong>WdfObjectAddCustomType</strong>](wdfobjectaddcustomtype.md) macro associates a framework object with a custom type.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>WdfObjectAddCustomTypeWithData</strong>](wdfobjectaddcustomtypewithdata.md)</p></td>
<td><div class="alert">
<strong>Note</strong>  Applies to KMDF and UMDF
</div>
<div>
 
</div>
<p>The [<strong>WdfObjectAddCustomTypeWithData</strong>](wdfobjectaddcustomtypewithdata.md) macro associates a framework object with a custom type, and optionally associates this pair with a data buffer and event callback functions.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>WdfObjectDereference</strong>](wdfobjectdereference.md)</p></td>
<td><div class="alert">
<strong>Note</strong>  Applies to KMDF and UMDF
</div>
<div>
 
</div>
<p>The [<strong>WdfObjectDereference</strong>](wdfobjectdereference.md) macro decrements the reference count for a specified framework object.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>WdfObjectDereferenceWithTag</strong>](wdfobjectdereferencewithtag.md)</p></td>
<td><div class="alert">
<strong>Note</strong>  Applies to KMDF and UMDF
</div>
<div>
 
</div>
<p>The [<strong>WdfObjectDereferenceWithTag</strong>](wdfobjectdereferencewithtag.md) macro decrements the reference count for a specified framework object and assigns the driver's current file name and line number to the reference. This macro also assigns a tag value to the reference.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>WdfObjectGetCustomTypeData</strong>](wdfobjectgetcustomtypedata.md)</p></td>
<td><div class="alert">
<strong>Note</strong>  Applies to KMDF and UMDF
</div>
<div>
 
</div>
<p>The [<strong>WdfObjectGetCustomTypeData</strong>](wdfobjectgetcustomtypedata.md) macro retrieves the data that the driver previously associated with a framework object and custom type.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>WdfObjectGetTypedContext</strong>](wdfobjectgettypedcontext.md)</p></td>
<td><div class="alert">
<strong>Note</strong>  Applies to KMDF and UMDF
</div>
<div>
 
</div>
<p>The [<strong>WdfObjectGetTypedContext</strong>](wdfobjectgettypedcontext.md) macro returns a pointer to an object's context space.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>WdfObjectIsCustomType</strong>](wdfobjectiscustomtype.md)</p></td>
<td><div class="alert">
<strong>Note</strong>  Applies to KMDF and UMDF
</div>
<div>
 
</div>
<p>The [<strong>WdfObjectIsCustomType</strong>](wdfobjectiscustomtype.md) macro determines whether a framework object is of a specified custom type.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>WdfObjectReference</strong>](wdfobjectreference.md)</p></td>
<td><div class="alert">
<strong>Note</strong>  Applies to KMDF and UMDF
</div>
<div>
 
</div>
<p>The [<strong>WdfObjectReference</strong>](wdfobjectreference.md) macro increments the reference count for a specified framework object.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>WdfObjectReferenceWithTag</strong>](wdfobjectreferencewithtag.md)</p></td>
<td><div class="alert">
<strong>Note</strong>  Applies to KMDF and UMDF
</div>
<div>
 
</div>
<p>The [<strong>WdfObjectReferenceWithTag</strong>](wdfobjectreferencewithtag.md) macro increments the reference count for a specified framework object and assigns the driver's current file name and line number to the reference. The macro also assigns a tag value to the reference.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20WDF%20General%20Object%20Macros%20%20RELEASE:%20%288/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


