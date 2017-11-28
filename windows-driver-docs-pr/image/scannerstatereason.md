---
title: ScannerStateReason element
description: The optional ScannerStateReason element specifies one piece of information about why the scanner is in its current state.
ms.assetid: 7f10476a-d3ef-40a1-a355-ab735a6afe60
keywords: ["ScannerStateReason element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScannerStateReason
api_type:
- Schema
---

# ScannerStateReason element


The optional **ScannerStateReason** element specifies one piece of information about why the scanner is in its current state.

Usage
-----

``` syntax
<wscn:ScannerStateReason>
  text
</wscn:ScannerStateReason>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. One of the following values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><span id="AttentionRequired"></span><span id="attentionrequired"></span><span id="ATTENTIONREQUIRED"></span>AttentionRequired</p></td>
<td><p>The scan device requires user intervention before it can continue.</p></td>
</tr>
<tr class="even">
<td><p><span id="Calibrating"></span><span id="calibrating"></span><span id="CALIBRATING"></span>Calibrating</p></td>
<td><p>The scan device is calibrating its internal components to prepare to acquire images.</p></td>
</tr>
<tr class="odd">
<td><p><span id="CoverOpen"></span><span id="coveropen"></span><span id="COVEROPEN"></span>CoverOpen</p></td>
<td><p>One of more covers on the scan device are open.</p></td>
</tr>
<tr class="even">
<td><p><span id="InterlockOpen"></span><span id="interlockopen"></span><span id="INTERLOCKOPEN"></span>InterlockOpen</p></td>
<td><p>The interlock is open.</p></td>
</tr>
<tr class="odd">
<td><p><span id="InternalStorageFull"></span><span id="internalstoragefull"></span><span id="INTERNALSTORAGEFULL"></span>InternalStorageFull</p></td>
<td><p>The internal storage component that is currently being written to is full.</p></td>
</tr>
<tr class="even">
<td><p><span id="LampError"></span><span id="lamperror"></span><span id="LAMPERROR"></span>LampError</p></td>
<td><p>The scanner lamp is failing and image acquisition cannot proceed.</p></td>
</tr>
<tr class="odd">
<td><p><span id="LampWarming"></span><span id="lampwarming"></span><span id="LAMPWARMING"></span>LampWarming</p></td>
<td><p>The scanner lamp is warming to prepare to acquire images.</p></td>
</tr>
<tr class="even">
<td><p><span id="MediaJam"></span><span id="mediajam"></span><span id="MEDIAJAM"></span>MediaJam</p></td>
<td><p>Media is jammed in one of the input sources, so image acquisition failed.</p></td>
</tr>
<tr class="odd">
<td><p><span id="MultipleFeedError"></span><span id="multiplefeederror"></span><span id="MULTIPLEFEEDERROR"></span>MultipleFeedError</p></td>
<td><p>The ADF was fed more than one piece of media simultaneously.</p></td>
</tr>
<tr class="even">
<td><p><span id="None"></span><span id="none"></span><span id="NONE"></span>None</p></td>
<td><p>There are no current state reasons.</p></td>
</tr>
<tr class="odd">
<td><p><span id="Paused"></span><span id="paused"></span><span id="PAUSED"></span>Paused</p></td>
<td><p>The scanner has paused, and the scanner state is Stopped. In this state, a scanner will not produce scanned output.</p></td>
</tr>
</tbody>
</table>

 

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
<td><p>[<strong>ScannerStateReasons</strong>](scannerstatereasons.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

Some of these reasons describe scanner state that the scanner cannot enter according to the currently defined WSD Scan Service operation set. For example, the scanner can be **Paused** even though there is no "*PauseScanner*" operation. Such states are present because some other protocol or console action can cause the scanner to enter that state.

The WSD Scan Service must support the values that represent conditions that are detectable in its implementation. Therefore, a WSD Scan Service can support only that subset of allowed values that it can detect.

You can extend the allowed values, but there are implications when you extend this list on a client. The client typically localizes the [**ScannerStateReasons**](scannerstatereasons.md) value (as with other string variable values) to the language of the end user, so the client will not recognize a vendor extension value. However, the client can display the value that is received directly. This value should be in English, so some end users might not understand the value. Alternatively, the Scan Service can use the general **AttentionRequired** value and then explain the problem on the scanner console, which the user will see when they are at the scanner.

## <span id="see_also"></span>See also


[**ScannerStateReasons**](scannerstatereasons.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ScannerStateReason%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





