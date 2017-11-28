---
title: DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI
description: DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI
ms.assetid: ac883bc8-3956-4bc3-a11e-b6e036305329
keywords: ["DEBUG_REQUEST_EXT_TYPED_DATA_ANSI Windows Debugging"]
topic_type:
- apiref
api_name:
- DEBUG_REQUEST_EXT_TYPED_DATA_ANSI
api_type:
- NA
---

# DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI


The DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI [**Request**](request.md) operation performs a variety of different sub-operations that aid in the interpretation of typed data.

**Parameters**

<span id="InBuffer"></span><span id="inbuffer"></span><span id="INBUFFER"></span>*InBuffer*  
Specifies the [**EXT\_TYPED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545306) structure that determines the sub-operation to perform. This EXT\_TYPED\_DATA structure contains the input parameters for that sub-operation along with any (optional) additional data. The additional data is included in *InBuffer* after the EXT\_TYPED\_DATA structure. The size of *InBuffer* is the total size of the buffer that contains the EXT\_TYPED\_DATA structure and the additional data. See **EXT\_TYPED\_DATA** for details on this structure and how to include the additional data.

The following sub-operations are supported.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Sub-Operation</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>EXT_TDOP_COPY</strong>](ext-tdop-copy.md)</p></td>
<td align="left"><p>Makes a copy of a typed data description.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EXT_TDOP_RELEASE</strong>](ext-tdop-release.md)</p></td>
<td align="left"><p>Releases a typed data description.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EXT_TDOP_SET_FROM_EXPR</strong>](ext-tdop-set-from-expr.md)</p></td>
<td align="left"><p>Returns the value of an expression.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EXT_TDOP_SET_FROM_U64_EXPR</strong>](ext-tdop-set-from-u64-expr.md)</p></td>
<td align="left"><p>Returns the value of an expression. An optional address can be provided as a parameter to the expression.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EXT_TDOP_GET_FIELD</strong>](ext-tdop-get-field.md)</p></td>
<td align="left"><p>Returns a member of a structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EXT_TDOP_EVALUATE</strong>](ext-tdop-evaluate.md)</p></td>
<td align="left"><p>Returns the value of an expression. An optional value can be provided as a parameter to the expression.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EXT_TDOP_GET_TYPE_NAME</strong>](ext-tdop-get-type-name.md)</p></td>
<td align="left"><p>Returns the type name for typed data.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EXT_TDOP_OUTPUT_TYPE_NAME</strong>](ext-tdop-output-type-name.md)</p></td>
<td align="left"><p>Prints the type name for typed data.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EXT_TDOP_OUTPUT_SIMPLE_VALUE</strong>](ext-tdop-output-simple-value.md)</p></td>
<td align="left"><p>Prints the value of typed data.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EXT_TDOP_OUTPUT_FULL_VALUE</strong>](ext-tdop-output-full-value.md)</p></td>
<td align="left"><p>Prints the type and value for typed data.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EXT_TDOP_HAS_FIELD</strong>](ext-tdop-has-field.md)</p></td>
<td align="left"><p>Determines if a structure contains a specified member.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EXT_TDOP_GET_FIELD_OFFSET</strong>](ext-tdop-get-field-offset.md)</p></td>
<td align="left"><p>Returns the offset of a member within a structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EXT_TDOP_GET_ARRAY_ELEMENT</strong>](ext-tdop-get-array-element.md)</p></td>
<td align="left"><p>Returns an element from an array.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EXT_TDOP_GET_DEREFERENCE</strong>](ext-tdop-get-dereference.md)</p></td>
<td align="left"><p>Dereferences a pointer, returning the value it points to.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EXT_TDOP_GET_TYPE_SIZE</strong>](ext-tdop-get-type-size.md)</p></td>
<td align="left"><p>Returns the size of the specified typed data.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EXT_TDOP_OUTPUT_TYPE_DEFINITION</strong>](ext-tdop-output-type-definition.md)</p></td>
<td align="left"><p>Prints the definition of the type for the specified typed data.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EXT_TDOP_GET_POINTER_TO</strong>](ext-tdop-get-pointer-to.md)</p></td>
<td align="left"><p>Returns a new typed data description that represents a pointer to specified typed data.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EXT_TDOP_SET_FROM_TYPE_ID_AND_U64</strong>](ext-tdop-set-from-type-id-and-u64.md)</p></td>
<td align="left"><p>Creates a typed data description from a type and memory location.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EXT_TDOP_SET_PTR_FROM_TYPE_ID_AND_U64</strong>](ext-tdop-set-ptr-from-type-id-and-u64.md)</p></td>
<td align="left"><p>Creates a typed data description that represents a pointer to a specified memory location with specified type.</p></td>
</tr>
</tbody>
</table>

 

<span id="OutBuffer"></span><span id="outbuffer"></span><span id="OUTBUFFER"></span>*OutBuffer*  
Receives the [**EXT\_TYPED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545306) structure that contains the output parameters and any additional data for the sub-operation. As with *InBuffer*, the size of *OutBuffer* is the total size of the buffer that contains the EXT\_TYPED\_DATA structure and any additional data.

The DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI operation will initially copy *InBuffer* into *OutBuffer* and then modify the contents of *OutBuffer* in place. This means that *OutBuffer* will be populated with the input parameters of the EXT\_TYPED\_DATA and any additional data that was provided in *InBuffer*. It also means that the size of *OutBuffer* must be at least as big as the size of *InBuffer*.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

<span id="S_OK"></span><span id="s_ok"></span>S\_OK  
The operation was successful.

This method can also return error values. See [**Return Values**](https://msdn.microsoft.com/library/windows/hardware/ff549771) for more details.

The value returned by this operation is also stored in the **Status** member of *OutBuffer*.

Remarks
-------

The sub-operation performed by the DEBUG\_REQUEST\_EXT\_TYPED\_DATA\_ANSI [**Request**](request.md) operation is determined by the **Operation** member of the [**EXT\_TYPED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545306) structure, which takes a value in the [**EXT\_TDOP**](https://msdn.microsoft.com/library/windows/hardware/ff544529) enumeration.

## <span id="see_also"></span>See also


[**EXT\_TYPED\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff545306)

[**EXT\_TDOP**](https://msdn.microsoft.com/library/windows/hardware/ff544529)

[**Request**](request.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20DEBUG_REQUEST_EXT_TYPED_DATA_ANSI%20%20RELEASE:%20%2811/27/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





