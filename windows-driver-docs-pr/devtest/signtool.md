---
title: SignTool
description: SignTool (Signtool.exe) is a command-line CryptoAPI tool that digitally-signs files, verifies signatures in files, and time stamps files.
keywords:
- SignTool Driver Development Tools
topic_type:
- apiref
api_name:
- SignTool
api_type:
- NA
ms.date: 04/20/2017
---

# SignTool

SignTool (Signtool.exe) is a command-line [CryptoAPI](/windows/win32/seccrypto/cryptography-portal) tool that digitally-signs files, verifies signatures in files, and time stamps files.

```command
    SignTool [Operation] [Options] [FileName ...]
```

## Partial list of operations, options, and arguments

### Operations

**catdb**  
Configures SignTool to update a catalog database. SignTool either adds catalog files to a database or removes catalogs from a database. By default, the **catdb** command adds the files, whose names are specified by the *FileName* argument, to the system component (driver) database.

>[!NOTE]
>Catalog databases are used for automatic lookup of catalog files.

**sign**  
Configures SignTool to digitally-sign the files whose names are specified by the *FileName* argument.

**timestamp**  
Configures SignTool to timestamp the files whose names are specified by the *FileName* argument.

**verify**  
Configures SignTool to verify the digital signature of the files whose names are specified by the *FileName* argument.

#### Catdb operation options

**/d**  
Configures SignTool to update the catalog database. If neither **/d** nor **/g** option is used, SignTool updates the system component and the driver database.

**/g** *Guid*  
Configures SignTool to update the catalog database identified by the *GUID* argument.

**/r**  
Configures SignTool to remove each of the catalog files, whose names are specified by the *FileName* argument, from the catalog database. If this option is not specified, SignTool adds the specified catalog files to the catalog database.

**/u**  
Configures SignTool to generate a unique name, if necessary, for a catalog file to prevent a conflict with an existing catalog file in the catalog database. If this option is not specified, SignTool overwrites any existing catalog that has the same name as the catalog being added.

#### Sign operation options

**/a**
Configures SignTool to automatically select the best signing certificate. If this option is not present, SignTool expects to find only one signing certificate.

**/ac** *CrossCertFileName*  
Specifies the name of a cross-certificate file that is used with a Software Publisher Certificate (SPC) that is named *CertificateName* and is installed in the certificate store *StoreName*. This option should only be used if the signing certificate is an SPC.

**/c** *CertTemplateName*  
Specifies the Certificate Template Name (a Microsoft extension) for the signing certificate.

**/csp** *CSPName*  
Specifies the cryptographic service provider (CSP) that contains the private key container.

**/d** *Desc*  
Specifies a description of the signed content.

**/du** *URL*  
Specifies a URL for the expanded description of the signed content.

**/f** *SignCertFile*  
Specifies the signing certificate in a file. Only the Personal Information Exchange (PFX) file format is supported. You can use the [**Pvk2Pfx**](pvk2pfx.md) tool to convert SPC and PVK files to PFX format.

If the file is in PFX format protected by a password, use the **/p** option to specify the password. If the file does not contain private keys, use the **/csp** and **/k** options to specify the CSP and private key container name, respectively.

**/fd**  
Specifies the file digest algorithm to use for creating file signatures. The default is SHA1.

**/i** *IssuerName*  
Specifies the name of the issuer of the signing certificate. This value can be a substring of the entire issuer name.

**/j** *DLL*  
Specifies the name of a DLL that provides attributes of the signature.

**/jp** *ParameterName*  
Specifies a parameter that is passed to the DLL specified by the **/j** command.

**/kc** *PrivKeyContainerName*  
Specifies the key container name of the private key.

**/n** *SubjectName*  
Specifies the name of the subject of the signing certificate. This value can be a substring of the entire subject name.

**/nph**  
If supported, suppresses page hashes for executable files. The default is determined by the SIGNTOOL\_PAGE\_HASHES environment variable and by the wintrust.dll version. This option is ignored for non-PE files.

**/p** *Password*  
Specifies the password to use when opening a PFX file. A PFX file can be specified by using the **/f** option

**/p7** *Path*  
Specifies that a Public Key Cryptography Standards (PKCS) \#7 file is produced for each specified content file. PKCS \#7 files are named path\\filename.p7.

**/p7ce** *Value*  
Specifies options for the signed PKCS \#7 content. Set Value to "Embedded" to embed the signed content in the PKCS \#7 file, or to "DetachedSignedData" to produce the signed data portion of a detached PKCS \#7 file. If the **/p7ce** option is not used, the signed content is embedded by default.

**/p7co** *OID*  
Specifies the object identifier (OID) that identifies the signed PKCS \#7 content.

**/ph**
If supported, generates page hashes for executable files.

**/r** *RootSubjectName*  
Specifies the subject name of the root certificate that the signing certificate must chain to. This value can be a substring of the entire subject name of the root certificate.

