---
title: INF SignatureAttributes Section
description: This section allows users to request additional signatures as required by certain certification scenarios.
ms.assetid: 8169686B-C45B-4D67-8B09-CD5F9977898D
keywords: ["INF SignatureAttributes Section Device and Driver Installation"]
topic_type:
- apiref
api_name:
- INF SignatureAttributes Section
api_type:
- NA
---

# INF SignatureAttributes Section


This section allows users to request additional signatures as required by certain certification scenarios. Examples of these scenarios are: Protected Environment media playback, Early Launch Antimalware, and third party HAL extensions. These additional signatures will only be applied if your Hardware Certification Kit package contains the proper Features and passing Tests.

``` syntax
[SignatureAttributes]
FileOne = SignatureAttributes.SigType

[SignatureAttributes.SigType]
Attribute = Value
```

## Entries


<a href="" id="sigtype-signature-type"></a>**SigType=***signature-type*  
Defines which signature or catalog attribute needs to be applied to the file. Should be one of the following:

-   Elam
-   HalExt
-   PETrust
-   DRM

<a href="" id="attribute-attribute-name"></a>**Attribute=***attribute-name*  
Each Signature Type has a corresponding attribute and value, as listed below. Use these definitions for your SignatureAttributes subsections:

-   **SignatureAttributes.Elam**: Elam = true
-   **SignatureAttributes.HalExt**: HalExt = true
-   **SignatureAttributes.DRM**: DRMLevel = {1300 | 1200}
-   **SignatureAttributes.PETrust**: PETrust = true

Remarks
-------

These additional signatures will only be applied if your Hardware Certification Kit package contains the proper Features and passing Tests. These are additions to the normal behavior of Hardware Certification, and the corresponding Certification Requirements for Elam, HalExt, PETrust, and DRM can be found [here](http://go.microsoft.com/fwlink/p/?linkid=239763).

These INF sections should be used when requesting additional signatures regardless of the target OS.

Examples
--------

The following examples demonstrate how to enumerate and request additional signatures for audio:

```
[SignatureAttributes]
ExampleFile1.dll=SignatureAttributes.PETrust
ExampleFile2.dll=SignatureAttributes.DRM

[SignatureAttributes.DRM]
DRMLevel=1300

 [SignatureAttributes.PETrust]
PETrust=true
```

The following examples demonstrate how to enumerate and request additional signatures for video:

```
[SignatureAttributes]
ExampleFile1.dll=SignatureAttributes.PETrust

[SignatureAttributes.PETrust]
PETrust=true
```

The following examples demonstrate how to enumerate and request additional signatures for HAL:

```
[SignatureAttributes]
HALFILE.dll=SignatureAttributes.HalExt

[SignatureAttributes.HalExt]
HalExt=true
```

The following examples demonstrate how to enumerate and request additional signatures for ELAM:

```
[SignatureAttributes]
ELAMFILE.dll=SignatureAttributes.Elam

[SignatureAttributes.Elam]
Elam=true
```

## See also


[Dashboard Help](https://msdn.microsoft.com/library/windows/hardware/br230803)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20INF%20SignatureAttributes%20Section%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





