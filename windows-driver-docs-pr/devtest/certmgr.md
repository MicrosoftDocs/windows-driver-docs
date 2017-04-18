---
title: CertMgr
description: CertMgr (Certmgr.exe) is a command-line CryptoAPI tool that manages certificates, certificate trust lists (CTLs), and certificate revocation lists (CRLs).
ms.assetid: 860693f5-de64-4ca9-be64-23e2fbb862c5
keywords: ["CertMgr Driver Development Tools"]
topic_type:
- apiref
api_name:
- CertMgr
api_type:
- NA
---

# CertMgr


CertMgr (Certmgr.exe) is a command-line [CryptoAPI](http://go.microsoft.com/fwlink/p/?linkid=136391) tool that manages certificates, certificate trust lists (CTLs), and certificate revocation lists (CRLs).

CertMgr supports a large number of switches, but this section describes only those that are relevant to managing [test certificates](https://msdn.microsoft.com/library/windows/hardware/ff553457) within a certificate store.

``` syntax
    CertMgr [/add|/del|/put] [Switches] [/s [/r RegistryLocation ] ] SourceName [/s [/r RegistryLocation] ] [DestinationName]
```

### <span id="partial_list_of_operations__switches__and_arguments"></span><span id="PARTIAL_LIST_OF_OPERATIONS__SWITCHES__AND_ARGUMENTS"></span>Partial list of operations, switches, and arguments

### <span id="operations"></span><span id="OPERATIONS"></span>Operations

<span id="add"></span><span id="ADD"></span>**add**  
Configures CertMgr to add certificates, CTLs, or CRLs from the file specified by *SourceName* to the certificate store specified by *DestinationName*.

<span id="del"></span><span id="DEL"></span>**del**  
Configures CertMgr to delete certificates, CTLs, or CRLs in the certificate store specified by *SourceName* from the certificate store specified by *DestinationName*. If *DestinationName* is not specified, *SourceName* will also serve as the destination store and will be modified.

<span id="put"></span><span id="PUT"></span>**put**  
Configures CertMgr to save certificates, CTLs, or CRLs from the certificate store specified by *SourceName* to a file specified by *DestinationName*.

<span id="none"></span><span id="NONE"></span>none  
If no command is specified, CertMgr displays all the certificates, CTLs, or CRLs in the certificate store or file specified by *SourceName*.

### <span id="switches_and_arguments"></span><span id="SWITCHES_AND_ARGUMENTS"></span>Switches and Arguments

<span id="_c"></span><span id="_C"></span>**/c**  
Configures CertMgr to only process certificates from the file specified by *SourceName*.

<span id="_CTL"></span><span id="_ctl"></span>**/CTL**  
Configures CertMgr to only process CTLs from the file specified by *SourceName*.

<span id="_CRL"></span><span id="_crl"></span>**/CRL**  
Configures CertMgr to only process CRLs from the file specified by *SourceName*.

<span id="_s"></span><span id="_S"></span>**/s**  
Configures CertMgr to access the certificate store specified by *SourceName* or *DestinationName* as a system store.

<span id="_r_registryLocation"></span><span id="_r_registrylocation"></span><span id="_R_REGISTRYLOCATION"></span>**/r** *registryLocation*  
Specifies the registry location of the system certificate store. The **/r** switch is only valid when used with the **/s** switch. The *registryLocation* argument must be either:

<span id="currentUser"></span><span id="currentuser"></span><span id="CURRENTUSER"></span>*currentUser*  
Specifies the registry location HKEY\_CURRENT\_USER.

<span id="localMachine"></span><span id="localmachine"></span><span id="LOCALMACHINE"></span>*localMachine*  
Specifies the registry location HKEY\_LOCAL\_MACHINE.

If the **/r** switch is not specified along with the **/s** switch, *currentUser* is the default.

For more information about these certificate stores, see [Certificate Stores](https://msdn.microsoft.com/library/windows/hardware/ff537890).

<span id="_v"></span><span id="_V"></span>**/v**  
Configures CertMgr to display detailed information about certificates, CTLs, and CRLs. If this switch is not specified, CertMgr only displays brief information.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

To use CertMgr, the user must be a member of the Administrators group on the system and run the command from an elevated command prompt.

For a complete list of CertMgr parameters, see the [Certificate Manager Tool](http://go.microsoft.com/fwlink/p/?linkid=70233) website.

A 32-bit version of the CertMgr tool is located in the *bin\\i386* folder of the WDK. A 64-bit version of the tool is located in the bin\\amd64 and bin\\ia64 folders of the WDK.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following two CertMgr commands add the certificate in the file *OutputFile.cer* to the Trusted Root Certification Authorities certificate store and the Trusted Publishers certificate store.

```
CertMgr /add OutputFile.cer /s /r localMachine root 
CertMgr /add OutputFile.cer /s /r localMachine trustedpublisher
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20CertMgr%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