**/s** *StoreName*  
Specifies the name of the certificate store to open when searching for the certificate to use for signing files. If this option is not specified, the **My** certificate store is opened.

**/sha1** *Hash*  
Specifies the SHA1 hash of the signing certificate.

**/sm**  
Configures SignTool to use a machine certificate store instead of a user certificate store.

**/t** *URL*  
Specifies a URL to a timestamp server. If this option is not provided, the signed file is not timestamped. A catalog file or driver file should be timestamped, because if the signer's key is compromised, the timestamp provides the information necessary to revoke the key that was used to sign the file.

**/td** *alg*  
Used with the /tr option to request a digest algorithm used by the RFC 3161 time stamp server.

**/tr** *URL*  
Specifies the URL of the RFC 3161 time stamp server. If this option (or **/t**) is not present, the signed file will not be time stamped. A warning is generated if time stamping fails. This option cannot be used with the **/t** option.

**/u** *Usage*  
Specifies the enhanced key usage (EKU) that must be present in the signing certificate. The usage value can be specified by OID or string. The default usage is "Code Signing" (1.3.6.1.5.5.7.3.3).

**/uw**
Specifies usage of "Windows System Component Verification" (1.3.6.1.4.1.311.10.3.6).

#### Timestamp operation options

**/p7**
Time stamps PKCS \#7 files.

**/t** *URL*  
Specifies the URL of the timestamp server. The file being timestamped must have been signed previously

**/td** *alg*  
Requests a digest algorithm used by the RFC 3161 time stamp server. **/td** is used with the **/tr** option.

**/tp** *index*  
Time stamps the signature at index.

**/tr** *alg*  
Requests a digest algorithm used by the RFC 3161 time stamp server. **/td** is used with the **/tr** option.

#### Verify operation options

**/a**  
Specifies that all methods can be used to verify the file. First, the catalog databases are searched to determine whether the file is signed in a catalog. If the file is not signed in any catalog, SignTool attempts to verify the file's embedded signature. This option is recommended when verifying files that may or may not be signed in a catalog.

**/ad**  
Specifies that only the default catalog database is searched for the catalog that the file was signed in.

**/all**  
Verifies all signatures in a file that includes multiple signatures.

**/as**  
Specifies that only the system component (driver) catalog database is searched for the catalog that the file was signed in.

**/ag** *CatDBGUID*  
Specifies that only the catalog database, identified through the *CatDBGUID* argument, is searched for the catalog that the file was signed in.

**/c** *CatalogFileName*  
Specifies the name of a catalog file.

**/d**
Specifies that Sign Tool should print the description and the description URL.

**/ds** *index*  
Verifies the signature at a specified position.

**/hash** {**SHA1**|**SHA256**}  
Specifies an optional hash algorithm to use when searching for a file in a catalog.

**/kp**  
Configures SignTool to verify that the digital signature of each of the files specified by the *FileName* argument complies with the [kernel-mode code signing policy](../install/kernel-mode-code-signing-policy--windows-vista-and-later-.md) and the [PnP device installation signing requirements](../install/pnp-device-installation-signing-requirements--windows-vista-and-later-.md) of Windows Vista and later versions of Windows. If this option is not specified, SignTool only verifies that a signature complies with the PnP device installation signing requirements.

**/ms**  
Uses multiple verification semantics. This is the default behavior of a [**WinVerifyTrust function**](/windows/win32/api/wintrust/nf-wintrust-winverifytrust) call on Windows 8 and above.

**/o** *Version*  
Verifies the file as per the operating system version. The format for the *Version* argument is *PlatformID:VerMajor.VerMinor.BuildNumber*

The use of the **/o** option is recommended. If **/o** is not specified, SignTool might return unexpected results. For example, if you do not include the **/o** option, system catalogs that validate correctly on an older operating systems might not validate correctly on a newer operating system.

**/p7**  
Verifies PKCS \#7 files. No existing policies are used for PKCS \#7 validation. The signature is checked and a chain is built for the signing certificate.

**/pa**  
Configures SignTool to verify that the digital signature of each of the files specified by the *FileName* argument complies with the [PnP device installation signing requirements](../install/pnp-device-installation-signing-requirements--windows-vista-and-later-.md).

>[!NOTE]
>This option cannot be used with the **catdb** options.

**/pg** *PolicyGUID*  
Specifies a verification policy by GUID. The PolicyGUID corresponds to the ActionID of the verification policy.

>[!NOTE]
>This option cannot be used with the **catdb** options.

**/ph**
Specifies that Sign Tool should print and verify page hash values.

**/r** *RootSubjectName*  
Specifies the subject name of the root certificate that the signing certificate must chain to. This value can be a substring of the entire subject name of the root certificate.

**/tw**  
Specifies that a warning is generated if the signature is not timestamped.

### General Options

**/q**  
Configures SignTool to display no output on successful execution and minimal output for failed execution.

**/v**  
Configures SignTool to display the verbose version of operation and warning messages.

**/?**  
Configures SignTool to display help information in a command window.

