---
title: WSD Scan Service Operation Error Reporting
description: WSD Scan Service Operation Error Reporting
ms.assetid: 78cf0cf9-f792-4dc9-b0df-c45b408b85ab
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WSD Scan Service Operation Error Reporting


This section describes how a WSD Scan Service generates and sends operation error codes. Error codes that most operations can return are described in [**Common WSD Scan Service Operation Error Codes**](common-wsd-scan-service-operation-error-codes.md).

When the WSD Scan Service encounters an error while processing an *Xxx***Request** operation, it returns an error code instead of an *Xxx***Response** element. The Scan Service returns error codes in the **&lt;soap:Fault&gt;** element.

All error messages that are defined within the WSD Scan Service must be sent according to the rules that described in the [Web Services Addressing (WS-Addressing) specification](http://go.microsoft.com/fwlink/p/?linkid=70144). Specifically, the WSD Scan Service should send fault messages, in order, to the following locations:

1.  The \[fault endpoint\], if it is present and valid.

2.  Otherwise, the \[reply endpoint\], if it is present.

3.  Otherwise, the \[source endpoint\].

Endpoints must include required message information headers on all fault messages. Fault messages are correlated as replies by using the \[relationship\] property as defined in WS-Addressing. The following \[action\] property designates fault messages:

```
http://schemas.xmlsoap.org/ws/2004/08/addressing/fault
```

The definitions of faults use the following properties.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Fault property</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[Code]</p></td>
<td><p>The fault code.</p></td>
</tr>
<tr class="even">
<td><p>[Subcode]</p></td>
<td><p>The fault subcode.</p></td>
</tr>
<tr class="odd">
<td><p>[Reason]</p></td>
<td><p>The English language reason element.</p></td>
</tr>
<tr class="even">
<td><p>[Detail]</p></td>
<td><p>The detail element. If this element is absent, no detail element is defined for the fault.</p></td>
</tr>
</tbody>
</table>

 

These properties bind to a SOAP 1.2 fault as the following code example shows.

```
<S:Envelope>
  <S:Header>
    <wsa:Action>http://schemas.xmlsoap.org/ws/2004/08/addressing/fault</wsa:Action>
    <!-- Headers excluded for clarity -->
  </S:Header>
  <S:Body>
    <S:Fault>
      <S:Code>
        <S:Value>[Code]</S:Value>
        <S:Subcode>
          <S:Value>[Subcode]</S:Value>
        </S:Subcode>
      </S:Code>
      <S:Reason>
        <S:Text xml:lang="en">[Reason]</S:Text>
      </S:Reason>
      <S:Detail>[Detail]</S:Detail>
    </S:Fault>
  </S:Body>
</S:Envelope>
```

The following code example shows a sample SOAP **Fault**.

```
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soapelope"
    xmlns:xml="http://www.w3.org/XML/1998/namespace"
    xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing"
    xmlns:nprt="http://schemas.microsoft.com/windows/2006/01/wdp/scan">
  <soap:Header>
    <wsa:Action>http://schemas.xmlsoap.org/ws/2004/08/addressing/fault</wsa:Action>
    <!-- Headers excluded for brevity -->
  </soap:Header>
  <soap:Body>
    <soap:Fault>
      <soap:Code>
        <soap:Value>env:Sender</soap:Value>
        <soap:Subcode>
          <soap:Value>wscn:OperationFailed</soap:Value>
        </soap:Subcode>
      </soap:Code>
      <soap:Reason>
        <soap:Text xml:lang="en">Service cannot perform the requested operation</soap:Text>
      </soap:Reason>
    </soap:Fault>
  </soap:Body>
</soap:Envelope>
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WSD%20Scan%20Service%20Operation%20Error%20Reporting%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




