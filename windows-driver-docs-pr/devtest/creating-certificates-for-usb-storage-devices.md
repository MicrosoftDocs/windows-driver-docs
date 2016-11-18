---
title: Creating Certificates for USB Storage Devices
description: The Enhanced Storage Certificate Management tool can create a self-signed certificate that is imported to an IEEE 1667-compliant USB storage device.
ms.assetid: c63e69c3-ba60-417e-8838-825d81ac7301
keywords: ["Creating Certificates for USB Storage Devices Driver Development Tools"]
topic_type:
- apiref
api_name:
- Creating
api_type:
- NA
---

# Creating Certificates for USB Storage Devices


The Enhanced Storage Certificate Management tool can create a self-signed certificate that is imported to an IEEE 1667-compliant USB storage device. The specifications for the certificate are stored within either a text (.txt) or initialization (.ini) file and must contain the following entries:

``` syntax
  [certificate]

    Subject=SubjectString
SignatureAlgorithm=[RSASSA-PSS-SHA1|
        RSASSA-PSS-SHA384|
        RSASSA-PSS-SHA512|
        RSASSA-PKCS1_5-SHA1|
        RSASSA-PKCS1_5-SHA256|
        RSASSA-PKCS1_5-SHA384|
        RSASSA-PKCS1_5-SHA512]
KeyType=RSAKeyStrength=[1024|2048|3072]
ExpirationDate=mm/dd/yy
[SelfSigned=[YES|NO]]
[OrganizationName=OrgNameString]
[OrganizationUnit=OrgUnitString]
[CompanyLocation=LocationString]
[State=StateString]
[ZipCode=ZipCodeString]
[Country=CountryString]
```

## <span id="Entries"></span><span id="entries"></span><span id="ENTRIES"></span>Entries


<span id="_______Subject______"></span><span id="_______subject______"></span><span id="_______SUBJECT______"></span> **Subject**   
This required entry specifies the certificate name for the subject. This name must comply with the X.509 standard.

<span id="_______SignatureAlgorithm______"></span><span id="_______signaturealgorithm______"></span><span id="_______SIGNATUREALGORITHM______"></span> **SignatureAlgorithm**   
This required entry specifies the algorithm that is used to digitally sign the certificate. The signature algorithms are described in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">SignatureAlgorithm value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>RSASSA-PSS-SHA1</strong></p></td>
<td align="left"><p>The RSASSA-PSS digital signature that uses the 160-bit SHA-1 hashing algorithm.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RSASSA-PSS-SHA256</strong></p></td>
<td align="left"><p>The RSASSA-PSS digital signature that uses the 256-bit SHA-256 hashing algorithm.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>RSASSA-PSS-SHA384</strong></p></td>
<td align="left"><p>The RSASSA-PSS digital signature that uses the 384-bit SHA-384 hashing algorithm.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RSASSA-PSS-SHA512</strong></p></td>
<td align="left"><p>The RSASSA-PSS digital signature that uses the 512-bit SHA-512 hashing algorithm.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>RSASSA-PKCS1_5-SHA1</strong></p></td>
<td align="left"><p>The RSASSA-PKCS1_5 (PKCS#1 version 1.5) digital signature that uses the 160-bit SHA-1 hashing algorithm.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RSASSA-PKCS1_5-SHA256</strong></p></td>
<td align="left"><p>The RSASSA-PKCS1_5 digital signature that uses the 256-bit SHA-256 hashing algorithm.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>RSASSA-PKCS1_5-SHA384</strong></p></td>
<td align="left"><p>The RSASSA-PKCS1_5 digital signature that uses the 384-bit SHA-384 hashing algorithm.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>RSASSA-PKCS1_5-SHA512</strong></p></td>
<td align="left"><p>The RSASSA-PKCS1_5 digital signature that uses the 512-bit SHA-512 hashing algorithm.</p></td>
</tr>
</tbody>
</table>

 

<span id="_______KeyType______"></span><span id="_______keytype______"></span><span id="_______KEYTYPE______"></span> **KeyType**   
This required entry specifies the key type for the subject. Starting with Windows 7 , this entry must have a value of **RSA**.

<span id="_______KeyStrengh______"></span><span id="_______keystrengh______"></span><span id="_______KEYSTRENGH______"></span> **KeyStrengh**   
This required entry specifies the strength of the key, which is based on its length (in units of bits).

<span id="_______SelfSigned______"></span><span id="_______selfsigned______"></span><span id="_______SELFSIGNED______"></span> **SelfSigned**   
This optional entry specifies whether the certificate is to be self-signed by the Enhanced Storage Certificate Management tool. If this entry is not specified, the tool signs the certificate when the certificate is created.

**Note**  Starting with Windows 7, a value of NO is not supported. If NO is specified, the tool issues an error message.

 

<span id="_______ExpirationDate______"></span><span id="_______expirationdate______"></span><span id="_______EXPIRATIONDATE______"></span> **ExpirationDate**   
This required entry specifies the end of the validity period for the certificate. The certificate is valid from the date it is created to the specified expiration date.

<span id="_______OrganizationName______"></span><span id="_______organizationname______"></span><span id="_______ORGANIZATIONNAME______"></span> **OrganizationName**   
This optional entry specifies the name of the organization that is publishing the certificate for the subject.

<span id="_______OrganizationUnit______"></span><span id="_______organizationunit______"></span><span id="_______ORGANIZATIONUNIT______"></span> **OrganizationUnit**   
This optional entry specifies the name of the business unit within the organization that is publishing the certificate for the subject.

<span id="_______CompanyLocation______"></span><span id="_______companylocation______"></span><span id="_______COMPANYLOCATION______"></span> **CompanyLocation**   
This optional entry specifies the street address of the company that is publishing the certificate for the subject.

<span id="_______State______"></span><span id="_______state______"></span><span id="_______STATE______"></span> **State**   
This optional entry specifies the state or province for the location of the company that is publishing the certificate for the subject.

<span id="_______ZipCode______"></span><span id="_______zipcode______"></span><span id="_______ZIPCODE______"></span> **ZipCode**   
This optional entry specifies the postal code for the location of the company that is publishing the certificate for the subject.

<span id="_______Country______"></span><span id="_______country______"></span><span id="_______COUNTRY______"></span> **Country**   
This optional entry specifies the country/region for the location of the company that is publishing the certificate for the subject.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The first entry in the certificate specification file must be the **\[certificate\]** label.

Entries for the certificate specification are case-sensitive but can be specified in any order.

For more information about how to create a certificate to import to an IEEE 1667-compliant USB storage device, see the **-New** parameter of the [**/Add**](enhstor-add-switch.md) and [**/Replace**](-replace-switch.md) switches of the Enhanced Storage Certificate Management tool.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Creating%20Certificates%20for%20USB%20Storage%20Devices%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




