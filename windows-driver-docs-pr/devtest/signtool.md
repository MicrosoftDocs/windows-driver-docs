---
title: SignTool
description: SignTool (Signtool.exe) is a command-line CryptoAPI tool that digitally-signs files, verifies signatures in files, and time stamps files.
ms.assetid: c1006c07-f204-4fc0-8f99-36e69cbee96d
keywords:
- SignTool Driver Development Tools
topic_type:
- apiref
api_name:
- SignTool
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SignTool


SignTool (Signtool.exe) is a command-line [CryptoAPI](http://go.microsoft.com/fwlink/p/?linkid=136391) tool that digitally-signs files, verifies signatures in files, and time stamps files.

```
    SignTool [Operation] [Options] [FileName ...]
```

### <span id="partial_list_of_operations__switches__and_arguments"></span><span id="PARTIAL_LIST_OF_OPERATIONS__SWITCHES__AND_ARGUMENTS"></span>Partial list of operations, options, and arguments

### <span id="operations"></span><span id="OPERATIONS"></span>Operations

<span id="catdb"></span><span id="CATDB"></span>**catdb**  
Configures SignTool to update a catalog database. SignTool either adds catalog files to a database or removes catalogs from a database. By default, the **catdb** command adds the files, whose names are specified by the *FileName* argument, to the system component (driver) database.

**Note**  Catalog databases are used for automatic lookup of catalog files.

 

<span id="sign"></span><span id="SIGN"></span>**sign**  
Configures SignTool to digitally-sign the files whose names are specified by the *FileName* argument.

<span id="timestamp"></span><span id="TIMESTAMP"></span>**timestamp**  
Configures SignTool to timestamp the files whose names are specified by the *FileName* argument.

<span id="verify"></span><span id="VERIFY"></span>**verify**  
Configures SignTool to verify the digital signature of the files whose names are specified by the *FileName* argument.

### <span id="catdb_operation_switches"></span><span id="CATDB_OPERATION_SWITCHES"></span>Catdb operation options

<span id="_d"></span><span id="_D"></span>**/d**  
Configures SignTool to update the catalog database. If neither **/d** nor **/g** option is used, SignTool updates the system component and the driver database.

<span id="_g_Guid"></span><span id="_g_guid"></span><span id="_G_GUID"></span>**/g** *Guid*  
Configures SignTool to update the catalog database identified by the *GUID* argument.

<span id="_r"></span><span id="_R"></span>**/r**  
Configures SignTool to remove each of the catalog files, whose names are specified by the *FileName* argument, from the catalog database. If this option is not specified, SignTool adds the specified catalog files to the catalog database.

<span id="_u"></span><span id="_U"></span>**/u**  
Configures SignTool to generate a unique name, if necessary, for a catalog file to prevent a conflict with an existing catalog file in the catalog database. If this option is not specified, SignTool overwrites any existing catalog that has the same name as the catalog being added.

### <span id="sign_operation_switches"></span><span id="SIGN_OPERATION_SWITCHES"></span>Sign operation options

<span id="_a_"></span><span id="_A_"></span>**/a**   
Configures SignTool to automatically select the best signing certificate. If this option is not present, SignTool expects to find only one signing certificate.

<span id="_ac_CrossCertFileName"></span><span id="_ac_crosscertfilename"></span><span id="_AC_CROSSCERTFILENAME"></span>**/ac** *CrossCertFileName*  
Specifies the name of a cross-certificate file that is used with a Software Publisher Certificate (SPC) that is named *CertificateName* and is installed in the certificate store *StoreName*. This option should only be used if the signing certificate is an SPC.

<span id="_c_CertTemplateName"></span><span id="_c_certtemplatename"></span><span id="_C_CERTTEMPLATENAME"></span>**/c** *CertTemplateName*  
Specifies the Certificate Template Name (a Microsoft extension) for the signing certificate.

<span id="_csp_CSPName"></span><span id="_csp_cspname"></span><span id="_CSP_CSPNAME"></span>**/csp** *CSPName*  
Specifies the cryptographic service provider (CSP) that contains the private key container.

<span id="_d_Desc"></span><span id="_d_desc"></span><span id="_D_DESC"></span>**/d** *Desc*  
Specifies a description of the signed content.

<span id="_du_URL"></span><span id="_du_url"></span><span id="_DU_URL"></span>**/du** *URL*  
Specifies a URL for the expanded description of the signed content.

<span id="_f_SignCertFile"></span><span id="_f_signcertfile"></span><span id="_F_SIGNCERTFILE"></span>**/f** *SignCertFile*  
Specifies the signing certificate in a file. Only the Personal Information Exchange (PFX) file format is supported. You can use the [**Pvk2Pfx**](pvk2pfx.md) tool to convert SPC and PVK files to PFX format.

If the file is in PFX format protected by a password, use the **/p** option to specify the password. If the file does not contain private keys, use the **/csp** and **/k** options to specify the CSP and private key container name, respectively.

<span id="_fd"></span><span id="_FD"></span>**/fd**  
Specifies the file digest algorithm to use for creating file signatures. The default is SHA1.

<span id="_i_IssuerName"></span><span id="_i_issuername"></span><span id="_I_ISSUERNAME"></span>**/i** *IssuerName*  
Specifies the name of the issuer of the signing certificate. This value can be a substring of the entire issuer name.

<span id="_j_DLL"></span><span id="_j_dll"></span><span id="_J_DLL"></span>**/j** *DLL*  
Specifies the name of a DLL that provides attributes of the signature.

<span id="_jp_ParameterName"></span><span id="_jp_parametername"></span><span id="_JP_PARAMETERNAME"></span>**/jp** *ParameterName*  
Specifies a parameter that is passed to the DLL specified by the **/j** command.

<span id="_kc_PrivKeyContainerName"></span><span id="_kc_privkeycontainername"></span><span id="_KC_PRIVKEYCONTAINERNAME"></span>**/kc** *PrivKeyContainerName*  
Specifies the key container name of the private key.

<span id="_n_SubjectName"></span><span id="_n_subjectname"></span><span id="_N_SUBJECTNAME"></span>**/n** *SubjectName*  
Specifies the name of the subject of the signing certificate. This value can be a substring of the entire subject name.

<span id="_nph"></span><span id="_NPH"></span>**/nph**  
If supported, suppresses page hashes for executable files. The default is determined by the SIGNTOOL\_PAGE\_HASHES environment variable and by the wintrust.dll version. This option is ignored for non-PE files.

<span id="_p_Password"></span><span id="_p_password"></span><span id="_P_PASSWORD"></span>**/p** *Password*  
Specifies the password to use when opening a PFX file. A PFX file can be specified by using the **/f** option

<span id="_p7__Path"></span><span id="_p7__path"></span><span id="_P7__PATH"></span>**/p7** *Path*  
Specifies that a Public Key Cryptography Standards (PKCS) \#7 file is produced for each specified content file. PKCS \#7 files are named path\\filename.p7.

<span id="_p7ce_Value"></span><span id="_p7ce_value"></span><span id="_P7CE_VALUE"></span>**/p7ce** *Value*  
Specifies options for the signed PKCS \#7 content. Set Value to "Embedded" to embed the signed content in the PKCS \#7 file, or to "DetachedSignedData" to produce the signed data portion of a detached PKCS \#7 file. If the **/p7ce** option is not used, the signed content is embedded by default.

<span id="_p7co__OID"></span><span id="_p7co__oid"></span><span id="_P7CO__OID"></span>**/p7co** *OID*  
Specifies the object identifier (OID) that identifies the signed PKCS \#7 content.

<span id="_ph___"></span><span id="_PH___"></span>**/ph**   
If supported, generates page hashes for executable files.

<span id="_r_RootSubjectName"></span><span id="_r_rootsubjectname"></span><span id="_R_ROOTSUBJECTNAME"></span>**/r** *RootSubjectName*  
Specifies the subject name of the root certificate that the signing certificate must chain to. This value can be a substring of the entire subject name of the root certificate.

<span id="_s_StoreName"></span><span id="_s_storename"></span><span id="_S_STORENAME"></span>**/s** *StoreName*  
Specifies the name of the certificate store to open when searching for the certificate to use for signing files. If this option is not specified, the **My** certificate store is opened.

<span id="_sha1_Hash"></span><span id="_sha1_hash"></span><span id="_SHA1_HASH"></span>**/sha1** *Hash*  
Specifies the SHA1 hash of the signing certificate.

<span id="_sm"></span><span id="_SM"></span>**/sm**  
Configures SignTool to use a machine certificate store instead of a user certificate store.

<span id="_t_URL"></span><span id="_t_url"></span><span id="_T_URL"></span>**/t** *URL*  
Specifies a URL to a timestamp server. If this option is not provided, the signed file is not timestamped. A catalog file or driver file should be timestamped, because if the signer's key is compromised, the timestamp provides the information necessary to revoke the key that was used to sign the file.

<span id="_td____alg"></span><span id="_TD____ALG"></span>**/td** *alg*  
Used with the /tr option to request a digest algorithm used by the RFC 3161 time stamp server.

<span id="_tr___URL"></span><span id="_tr___url"></span><span id="_TR___URL"></span>**/tr** *URL*  
Specifies the URL of the RFC 3161 time stamp server. If this option (or **/t**) is not present, the signed file will not be time stamped. A warning is generated if time stamping fails. This option cannot be used with the **/t** option.

<span id="_u___Usage"></span><span id="_u___usage"></span><span id="_U___USAGE"></span>**/u** *Usage*  
Specifies the enhanced key usage (EKU) that must be present in the signing certificate. The usage value can be specified by OID or string. The default usage is "Code Signing" (1.3.6.1.5.5.7.3.3).

<span id="_uw_"></span><span id="_UW_"></span>**/uw**   
Specifies usage of "Windows System Component Verification" (1.3.6.1.4.1.311.10.3.6).

### <span id="timestamp_operation_switches"></span><span id="TIMESTAMP_OPERATION_SWITCHES"></span>Timestamp operation options

<span id="_p7_"></span><span id="_P7_"></span>**/p7**   
Time stamps PKCS \#7 files.

<span id="_t_URL"></span><span id="_t_url"></span><span id="_T_URL"></span>**/t** *URL*  
Specifies the URL of the timestamp server. The file being timestamped must have been signed previously

<span id="_td___alg"></span><span id="_TD___ALG"></span>**/td** *alg*  
Requests a digest algorithm used by the RFC 3161 time stamp server. **/td** is used with the **/tr** option.

<span id="_tp__index"></span><span id="_TP__INDEX"></span>**/tp** *index*  
Time stamps the signature at index.

<span id="_tr___alg"></span><span id="_TR___ALG"></span>**/tr** *alg*  
Requests a digest algorithm used by the RFC 3161 time stamp server. **/td** is used with the **/tr** option.

### <span id="verify_operation_switches"></span><span id="VERIFY_OPERATION_SWITCHES"></span>Verify operation options

<span id="_a"></span><span id="_A"></span>**/a**  
Specifies that all methods can be used to verify the file. First, the catalog databases are searched to determine whether the file is signed in a catalog. If the file is not signed in any catalog, SignTool attempts to verify the file's embedded signature. This option is recommended when verifying files that may or may not be signed in a catalog.

<span id="_ad"></span><span id="_AD"></span>**/ad**  
Specifies that only the default catalog database is searched for the catalog that the file was signed in.

<span id="_all"></span><span id="_ALL"></span>**/all**  
Verifies all signatures in a file that includes multiple signatures.

<span id="_as"></span><span id="_AS"></span>**/as**  
Specifies that only the system component (driver) catalog database is searched for the catalog that the file was signed in.

<span id="_ag_CatDBGUID"></span><span id="_ag_catdbguid"></span><span id="_AG_CATDBGUID"></span>**/ag** *CatDBGUID*  
Specifies that only the catalog database, identified through the *CatDBGUID* argument, is searched for the catalog that the file was signed in.

<span id="_c___CatalogFileName"></span><span id="_c___catalogfilename"></span><span id="_C___CATALOGFILENAME"></span>**/c** *CatalogFileName*  
Specifies the name of a catalog file.

<span id="_d___"></span><span id="_D___"></span>**/d**   
Specifies that Sign Tool should print the description and the description URL.

<span id="_ds___index"></span><span id="_DS___INDEX"></span>**/ds** *index*  
Verifies the signature at a specified position.

<span id="_hash__SHA1SHA256"></span><span id="_hash__sha1sha256"></span><span id="_HASH__SHA1SHA256"></span>**/hash** {**SHA1**|**SHA256**}  
Specifies an optional hash algorithm to use when searching for a file in a catalog.

<span id="_kp"></span><span id="_KP"></span>**/kp**  
Configures SignTool to verify that the digital signature of each of the files specified by the *FileName* argument complies with the [kernel-mode code signing policy](https://msdn.microsoft.com/library/windows/hardware/ff548231) and the [PnP device installation signing requirements](https://msdn.microsoft.com/library/windows/hardware/ff549724) of Windows Vista and later versions of Windows. If this option is not specified, SignTool only verifies that a signature complies with the PnP device installation signing requirements.

<span id="_ms"></span><span id="_MS"></span>**/ms**  
Uses multiple verification semantics. This is the default behavior of a [**WinVerifyTrust function**](https://msdn.microsoft.com/library/windows/desktop/aa388208) call on Windows 8 and above.

<span id="_o_Version"></span><span id="_o_version"></span><span id="_O_VERSION"></span>**/o** *Version*  
Verifies the file as per the operating system version. The format for the *Version* argument is <em>PlatformID</em>**:**<em>VerMajor</em>**.**<em>VerMinor</em>**.**<em>BuildNumber</em>

The use of the **/o** option is recommended. If **/o** is not specified, SignTool might return unexpected results. For example, if you do not include the **/o** option, system catalogs that validate correctly on an older operating systems might not validate correctly on a newer operating system.

<span id="_p7"></span><span id="_P7"></span>**/p7**  
Verifies PKCS \#7 files. No existing policies are used for PKCS \#7 validation. The signature is checked and a chain is built for the signing certificate.

<span id="_pa"></span><span id="_PA"></span>**/pa**  
Configures SignTool to verify that the digital signature of each of the files specified by the *FileName* argument complies with the [PnP device installation signing requirements](https://msdn.microsoft.com/library/windows/hardware/ff549724).

**Note**  This option cannot be used with the **catdb** options.

 

<span id="_pg__PolicyGUID"></span><span id="_pg__policyguid"></span><span id="_PG__POLICYGUID"></span>**/pg** *PolicyGUID*  
Specifies a verification policy by GUID. The PolicyGUID corresponds to the ActionID of the verification policy.

**Note**  This option cannot be used with the **catdb** options.

 

<span id="_ph__"></span><span id="_PH__"></span>**/ph**   
Specifies that Sign Tool should print and verify page hash values.

<span id="_r_RootSubjectName"></span><span id="_r_rootsubjectname"></span><span id="_R_ROOTSUBJECTNAME"></span>**/r** *RootSubjectName*  
Specifies the subject name of the root certificate that the signing certificate must chain to. This value can be a substring of the entire subject name of the root certificate.

<span id="_tw"></span><span id="_TW"></span>**/tw**  
Specifies that a warning is generated if the signature is not timestamped.

### <span id="general_switches"></span><span id="GENERAL_SWITCHES"></span>General Options

<span id="_q"></span><span id="_Q"></span>**/q**  
Configures SignTool to display no output on successful execution and minimal output for failed execution.

<span id="_v"></span><span id="_V"></span>**/v**  
Configures SignTool to display the verbose version of operation and warning messages.

<span id="__"></span>**/?**  
Configures SignTool to display help information in a command window.

<span id="FileName_..."></span><span id="filename_..."></span><span id="FILENAME_..."></span>*FileName ...*  
Specifies a list of one or more file names. Depending on the command, SignTool will sign, timestamp, or verify the specified files. If the **catdb** command is used, SignTool will add or remove the specified files from a catalog database.

For the **sign**, **timestamp**, and **verify** commands, a file can be a catalog file for a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840) or a driver file.

For the **catdb** command, a file must be a catalog file for a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840).

### <span id="comments"></span><span id="COMMENTS"></span>Comments

SignTool supports a large number of options. The options described in this topic are limited to the ones that you can use to sign or verify a driver package or driver file.

For a complete list of SignTool parameters, see the Microsoft [SignTool](http://go.microsoft.com/fwlink/p/?linkid=62661) website.

For more information about signing files, see the Microsoft [Cryptography Tools](http://go.microsoft.com/fwlink/p/?linkid=10637) website.

A 32-bit version of SignTool is located in the bin\\i386 folder of the WDK. A 64-bit version of the tool is located in the bin\\amd64 and bin\\ia64 folders of the WDK.

### <span id="signing_examples"></span><span id="SIGNING_EXAMPLES"></span>Signing Examples

The following is an example of how to sign a [driver package's](https://msdn.microsoft.com/library/windows/hardware/ff544840) catalog file using a Software Publisher Certificate (SPC) and a corresponding cross-certificate. This example is valid for signing a driver package for 64-bit versions of Windows Vista and later versions of Windows, which enforce the kernel-mode code signing policy. The example signs the driver package's catalog file AbcCatFileName.cat. To sign the catalog file, the example uses the cross-certificate AbcCrossCertificate and the AbcSPCCertificate certificate. The AbcSPCCertificate certificate is located in the AbcCertificateStore certificate store.

The example also uses a publicly-available timestamp server to sign the catalog file. The timestamp server is provided by VeriSign and its URL is http://timestamp.verisign.com/scripts/timstamp.dll.

```
SignTool sign /ac AbcCrossCertificate.cer /s AbcCertificateStore /n AbcSPCCertificate /t http://timestamp.verisign.com/scripts/timstamp.dll AbcCatFileName.cat
```

The following is an example of how to embed a signature in a driver file using an SPC and cross-certificate. All the parameters are the same as in the example that signs a catalog file, except that the file that is signed is AbcDriverFile.sys instead of the catalog file AbcCatFileName.cat.

```
SignTool sign /ac AbcCrossCertificate.cer /s AbcCertificateStore /n AbcSPCCertificate /t http://timestamp.verisign.com/scripts/timstamp.dll AbcDriverFile.sys
```

The following is an example of how to sign a [driver package's](https://msdn.microsoft.com/library/windows/hardware/ff544840) catalog file using a [commercial release certificate](https://msdn.microsoft.com/library/windows/hardware/ff539935) or a [commercial test certificate](https://msdn.microsoft.com/library/windows/hardware/ff539940). This example is valid for signing a driver package for 32-bit versions of Windows Vistaand later versions of Windows, which do not enforce the kernel-mode code signing policy. The example signs the driver package's catalog file CatalogFileName.cat. The example uses the AbcTestCertificate test certificate, located in the TestCertificateStore certificate store, to sign the catalog file.

The example also uses a publicly-available timestamp server to sign the catalog file. The timestamp server is provided by VeriSign and its URL is http://timestamp.verisign.com/scripts/timstamp.dll.

```
SignTool sign /s TestCertificateStore /n AbcTestCertificate /t http://timestamp.verisign.com/scripts/timstamp.dll CatalogFileName.cat
```

### <span id="verifying_examples"></span><span id="VERIFYING_EXAMPLES"></span>Verifying Examples

The following is an example of how to verify that the signature of a [driver package's](https://msdn.microsoft.com/library/windows/hardware/ff544840) catalog file complies with the kernel-mode code signing policy and the PnP device installation signing requirements. The example verifies the signature of the catalog file AbcCatalogFile.cat.

```
SignTool verify /kp CatalogFileName.cat
```

The following is an example of how to verify that the signature of a file listed in a driver package's catalog file complies with the kernel-mode code signing policy and the PnP device installation signing requirements. The example verifies the signature of the file AbcDriverPackage.inf, which must have a thumbprint entry in the catalog file CatalogFileName.cat.

```
SignTool verify /kp /c CatalogFileName.cat AbcDriverPackage.inf
```

The following is an example of how to verify that an embedded signature complies with the kernel-mode code signing policy on Windows Vista and later versions of Windows. The example verifies the signature that is embedded in the driver file AbcDriverFile.sys.

```
SignTool verify /kp AbcDriverFile.sys
```

The following is an example of how to verify that the signature of a [driver package's](https://msdn.microsoft.com/library/windows/hardware/ff544840) catalog file complies with the PnP device installation signing requirements. The example verifies the signature of the catalog file CatalogFileName.cat.

```
SignTool verify /pa CatalogFileName.cat
```

### <span id="example_of_adding_a_catalog_file_to_the_system_component__driver__data"></span><span id="EXAMPLE_OF_ADDING_A_CATALOG_FILE_TO_THE_SYSTEM_COMPONENT__DRIVER__DATA"></span>Example of Adding a Catalog File to the System Component (Driver) Database

The following is an example of how to use SignTool to add the catalog file CatalogFileName.cat to the system component (driver) database. The **/v** option configures SignTool to operate in verbose mode and the **/u** option configures SignTool to generate a unique name for the catalog file being added, if necessary, to prevent replacing an already existing catalog file that has the same name as CatalogFileName.cat.

```
SignTool catdb /v /u CatalogFileName.cat
```

 

 





