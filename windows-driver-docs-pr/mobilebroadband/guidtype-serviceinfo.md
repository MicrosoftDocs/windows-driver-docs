---
title: GUIDType (ServiceInfo)
description: GUIDType (ServiceInfo)
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GUIDType (ServiceInfo)

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

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

 

 