*FileName ...*  
Specifies a list of one or more file names. Depending on the command, SignTool will sign, timestamp, or verify the specified files. If the **catdb** command is used, SignTool will add or remove the specified files from a catalog database.

For the **sign**, **timestamp**, and **verify** commands, a file can be a catalog file for a [driver package](../install/driver-packages.md) or a driver file.

For the **catdb** command, a file must be a catalog file for a [driver package](../install/driver-packages.md).

## Remarks

SignTool supports a large number of options. The options described in this topic are limited to the ones that you can use to sign or verify a driver package or driver file.

For a complete list of SignTool parameters, see the Microsoft [SignTool](/windows/win32/seccrypto/signtool) website.

For more information about signing files, see the Microsoft [Cryptography Tools](/windows/win32/seccrypto/cryptography-tools) website.

A 32-bit version of SignTool is located in the bin\\i386 folder of the WDK. A 64-bit version of the tool is located in the bin\\amd64 and bin\\ia64 folders of the WDK.

## Examples

The following is an example of how to sign a [driver package's](../install/driver-packages.md) catalog file using a Software Publisher Certificate (SPC) and a corresponding cross-certificate. This example is valid for signing a driver package for 64-bit versions of Windows Vista and later versions of Windows, which enforce the kernel-mode code signing policy. The example signs the driver package's catalog file AbcCatFileName.cat. To sign the catalog file, the example uses the cross-certificate AbcCrossCertificate and the AbcSPCCertificate certificate. The AbcSPCCertificate certificate is located in the AbcCertificateStore certificate store.

The example also uses a publicly-available timestamp server to sign the catalog file. The timestamp server is provided by DigiCert and its URL is `http://timestamp.digicert.com`.

```command
SignTool sign /ac AbcCrossCertificate.cer /s AbcCertificateStore /n AbcSPCCertificate /t http://timestamp.digicert.com AbcCatFileName.cat
```

The following is an example of how to embed a signature in a driver file using an SPC and cross-certificate. All the parameters are the same as in the example that signs a catalog file, except that the file that is signed is AbcDriverFile.sys instead of the catalog file AbcCatFileName.cat.

```command
SignTool sign /ac AbcCrossCertificate.cer /s AbcCertificateStore /n AbcSPCCertificate /t http://timestamp.digicert.com AbcDriverFile.sys
```

The following is an example of how to sign a [driver package's](../install/driver-packages.md) catalog file using a [commercial release certificate](/windows-hardware/drivers/install/deprecation-of-software-publisher-certificates-and-commercial-release-certificates) or a [commercial test certificate](/windows-hardware/drivers/install/deprecation-of-software-publisher-certificates-and-commercial-release-certificates). This example is valid for signing a driver package for 32-bit versions of Windows Vista and later versions of Windows, which do not enforce the kernel-mode code signing policy. The example signs the driver package's catalog file CatalogFileName.cat. The example uses the AbcTestCertificate test certificate, located in the TestCertificateStore certificate store, to sign the catalog file.

The example also uses a publicly-available timestamp server to sign the catalog file. The timestamp server is provided by DigiCert and its URL is `http://timestamp.digicert.com`.

```command
SignTool sign /s TestCertificateStore /n AbcTestCertificate /t http://timestamp.digicert.com CatalogFileName.cat
```

### Verifying Examples

The following is an example of how to verify that the signature of a [driver package's](../install/driver-packages.md) catalog file complies with the kernel-mode code signing policy and the PnP device installation signing requirements. The example verifies the signature of the catalog file AbcCatalogFile.cat.

```command
SignTool verify /kp CatalogFileName.cat
```

The following is an example of how to verify that the signature of a file listed in a driver package's catalog file complies with the kernel-mode code signing policy and the PnP device installation signing requirements. The example verifies the signature of the file AbcDriverPackage.inf, which must have a thumbprint entry in the catalog file CatalogFileName.cat.

```command
SignTool verify /kp /c CatalogFileName.cat AbcDriverPackage.inf
```

The following is an example of how to verify that an embedded signature complies with the kernel-mode code signing policy on Windows Vista and later versions of Windows. The example verifies the signature that is embedded in the driver file AbcDriverFile.sys.

```command
SignTool verify /kp AbcDriverFile.sys
```

The following is an example of how to verify that the signature of a [driver package's](../install/driver-packages.md) catalog file complies with the PnP device installation signing requirements. The example verifies the signature of the catalog file CatalogFileName.cat.

```command
SignTool verify /pa CatalogFileName.cat
```

### Example of Adding a Catalog File to the System Component (Driver) Database

The following is an example of how to use SignTool to add the catalog file CatalogFileName.cat to the system component (driver) database. The **/v** option configures SignTool to operate in verbose mode and the **/u** option configures SignTool to generate a unique name for the catalog file being added, if necessary, to prevent replacing an already existing catalog file that has the same name as CatalogFileName.cat.

```command
SignTool catdb /v /u CatalogFileName.cat
```
