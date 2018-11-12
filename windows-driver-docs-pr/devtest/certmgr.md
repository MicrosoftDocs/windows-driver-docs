---
title: CertMgr
description: CertMgr (Certmgr.exe) is a command-line CryptoAPI tool that manages certificates, certificate trust lists (CTLs), and certificate revocation lists (CRLs).
ms.assetid: 860693f5-de64-4ca9-be64-23e2fbb862c5
keywords:
- CertMgr Driver Development Tools
topic_type:
- apiref
api_name:
- CertMgr
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CertMgr


CertMgr (Certmgr.exe) is a command-line [CryptoAPI](http://go.microsoft.com/fwlink/p/?linkid=136391) tool that manages certificates, certificate trust lists (CTLs), and certificate revocation lists (CRLs).

CertMgr supports a large number of switches, but this section describes only those that are relevant to managing [test certificates](https://msdn.microsoft.com/library/windows/hardware/ff553457) within a certificate store.

```
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

 

 





