---
title: MakeCert
description: MakeCert (Makecert.exe) is a command-line CryptoAPI tool that creates an X.509 certificate that is signed by a system test root key or by another specified key.
ms.assetid: 752aa806-5e8c-4519-bece-dcd91161b98a
keywords: ["MakeCert Driver Development Tools"]
topic_type:
- apiref
api_name:
- MakeCert
api_type:
- NA
---

# MakeCert


MakeCert (Makecert.exe) is a command-line [CryptoAPI](http://go.microsoft.com/fwlink/p/?linkid=136391) tool that creates an X.509 certificate that is signed by a system test root key or by another specified key. The certificate binds a certificate name to the public part of the key pair. The certificate is saved to a file, a system certificate store, or both.

MakeCert supports a large number of switches but this section only describes the basic switches that are relevant to creating a [test certificate](https://msdn.microsoft.com/library/windows/hardware/ff548693) that can be used to test-sign a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) or embed a signature in a driver file.

``` syntax
    MakeCert [/b DateStart] [/e DateEnd] [/len KeyLength] [/m nMonths] [/n "Name"] [/pe] [/r] [/sc SubjectCertFile] [/sk SubjectKey] [/sr SubjectCertStoreLocation] [/ss SubjectCertStoreName] [/sv SubjectKeyFile]OutputFile
```

### <span id="partial_list_of_switches_and_arguments"></span><span id="PARTIAL_LIST_OF_SWITCHES_AND_ARGUMENTS"></span>Partial list of switches and arguments

<span id="_b_DateStart"></span><span id="_b_datestart"></span><span id="_B_DATESTART"></span>**/b** *DateStart*  
Specifies the start date when the certificate first becomes valid. The format of *DateStart* is mm/dd/yyyy.

If the **/b** switch is not specified, the default start date is the date when the certificate is created.

<span id="_e_DateEnd"></span><span id="_e_dateend"></span><span id="_E_DATEEND"></span>**/e** *DateEnd*  
Specifies the end date when the certificate's validity period ends. The format of *DateEnd* is mm/dd/yyyy.

If the **/e** switch is not specified, the default end date is 12/31/2039.

<span id="_len_KeyLength"></span><span id="_len_keylength"></span><span id="_LEN_KEYLENGTH"></span>**/len** *KeyLength*  
Specifies the length, in units of bits, of the subject's private and public keys.

If the /len switch is not specified, the default key length is 1024 bits.

<span id="_m_nMonths"></span><span id="_m_nmonths"></span><span id="_M_NMONTHS"></span>**/m** *nMonths*  
Specifies the number of months starting from the start date during which the certificate will remain valid.

<span id="_n__Name_"></span><span id="_n__name_"></span><span id="_N__NAME_"></span>**/n** "*Name***"**  
Specifies a name for the certificate. This name must conform to the X.500 standard. The simplest method is to use the "CN=*MyName*" format.

If the **/n** switch is not specified, the default name of the certificate is "Joe's Software Emporium".

<span id="_pe"></span><span id="_PE"></span>**/pe**  
Configures MakeCert to make the private key that is associated with the certificate exportable.

<span id="_r"></span><span id="_R"></span>**/r**  
Configures MakeCert to create a self-signed root certificate.

<span id="_sc_SubjectCertFile"></span><span id="_sc_subjectcertfile"></span><span id="_SC_SUBJECTCERTFILE"></span>**/sc** *SubjectCertFile*  
Specifies the subject's certificate file name along with the existing subject public key that is used.

<span id="_sk_SubjectKey"></span><span id="_sk_subjectkey"></span><span id="_SK_SUBJECTKEY"></span>**/sk** *SubjectKey*  
Specifies the name of the subject's key container that holds the private key. If a key container does not exist, a new key container is created. If neither **/sk** nor **/sv** switch is entered, a default key container is created and used by default.

<span id="_sr_SubjectCertStoreLocation"></span><span id="_sr_subjectcertstorelocation"></span><span id="_SR_SUBJECTCERTSTORELOCATION"></span>**/sr** *SubjectCertStoreLocation*  
Specifies the registry location of the certificate store. The *SubjectCertStoreLocation* argument must be either of the following:

<span id="currentUser"></span><span id="currentuser"></span><span id="CURRENTUSER"></span>*currentUser*  
Specifies the registry location HKEY\_CURRENT\_USER.

<span id="localMachine"></span><span id="localmachine"></span><span id="LOCALMACHINE"></span>*localMachine*  
Specifies the registry location HKEY\_LOCAL\_MACHINE.

If the **/r** switch is not specified along with the **/s** switch, *currentUser* is the default.

<span id="_ss_SubjectCertStoreName"></span><span id="_ss_subjectcertstorename"></span><span id="_SS_SUBJECTCERTSTORENAME"></span>**/ss** *SubjectCertStoreName*  
Specifies the name of the certificate store where the generated certificate is saved.

<span id="_sv_SubjectKeyFile"></span><span id="_sv_subjectkeyfile"></span><span id="_SV_SUBJECTKEYFILE"></span>**/sv** *SubjectKeyFile*  
Specifies the name of the subject's .pvk file that holds the private key. If neither **/sk** nor **/sv** switch is entered, a default key container is created and used by default.

<span id="OutputFile"></span><span id="outputfile"></span><span id="OUTPUTFILE"></span>*OutputFile*  
The name of the file in which the generated certificate is saved.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

MakeCert supports a large number of switches. The switches described in this topic are limited to the ones that you can use to create a [test certificate](https://msdn.microsoft.com/library/windows/hardware/ff548693).

For a complete list of MakeCert parameters, see the [MakeCert](http://go.microsoft.com/fwlink/p/?linkid=62653) website and the [Using MakeCert](http://go.microsoft.com/fwlink/p/?linkid=62655) website.

A 32-bit version of the MakeCert tool is located in the bin\\i386 folder of the WDK. A 64-bit version of the tool is located in the bin\\amd64 and bin\\ia64 folders of the WDK.

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

In the following example, the MakeCert command generates a self-signed test certificate named "Contoso.com(Test)," installs the test certificate in the PrivateCertStore certificate store, and creates the Testcert.cer file, which contains a copy of the test certificate.

```
MakeCert -r -pe -ss PrivateCertStore -n "CN=Contoso.com(Test)" testcert.cer
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20MakeCert%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




