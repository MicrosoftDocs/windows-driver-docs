---
title: /Export Switch
description: The /Export switch of the Enhanced Storage Certificate Management tool exports a specified certificate from the authentication silo certificate (ASC) store in an IEEE 1667-compliant USB storage device to a file.
ms.assetid: 00612a63-057a-4ff9-baef-d44de0280cb5
keywords: ["/Export Switch Driver Development Tools"]
topic_type:
- apiref
api_name:
- /Export
api_type:
- NA
---

# /Export Switch


The **/Export** switch of the Enhanced Storage Certificate Management tool exports a specified certificate from the authentication silo certificate (ASC) store in an IEEE 1667-compliant USB storage device to a file. This switch also supports the export of a certificate signing request (CSR) to a file.

**Note**  In this topic, the specified IEEE 1667-compliant USB storage device is referred to as the *target device*.

 

``` syntax
    EhStorCertMgrCmd 
    /Export 
     -Volume:
    VolumeName  -Path:PathToFile [-Certificate  -Index:IndexValue [-NoType]] [-Request]
```

## <span id="Subparameters"></span><span id="subparameters"></span><span id="SUBPARAMETERS"></span>Subparameters


<span id="_______-Volume_______"></span><span id="_______-volume_______"></span><span id="_______-VOLUME_______"></span> **-Volume:**   
The volume name of the target device. For more information about the format of this parameter, see [Overview of the Enhanced Storage Certificate Management Tool](overview-of-the-enhanced-storage-certificate-management-tool.md).

**Note**  To produce a list of the volume names of the IEEE 1667-compliant USB storage devices that are currently connected to a computer, type **EhStorCertMgrCmd /List** at the command prompt and then press Enter.

 

<span id="_______-Path______"></span><span id="_______-path______"></span><span id="_______-PATH______"></span> **-Path**   
The full path and name of the file that will contain the exported certificate or CSR.

<span id="_______-Certificate_______"></span><span id="_______-certificate_______"></span><span id="_______-CERTIFICATE_______"></span> **-Certificate:**   
This switch specifies that the export of a certificate is requested. The following switches are used with this type of request:

<span id="-Index"></span><span id="-index"></span><span id="-INDEX"></span>**-Index**  
The index within the ASC store where the certificate will be exported from the target device. This switch is required.

<span id="-NoType"></span><span id="-notype"></span><span id="-NOTYPE"></span>**-NoType**  
If this parameter is specified, the tool does not append the certificate type to the file name that was specified by using the **-Path** parameter.

This switch is optional and must only be used with the **-Certificate** parameter.

<span id="_______-Request______"></span><span id="_______-request______"></span><span id="_______-REQUEST______"></span> **-Request**   
This switch specifies that the export of a CSR is requested. The CSR is typically sent to a certificate authority (CA) to create an ASC host (ASCh) certificate for the target device.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

If you request the export of a certificate from the device's ASC store, you must specify an index. If the specified index does not contain a certificate, the tool reports an error.

If the **-Certificate** parameter is specified, the tool will automatically append a string that represents the certificate type to the file name that is specified through the **-Path** parameter. The following table defines the strings for the various certificate types:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Certificate type string</th>
<th align="left">Description</th>
<th align="left">Index</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>&quot;ASCm&quot;</p></td>
<td align="left"><p>The authentication silo certificate (ASC) manufacturer.</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>&quot;ASCh&quot;</p></td>
<td align="left"><p>The ASC host certificate that is used to authenticate the certificate authentication silo to the host.</p></td>
<td align="left"><p>Any index greater than 1.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>&quot;HCh&quot;</p></td>
<td align="left"><p>The host certificate that is used to authenticate the host to the certificate authentication silo.</p></td>
<td align="left"><p>Any index greater than 1.</p></td>
</tr>
<tr class="even">
<td align="left"><p>&quot;PCp&quot;</p></td>
<td align="left"><p>The provisioning certificate that is used in administrative command sequences to provision and administer the certificate authentication silos.</p></td>
<td align="left"><p>1</p></td>
</tr>
<tr class="odd">
<td align="left"><p>&quot;SCh&quot;</p></td>
<td align="left"><p>The signer certificate that is used to define a certificate that is trusted by the host. This trusted certificate is a chain of the ASCh certificate and zero or more SCh certificates.</p></td>
<td align="left"><p>Any index greater than 1.</p></td>
</tr>
<tr class="even">
<td align="left"><p>&quot;Invalid&quot;</p></td>
<td align="left"><p>An unknown certificate type was located at the specified index.</p></td>
<td align="left"><p>Not applicable</p></td>
</tr>
</tbody>
</table>

 

For example, the following command, which exports the PCp certificate from the target device, produces a file that is named c:\\MyCertificates\\myCertPCp.cer:

```
EhStorCertMgrCmd /export -Certificate -Volume:"\\?\usbstor#ieee1667control&ven_&prod_&rev_#123456789&0&control#{4f40006f-b933-4550-b532-2b58cee614d3}" -Index:1 -Path:c:\MyCertificates\myCert.cer
```

If you specify the **-NoType** parameter with the **-Certificate** parameter, the tool does not append a string for the certificate type to the file name that is specified through the **-Path** parameter.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following example shows how to export the certificate at index 1 from the ASC store in the target device:

```
EhStorCertMgrCmd /export -Certificate -Volume:"\\?\usbstor#ieee1667control&ven_&prod_&rev_#123456789&0&control#{4f40006f-b933-4550-b532-2b58cee614d3}" -Index:1 -Path:c:\MyCertificates\myCert.cer
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20/Export%20Switch%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




