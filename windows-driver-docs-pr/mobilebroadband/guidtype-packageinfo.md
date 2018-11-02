---
title: GUIDType (PackageInfo)
description: GUIDType (PackageInfo)
ms.assetid: 3f88df5a-2a17-4006-ad3b-aab9a12cbcb9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GUIDType (PackageInfo)

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The GUIDType XML simple type specifies a GUID.

``` syntax
<xs:simpleType name="GUIDType">
  <xs:restriction base="xs:string">
    <xs:pattern value="[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}" />
  </xs:restriction>
</xs:simpleType>
```

## <span id="Patterns"></span><span id="patterns"></span><span id="PATTERNS"></span>Patterns


The GUIDType simple type is a **xs:string** that is restricted by the following pattern:

-   \[0-9a-fA-F\]{8}-\[0-9a-fA-F\]{4}-\[0-9a-fA-F\]{4}-\[0-9a-fA-F\]{4}-\[0-9a-fA-F\]{12}

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


The GUIDType XML simple type specifies a GUID that uniquely identifies components within the device metadata package, such as the device's [ExperienceID](experienceid.md), [LanguageNeutralIdentifier](languageneutralidentifier.md), and [ModelID](modelid.md) values.

 

 





