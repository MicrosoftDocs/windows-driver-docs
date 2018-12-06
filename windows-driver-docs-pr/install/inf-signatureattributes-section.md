---
title: INF SignatureAttributes Section
description: This section allows users to request additional signatures as required by certain certification scenarios.
ms.assetid: 8169686B-C45B-4D67-8B09-CD5F9977898D
keywords:
- INF SignatureAttributes Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF SignatureAttributes Section
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF SignatureAttributes Section


This section allows users to request additional signatures as required by certain certification scenarios. Examples of these scenarios are: Protected Environment media playback, Early Launch Antimalware, and third party HAL extensions. These additional signatures will only be applied if your Hardware Certification Kit package contains the proper Features and passing Tests.

```cpp
[SignatureAttributes]
FileOne = SignatureAttributes.SigType

[SignatureAttributes.SigType]
Attribute = Value
```

## Entries


<a href="" id="sigtype-signature-type"></a>**SigType=**<em>signature-type</em>  
Defines which signature or catalog attribute needs to be applied to the file. Should be one of the following:

-   Elam
-   HalExt
-   PETrust
-   DRM
-   WindowsHello

<a href="" id="attribute-attribute-name"></a>**Attribute=**<em>attribute-name</em>  
Each Signature Type has a corresponding attribute and value, as listed below. Use these definitions for your SignatureAttributes subsections:

-   **SignatureAttributes.Elam**: Elam = true
-   **SignatureAttributes.HalExt**: HalExt = true
-   **SignatureAttributes.DRM**: DRMLevel = {1300 | 1200}
-   **SignatureAttributes.PETrust**: PETrust = true
-   **SignatureAttributes.WindowsHello**: WindowsHello = true

Remarks
-------

These additional signatures will only be applied if your Hardware Certification Kit package contains the proper Features and passing Tests. These are additions to the normal behavior of Hardware Certification, and the corresponding Certification Requirements for Elam, HalExt, PETrust, and DRM can be found [here](http://go.microsoft.com/fwlink/p/?linkid=239763).

These INF sections should be used when requesting additional signatures regardless of the target OS.

Examples
--------

The following examples demonstrate how to enumerate and request additional signatures for audio:

```cpp
[SignatureAttributes]
ExampleFile1.dll=SignatureAttributes.PETrust
ExampleFile2.dll=SignatureAttributes.DRM

[SignatureAttributes.DRM]
DRMLevel=1300

 [SignatureAttributes.PETrust]
PETrust=true
```

The following examples demonstrate how to enumerate and request additional signatures for video:

```cpp
[SignatureAttributes]
ExampleFile1.dll=SignatureAttributes.PETrust

[SignatureAttributes.PETrust]
PETrust=true
```

The following examples demonstrate how to enumerate and request additional signatures for HAL:

```cpp
[SignatureAttributes]
HALFILE.dll=SignatureAttributes.HalExt

[SignatureAttributes.HalExt]
HalExt=true
```

The following examples demonstrate how to enumerate and request additional signatures for ELAM:

```cpp
[SignatureAttributes]
ELAMFILE.dll=SignatureAttributes.Elam

[SignatureAttributes.Elam]
Elam=true
```

The following examples demonstrate how to enumerate and request additional signatures for Windows Hello:

```cpp
[SignatureAttributes]
WindowsHelloFile.dll=SignatureAttributes.WindowsHello

[SignatureAttributes.WindowsHello]
WindowsHello=true
```


## See also


[Dashboard Help](https://msdn.microsoft.com/library/windows/hardware/br230803)

 

 






