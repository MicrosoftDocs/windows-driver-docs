---
title: Minidriver Registration
description: Minidriver Registration
ms.assetid: 332FEBD6-9803-4502-8F84-9DB2F17BB19B
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Minidriver Registration


## <span id="DllMain"></span><span id="dllmain"></span><span id="DLLMAIN"></span>DllMain


The smart card minidriver implements and exports a [*DllMain*](https://msdn.microsoft.com/library/windows/desktop/ms682583) funtion to handle load/unload and attach/detach notifications. This allows the minidriver DLL to manage its state and allocated resources. For implementation details, see the *DllMain* reference topic.

## <span id="DllRegisterServer_and_DllUnregisterServer"></span><span id="dllregisterserver_and_dllunregisterserver"></span><span id="DLLREGISTERSERVER_AND_DLLUNREGISTERSERVER"></span>DllRegisterServer and DllUnregisterServer


*DllRegisterServer* and *DllUnregisterServer* are no longer called stating with v5 of the Smart Card Minidriver Specification. The registration of the card minidriver is performed through an INF-based update to the system registry.

## <span id="_Registration_Mechanisms"></span><span id="_registration_mechanisms"></span><span id="_REGISTRATION_MECHANISMS"></span> Registration Mechanisms


An INF-based approach should be used for the registration of a smart card minidriver. The INF file allows for the creation of the necessary registry entries as well as the copy of files from the driver package to the appropriate directories

For an example of a smart card INF file, see [Smart Card Plug and Play](smart-card-plug-and-play.md).

## <span id="INF_File_Requirements"></span><span id="inf_file_requirements"></span><span id="INF_FILE_REQUIREMENTS"></span>INF File Requirements


The smart card INF file should contain directives that create the following registry entries for each card.

``` syntax
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography\Calais\SmartCards\VENDORCARDNAME]
"80000001"="VENDOR.dll"
"ATR"=hex:01,23,45,67,89,01,23,45,67,89,01,23,45,67,89,01,23,45
"ATRMask"=hex:ff,ff,ff,ff,ff,ff,ff,ff,ff,ff,ff,ff,ff,ff,ff,ff,ff,ff
```

If the minidriver supports loading under CAPI, the following line should be included in the registry file:

``` syntax
"Crypto Provider"="Microsoft Base Smart Card Crypto Provider"
```

If the minidriver supports loading under CNG, the following line should be included in the registry file:

``` syntax
"Smart Card Key Storage Provider"="Microsoft Smart Card Key Storage Provider"
```

 

 





