---
title: /Replace Switch
description: The /Replace switch of the Enhanced Storage Certificate Management tool replaces a certificate from the authentication silo certificate (ASC) store in a device.
ms.assetid: 8fbdeb88-ec38-4ffc-a669-83fd612819ed
keywords:
- /Replace Switch Driver Development Tools
topic_type:
- apiref
api_name:
- /Replace
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# /Replace Switch


The **/Replace** switch of the Enhanced Storage Certificate Management tool replaces a specified certificate from the authentication silo certificate (ASC) store in an IEEE 1667-compliant USB storage device.

**Note**  In this topic, the specified IEEE 1667-compliant USB storage device is referred to as the *target device*.

 

```
    EhStorCertMgrCmd 
    /Replace 
    -Volume:
    VolumeName  -Type:CertificateType  [-Validation:{None|Basic|Extended}] [-Index:IndexValue] [[-Store:Certificate]|[-File:PathToFile]|[-New:PathToIniFile]]
```

## <span id="Subparameters"></span><span id="subparameters"></span><span id="SUBPARAMETERS"></span>Subparameters


<span id="_______-Volume______"></span><span id="_______-volume______"></span><span id="_______-VOLUME______"></span> **-Volume**   
The volume name of the target device. For more information about the format of this parameter, see [Overview of the Enhanced Storage Certificate Management Tool](overview-of-the-enhanced-storage-certificate-management-tool.md).

**Note**  To produce a list of the volume names of the IEEE 1667-compliant USB storage devices that are currently connected to a computer, type **EhStorCertMgrCmd /List** at the command prompt and then press Enter.

 

<span id="_______-Type______"></span><span id="_______-type______"></span><span id="_______-TYPE______"></span> **-Type**   
The type of the certificate to be added to the ASC store in the target device. The following table defines the valid certificate types.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Type value</th>
<th align="left">Description</th>
<th align="left">Index</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>ASCh</strong></p></td>
<td align="left"><p>The authentication silo certificate (ASC) host certificate that is used to authenticate the certificate authentication silo to the host.</p></td>
<td align="left"><p>Any index greater than 1.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>HCh</strong></p></td>
<td align="left"><p>The host certificate that is used to authenticate the host to the certificate authentication silo.</p></td>
<td align="left"><p>Any index greater than 1.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>SCh</strong></p></td>
<td align="left"><p>The signer certificate that is used to define a certificate that is trusted by the host. This trusted certificate is a chain of the ASCh certificate and zero or more SCh certificates.</p></td>
<td align="left"><p>Any index greater than 1.</p></td>
</tr>
</tbody>
</table>

 

<span id="_______-Validation______"></span><span id="_______-validation______"></span><span id="_______-VALIDATION______"></span> **-Validation**   
The type of certificate validation procedure that is performed by the addressable command target (ACT) in the target device. The following table defines the correct validation types.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Validation value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>None</strong></p></td>
<td align="left"><p>The certificate is not validated.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Basic</strong></p></td>
<td align="left"><p>The certificate is validated by using the Basic Validation Policy as defined within the IEEE 1667 standard.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Extended</strong></p></td>
<td align="left"><p>The certificate is validated by using the Extended Validation Policy as defined within the IEEE 1667 standard.</p></td>
</tr>
</tbody>
</table>

 

**Note**  If the -Validation: parameter is not specified, the tool uses a validation value of **None**.

 

<span id="_______-Index______"></span><span id="_______-index______"></span><span id="_______-INDEX______"></span> **-Index**   
The index within the ASC store where the certificate will be replaced. The index value must be greater than one.

**Note**  A certificate must exist at the specified index in the target device.

 

<span id="_______-Store______"></span><span id="_______-store______"></span><span id="_______-STORE______"></span> **-Store**   
The name of a certificate in a certificate store on the host. If the certificate is found in a certificate store, the tool adds it to the target device.

For more information, see [Importing Certificates from a Windows Certificate Store](importing-certificates-from-a-windows-certificate-store.md).

<span id="_______-File______"></span><span id="_______-file______"></span><span id="_______-FILE______"></span> **-File**   
The path and name of a file that contains a certificate. If the certificate file is found, the tool adds it to the target device. This certificate could have been created by using the MakeCert tool or imported by using the [**/Export switch**](-export-switch.md) of the Enhanced Storage Certificate Management tool.

For more information, see [Importing Certificates from a File](importing-certificates-from-a-file.md).

<span id="_______-New______"></span><span id="_______-new______"></span><span id="_______-NEW______"></span> **-New**   
The path and name of a file that contains the specifications that are used to create a self-signed certificate. If the file is found and the specifications are valid, the tool creates the certificate, digitally signs it, and adds the certificate to the target device.

For more information, see [**Creating Certificates for USB Storage Devices**](creating-certificates-for-usb-storage-devices.md).

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The **/Replace** switch is used to replace any certificate from the target device except for following certificates:

-   The provisioning certificate (PCp). To replace the PCp certificate, you must use the [**/Initialize switch**](-initialize-switch.md).

-   The ASC-manufacturer certificate (ASCm).

    **Note**   The Enhanced Storage Certificate Management tool cannot add, remove, or replace the ASCm certificate from the ASC store in the target device.

     

To replace certificates in the target device, the device must have been provisioned with a PCp certificate, and the private key of that certificate must reside in the host so that it can pass administrative authentication with the device.

If you replace an ASCh certificate, the tool removes all related SCh in the ASCh certificate chain.

If you replace an SCh certificate from an ASCh certificate chain, the tool removes the specified SCh certificate together with all its parent SCh certificates in the certificate chain.

Only one of the **-Store**, **-File** or **-New** parameters must be specified.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following example shows how to replace the certificate at index two within the ASC store of an IEEE 1667-compliant USB storage device.

```
EhStorCertMgrCmd /Replace -Volume:"\\?\usbstor#ieee1667control&ven_&prod_&rev_#123456789&0&control#{4f40006f-b933-4550-b532-2b58cee614d3}" -Index:2 -Store:TestCert -Type:SCh -Validation:None
```

 

 





