---
title: /Add Switch
description: The /Add switch of the Enhanced Storage Certificate Management tool adds a certificate to the authentication silo certificate (ASC) store on a specified USB device.
keywords:
- /Add Switch Driver Development Tools
topic_type:
- apiref
api_name:
- /Add
api_type:
- NA
ms.date: 04/20/2017
---

# /Add Switch


The **/Add** switch of the Enhanced Storage Certificate Management tool adds a certificate to the authentication silo certificate (ASC) store on a specified IEEE 1667-compliant USB storage device.

**Note**  In this topic, the specified IEEE 1667-compliant USB storage device is known as the *target device*.

 

```
    EhStorCertMgrCmd 
    /Add
     -Volume:
    VolumeName  -Type:CertificateType  -Validation:{None|Basic|Extended} [-Index:IndexValue] [[-Store:Certificate]|[-File:PathToFile]|
[-New:PathToIniFile]]
```

## <span id="Subparameters"></span><span id="subparameters"></span><span id="SUBPARAMETERS"></span>Subparameters


<span id="_______-Volume______"></span><span id="_______-volume______"></span><span id="_______-VOLUME______"></span> **-Volume**   
The volume name of the target device. For more information about the format of this parameter, see [Overview of the Enhanced Storage Certificate Management Tool](overview-of-the-enhanced-storage-certificate-management-tool.md).

**Note**  To produce a list of the volume names of the IEEE 1667-compliant USB storage devices currently connected to a computer, type **EhStorCertMgrCmd /List** at the command prompt and then press **Enter**.

 

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
<td align="left"><p>The host certificate (HCh) that is used to authenticate the host to the certificate authentication silo.</p></td>
<td align="left"><p>Any index greater than 1.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>PCp</strong></p></td>
<td align="left"><p>The provisioning certificate (PCp) that is used in administrative command sequences to provision and administer the certificate authentication silos.</p></td>
<td align="left"><p>1</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>SCh</strong></p></td>
<td align="left"><p>The signer certificate (SCh) that is used to define a certificate that is trusted by the host. This trusted certificate is a chain of the ASCh certificate and zero or more SCh certificates.</p></td>
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
<td align="left"><p>The certificate is validated through the Basic Validation Policy as defined within the IEEE 1667 standard.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Extended</strong></p></td>
<td align="left"><p>The certificate is validated through the Extended Validation Policy as defined within the IEEE 1667 standard.</p></td>
</tr>
</tbody>
</table>

 

**Note**  If the -Validation: parameter is not specified, the tool uses a validation value of **None**.

 

<span id="_______-Index______"></span><span id="_______-index______"></span><span id="_______-INDEX______"></span> **-Index**   
The index within the ASC store where the certificate will be saved. If the specified index contains a certificate, that certificate will be replaced. The index value must be greater than zero.

<span id="_______-Store______"></span><span id="_______-store______"></span><span id="_______-STORE______"></span> **-Store**   
The name of a certificate in a certificate store on the host. If the certificate is found in a certificate store, the tool adds it to the target device.

For more information, see [Importing Certificates from a Windows Certificate Store](importing-certificates-from-a-windows-certificate-store.md).

<span id="_______-File______"></span><span id="_______-file______"></span><span id="_______-FILE______"></span> **-File**   
The path and name of a file that contains a certificate. If the certificate file is found, the tool adds it to the target device. This certificate could have been created through the [**MakeCert**](makecert.md) tool or imported through the [**/Export switch**](-export-switch.md) of the Enhanced Storage Certificate Management tool.

For more information, see [Importing Certificates from a File](importing-certificates-from-a-file.md).

<span id="_______-New______"></span><span id="_______-new______"></span><span id="_______-NEW______"></span> **-New**   
The path and name of a file that contains the specifications that are used to create a self-signed certificate. If the file is found and the specifications are valid, the tool creates the certificate, digitally signs it, and adds the certificate to the target device.

For more information, see [**Creating Certificates for USB Storage Devices**](creating-certificates-for-usb-storage-devices.md).

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The following guidelines apply when you add certificates to the target device:

-   The PCp certificate is used to perform administrative authentication between the host and the target device. If the target device does not have a PCp certificate, you must first provision the target device with a PCp certificate. For the PCp certificate type, the **-Index** switch must be specified with a value of one.

    **Important**  It is best to only provision the target device with a PCp certificate that has its private key stored in a certificate store on your computer. If an incorrect PCp certificate is provisioned on the target device, you will not be able to clear the certificate store (which includes the PCp certificate) by using the [**/Initialize switch**](-initialize-switch.md).

     

-   If the **-Index** switch is not specified when you add HCh, ASCh, and SCh certificates, the tool stores the certificate in the first index within the ASC store that is not used.

    **Note**  In order to add these certificate types to the target device, the correct PCp certificate must reside in the host in order to pass administrative authentication with the device.

     

-   If the specified index is not empty in the target device, the **/Add** switch replaces the existing certificate with the specified certificate.

    **Note**  If the Enhanced Storage Certificate Management tool replaces an ASCh certificate at the specified index, the tool removes all related SCh in the ASCh certificate chain.
    If the tool replaces an SCh certificate at the specified index that is part of an ASCh certificate chain, the tool removes the SCh certificate together with all its parent SCh certificates in the certificate chain.

     

-   Only one of the **-Store**, -**File** or **-New** parameters must be specified.

**Note**   The Enhanced Storage Certificate Management tool cannot add, remove, or replace the ASC-manufacturer (ASCm) certificate from the ASC store in the target device.

 

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following example shows how to add a certificate from the certificate store on the host to a target device:

```
EhStorCertMgrCmd /Add -Volume:"\\?\usbstor#ieee1667control&ven_&prod_&rev_#123456789&0&control#{4f40006f-b933-4550-b532-2b58cee614d3}" -Index:1 -Store:TestCert -Type:PCp -Validation:None
```

 

 





